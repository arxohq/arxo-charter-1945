#!/usr/bin/env python3
"""One dispute, two tracks: expectations from articles 33-38, 52 and UNC-38-48."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from _check import main  # noqa: E402

PACKAGE = Path(__file__).resolve().parent

# Track B (Council powers) truth queries asked in every case, whether or not
# that stage's story touches them: an unanswered branch would be a defect on
# the "two tracks" page. Article 34 and article 37(2) name the Security
# Council as the assessor of the underlying evaluative question (§47.3,
# DECISION-0194); until a case supplies the Council's own finding as an
# `origin adjudicated` assertion, the engine answers `REQUIRES_JUDGMENT`
# ("left to the Council"), never a guess in either direction.
COUNCIL_STILL_DELIBERATING = {
    "endangerment-determined": {"truth": "NEITHER", "evaluation": "REQUIRES_JUDGMENT"},
    "settlement-terms-recommended": {"truth": "NEITHER", "evaluation": "REQUIRES_JUDGMENT"},
}

EXPECTED = {
    "DisputeArises": {
        "positions": {
            "position": ("SeekPeacefulSettlementFirst", "ACTIVE"),
            "position_absent": "ReferUnsettledDisputeToSecurityCouncil",
        },
        "entitled-to-attention": {"truth": "TRUE_ONLY"},
        "procedures-recommended": {"truth": "NEITHER"},
        "icj-referral-recommended": {"truth": "NEITHER"},
        "article-38-recommendation": {"truth": "NEITHER"},
        "regional-settlement-encouraged": {"truth": "NEITHER"},
        **COUNCIL_STILL_DELIBERATING,
    },
    "SettlementSoughtFailed": {
        "positions": {
            "position": ("SeekPeacefulSettlementFirst", "SATISFIED"),
            "position_absent": "SeekRegionalSettlementFirst",
        },
        "entitled-to-attention": {"truth": "TRUE_ONLY"},
        "procedures-recommended": {"truth": "NEITHER"},
        "icj-referral-recommended": {"truth": "NEITHER"},
        "article-38-recommendation": {"truth": "NEITHER"},
        "regional-settlement-encouraged": {"truth": "NEITHER"},
        **COUNCIL_STILL_DELIBERATING,
    },
    "ReferredToCouncil": {
        "positions": {
            "position": ("ReferUnsettledDisputeToSecurityCouncil", "SATISFIED"),
            "position_absent": "SeekRegionalSettlementFirst",
        },
        "entitled-to-attention": {"truth": "TRUE_ONLY"},
        "procedures-recommended": {"truth": "NEITHER"},
        "icj-referral-recommended": {"truth": "NEITHER"},
        "article-38-recommendation": {"truth": "NEITHER"},
        "regional-settlement-encouraged": {"truth": "NEITHER"},
        **COUNCIL_STILL_DELIBERATING,
    },
    "CouncilFindsEndangerment": {
        "positions": {
            "position": ("ReferUnsettledDisputeToSecurityCouncil", "SATISFIED"),
            "position_absent": "SeekRegionalSettlementFirst",
        },
        "entitled-to-attention": {"truth": "TRUE_ONLY"},
        "endangerment-determined": {"truth": "TRUE_ONLY"},
        "settlement-terms-recommended": {"truth": "TRUE_ONLY"},
        "procedures-recommended": {"truth": "NEITHER"},
        "icj-referral-recommended": {"truth": "NEITHER"},
        "article-38-recommendation": {"truth": "NEITHER"},
        "regional-settlement-encouraged": {"truth": "NEITHER"},
    },
    "LegalDisputeToCourt": {
        "positions": {
            "position": ("ReferUnsettledDisputeToSecurityCouncil", "SATISFIED"),
            "position_absent": "SeekRegionalSettlementFirst",
        },
        "entitled-to-attention": {"truth": "TRUE_ONLY"},
        "procedures-recommended": {"truth": "TRUE_ONLY"},
        "icj-referral-recommended": {"truth": "TRUE_ONLY"},
        "article-38-recommendation": {"truth": "NEITHER"},
        "regional-settlement-encouraged": {"truth": "NEITHER"},
        **COUNCIL_STILL_DELIBERATING,
    },
    "AllPartiesRequest": {
        "positions": {
            "position": ("ReferUnsettledDisputeToSecurityCouncil", "SATISFIED"),
            "position_absent": "SeekRegionalSettlementFirst",
        },
        "entitled-to-attention": {"truth": "TRUE_ONLY"},
        "procedures-recommended": {"truth": "NEITHER"},
        "icj-referral-recommended": {"truth": "NEITHER"},
        "article-38-recommendation": {"truth": "TRUE_ONLY"},
        "regional-settlement-encouraged": {"truth": "NEITHER"},
        **COUNCIL_STILL_DELIBERATING,
    },
    "RegionalRoute": {
        "positions": {
            "position": ("SeekRegionalSettlementFirst", "ACTIVE"),
            "position_absent": "ReferUnsettledDisputeToSecurityCouncil",
        },
        "entitled-to-attention": {"truth": "TRUE_ONLY"},
        "procedures-recommended": {"truth": "NEITHER"},
        "icj-referral-recommended": {"truth": "NEITHER"},
        "article-38-recommendation": {"truth": "NEITHER"},
        "regional-settlement-encouraged": {"truth": "TRUE_ONLY"},
        **COUNCIL_STILL_DELIBERATING,
    },
}

if __name__ == "__main__":
    raise SystemExit(main(PACKAGE, EXPECTED, "pacific-settlement"))
