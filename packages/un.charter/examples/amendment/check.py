#!/usr/bin/env python3
"""Why the Charter is so hard to amend: expectations from Articles 108-109."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from _check import main  # noqa: E402

PACKAGE = Path(__file__).resolve().parent
EXPECTED = {
    "InForce": {
        "amendment-adopted": {"truth": "TRUE_ONLY"},
        "amendment-in-force": {"truth": "TRUE_ONLY"},
        "amendment-blocked": {"truth": "NEITHER"},
    },
    "OnePermanentMemberMissing": {
        "amendment-adopted": {"truth": "TRUE_ONLY"},
        "amendment-in-force": {"truth": "NEITHER"},
        "amendment-blocked": {"truth": "TRUE_ONLY"},
    },
    "BelowTwoThirdsRatification": {
        "amendment-adopted": {"truth": "TRUE_ONLY"},
        "amendment-in-force": {"truth": "NEITHER"},
        "amendment-blocked": {"truth": "NEITHER"},
    },
    "NotAdoptedByAssembly": {
        "amendment-adopted": {"truth": "NEITHER"},
        "amendment-in-force": {"truth": "NEITHER"},
        "amendment-blocked": {"truth": "NEITHER"},
    },
    "ConferenceConvenedNoVeto": {
        "ga-vote-approved": {"truth": "TRUE_ONLY"},
        "sc-vote-approved": {"truth": "TRUE_ONLY"},
        "conference-convened": {"truth": "TRUE_ONLY"},
    },
    "ConferenceNotConvenedEightVotes": {
        "ga-vote-approved": {"truth": "TRUE_ONLY"},
        "sc-vote-approved": {"truth": "NEITHER"},
        "conference-convened": {"truth": "NEITHER"},
    },
    "AlterationBlockedSameLock": {
        "alteration-recommended": {"truth": "TRUE_ONLY"},
        "alteration-in-force": {"truth": "NEITHER"},
        "alteration-blocked": {"truth": "TRUE_ONLY"},
    },
}

if __name__ == "__main__":
    raise SystemExit(main(PACKAGE, EXPECTED, "amendment"))
