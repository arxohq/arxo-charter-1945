#!/usr/bin/env python3
"""Binding or not: expectations from articles 25, 10, 12, 18, 27 and UNC-22/22B-D/30/30B/31/31B."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from _check import main  # noqa: E402

PACKAGE = Path(__file__).resolve().parent
EXPECTED = {
    "CouncilDecisionBinds": {
        "decision-adopted-active": {"truth": "TRUE_ONLY"},
        "positions": {"position": ("ComplyWithSecurityCouncilDecision", "ACTIVE")},
    },
    "CouncilDecisionComplied": {
        "decision-adopted-complied": {"truth": "TRUE_ONLY"},
        "positions": {"position": ("ComplyWithSecurityCouncilDecision", "SATISFIED")},
    },
    "AssemblyRecommendation": {
        "recommendation-power-ga-matter": {"truth": "TRUE_ONLY"},
        "positions": {"position_absent": "ComplyWithSecurityCouncilDecision"},
    },
    "AbstentionLetter": {
        "decision-adopted-abstention": {"truth": "NEITHER"},
        "decision-blocked-abstention": {"truth": "TRUE_ONLY"},
        "positions": {"position_absent": "ComplyWithSecurityCouncilDecision"},
    },
    "AbstentionPractice": {
        "decision-adopted-abstention": {"truth": "TRUE_ONLY"},
        "decision-blocked-abstention": {"truth": "TRUE_ONLY"},
        "positions": {"position": ("ComplyWithSecurityCouncilDecision", "ACTIVE")},
    },
    "ExactlyTwoThirds": {
        "important-question-adopted": {"truth": "TRUE_ONLY"},
        "important-question-not-adopted": {"truth": "NEITHER"},
    },
    "BelowTwoThirds": {
        "important-question-adopted": {"truth": "NEITHER"},
        "important-question-not-adopted": {"truth": "TRUE_ONLY"},
    },
    "BarredWhileSeized": {
        "recommendation-barred": {"truth": "TRUE_ONLY"},
        "recommendation-permitted": {"truth": "NEITHER"},
    },
    "LiftedByCouncilRequest": {
        "recommendation-barred": {"truth": "NEITHER"},
        "recommendation-permitted": {"truth": "TRUE_ONLY"},
    },
}

if __name__ == "__main__":
    raise SystemExit(main(PACKAGE, EXPECTED, "binding-or-not"))
