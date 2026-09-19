"""Shared check of the Charter case collections: expectations from UNC/the text, Rust = Python = replay."""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "engines" / "lawref"))

from lawref.canon import canonical_bytes  # noqa: E402
from lawref.cases import check_registration  # noqa: E402
from lawref.evaluator import EvaluationRequest, evaluate  # noqa: E402

NS = "urn:un:corpus:clir:charter#"


def run_json(command: list[str]) -> dict:
    completed = subprocess.run(command, capture_output=True, text=True, check=False)
    if completed.returncode:
        raise RuntimeError(f"{' '.join(command)}\n{completed.stderr}\n{completed.stdout}")
    return json.loads(completed.stdout)


def materialize(package: Path) -> None:
    script = ROOT / "packs" / "examples" / "cases" / "materialize_deps.py"
    completed = subprocess.run(
        [sys.executable, str(script), str(package)],
        capture_output=True, text=True, check=False,
    )
    if completed.returncode:
        raise RuntimeError(completed.stderr or completed.stdout or "materialize_deps failed")
    if completed.stdout:
        print(completed.stdout, end="")


def position_statuses(result: dict, name: str) -> set[str]:
    """Statuses of the holders of positions of the Charter template `name` (field `template`).

    Expectations name the template: a position `id` carries the rule name and the
    holder number, and the query-wide `normativeStatus` folds every position of
    the case, not this template. An empty set means the engine created none.
    """
    return {
        str(pos["status"])
        for pos in result.get("positions") or []
        if pos["template"] == NS + name
    }


def check(package: Path, expected: dict, law: str, output: Path, title: str) -> int:
    materialize(package)
    entries = check_registration(package)
    if {entry.name for entry in entries} != set(expected):
        raise RuntimeError("the registered cases differ from the ones checked here")
    if check_registration(package.parents[1]):
        raise RuntimeError("cases were attached to the parent canon")
    questions = 0
    for entry in entries:
        for query, want in expected[entry.name].items():
            saved = output / entry.name / query
            result = run_json([
                law, "ask", str(package), "--case", entry.name,
                "--query-json", str(package / "queries" / f"{query}.json"),
                "--out", str(saved),
            ])
            answer, = result["results"]
            # A case may leave an organ's §47.3 finding out: the answer is then
            # REQUIRES_JUDGMENT ("Left to the Council"), and the expectation names
            # it with `evaluation`. A non-COMPUTED answer is never accepted silently.
            evaluation = want.get("evaluation", "COMPUTED")
            if answer["evaluationStatus"] != evaluation:
                raise RuntimeError(
                    f"{entry.name}/{query}: expected {evaluation}, got {answer['evaluationStatus']}")
            if "truth" in want and answer.get("truthStatus") != want["truth"]:
                raise RuntimeError(
                    f"{entry.name}/{query}: expected {want['truth']}, got {answer.get('truthStatus')}")
            if "position" in want:
                # The expected status holds for EVERY holder of the template, and there is at least one.
                name, status = want["position"]
                statuses = position_statuses(result, name)
                if statuses != {status}:
                    raise RuntimeError(
                        f"{entry.name}/{query}: expected every {name} position {status}, "
                        f"got {sorted(statuses) or 'no positions'}")
            if "position_absent" in want:
                name = want["position_absent"]
                statuses = position_statuses(result, name) - {"UNDETERMINED"}
                if statuses:
                    raise RuntimeError(
                        f"{entry.name}/{query}: {name} should be absent, got {sorted(statuses)}")
            request = json.loads((saved / "request.json").read_bytes())
            expected_bytes = canonical_bytes(result)
            if canonical_bytes(evaluate(EvaluationRequest.from_dict(request))) != expected_bytes:
                raise RuntimeError(f"{entry.name}/{query}: Rust != Python")
            if canonical_bytes(run_json([law, "eval", str(saved)])) != expected_bytes:
                raise RuntimeError(f"{entry.name}/{query}: ask != replay")
            questions += 1
        print(f"{entry.name}: {len(expected[entry.name])} question(s) — "
              "text expectations, Rust/Python and replay all agree", flush=True)
    print(f"{title}: {len(expected)} cases, {questions} questions — OK")
    return questions


def main(package: Path, expected: dict, title: str) -> int:
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--law", default=str(ROOT / "law"))
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()
    try:
        if args.out:
            check(package, expected, args.law, args.out.resolve(), title)
        else:
            with tempfile.TemporaryDirectory(prefix="un-charter-ex-") as temporary:
                check(package, expected, args.law, Path(temporary), title)
    except (RuntimeError, ValueError, OSError, KeyError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        return 1
    return 0
