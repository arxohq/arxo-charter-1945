#!/usr/bin/env python3
"""Membership arc: expectations from articles 4–6 and UNC-20/21/28/29."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from _check import main  # noqa: E402

PACKAGE = Path(__file__).resolve().parent
EXPECTED = {
    "Admitted": {
        "admitted": {"truth": "TRUE_ONLY"},
        "blocked": {"truth": "NEITHER"},
    },
    "AdmissionBlocked": {
        "admitted": {"truth": "NEITHER"},
        "blocked": {"truth": "TRUE_ONLY"},
    },
    "Suspended": {
        "suspended": {"truth": "TRUE_ONLY"},
        "suspension-denied": {"truth": "NEITHER"},
    },
    "SuspensionDenied": {
        "suspension-denied": {"truth": "TRUE_ONLY"},
        "suspended": {"truth": "NEITHER"},
    },
    "RightsRestored": {
        "restored": {"truth": "TRUE_ONLY"},
    },
    "Expelled": {
        "expelled": {"truth": "TRUE_ONLY"},
        "expulsion-denied": {"truth": "NEITHER"},
    },
    "ExpulsionDenied": {
        "expulsion-denied": {"truth": "TRUE_ONLY"},
        "expelled": {"truth": "NEITHER"},
    },
}

if __name__ == "__main__":
    raise SystemExit(main(PACKAGE, EXPECTED, "membership-arc"))
