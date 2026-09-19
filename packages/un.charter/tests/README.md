The package's regression battery is declarative, per DECISION-0127 ("package
tests are declarative", `spec/decisions/0127-package-tests-are-declarative.ru.md`):
the sole source of facts, questions, and expectations for the `un_charter`
family is `tests/un-charter.lawtest` (164 scenarios, `UNC-01`…`UNC-95`,
`law.toml`'s `[[tests]]` entry with `world = ["un.charter"]`). There is no
`corpus/kz/acts/un_charter.py` — this package's scenarios have never lived in
a Python runner since the migration to declarative `.lawtest` suites; both
evaluators (`lawc test`/`lawref`) read the same file and agree on all 164
scenarios, including every letter/practice divergence this package's own
README documents (Articles 23, 27) and all three disputed readings of
Article 51 — a `.lawtest` `interpretation X;` selection inside a `given`
block is read and enforced by both evaluators exactly as written; nothing
about a chosen reading is silently dropped.

Five additional, older, hand-authored scenarios (`language "law.core" version
"0.1"`, predating this package's move to the declarative `.lawtest` battery)
live in `01`-`05-*.lawtest`, under the separate `un.charter#authored` family
(`law.toml`, `regression = false` — they are not part of the corpus's
regression gate). `05-article-108-amendment-in-force.lawtest` fails under
both evaluators with an unrelated, pre-existing bug
(`truth_status == TRUE_ONLY: in the document NEITHER`), traced at stage E0
to a cause independent of this package and left untouched by every stage
since (`docs/foundations/un-charter/HANDOFF.md`) — whoever next revisits
Article 108 or this five-file suite should start there.
