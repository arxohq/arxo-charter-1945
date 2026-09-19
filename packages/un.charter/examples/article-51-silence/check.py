#!/usr/bin/env python3
"""Article 51 silence: expectations from UNC-03–12 and the letter of articles 2(4) and 51."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from _check import main  # noqa: E402

PACKAGE = Path(__file__).resolve().parent
EXPECTED = {
    "UnreportedDuty": {
        "positions": {"position": ("ReportSelfDefenceMeasures", "ACTIVE")},
    },
    "LowSilent": {
        "self-defence": {"truth": "NEITHER"},
    },
    "LowPermits": {
        "self-defence": {"truth": "TRUE_ONLY"},
    },
    "BeforeAttack": {
        "anticipatory": {"truth": "NEITHER"},
    },
    "CarolinePermits": {
        "anticipatory": {"truth": "TRUE_ONLY"},
    },
    "NonStateSilent": {
        "self-defence-harbor": {"truth": "NEITHER"},
    },
    "NonStatePermits": {
        "self-defence-harbor": {"truth": "TRUE_ONLY"},
    },
    "Kosovo": {
        "violates-24": {"truth": "TRUE_ONLY"},
    },
    "KosovoLow": {
        "violates-24": {"truth": "TRUE_ONLY"},
    },
    "KosovoCaroline": {
        "violates-24": {"truth": "TRUE_ONLY"},
    },
    "KosovoNonState": {
        "violates-24": {"truth": "TRUE_ONLY"},
    },
}

if __name__ == "__main__":
    raise SystemExit(main(PACKAGE, EXPECTED, "article-51-silence"))
