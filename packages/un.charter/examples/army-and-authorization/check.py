#!/usr/bin/env python3
"""Army and authorization: expectations from articles 42–47, 106 and UNC-11/26/77."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from _check import main  # noqa: E402

PACKAGE = Path(__file__).resolve().parent
EXPECTED = {
    "DeadChain": {
        "force-authorized": {"truth": "TRUE_ONLY"},
        "positions": {"position_absent": "ProvideArmedForcesUnderArticle43"},
    },
    "KuwaitAuthorised": {
        "force-authorized": {"truth": "TRUE_ONLY"},
    },
    "ConsultActive": {
        "positions": {"position": ("ConsultForJointActionPendingArticle43", "ACTIVE")},
    },
    "ConsultDischarged": {
        "positions": {"position": ("ConsultForJointActionPendingArticle43", "SATISFIED")},
    },
    "ConsultGone": {
        "positions": {"position_absent": "ConsultForJointActionPendingArticle43"},
    },
}

if __name__ == "__main__":
    raise SystemExit(main(PACKAGE, EXPECTED, "army-and-authorization"))
