# Charter of the United Nations: all 111 articles, Chapters I-XIX (`un.charter`)

The corpus's first act about an organization holding power over States, not a
State itself. The jurisdiction is `International`, like its neighbours
(`csto-treaty-1992`, `rome-statute-1998`, `nuremberg-principles`,
`united-nations-1942`); the depositary of the original is the Government of
the United States (Art. 111), but the pinned bytes are a republication by the
UN Secretariat on its portal, hence `materialization_status
PINNED_UNOFFICIAL_COPY` for the text at `officiality official` (the same
reasoning as `rome-statute-1998`). As of stage E0 (18.09.2026), the package
pins a SINGLE authentic edition — English — with fragments keyed by article
number (`sources.law`, generator
`corpus/tools/sources/sync/sync_un_charter_fragments.py`). The Russian text
used during earlier drafting remains on disk at `sources/charter/ru.txt` as
evidentiary backing for the Article 111 fact that five texts are equally
authentic; it is no longer a second pinned publication of this package (see
`docs/foundations/un-charter/DECISIONS.md`).

Slice: Chapter I in full (Art. 1-2), Chapter II Art. 3, 5, 6 (original
Members, suspension, expulsion — Art. 4, admission, was already in scope),
Chapter III Art. 7-8 (organs, equal eligibility), Chapter IV Art. 9-17 and
19-22 (COMPOSITION / FUNCTIONS AND POWERS / VOTING / PROCEDURE of the General
Assembly — Art. 18, voting, was already in scope), Chapter V in full
(Art. 23-32: COMPOSITION / FUNCTIONS AND POWERS / VOTING / PROCEDURE of the
Security Council — Art. 28-32 "PROCEDURE" closed at stage E3, Art. 23-27 was
already in scope), Chapter VI in full (Art. 33-38: pacific settlement of
disputes, closed at stage E4), Chapter VII in full (Art. 39-51), Chapter VIII
in full (Art. 52-54: regional arrangements, closed at stage E5), Chapter IX in
full (Art. 55-60: international economic and social co-operation, closed at
stage E6), Chapter X in full (Art. 61-72: the Economic and Social Council —
composition, functions and powers, voting, procedure, closed at stage E6),
Chapter XI in full (Art. 73-74: declaration regarding non-self-governing
territories, closed at stage E7), Chapter XII in full (Art. 75-85: the
international trusteeship system, closed at stage E7), Chapter XIII in full
(Art. 86-91: the Trusteeship Council, closed at stage E7), Chapter XIV in
full (Art. 92-96: the International Court of Justice — Art. 92 was already in
scope, Art. 93-96 closed at stage E8), Chapter XV in full (Art. 97-101: the
Secretariat, closed at stage E8), Chapter XVI in full (Art. 102, 104-105 —
Art. 103 was already in scope, Art. 102/104-105 closed at stage E9), Chapter
XVII in full (Art. 106-107, transitional security arrangements, closed at
stage E9), Chapter XVIII in full (Art. 109 — Art. 108 was already in scope,
Art. 109 closed at stage E9), Chapter XIX in full (Art. 110 — Art. 111 was
already in scope, Art. 110 closed at stage E9). **SCOPE NOW COVERS ALL 111
ARTICLES OF THE CHARTER** — no chapter or article remains
pinned-but-unfragmented (`sources/charter/articles.json`, the `scope` field).

## The headline number: the share of letter against the share of reading

The §33.1 measure honestly shows what previously had to be ASSERTED: 85 of
ALL 111 articles of the Charter are EXECUTABLE (none of them is marked
INTERPRETED — the base is NEVER wholly silent), 26 are a declared boundary
with a reason (Art. 1, 7, 13, 15, 16, 22, 24, 26, 46, 55, 60, 62, 65, 66,
74, 75, 76, 79, 80, 81, 82, 87, 91, 92, 107, 111). The former entity-gap
and no-consumer boundaries (Art. 8, 9, 17, 21, 28–30, 57–59, 61, 63–64,
68, 70–72, 90, 95, 104, 105) are now EXECUTABLE: `Person`, `Organ`,
`SpecializedAgency`, `NonGovernmentalOrganization` and `BudgetYear` close
the type gap, Article 17's unpaid apportionment feeds Article 19's arrears
threshold, and Article 107 remains declared because Article 53 already
consumes the enemy-state carve-out at its point of use (Finding 13). `INTERPRETED` (an article whose
conclusion exists ONLY under a selected reading) is zero — and this is not a
measurement gap but a finding about the package's construction: everywhere
the letter and practice diverge (Art. 23, 27) or the text is silent on a
threshold (Art. 51), the BASE already holds at least one undisputed rule (the
five permanent members by name; voting by the letter; the grave form of the
use of force), and `interpretation` only ADDS neighbouring paths to the same
conclusion — no norm of the slice is opened for the first time by a reading.

This axis is seen more precisely at the level of RULES, not articles: of the
package's ~93 norms, six are enabled only by a selected `interpretation`
(`LowIntensityAttackIsArmedAttack`,
`CarolineStandardPermitsAnticipatorySelfDefence`,
`NonStateActorAttackImputedToHarbouringState`, `ContinuityPreservesPermanentSeat`,
`SeatTransferPreservesPermanentSeat`, `NonProceduralDecisionAdoptedDespiteAbstention`)
plus one adjacent label with no rule of its own (`NicaraguaThresholdReading` —
the narrow reading adds nothing, it simply is the unfinished base). Six rules
out of ~76 are a **for-the-first-time measurable, rather than asserted, share
of letter against the share of reading** in this act.

## Finding 1: Articles 43-47 — a dead chapter by the text, not by oversight

Agreements for the provision of armed forces under Article 43 have not been
concluded, not a single one, in the entire history of the Charter — a
well-known fact, not a measurement of the package. Formalized literally: the
duty to provide forces (Art. 43), immediately-available contingents
(Art. 45), and the right to participate in decisions on their use (Art. 44)
are all three conditioned on `special_agreement_concluded`, exactly as
required by the text ("on its call AND IN ACCORDANCE WITH A SPECIAL
AGREEMENT"). No scenario of the package asserts such an agreement as
concluded (UNC-26), and the Article 43 duty remains unreachable on any case —
not because the rule is broken, but because the premise the article itself
requires has never been true. The Military Staff Committee (Art. 47, para. 2)
is reduced to an organizational fact of membership (the Chiefs of Staff of
the permanent members), since the plans it is tasked with preparing
(Art. 46-47, paras. 1, 3-4) pertain to forces under Article 43 — which do not
exist; formalizing them separately would give voice to a chapter that has no
content in practice. Real practice goes around this through Article 42
(authorization of States by "all necessary means" — Kuwait-1991, UNC-11),
which by the letter of the text has no tie to Article 43 at all.

## Finding 2: letter against practice — twice in one package

**Article 23** names the five permanent members BY NAME, and the text has not
been amended since 1945: Russia's continuity (as successor to the USSR,
recognized without objection in 1991-1992) and the transfer of the PRC's seat
(GA resolution 2758 (XXVI), 1971) are political practice ON TOP OF the
letter, not an amendment under Article 108. The base (`package.law`) names
the five States by the names of Article 23 itself (`RepublicOfChina`,
`FranceState`, `SovietUnion`, `UnitedKingdomState`, `UnitedStatesState`);
continuity and the seat transfer add `permanent_member_seat_held_by` to the
successors THROUGH `interpretation` (`RussianContinuityReading`,
`ChinaSeatTransferReading`), without rewriting the base. The consequence is
checked by execution, not asserted: scenario UNC-17 casts the
`RussianFederation`'s vote AGAINST a decision with nine votes "for" — and
WITHOUT a selected reading this vote is INVISIBLE as a permanent member's
veto (`decision_adopted` = `TRUE_ONLY`, Art. 27, para. 3 reads only the
literal five); with `RussianContinuityReading`, the same case gives
`decision_blocked_by_permanent_member` (UNC-18). Without an interpretation,
the Security Council in its present composition cannot rely on the letter of
Article 23 at all — continuity here is not cosmetic but a condition of the
institution's workability.

**Article 27, paragraph 3** requires "the concurring votes of ALL the
permanent members"; abstention is not a vote "for", and by the letter it
blocks a decision just as a vote "against" does
(`NonProceduralDecisionBlockedByPermanentMemberLetter` — the base, ALWAYS in
effect). Council practice since 1946, blessed by the International Court of
Justice (Namibia advisory opinion, 1971, para. 22), does not treat abstention
as blocking. The pair UNC-13/UNC-14 holds BOTH answers on the same facts:
without `AbstentionDoesNotBlockReading` — `decision_adopted = NEITHER`,
`decision_blocked_by_permanent_member = TRUE_ONLY`; with the reading —
`decision_adopted = TRUE_ONLY`, AND `decision_blocked_by_permanent_member`
remains `TRUE_ONLY` on the same facts: `interpretation` adds a path to the
conclusion without overriding the base one. The mandatory abstention of a
DISPUTING party (Art. 27, para. 3, second sentence) is formalized as a `duty`
and has never once been observed in practice by a permanent member —
UNC-16 shows the duty unfulfilled (ACTIVE) when the disputing party votes
instead of abstaining.

## Finding 3: three disputed axes of Article 51, one undisputed core

The text does not define "armed attack" at all. A grave form of the use of
force by a State is an armed attack under ANY reading (Nicaragua, para. 191,
an undisputed core, needing no interpretation). The three axes of dispute are
each expressed by their own `interpretation`, ADDING a path to
`armed_attack_by`/`self_defence_permitted` rather than redefining the letter:

| axis | the letter (no reading) | the reading adds |
|---|---|---|
| threshold | only a grave form (UNC-04: `NEITHER` on a border incident) | `LowIntensityAttackReading` — a minor incident too (UNC-05) |
| anticipation | the attack must have ALREADY occurred (UNC-07: `NEITHER` on an imminent threat) | `CarolineStandardReading` — the right arises already at an imminent threat (UNC-08) |
| non-State actors | the subject is `State`-typed (UNC-09: `NEITHER` on an attack by an armed group) | `NonStateActorSelfDefenceReading` (practice after Security Council resolutions 1368/1373, 2001) — the attack is imputed to the harbouring State (UNC-10) |

Collective self-defence additionally requires a DECLARATION by the victim
State and its REQUEST to an ally (Nicaragua, para. 199) — this is the base,
not a disputed axis: UNC-06 shows the absence of the right without a
request, UNC-06B the same case with a request.

The duty to IMMEDIATELY report measures taken to the Security Council
(Art. 51, second sentence) is famously breached in practice, a duty separate
from the right itself: UNC-03 shows it ACTIVE (unfulfilled) when measures are
taken but the report is missing.

## Finding 4: Article 103 — a metanorm, not an engine priority edge

Priority between norms of ONE package is expressed by
`priority`/`priority_policy`, and they see only rules of their own stratum
(`fiqh.taqlid`: a priority cannot refer to a rule of the base). Article 103
speaks of priority between obligations under DIFFERENT treaties — the
conflicting treaty lies outside this package in principle (the Lockerbie
motif: Libya against the Montreal Convention versus Security Council
resolution 748 (1992) under Chapter VII). It is therefore expressed as an
ordinary conclusion (`charter_obligation_prevails` — an institutional fact
from `treaty_obligation_of` + `conflicts_with_charter_obligation`), not as
engine priority edges; the reasoning is recorded explicitly in
07-final-provisions.law so as not to look like an oversight (UNC-23).

## Finding 5: stage E1 — Articles 3/5/6 reuse the Article 18 threshold, Article 5 splits its own sentences

Suspension (Art. 5) and expulsion (Art. 6) are each a General Assembly
DECISION upon a Security Council recommendation — Article 18, paragraph 2
already lists both by name among the "important questions". Rather than
reasserting a two-thirds threshold, `MembershipRightsSuspendedByGeneralAssembly`
and `ExpelledByGeneralAssembly` (02-membership.law) read
`important_question_adopted`/`important_question_not_adopted`
(04-general-assembly.law) directly, tied to the specific State by the
package's generic `directed_at` link (the same one Article 25's
`SecurityCouncilDecisionBinding` uses). Article 5's two sentences are NOT one
rule: "may be suspended… by the General Assembly upon the recommendation of
the Security Council" (first sentence, a two-organ procedure) and "the
exercise of these rights and privileges may be restored by the Security
Council" (second sentence) name DIFFERENT actors — restoration reads no
Assembly fact at all, guarded only by a prior suspension having occurred.
Article 6's "persistently violated the Principles" is a §47.3 judgment
channel (`authority GeneralAssembly`) by the same reasoning as Article 4's
`peace_loving`, even though Article 6 never repeats the literal phrase "in
the judgment of the Organization" — DECISION-0194 channel 1 turns on the
LAW delegating an assessment to an organ, not on a fixed form of words.
Article 3's two branches ("having participated in the … Conference … at San
Francisco, OR having previously signed the Declaration by United Nations of
1 January 1942") are two independently sufficient named rules sharing one
head, not an `or` folded into a single body. Articles 7 and 8 (Chapter III)
are both declared, for two DIFFERENT reasons (03-organs.law): Article 7
carries no deontic marker, condition or quantity at all; Article 8 is a
genuine prohibition, but formalizing it would need a natural-person entity
this package has never modelled for any other article — an architectural
gap, not a denial of content.

## Finding 6: stage E2 — one recommendation-power conclusion, three text-named bases, one shared exception

Articles 10, 11 and 14 each grant the General Assembly a power to discuss
and recommend on a different class of matter (anything within the Charter's
scope; general peace-and-security co-operation principles or a specific
question brought before it; a situation the Assembly itself deems likely to
impair the general welfare or friendly relations), and EACH names the same
proviso — "except as provided in Article 12" (Art. 10, 11) or "Subject to
the provisions of Article 12" (Art. 14). Rather than repeating the exception
three times, all three bases feed one shared conclusion,
`general_assembly_recommendation_power` (04-general-assembly.law), and
Article 12's bar reads that one predicate, not each base separately —
the text's own triple cross-reference, not a simplification introduced by
the package. Article 12 itself follows this package's now-standard
base-rule + exception-with-positive-predicate pattern (Article 4/5/6's
`*_blocked`/`*_denied` predicates): `general_assembly_recommendation_barred`
fires on `security_council_seized_of_matter` guarded by
`not_known(security_council_requests_general_assembly_recommendation(m))`,
never by negating the power predicate itself (which would collide with the
base rule's own head without a priority declaration). Article 14's "which
it deems likely to impair" is a DECISION-0194 channel-1 judgment
(`external judgment relation …, authority GeneralAssembly`), the same
construction Article 4's `peace_loving` and Article 6's
`persistently_violated_charter_principles` already use.

**Article 19 is this stage's centrepiece, and is fully computable without
division.** "Arrears... equal or exceed... the contributions due... for the
preceding two full years" is expressed as `arrears >= annual_contribution *
2` (a `Money` comparison against a `Decimal`-scaled `Money`, never a
division of one `Money` by another — the documented engine trap
`integer division yields Rational` never arises because nothing is ever
divided). The Assembly's discretion to "permit such a Member to vote if it
is satisfied that the failure to pay is due to conditions beyond the
control of the Member" is, again, a DECISION-0194 channel-1 judgment named
directly by the text ("if it is satisfied") and attributed to the very
organ the text names as the one making the call — the base rule
`VoteForfeitedUnderArticle19` fires unless
`general_assembly_permits_vote_despite_arrears` is established, and
`VoteRetainedByGeneralAssemblyPermission` is the separate positive
predicate for the granted branch, following the same non-colliding-heads
convention as Article 12 above.

**Article 20's special-session majority is a computed threshold, not a flat
fact** — deliberately NOT reusing Article 18's `important_question_adopted`
machinery, because the denominator differs: "a majority of the Members of
the United Nations" counts ALL Members (`member_state`), not members
"present and voting". Expressed the same division-free way as Article 18:
`requesting_count * 2 > member_count`.

**Seven articles of this stage are declared, each for its own text-grounded
reason** (`sources/charter/articles.json`): Article 9 (composition —
already reused via `member_state` — and a five-representative cap this
package cannot test without a natural-person/delegate entity, the same
entity gap Article 8 logged at stage E1); Article 13 (studies and
recommendations for a stated purpose, with no addressee-conduct condition,
contrasted directly against Article 14's genuine evaluative gate); Article
15 (the Assembly receiving and considering reports — the same internal,
addressee-less register as Article 24, paragraph 3's Security-Council-to-
Assembly reporting duty); Article 16 (trusteeship functions "under Chapters
XII and XIII", chapters entirely outside this package's scope, the same
class of cross-reference boundary as Article 92's ICJ Statute); Article 17
(budgetary authority that routes back to the Assembly's own unconstrained
discretion, with no formula the text itself supplies — contrasted directly
against Article 19's genuine computable magnitude); Article 21 (rules of
procedure and Presidency — pure self-governance); Article 22 (subsidiary
organs "as it deems necessary" — the same permissive, organ-founding
register as Article 7).

## An engine limitation found during formalization

An `unless` clause of a presumption that reads ANOTHER presumption directly
resolves in the engine to `BOTH` instead of `FALSE_ONLY` — a presumption
nested inside a presumption does not close cleanly (measured on Article 2(4):
the carve-out read `self_defence_permitted`, the presumption itself; the fix
was to read the strict conclusion `armed_attack_by`, on which the
self-defence presumption itself depends first). Separately: `interpretation …
{ include PresumptionName; }` does NOT gate a presumption — it fires
regardless of the chosen reading (measured on the Caroline standard; the fix
was a strict rule instead of a presumption wherever gating is needed, at the
cost of losing the "until Security Council measures" nuance specifically for
this derived head). Both limitations are documented in the code at the point
of occurrence (01-purposes-and-principles.law, 06-enforcement.law) and are
not a gap in formalizing the Charter — they are a property of the engine
found by this act.

## Finding 7: stage E3 — participation without vote, two different tests for two different sentences

Articles 31 and 32 both grant a non-member-of-the-Council State (or, for
Article 32's second branch, a state outside the UN altogether) the right to
take part, without a vote, in a Security Council discussion — but the two
articles gate that right on DIFFERENT kinds of fact, and the package keeps
them as two SEPARATE conclusions rather than folding them into one shared
head (unlike Articles 10/11/14's shared `general_assembly_recommendation_power`
at stage E2, where the text itself names one common proviso three times).
Article 31's "may participate… whenever the [Council] considers that the
interests of that Member are specially affected" is a permission gated by a
DECISION-0194 channel-1 judgment (`security_council_considers_interests_specially_affected`,
`authority SecurityCouncil`) — the same construction as Article 39's
`article_39_determination`. Article 32's "shall be invited to participate…
if it is a party to a dispute" is a mandatory institutional entitlement
gated instead by a plain FACTUAL test a case reports directly
(`party_to_dispute_before_security_council`, `kind empirical`) — the same
class of fact as Article 27, paragraph 3's `party_to_dispute_under_chapter_six`,
not an assessment the Council makes. Article 32's own two subject classes (a
UN Member not on the Council; a state outside the UN altogether) DO share
one conclusion, `invited_to_participate_without_vote_in`, fed by two base
rules — the "two bases, one shared head" shape of the text's own single
sentence, the same pattern Article 10/11/14 used for their explicit
cross-reference.

**"Not a member" is its own positive case fact, never a negation.** Both
articles speak of a State that is NOT something (not a member of the
Security Council; for Article 32's second branch, not a Member of the UN at
all). Following the package's own established idiom (Article 4's
`security_council_recommendation_blocked` — a bare `not member_state(s)` or
`not_known(member_state(s))` would silently treat every state a scenario
simply never bothered to characterize as a confirmed non-member, which is
not what the text says), Article 31/32 introduce their own dedicated
positive `kind empirical` relations, `non_security_council_member_state`
and `non_member_state`, that a scenario must assert directly — never a
classical negation nor negation-as-failure over `member_state` itself.

**Article 32's second sentence sets no further test.** "The Security
Council shall lay down such conditions as it deems just for the
participation of a [non-Member] state" is the Council's own discretion over
WHICH conditions to impose once participation is already established by the
first sentence — no other rule of the slice reads a resulting "conditions
set" fact, so modelling it as a judgment-channel bridge would add machinery
with no consumer, the same trap the package already avoided for Article 9's
five-representative cap. Left as unformalized residue inside an otherwise
EXECUTABLE article, the same treatment Article 4 gives the 1948 ICJ advisory
opinion boundary (Finding on Article 4, 02-membership.law).

**Three articles declared, each against a verbatim precedent already in the
package.** Articles 28 (continuous organization of the Council; venue at its
own discretion), 29 (subsidiary organs "as it deems necessary" — the same
words as Article 22 and Article 7), and 30 (own rules of procedure, method
of selecting its President) repeat, almost word for word, the organizational
self-governance register already declared for Article 21 (rules of
procedure/Presidency) and Article 22/7 (subsidiary organs) — no addressee
outside the Council, no condition, no quantity in any of the three.

**A note for whoever formalizes Chapters VI and VIII (stages E4-E5):**
Article 27, paragraph 3's mandatory-abstention duty
(`DisputantMustAbstainDuty`, 05-security-council.law) already reads
`party_to_dispute_under_chapter_six(d, s)` and its own label already quotes
the text's cross-reference to "paragraph 3 of Article 52" verbatim — that
predicate is NOT extended by this stage. Article 52, paragraph 3 (regional
arrangements, Chapter VIII, stage E5) is the second limb of that same
duty's textual condition; a future stage should check whether
`party_to_dispute_under_chapter_six` needs a companion producer rule once
Chapter VI's own dispute-settlement machinery (Article 33 onward, stage E4)
and Article 52 (stage E5) exist, so that a dispute referred to the Council
under either chapter actually feeds the existing Article 27(3) duty rather
than leaving it reachable only by a bare case fact. This stage (E3) leaves
that connection untouched, as flagged by `docs/foundations/un-charter/HANDOFF.md`.

## Finding 8: stage E4 — a new `Dispute` entity, and the same evaluative phrase read through two different textual gates

Chapter VI (Articles 33-38) grants a new entity, `Dispute` (`08-pacific-settlement.law`),
distinct from `Situation` (Article 39's determination chain), `Matter`
(Articles 10-14's recommendation power) and `SecurityCouncilMatter`
(Articles 31-32's participation-without-vote tests) — following the same
"one new entity per chapter's own textual object" convention E2 and E3
established, since none of the three existing objects fits without silently
narrowing the text. All six articles of the chapter are EXECUTABLE, none
declared.

**The identical phrase "likely to endanger the maintenance of international
peace and security" is read through TWO different gates, deliberately.**
Article 33, paragraph 1's duty on the disputing parties names NO organ
making this assessment for the duty's own purposes — `dispute_likely_to_endanger_peace_and_security`
is a plain `kind empirical` case fact, the same convention already used for
Article 27, paragraph 2's `procedural_matter` and Article 32's
`party_to_dispute_before_security_council`. Article 34 ("in order to
DETERMINE whether...") and Article 37, paragraph 2 ("if the Security
Council DEEMS that...") explicitly delegate the SAME phrase to the Security
Council — `article_34_determination` and
`security_council_deems_dispute_endangers_peace` are genuine DECISION-0194
channel-1 judgments (`authority SecurityCouncil`), mirroring Article 39's
`article_39_determination`. The two readings are never unified: Article 36
and Article 37's own duty read only Article 33's plain case fact ("of the
nature referred to in Article 33"), never Article 34's separately-gated
conclusion — the text itself never cross-references Article 34's
determination from the other articles of this chapter.

**Article 37, paragraph 2 mirrors Chapter VII's own determination-then-
measures shape.** The Security Council's determination
(`article_37_determination_made`) gates a further recommendation act
(`settlement_terms_recommended`), the same two-step shape as Article 39's
determination feeding Articles 40-42's measures — the "take action under
Article 36" branch needs no separate rule, since Article 36 is reachable
independently "at any stage" of a qualifying dispute.

**Article 35's two bases (a Member; a non-Member accepting the Charter's
obligations) share one conclusion**, `entitled_to_bring_dispute_to_attention`,
the same "two bases, one head" shape Articles 10/11/14 and Article 32 use —
reusing Article 32's own "not a Member" idiom (`accepts_charter_obligations_for_dispute`
alongside `non_member_state`, never a negation of `member_state`).

**Article 36's two paragraphs (procedures; ICJ referral for legal disputes)
are both genuinely EXECUTABLE despite "should" rather than "shall"** — the
advisory REGISTER does not change that the text names a determinate,
testable act (the Council recommends X), the same reasoning already applied
to Article 4's own "shall recommend". The ICJ-referral rule terminates at
the institutional-fact level (Art. 92's declared ICJ Statute boundary is
untouched). **Article 38 is a distinct, request-gated power that deliberately
does NOT read Article 33's threshold** — the text's own "without prejudice
to the provisions of Articles 33 to 37" makes it broader ("any dispute"),
not a continuation of the same chain.

**Three residues left unformalized, none as a separate `declared` entry**
(the article as a whole is EXECUTABLE via its other clauses, the same
treatment as Article 32's second sentence): Article 33, paragraph 2 (the
Council's own "call upon" power, not a trigger of the paragraph 1 duty);
Article 35, paragraph 3 (a cross-reference to Articles 11/12's `Matter`-typed
machinery — bridging `Dispute` and `Matter` would add a producer/consumer
relationship the text never states as such); Article 36, paragraph 2 (a
direction on HOW to exercise the recommending power, not a separate
condition).

**The Article 27(3)/Article 52(3) connection flagged at E3 is STILL not
built.** `party_to_dispute_under_chapter_six` (Article 27, paragraph 3,
keyed to a `Decision`) and this stage's own `party_to_dispute` (keyed to a
`Dispute`) remain two separate relations on two separate entity types — no
rule of this package maps a `Decision` to the `Dispute` it concerns. Left
for Article 52, paragraph 3 (Chapter VIII, stage E5) or the integration
stage (E10) to consider, per `docs/foundations/un-charter/HANDOFF.md`'s
open items.

## Finding 9: stage E5 — Chapter VIII closes the Article 27(3)/52(3) bridge, a prohibition without a `State`-typed bearer, and a dead-letter exception kept minimal

Chapter VIII (Articles 52-54, regional arrangements) is now formalized in
full, closing the last open item E3/E4 flagged for the Article 27(3)/
Article 52(3) cross-reference. All three articles are EXECUTABLE.

**Article 52 reuses Chapter VI's `Dispute` entity with a QUALIFYING FACT,
not a parallel entity.** "Local disputes" (Art. 52, paragraphs 2-3) are the
same kind of object Chapter VI already models — paragraph 4's own savings
clause ("This Article in no way impairs the application of Articles 34 and
35") confirms Articles 34-35 apply to the very same disputes — so `local_dispute`
is a positive qualifier on a `Dispute` (09-regional-arrangements.law), the
same anti-duplication convention CLAUDE.md states for a neighbour's `pub`
type (no bridge twins). Paragraph 2's duty
(`DutyToSeekRegionalSettlementFirst`) mirrors Article 33's
`SeekPeacefulSettlementFirst` rule for rule — a Member that has entered a
regional arrangement and is party to a local dispute must make every effort
at regional settlement before referring the dispute to the Council.
Paragraph 3's Council encouragement (`Article52ParagraphThreeEncouragement`)
is a flat institutional act of will, the same construction as Article 36's
recommendation acts, never a DECISION-0194 judgment channel (no organ is
asked to ASSESS anything; the Council simply acts). Paragraph 1 (nothing
precludes regional arrangements "provided that... consistent with the
Purposes and Principles") and paragraph 4 (the savings clause) are left as
unformalized residue inside an otherwise EXECUTABLE article — no organ is
named to assess paragraph 1's consistency proviso, and no rule of this
chapter or any other reads a "the arrangement is valid" fact as a gate
(Article 53's authorization requirement applies regardless), the same "some
predicate could technically be written" trap already avoided for Article 9,
Article 32's second sentence, and Article 33's paragraph 2.

**Article 53 is this stage's centrepiece: a genuine PROHIBITION, modelled
without a `duty`, because its actor is never `State`-typed in this
package.** Unlike Articles 41-42's `force_authorized` (an ENABLING fact
other rules read to permit further consequences), "no enforcement action
shall be taken under regional arrangements... without the authorization of
the Security Council" is a prohibition whose ACTOR is a regional
arrangement or agency — an entity this package has never modelled as
`State`-typed (only its Member States are), so a `duty` with `bearer:
State` would misattribute the obligation to one Member rather than to the
arrangement's own enforcement act. Following this package's own
established exception idiom (a positive predicate for the negative branch,
never a negated head — `general_assembly_recommendation_barred` at E2):
`regional_enforcement_action_unauthorized` is a separate positive
institutional conclusion, guarded by `not_known(...)` over BOTH the
ordinary Council-authorization branch and the enemy-state exception, never
a negation of `regional_enforcement_action_authorized` itself (which would
collide with that predicate's own head without a `priority` declaration,
§116). The two authorization branches — Council authorization
(`RegionalEnforcementActionAuthorizedBySecurityCouncil`) and the enemy-state
exception (`RegionalEnforcementActionExemptAsEnemyStateMeasure`) — share one
conclusion, the same "two bases, one head" shape Article 35 uses.

**The enemy-state exception (paragraph 1's proviso, paragraph 2's
definition) is formalized by the letter, as ONE flat case fact, deliberately
NOT built into a live escape hatch.** The exception is alive in the text and
dead in practice — the same divergence this package already documents for
Articles 43-47 (Finding 1: agreements under Article 43 have never been
concluded). Unlike Article 43-47's chain (formalized with its full
conditional structure, simply never triggered because its own premise has
never held), Article 53's carve-out gets the MINIMAL literal treatment:
`enemy_state_measure_under_article_107` is a single flat `kind empirical`
relation a case COULD assert, but no scenario of this package's own test
corpus ever does (UNC-50 is the only scenario that exercises it at all, and
does so precisely to show the branch exists, not that it is live). No
"which States count as an enemy state under the Second World War
definition" lookup chain (paragraph 2's own definitional sentence) is
built — no other rule of this package would ever consume it, the same trap
already avoided for Article 9's five-representative cap.

**Article 54 is a duty on each Member of the regional arrangement, the same
shape as Article 51's reporting duty.** "The Security Council shall at all
times be kept fully informed of activities undertaken or in contemplation
under regional arrangements..." is passive — the text names no addressee
directly — but Article 52, paragraph 2 already establishes that Members
entering a regional arrangement bear the arrangement's Charter-facing
obligations; Article 54 is read the same way, as a duty on each Member of
the arrangement under which the activity is undertaken, keyed to the
specific activity and the specific Member (`DutyToKeepSecurityCouncilInformed`),
mirroring `ReportSelfDefenceMeasuresDuty` (Art. 51, second sentence).

**The Article 27(3)/Article 52(3) bridge, flagged at E3 and E4, is now
built — as an ADDED path, not a rewrite.** `RegionalDisputePartyMustAbstainViaArticle52`
(05-security-council.law) reads a new bridge fact,
`security_council_decision_under_article_52_paragraph_3(d: Decision, disp:
Dispute)`, together with `local_dispute(disp)` and `party_to_dispute(disp,
s)` (09-regional-arrangements.law, 08-pacific-settlement.law), to derive
`party_to_dispute_under_chapter_six(d, s)` — the SAME premise
`DisputantMustAbstainDuty` already read since the original slice. The base
duty rule is UNCHANGED: this stage adds a SECOND producer path to its
existing premise, exactly per the multisession prompt's rule #1 (letter in
the base, added paths only). The pre-existing UNC-13/14/16/17/18 scenarios
(letter/practice divergence on Article 23/27, the original bare-case-fact
abstention duty) pass unchanged, confirming the addition is genuinely
additive. The OTHER half of the same cross-reference — a Chapter VI dispute
referred to the Council under Article 37 (`dispute_referred_to_security_council`,
keyed to `(Dispute, State)`, not to a specific `Decision`) — remains
deliberately unbridged: inventing a Decision-level referent for it would
repeat the "predicate nobody reads" over-reach this package's own
convention already avoids elsewhere.

## Finding 10: stage E6 — Chapter IX/X are the most `declared`-heavy stage yet, and for text-grounded reasons, not fatigue

Chapters IX (Art. 55-60, international economic and social co-operation) and
X (Art. 61-72, the Economic and Social Council) are now formalized: three of
eighteen articles EXECUTABLE (56, 67, 69), fifteen declared. This is the
package's own highest declared-to-executable ratio so far, and by design:
Chapter IX is a statement of purposes plus institutional-competence grants
between organs, and Chapter X is overwhelmingly ECOSOC's own discretionary
functions (Articles 62, 64, 66) and self-governance (Articles 61, 68, 72).

**Article 56 is a genuine, if broad, duty on every Member — the chapter's
centrepiece.** "All Members pledge themselves to take joint and separate
action in co-operation with the Organization for the achievement of the
purposes set forth in Article 55" names a determinate addressee (every
Member) and a determinate kind of conduct — unlike Articles 57-60, which name
no party's conduct at all. Article 55's own list of purposes is read as ONE
undecomposed textual anchor folded into a single relation
(`cooperates_for_article_55_purposes`), not split into three separately typed
goals: no rule of this package, present or foreseeable, needs to distinguish
WHICH Article 55 purpose is at stake for a given act of co-operation.
`DutyToCooperateForArticle55Purposes` (10-economic-social-cooperation.law)
mirrors Article 33's `SeekPeacefulSettlementFirst` and Article 52's
`SeekRegionalSettlementFirst` — an open-ended achieve-duty with no fixed
deadline, the package's established idiom for a standing obligation.

**Article 61's composition follows Article 23's own precedent: declared as
BASE FACTS, not a computed validity-checker.** Article 61 names genuinely
computable numbers (fifty-four Members, eighteen elected annually, three-year
terms, immediate re-election permitted) — but no rule of this package's
declared scope ever asks "was this ECOSOC composition validly elected" or
"is this Member's ECOSOC term still active on date D": Articles 65, 67 and 69
all read `member_state`/votes directly, never an ECOSOC-seat-specific fact.
Building a live election/term-tracking rule would manufacture a consumer
that does not exist, and would need calendar/staggered-term machinery this
package has never needed elsewhere — declared for the SAME reason Article
23's composition is (a precedent, not a shortfall).

**Article 67 reuses the shared voting model (`Decision`,
`casts_vote_for`/`casts_vote_against`/`abstains`) already built for the
General Assembly (Art. 18) and Security Council (Art. 27), with a THIRD,
simpler threshold.** "Decisions... shall be made by a majority of the members
present and voting" is exactly Article 18, paragraph 3's own ordinary-
question threshold — no two-thirds branch exists for ECOSOC. A binding
marker fact, `is_ecosoc_decision`, plays the same role
`is_important_question`/`is_ordinary_question` play for Article 18: the
shared `Decision` entity carries no organ of its own, so a case must report
directly which decisions are the Council's. `ecosoc_decision_adopted` keeps
this organ's own conclusion apart from the General Assembly's and Security
Council's, even though all three read the same underlying `Decision` type.

**Article 69 is EXECUTABLE via a new entity, `EcosocMatter`; Articles 70-71
are declared for an ENTITY-GAP reason, not for lacking conditional content.**
Article 69's "any matter of particular concern to that Member" names no
organ making that assessment (unlike Article 31's "the Security Council
considers... specially affected"), so `matter_of_particular_concern_to` is a
plain case-reported fact, not a DECISION-0194 channel — the same reasoning
already applied to Article 33's "likely to endanger" threshold against
Article 34/37's organ-delegated phrasing of the identical words (Finding 8).
The participating subject of Article 69 is a Member STATE, fitting `State`
directly; `EcosocMatter` covers only the "matter" itself, following the
established "one entity per chapter's own object" convention (`Matter`,
`SecurityCouncilMatter`, `Dispute`, `RegionalArrangementActivity`). Articles
70 and 71, by contrast, name a specialized-agency representative and a
non-governmental organization as their OWN participating subjects — neither
fits `State`, and this package has never modelled either kind of actor: the
same entity-gap boundary already logged for Article 8's eligibility clause
and Article 9's delegation cap, not a judgment that these articles lack
deontic content.

**Three articles (61, 63, 65) are declared for a text-grounded
"no-consumer" reason distinct from the usual entity/register gaps.** Article
61's numbers are genuinely computable (see above); Article 63's
agreement-and-approval chain and Article 65's "shall assist... upon its
request" duty are both real, testable conditions — but no OTHER rule of this
package's declared scope would ever read the resulting fact (no article
tests specialized-agency status against a case; no article reads "ECOSOC
assisted the Security Council"). Formalizing them anyway would repeat the
"some predicate could technically be written" trap already avoided for
Article 9's delegation cap, Article 32's second sentence, and Article 52's
paragraph 1 — logged here as its own category because, unlike those
precedents, the missing piece is not an entity gap but a genuine absence of
any consumer within the package's own declared scope.

## Finding 11: stage E7 — non-self-governing territories, the trusteeship system, and a third organ that reuses the shared voting model

Chapters XI (Art. 73-74, declaration regarding non-self-governing
territories), XII (Art. 75-85, the international trusteeship system) and
XIII (Art. 86-91, the Trusteeship Council) are now formalized: nine of
nineteen articles EXECUTABLE (73, 77, 78, 83, 84, 85, 86, 88, 89), ten
declared. Two new entities, `NonSelfGoverningTerritory`
(12-non-self-governing-territories.law) and `TrustTerritory`
(13-trusteeship-system.law), are deliberately DISJOINT from one another,
following Article 73, paragraph (e)'s own closing words ("other than those
territories to which Chapters XII and XIII apply") — the text itself states
that the two populations never overlap, so no qualifying-fact bridge (the
device Article 52 used to fold "local disputes" into Chapter VI's `Dispute`)
applies here.

**Article 73 is EXECUTABLE via paragraph (e) alone — a narrow, well-defined
reporting duty, the chapter's centrepiece.** Paragraphs (a)-(d) ask an
administering Member to "ensure... advancement", "develop self-government",
"further international peace and security" and "promote constructive
measures of development" — open-ended, aspirational, no organ assessing
compliance, no determinate act a case could report — left as unformalized
residue, the same treatment Article 33's paragraph 2 and Article 52's
paragraph 1 already receive. Paragraph (e), by contrast, names a determinate
bearer (the administering Member) and a determinate achievable act
(transmitting information to the Secretary-General): `TransmitTerritorialInformation`
mirrors Article 56's pledge and Article 84's duty below exactly. Article 74
is declared on its own — the SAME open-ended-policy-directive register, but
as the whole of a separate article rather than residue inside another.

**Article 77's three categories of trusteeable territories are EXECUTABLE
even though no other rule of this package's declared scope reads the
conclusion — a deliberate choice, not an oversight.** Unlike Articles
61/63/65 (Finding 10), declared BECAUSE no consumer exists, Article 77 names
three textually concrete, independently testable classifications (mandate;
detached from an enemy state; voluntarily placed) feeding one shared head,
`territory_placeable_under_trusteeship_system` — the same "N bases, one
head" shape as Articles 10/11/14 and Article 32's two subject classes. The
categorical test is real content worth keeping EXECUTABLE on its own
textual merit.

**Article 78 reuses `member_state` (02-membership.law) directly for the
package's only Chapter XI-XIII cross-entity link.** "The trusteeship system
shall not apply to territories which have become Members of the United
Nations" ties a `TrustTerritory` to the `State` it has become via a
dedicated bridging fact, `trust_territory_became_member_state` — a case
reports the correspondence directly, the same register as the correspondence
itself (a fact about the territory's subsequent history). The exclusion,
`trusteeship_system_inapplicable`, is a genuinely POSITIVE conclusion: unlike
Article 12 or Article 19's exceptions, nothing else in this package ever
asserts "the trusteeship system applies" as an institutional fact to defeat,
so no `not_known`/`priority` machinery is needed at all.

**Articles 82-83/85 are the stage's second flagged centrepiece: a genuine
Security-Council/General-Assembly competence split over strategic and
non-strategic areas.** Article 82's designation of a strategic area is read
directly as a case premise (`is_strategic_area`), the same register as
`member_state`/`permanent_member` themselves — declared on its own, since the
designation act IS the fact Article 83 reads. Article 83's "all functions...
relating to strategic areas... shall be exercised by the Security Council"
and Article 85's identical sentence for "areas not designated as strategic...
exercised by the General Assembly" produce two SEPARATE competence
conclusions, never a shared head needing a `priority` declaration. Following
this package's own "absence of a fact is not its negation" convention
(Articles 31/32/35's `non_member_state`-style relations), a dedicated
positive relation, `non_strategic_area`, carries the Article 85 branch — a
case must assert it directly, never infer it from the mere absence of
`is_strategic_area`.

**Article 86's composition parity is the stage's third flagged centrepiece —
a genuine structural-arithmetic test, the same register as Articles
27/109's vote thresholds.** A new entity, `TrusteeshipCouncilComposition`,
represents one proposed or actual composition at a point in time; a case
reports which States count on the administering side
(`counted_as_administering_member_of`) and which on the non-administering
side (`counted_as_non_administering_member_of`), and
`TrusteeshipCouncilCompositionParity` checks the two counts for direct
equality (`==`), no new engine machinery, the same idiom as Article
18/27/67/89's own cross-multiplication thresholds. Paragraph 2's individual
representative is left as unformalized residue — the same natural-person
entity gap already logged for Article 9's delegation cap.

**Article 89 reuses the shared voting model a THIRD time (after Article 18's
General Assembly and Article 67's ECOSOC).** "Decisions of the Trusteeship
Council shall be made by a majority of the members present and voting" is,
once again, Article 18, paragraph 3's own ordinary-question threshold; a new
binding marker, `is_trusteeship_council_decision`, plays the same role
`is_ecosoc_decision` plays for Article 67. Article 88's annual-report duty
(`SubmitAnnualTrusteeshipReport`) mirrors Article 84's shape exactly, on the
same `administers_trust_territory` addressee.

**The Trusteeship Council's suspension of operations since 1994 is noted as
practice, never built as a rule** — the same "letter in base, practice as
commentary only" treatment Article 23's continuity and Article 27's
abstention practice already receive (Finding 2); see "What this package does
not do" below.

## Finding 12: stage E8 — the Court's own Statute stays outside, and the package acquires its first officer

Chapter XIV (Articles 92-96, the International Court of Justice) and Chapter
XV (Articles 97-101, the Secretariat) are now formalized in full: eight of
the nine articles added at this stage are EXECUTABLE (93, 94, 96, 97, 98, 99,
100, 101), one is declared (95), and Article 92 keeps the declared status it
already had.

**The Statute of the Court is a declared boundary, and every rule of Chapter
XIV stops short of it.** Article 92 calls the annexed Statute "an integral
part of the present Charter", but the Statute is a separate text this package
neither pins nor fragments. Article 93 therefore answers only WHO is a party
to the Statute; Article 94 answers only what a party must do about a decision
and what the other party may do if it does not; Article 96 answers only who
may put a legal question to the Court. None of them models the Court's
composition, its jurisdiction, its procedure, or what it does with a request
once made — the same boundary Article 36, paragraph 3's ICJ-referral rule
already respected at stage E4.

**Article 93, paragraph 1 is a pure derivation from `member_state`.** "Ipso
facto" means precisely that no act, assertion or condition stands between
membership and party status, so the rule reads the existing `pub` relation
directly and nothing else. Paragraph 2's non-Member route is a genuine
approval chain reusing this package's "not a Member" idiom
(`non_member_state`, never a negation of `member_state`), and the two routes
share one head — the same "N bases, one head" shape as Articles 10/11/14,
32, 35 and 77.

**The General Assembly step of Articles 93(2) and 97 is a flat fact, and the
textual basis for that was checked rather than assumed.** Article 18,
paragraph 2's list of "important questions" was read against both articles:
it names neither the conditions on which a non-Member joins the Statute nor
the appointment of the Secretary-General, so nothing in the text supports a
two-thirds threshold in either place; under paragraph 3 both would be
ordinary questions decided by a simple majority. Rather than unroll a vote
whose threshold the text does not single out, both follow Article 4's own
convention (`general_assembly_decides_admission`, a flat empirical fact even
though admission IS on the paragraph 2 list). The vote-threshold machinery
stays reserved for articles whose own text turns on the threshold (5, 6, 18,
67, 89).

**Article 94 is the stage's centrepiece: a duty plus a remedy chain, in three
steps.** Paragraph 1's undertaking to comply with a decision of the Court is
a duty of exactly the shape Article 25's `ComplyWithSecurityCouncilDecision`
already has — the nearest textual sibling in the package, both being
undertakings to carry out an organ's decision. Paragraph 2 then stages the
remedy the way the text itself stages it: an ESTABLISHED failure to perform
opens the OTHER party's recourse to the Security Council, and the Council's
own power to make recommendations or decide upon measures is gated on a
DECISION-0194 channel-1 judgment ("if it deems necessary", `authority
SecurityCouncil`, the same construction as Articles 34, 37 and 39). The
failure to perform is its own positive relation, never the absence of
compliance: a duty going unsatisfied in a scenario is a different statement
from a judgment having been defaulted on. The prompt's requested cross-cutting
scenario — non-performance of an ICJ judgment feeding Article 94(2) — is
built here in full (UNC-66/66B/67/67B), not deferred: every fact it needs
lives in this chapter, and UNC-67 shows the compliance duty still ACTIVE at
the same moment the Council's own power opens.

**Article 96 introduces `RequestingBody`, and the two named organs are
asserted BY NAME from the letter.** Paragraph 1 grants the General Assembly
and the Security Council an unconditional power over any legal question;
paragraph 2 grants other organs and specialized agencies the same power
subject to a General Assembly authorization AND the question arising within
the scope of their own activities. The two organs are `assert`ed by name
under `@source(UNC_EN_ART96)`, exactly as Article 23's five permanent members
are asserted in `package.law`. This is a deliberate, narrow departure from
the entity-gap reason that declared Articles 70-71 at stage E6: there, the
specialized-agency subject sat in an article with no testable consequence of
its own, so the entity would have bought nothing; here the consequence is
determinate and the entity carries the real distinction between paragraph 1's
unconditional power and paragraph 2's gated one.

**Article 95 is declared as a pure non-preclusion clause.** "Nothing in the
present Charter shall prevent Members… from entrusting the solution of their
differences to other tribunals" withholds a restriction rather than imposing
a condition; the only thing it could formalize is the ABSENCE of a rule this
package never asserts. The "shall" belongs to the Charter itself, not to a
party — the same register as Article 80's savings clause and Article 52,
paragraph 4's proviso.

**Chapter XV gives the package its first officer entity, and this is where
stage E1's Article 8/9 boundary deliberately stops.** Articles 8 and 9 were
declared at E1 with a stated reason — no natural person had ever been
modelled, and introducing one for a single article no other rule consumed
would be machinery bought for nothing — and with an explicit forward pointer
to "a future session working on Art. 97/101 (individual officers)". Chapter
XV is about its officers from end to end: five articles consume
`SecretariatOfficial`, four of them through rules. The entity now earns its
place on exactly the test Articles 8 and 9 failed. Membership of the
Secretariat is DERIVED, not asserted: Article 97's own first sentence
("the Secretariat shall comprise a Secretary-General and such staff…") is
read as a two-branch definition feeding one head, so that sentence does real
inferential work rather than sitting as organizational scenery, and a case
cannot report a staff member who is somehow not of the Secretariat.

**Article 99 is the package's clearest DECISION-0194 channel, and its first
one held by an officer rather than an organ.** "Any matter WHICH IN HIS
OPINION may threaten the maintenance of international peace and security"
names the holder of the evaluative call in the article's own words, so
`authority SecretaryGeneral` joins `GeneralAssembly` and `SecurityCouncil` as
a value of this package's judgment channels (`authority` is a free
identifier; extending it is additive and needs no core change). That the
holder is the officer and not the Council is exactly what distinguishes an
Article 99 referral from Article 35's Member-driven referral and Article 34's
Council-driven determination of the same subject matter. Like Articles 35 and
96, the rule models the POWER, not its exercise: whether a discretionary
power was used is not a condition of having it, so the meaningful negative
case is the absence of the Secretary-General's own opinion, not the absence
of a referral.

**Article 100 is the only article in the package whose two paragraphs bind
two different classes of bearer over one subject matter, and both directions
are built.** Paragraph 1 binds the Secretary-General and the staff (not to
seek or receive external instructions, and to refrain from action reflecting
on their position as international officials); paragraph 2 binds each Member
(to respect that exclusively international character and not to seek to
influence them). Two separate duties with two separate bearers and two
separate discharge facts — folding them into one would have to pick a bearer
and silently drop half the article. UNC-73 exercises both at once: a Member's
duty ACTIVE while the officer's own duty is SATISFIED.

**Article 101 is EXECUTABLE through paragraph 1, whose condition is genuine
and whose evaluative residue is left alone.** "Appointed by the
Secretary-General under regulations established by the General Assembly"
carries two testable conditions, not one, and an appointment outside those
regulations does not satisfy it (UNC-74B). Paragraph 3's "paramount
consideration… efficiency, competence, and integrity" and its "due regard…
to… as wide a geographical basis as possible" were both checked against
DECISION-0194's own test and are NOT channels: neither sentence names any
organ or officer as the holder of the balance between the two considerations
(contrast Article 99's "in his opinion", Article 31's "the Council
considers", Article 14's "it deems"). Making either a judgment relation would
invent a judge the text does not appoint; making them bare case facts would
leave an evaluative fact with no producer. Both stay unformalized residue
inside an EXECUTABLE article, as does Article 97's third sentence ("chief
administrative officer" — a copula in the same descriptive register as
Article 92's own declared "shall be the principal judicial organ") and
Article 98's first sentence.

## Finding 13: stage E9 — the scope closes at 111 articles, a genuine bar bridged to Article 103, and a vote that deliberately bypasses the veto

Chapters XVI (Miscellaneous Provisions), XVII (Transitional Security
Arrangements), XVIII (Amendments) and XIX (Ratification and Signature) are
now formalized in full: four of the seven articles added at this stage are
EXECUTABLE (102, 106, 109, 110), three are declared (104, 105, 107). Combined
with the 104 articles already in scope through stage E8, **`sources/charter/articles.json`'s
`scope` now covers all 111 articles of the Charter — no chapter or article
remains pinned-but-unfragmented.**

**Article 102 is a genuine bar, and the bridge to Article 103 the task brief
requested is built as two independent conclusions over the SAME entity, not
one gating the other.** Paragraph 1's registration duty and paragraph 2's bar
on invocation both read `TreatyObligation` (`package.law`), the entity
Article 103 has used since the original slice — no bridge twin.
`invocable_before_un_organ` (registered) and `barred_from_invoking_before_un_organ`
(unregistered, `not_known`-guarded, the package's established exception idiom)
are two separate positive conclusions over one base fact,
`registered_with_secretariat`, never a negated head. Article 103's own rule
(`CharterObligationsPrevailOverConflictingTreaty`) is UNCHANGED by this
stage — no premise on registration was added to it, because registration
status is ORTHOGONAL to the priority test: an unregistered treaty obligation
can still exist, still conflict with a Charter obligation, and still lose
that conflict under Article 103, entirely independently of whether it may be
invoked before a UN organ. UNC-76 builds exactly the scenario the task brief's
own completion criteria named — an unregistered treaty against Article 103 —
and both conclusions hold simultaneously on the same `TreatyObligation`/
`State` pair: the treaty is barred from invocation AND the Charter obligation
prevails, two independent findings, not a chain.

**Article 106 reuses the Article 43 dead chain directly, as a global
aggregate, rather than inventing a second "is the system operative" flag.**
"Pending the coming into force of such special agreements referred to in
Article 43…" is the "meanwhile" clause of the very same chain Finding 1
already documents (not one Article 43 agreement has ever been concluded in
the Charter's history): the rule reads `special_agreement_concluded`
(06-enforcement.law) through `(count distinct o: State where
special_agreement_concluded(o)) == 0`, so the pending condition is exactly
"no Member has one", with no new predicate duplicating that fact. The parties
to the 1943 Four-Nation Declaration are, textually, the SAME five States
Article 23 already names as permanent members (after France's accession)
— `permanent_member` (package.law) is read directly, no new entity. Because
the Article 43 system has never come into force, this duty has been live, in
principle, for the Charter's entire history — a STANDING rather than
one-time dormancy, unlike Articles 43-47's own dead branch, which UNC-77C
demonstrates directly: asserting a single concluded special agreement
anywhere defeats the pending condition and the duty disappears from the
document entirely (`evaluate positions()` reports none), the same idiom
UNC-26 already established for Article 43 itself.

**Article 107 is declared, deliberately NOT a second, wider carve-out beside
Article 53's existing one.** The general non-preclusion clause behind the
SAME enemy-state exception Article 53, paragraph 1 already formalizes at its
point of actual use (`enemy_state_measure_under_article_107`,
09-regional-arrangements.law, Finding 9) is broader in principle ("action" at
large, not only regional enforcement action) but no rule of this package's
scope other than Article 53's own exception would ever read a general
enemy-state fact — building a second carve-out here would repeat exactly the
"predicate nobody reads" over-reach Article 53's own stage already declined
(no WWII-enemy-state lookup chain). Declared, with the identical rationale
logged against Article 53, not reinvented.

**Article 109 is the vote-asymmetry centrepiece the task brief flagged, and
the asymmetry is real, not a modelling artefact.** Paragraph 1's CONVENING
vote needs "a two-thirds vote of the members of the General Assembly" (the
same all-members threshold Article 108's adoption step uses) AND "a vote of
ANY NINE members of the Security Council" — the pinned text (post-1968
amendment) names nine members, not nine including the five permanent
members' concurrence, so `GeneralConferenceConveningApprovedBySecurityCouncil`
counts `casts_vote_for` directly and reads NEITHER
`permanent_member_seat_held_by` NOR Article 27, paragraph 3's veto machinery
at all — UNC-79 demonstrates this literally, with none of the nine voting
States a permanent member. Paragraph 2's alteration-ratification step is the
IDENTICAL named-lock test Article 108 already performs ("ratified… by two
thirds of the Members… including all the permanent members"), so this stage
adds no new predicate for the same effect: `AlterationEntersIntoForceViaArticle108Ratification`
and `AlterationBlockedByMissingPermanentRatification` are a SECOND PRODUCER
PATH into Article 108's own conclusions (`amendment_in_force`,
`amendment_blocked_missing_permanent_ratification`), the same "second path
into an existing head" shape as the Article 27(3)/Article 52(3) bridge
(Finding 9) — Article 108's base rules and their original path are
unchanged. Paragraph 3's fallback is formalized by the letter EXACTLY as the
pinned text preserves it: "any seven members of the Security Council", the
figure the 1968 amendment left untouched because, as the pinned publication's
own colophon records, the paragraph was already acted upon in 1955 at the
Assembly's tenth regular session — alive in the text, spent in practice, the
same register Finding 1 gives Articles 43-47.

**Article 110's live branch is a third basis into Article 3's existing
`original_member` head, not a parallel concept.** Paragraphs 1-3 (ratification,
deposit, coming into force) describe a one-time historical event this
package's own `law.toml`/`sources.law` already record as concluded
(`legalStatus = "in_force"`) — residue, not a gap, since no rule of this
package's scope would ever re-test whether the Charter itself has entered
into force. Paragraph 4 is different: a State that ratifies AFTER entry into
force becomes an original Member exactly as one that ratified before it, so
`OriginalMemberByRatificationAfterEntryIntoForce` extends Article 3's own
two-branch idiom (02-membership.law) to a third branch, reading its own new
premise (`ratifies_after_charter_in_force`) — `ratifies_charter`, Article 3's
original premise (deliberately left unwired to Article 110's mechanics at
stage E1, "Article 110 itself lies outside the declared slice"), is
UNCHANGED, so every pre-E9 scenario built on it is unaffected.

## Finding 14: stage E10 — integration closes the multisession task; the seven cross-cutting scenarios were mostly already there

Stage E10 is pure integration, not new formalization: the scope, the base
rules and every prior finding above are unchanged. Its job was to check the
seven cross-cutting scenarios the multisession prompt's own completion
criteria (§11) named, close the one genuine gap among them, finalize this
README, and settle the long-open `geneva-1949` question. Each of the seven is
addressed here explicitly, by reading the actual `.lawtest` content, not by
trusting a prior stage's own report of itself:

1. **Admission → suspension → expulsion.** Stage E1 covered Article 4
   (UNC-20/21), Article 5 (UNC-28/28B/28C) and Article 6 (UNC-29/29B) — each
   in full, on its own throwaway State entity (`candidate`, `suspended`,
   `expelled`). Reading `02-membership.law` directly: none of Article 5 or 6's
   rules take `admitted_to_membership`/`membership_rights_suspended` as a
   precondition — each reads only its own empirical facts about the State, so
   there was no logical chain for a shared entity to expose. This is a
   genuine gap in the NARRATIVE the prompt asks to see, not a logical one:
   **UNC-86** (new, this stage) closes it with one scenario, one State, one
   `given` block, and three `evaluate`/`expect` pairs in sequence — admitted,
   then suspended, then expelled — the same multi-query-per-test shape UNC-49
   already used for Article 53's two institutional conclusions.
2. **Article 19 arrears.** UNC-33/33B/33C (stage E2) already cover the
   forfeiture threshold, the below-threshold non-forfeiture, and the
   Assembly's own discretion to excuse it — confirmed unchanged, no new
   scenario needed.
3. **A Chapter VI dispute with mandatory abstention.** UNC-52/52B (stage E5)
   already exercise the Article 27(3)/Article 52(3) bridge on a genuine
   Chapter VI `Dispute` entity qualified `local_dispute` — a permanent member
   party to the dispute either votes instead of abstaining (`AbstainAsDisputant`
   ACTIVE) or abstains (SATISFIED). Confirmed by reading the scenario body
   directly, not the stage's own summary: this already is the Chapter-VI-
   flavoured dispute the prompt asks for, no new scenario needed.
4. **Regional enforcement without Security Council authorization.** UNC-49/49B
   (stage E5) already hold both directions — authorized action (`regional_enforcement_action_authorized`
   TRUE, `_unauthorized` NEITHER) and unauthorized action (the reverse) — on
   two independent institutional conclusions, confirmed unchanged.
5. **Non-performance of an ICJ judgment → Article 94(2).** UNC-66/66B/67/67B
   (stage E8) already build the full three-step chain — an established
   failure to perform opening recourse, its absence without one, the
   Council's own measures once it deems them necessary, and their absence
   without that judgment — confirmed unchanged.
6. **Unregistered treaty (Art. 102) against Art. 103.** UNC-76 (stage E9)
   already holds both `barred_from_invoking_before_un_organ` and
   `charter_obligation_prevails` TRUE on the same unregistered, conflicting
   `TreatyObligation`, demonstrating the two conclusions coexist rather than
   chain (Finding 13) — confirmed unchanged.
7. **Amendment (Art. 108) against revision by conference (Art. 109).** This
   DSL's own contract for a `.lawtest` test is one query per `evaluate`/`expect`
   pair sharing the enclosing test's fact base, so no SINGLE scenario can
   "run" both Article 108's route and Article 109's route as one query — the
   two routes are instead exercised side by side as designed: UNC-24/25 (Art.
   108's own `amendment_adopted_by_general_assembly` route) and UNC-81/81B
   (Art. 109, paragraph 2's `general_conference_alteration_vote` route) reach
   the IDENTICAL head, `amendment_in_force`/`amendment_blocked_missing_permanent_ratification`
   (Finding 13, "a second producer path, not a new predicate") — the contrast
   the prompt asks for is the fact that two textually different procedures
   conclude in the same predicate, which is exactly what having them as two
   separate, passing scenarios over one shared head demonstrates. No new
   scenario was manufactured for this item; the existing four already are the
   side-by-side comparison.

**The `geneva-1949` consumer question, open since stage E0, is resolved as a
documentation correction, not a new dependency.** `intl/geneva-1949` has no
`law.lock` at all and does not import `un.charter` as a compiled dependency —
its only reference is a one-line thematic comparison in a `law.toml` comment
(the shared depositary-registration rationale behind Article 64/63/143/159 of
the four Geneva Conventions and Article 102 of this Charter, "the same
argument as `rome-statute-1998` and `un/charter`"), which does not claim an
import and needed no correction. Read against what `geneva-1949`'s own
content would gain from a real import: nothing in its rules reads a
`member_state`, a Security Council determination, or any other `un.charter`
conclusion — the two packages formalize disjoint bodies of treaty text with a
shared THEME (registration with the UN Secretariat), not a shared legal
consequence. Building an import here would be machinery for a citation, the
same "predicate nobody reads" trap this package has declined at every other
turn (Finding 9's enemy-state carve-out, Finding 10's Articles 61/63/65).
Decision, logged in `docs/foundations/un-charter/DECISIONS.md`: (a) — leave
`geneva-1949` thematically related and uncompiled; no code change. The
original slice's README and the multisession prompt's own §2 description of
`geneva-1949` as a "consumer" were already corrected to a thematic
characterization at stage E0; this stage found nothing further to fix.

**Verification run for this stage.** `lawc check` clean; `lawc test`
155/155 (134 pre-existing + UNC-86); `lawref` (scratch driver,
`lawtests.discovery.discover_with_problems()` + `lawtests.run.run_suite()`,
`un_charter`/`un.charter#authored` families) 155/155 and 4/5 respectively —
the SAME single pre-existing `05-article-108-amendment-in-force.lawtest`
failure traced to a bug unrelated to this package since stage E0, unchanged.
CLIR regenerated and grepped before trusting it (no new predicate was added
this stage, so the regeneration is a no-op byte-for-byte against HEAD — the
working tree already matched HEAD exactly, the same benign stale-shared-index
artifact stage E9 documented for files 09-16). `check_kz_differential --only
un_charter --write-manifest`: 173 `evaluate` calls byte-identical between
`liblaw_ffi` and `lawref`, 155/155 PASS. Grep gate: `grep -rlP
'[\x{0400}-\x{04FF}]' corpus/laws/intl/charter` returns only
`sources/charter/ru.txt`, the intentional Article 111 evidentiary exception.
`audit-formalization --fast`: no orphan references, no dead symbols, `sync
--check` clean. After the deepening of entity-gap articles, 85 articles are
`EXECUTABLE` and 26 `SOURCE_ONLY` remain, each with a text-grounded reason in
`sources/charter/articles.json`.

## What this package does not do

- **Does not decide what a "threat to the peace" is.** The §47.3 judgment
  channel (`article_39_determination`, `authority SecurityCouncil`) is a
  construction of the text itself ("the Security Council SHALL DETERMINE"),
  not a gap: the package does not attempt to compute a political judgment
  that the Charter expressly hands to an organ.
- **Does not formalize customary international law** in parallel to the
  Charter (jus cogens, custom) — entirely outside the package.
- **Formalizes Article 53's enemy-state exception (para. 1's proviso, para.
  2's definition) by the letter only, never as a live escape hatch.** The
  letter is alive by the text, its application is dead by practice (the
  same "alive in the text, dead in practice" register as Articles 43-47,
  Finding 1) — a single flat case fact
  (`enemy_state_measure_under_article_107`) that no scenario of this
  package's own test corpus ever asserts. Article 107 itself is now in
  scope (stage E9) and declared, deliberately NOT a second, wider carve-out
  beside Article 53's own — the same rationale, logged once and reused, not
  reinvented (Finding 13).
- **Does not choose** among the three readings of Article 51 or the two
  readings of Article 27/23: the package shows WHICH answer follows under
  WHICH reading, not which reading is correct — a decision that is not
  technical (see the `formalize-act` skill, "where it must stop").
- **All 111 articles of the Charter are now in scope — no chapter remains
  pinned-but-unfragmented.** Chapter VIII (Art. 52-54, regional arrangements)
  is formalized in full (stage E5) — including the bridge from Article
  27(3)'s abstention duty to Article 52(3)'s regional-referral machinery,
  previously left as a bare textual quotation (Finding 7); see Finding 9.
  Chapters IX-X (Art. 55-72, economic and social co-operation, the Economic
  and Social Council) are formalized as well (stage E6, Finding 10). Chapters
  XI-XIII (Art. 73-91, non-self-governing territories, the international
  trusteeship system, the Trusteeship Council) are now formalized too (stage
  E7, Finding 11), as are Chapters XIV-XV (Art. 92-101, the International
  Court of Justice and the Secretariat — stage E8, Finding 12) and Chapters
  XVI-XIX (Art. 102, 104-107, 109-110, on top of Art. 103/108/111 already in
  scope from the original slice — stage E9, Finding 13).
- **Does not model individuals serving in an organ in their personal
  capacity, nor a specialized agency or non-governmental organization as a
  participating subject** — Article 8's non-discrimination guarantee
  (Finding 5), Article 9's delegation cap, and Articles 70-71's
  agency-representative/NGO participation (Finding 10) are all declared for
  the same entity-gap reason; no entity of the package is a natural person,
  a specialized agency, or an NGO. Article 86, paragraph 2's individual
  Trusteeship Council representative (Finding 11) is the same boundary,
  logged again at Chapter XIII. Stage E8 STOPS this boundary at Chapter XV:
  `SecretariatOfficial` (Articles 97-101) is the package's first officer
  entity, introduced because five articles of that chapter consume it and
  four derive rules from it — the specialized-agency and NGO halves of the
  gap remain open, except for Article 96's `RequestingBody`, which is a body
  entitled to put a question to the Court, not a participating subject
  (Finding 12).
- **Does not track whether the Trusteeship Council is currently sitting.**
  The Council has suspended operations since 1994 (the last trust
  territory, Palau, achieved self-government) — practice on top of the
  letter, not a Charter amendment (the same register as Article 23's
  continuity practice and Article 27's abstention practice, Finding 2). No
  rule of this package reads a "currently active" fact; Articles 86 and 89
  state the Charter's LETTER regardless of whether any State presently
  administers a trust territory in the world (Finding 11).

## Comparative axes of the corpus

`csto-treaty-1992` (Art. 4 of the CSTO — an inter-State reading against
Art. 51 of the UN Charter, each side reads the other by text),
`united-nations-1942` (an ancestor — the Declaration by United Nations, from
which Article 3 of the Charter takes its original members),
`un.ilc.nuremberg_principles`, `intl.icc.rome_statute` (complementarity, the
same §47.3 judgment channel through an organ named by the text). Facts do not
cross package boundaries; the comparison is at the level of reading the text,
not shared entities.


## Scenarios (`tests/un-charter.lawtest`, family `un_charter`, `UNC-01`…`UNC-95`, 164 checks)

Declared per DECISION-0127 (package scenarios are declarative, not a Python
runner): the sole source of facts, questions, and expectations for the
`un_charter` family is `tests/un-charter.lawtest`; five additional
hand-authored scenarios live in `tests/0N-*.lawtest` under the
`un.charter#authored` family (`law.toml`).

A historical battery: Kuwait-1991 (authorization bypassing Article 41,
UNC-11), Kosovo-1999 (a violation of Article 2(4) under ANY reading, UNC-12),
Nicaragua (threshold + request requirement, UNC-04…UNC-06B), 11 September
2001 (self-defence against non-State actors, UNC-09/10), admission of a
member with a veto (UNC-20/21), an amendment without one permanent member's
ratification (UNC-24/25), the Lockerbie motif (UNC-23). Stage E1
(18.09.2026) added original membership by either branch of Article 3
(UNC-27/27B/27C), suspension of rights adopted and denied by the Article 18
two-thirds threshold plus restoration by the Security Council alone
(UNC-28/28B/28C), and expulsion adopted and denied by the same threshold
(UNC-29/29B). Stage E2 (18.09.2026) added the General Assembly's
recommendation power under Articles 10/11/14 and its Article 12 bar/lift
(UNC-30…UNC-31B, UNC-32), Article 19's arrears threshold and both its
forfeiture and Assembly-permission branches (UNC-33…UNC-33C), and Article
20's special-session convocation by Security Council request or by a
computed majority of Members (UNC-34…UNC-34C). Stage E3 (18.09.2026) added
Article 31's participation-without-vote of a specially-affected Member
(UNC-35/35B) and Article 32's invitation-without-vote of a Member not on
the Council and of a state outside the UN altogether, both branches
conditioned on being a party to the dispute (UNC-36…UNC-37B). Stage E4
(18.09.2026) added Article 33's duty to seek a peaceful solution first,
active and discharged (UNC-38/38B), Article 34's Security Council
determination of endangerment (UNC-39/39B), Article 35's Member and
non-Member entitlements to bring a dispute to attention (UNC-40…UNC-41B),
Article 36's procedures and ICJ-referral recommendations (UNC-42…UNC-43B),
Article 37's duty to refer an unsettled dispute plus the Council's
determination-and-settlement-terms chain (UNC-44…UNC-45B), and Article 38's
request-gated recommendation (UNC-46/46B). Stage E5 (18.09.2026) added
Article 52's duty to seek regional settlement first and its discharge
(UNC-47/47B), the Security Council's paragraph 3 encouragement (UNC-48/48B),
Article 53's enforcement-action authorization by the Security Council, its
violation without authorization, and its enemy-state exemption
(UNC-49…UNC-50), Article 54's duty to keep the Security Council informed and
its discharge (UNC-51/51B), and the Article 27(3)/Article 52(3) abstention
bridge — a permanent member party to a regionally-referred dispute that
votes instead of abstaining (ACTIVE, UNC-52) and one that abstains
(SATISFIED, UNC-52B). Stage E6 (18.09.2026) added Article 56's pledge to
co-operate, active and discharged (UNC-53/53B), Article 67's ECOSOC
majority-voting threshold reached and not reached (UNC-54/54B), and Article
69's mandatory invitation of a Member of particular concern, present and
absent (UNC-55/55B). Stage E7 (18.09.2026) added Article 73, paragraph
(e)'s duty to transmit territorial information, active and discharged
(UNC-56/56B), Article 77's categorical recognition of a trusteeable
territory and its absence outside any category (UNC-57/57B), Article 78's
exclusion of a territory that has become a Member and its continued
applicability absent membership (UNC-58/58B), the Article 82-83/85
strategic/non-strategic competence split between the Security Council and
the General Assembly (UNC-59/59B), Article 84's duty to ensure a trust
territory's contribution to peace and security, active and discharged
(UNC-60/60B), Article 86's composition parity satisfied and not satisfied
(UNC-61/61B), Article 88's duty to submit an annual report, active and
discharged (UNC-62/62B), and Article 89's Trusteeship Council majority-voting
threshold reached and not reached (UNC-63/63B). Stage E8 (18.09.2026) added
Article 93's two routes to the Statute of the Court — a Member ipso facto and
a non-Member on conditions determined by the Assembly, with and without that
determination (UNC-64/64B/64C) — Article 94, paragraph 1's compliance duty,
active and discharged (UNC-65/65B), the cross-cutting non-performance chain
of Article 94, paragraph 2: a defaulting party's failure opening the other
party's recourse to the Security Council and not the reverse (UNC-66), the
absence of recourse without an established failure (UNC-66B), the Council's
own measures once it deems them necessary (UNC-67) and their absence without
that judgment (UNC-67B), Article 96's request competence — the named organs
unconditionally (UNC-68), an authorized body within the scope of its
activities (UNC-68B) and an unauthorized one (UNC-68C) — Article 97's
appointment chain, completed and blocked by a Council veto (UNC-69/69B),
Article 98's annual-report duty, active and discharged (UNC-70/70B), Article
99's referral power with and without the Secretary-General's own opinion
(UNC-71/71B), Article 100's TWO independence duties — the officer's, active
and discharged (UNC-72/72B), and each Member's, active and discharged
(UNC-73/73B) — and Article 101's staff appointment inside and outside the
Assembly's regulations (UNC-74/74B). Stage E9 (18.09.2026) added Article
102's registration test, invocable and barred (UNC-75/75B), the cross-cutting
scenario the task brief itself named — an unregistered treaty held simultaneously
barred from invocation AND still subordinate to a Charter obligation under
Article 103 (UNC-76) — Article 106's consultation duty pending Article 43,
active, discharged, and gone once a single special agreement is concluded
anywhere (UNC-77/77B/77C), Article 109's vote-asymmetry centrepiece across
five scenario pairs — the General Assembly's convening vote (UNC-78/78B), the
Security Council's own convening vote requiring nine members and reading NO
permanent-member machinery at all (UNC-79/79B), both organs' convening vote
combined (UNC-80), the alteration-ratification path feeding Article 108's own
conclusions (UNC-81/81B), and both paragraph 3 fallback thresholds, Assembly
and Council (UNC-82…UNC-84) — and Article 110, paragraph 4's third route into
original membership by ratification after entry into force (UNC-85/85B).
Stage E10 (18.09.2026, integration) added one narrative scenario spanning
Articles 4, 5 and 6 on a single State across three `evaluate`/`expect` pairs
sharing one `given` fact base — admission, then suspension, then expulsion
(UNC-86) — the connection the multisession prompt's own completion criteria
asked to see demonstrated, rather than left implicit across three disjoint
entities (`case:state:candidate`, `suspended`, `expelled`) in the pre-existing
Article 4/5/6 scenarios, none of which take one another as a precondition.
The later deepening (18.09.2026) added Articles 8, 9(2), 17, 21, 28–30,
57–59, 61, 63–64, 68, 70–72, 90, 95, 104 and 105 as EXECUTABLE: a
sex-based eligibility restriction (UNC-87), a six-person General Assembly
delegation (UNC-88), a specialized-agency relationship agreement (UNC-89),
unpaid Article 17 apportionments triggering Article 19 (UNC-90), Assembly
rules and President (UNC-91), ECOSOC re-election and a majority-request
meeting (UNC-92), an invalid specialized-agency vote and NGO consultative
status (UNC-93), legal capacity and representative immunity (UNC-94), and
an outside tribunal not precluded (UNC-95).
`lawc test` and `lawref` agree on all 164 scenarios of the `un_charter`
family.

## Multisession task closure

`un.charter` was formalized across ten stages (E0-E10, `docs/foundations/un-charter/MULTISESSION-PROMPT.ru.md`),
starting from a 26-article slice and closing at all 111 articles: `scope` =
111, EXECUTABLE 85 + declared 26 = 111 exactly, zero `INTERPRETED`-only
articles, zero out-of-scope. 164 `.lawtest` scenarios in the `un_charter`
regression family (plus five hand-authored ones in `un.charter#authored`),
`lawc`/`lawref` agreeing on all of them, `check_kz_differential` byte-
identical (173 `evaluate` calls). The full process history — engine
limitations found along the way, modelling idioms established and reused
chapter to chapter, the shared-tree git hazards each stage documented and
worked around — lives in `docs/foundations/un-charter/HANDOFF.md` and
`docs/foundations/un-charter/DECISIONS.md`, not here: this README stays about
the package's substance, per this repository's own convention that process
narration belongs in the session record, not in a package's own findings
document.
