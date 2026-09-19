#!/usr/bin/env python3
"""Same vote, two answers: expectations from articles 27(3), 23 and UNC-13–19."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from _check import main  # noqa: E402

PACKAGE = Path(__file__).resolve().parent
EXPECTED = {
    "ProceduralNineFor": {
        "decision-adopted-procedural": {"truth": "TRUE_ONLY"},
        "decision-blocked-procedural": {"truth": "NEITHER"},
    },
    "AbstentionLetter": {
        "decision-adopted-abstention": {"truth": "NEITHER"},
        "decision-blocked-abstention": {"truth": "TRUE_ONLY"},
    },
    "AbstentionPractice": {
        "decision-adopted-abstention": {"truth": "TRUE_ONLY"},
        "decision-blocked-abstention": {"truth": "TRUE_ONLY"},
    },
    "DisputantVotes": {
        "disputant-positions": {"position": ("AbstainAsDisputant", "ACTIVE")},
    },
    "ContinuityLetter": {
        "decision-adopted-russia": {"truth": "TRUE_ONLY"},
        "decision-blocked-russia": {"truth": "NEITHER"},
        "china-seat": {"truth": "NEITHER"},
    },
    "ContinuityPractice": {
        "decision-adopted-russia": {"truth": "NEITHER"},
        "decision-blocked-russia": {"truth": "TRUE_ONLY"},
        "china-seat": {"truth": "TRUE_ONLY"},
    },
}

if __name__ == "__main__":
    raise SystemExit(main(PACKAGE, EXPECTED, "same-vote"))
