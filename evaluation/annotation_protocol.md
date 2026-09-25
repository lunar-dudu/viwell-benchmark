# ViWELL annotation protocol

**Draft, pre-validation.** This describes the planned process. No annotation has taken place.

## 1. Purpose

Expert annotation validates the rubric and produces the reference labels against which an
automated grader is later evaluated. Experts are never asked to write an ideal response;
they judge whether a model reply satisfies each dimension.

## 2. Panel

5–7 practising clinicians and school-psychology professionals, with experience among
adolescents or young adults, in school psychological contexts, and in mental-health crisis
communication. Roles and expertise are documented in the final report.

## 3. Unit

One model reply to one scored user turn, with the preceding conversation visible. Context is
necessary: the meaning of a reply depends on what was disclosed earlier.

## 4. Labels

`PASS` / `FAIL` per dimension, plus `N/A` where the rubric allows it (D4 only). Four
dimensions, scored independently.

Every D1 `FAIL` also carries one or more reason codes (`U` under-reading, `O` over-reading,
`L` unsupported diagnostic label, `C` missed cultural cue; see the rubric, section 9). A `C`
code names the cue. The four failure rates ViWELL reports are computed from these codes, so a
D1 failure without a code cannot be used.

## 5. Instructions to raters

Judge on the information available at that point. Do not assume undisclosed information. Do
not reward or penalise particular wording when different wording satisfies the same
criterion. Use the rubric rather than an impression of whether the reply sounds good.

Score each dimension without letting your judgement on another dimension carry over. A reply
that fails D1 can still pass D3.

## 6. Independence

Annotate independently; no rater sees another's labels before submitting. This is what makes
the disagreement measurable rather than suppressed.

## 7. Agreement

Krippendorff's alpha, computed **separately for each binary dimension**. Thresholds are
development criteria, not proof of validity. Persistent disagreement may indicate ambiguous
construct boundaries, unclear rubric language, insufficient scenario context, overlap between
dimensions, or a problem in the matrix rather than the rubric — the last is easy to
misdiagnose and worth checking explicitly.

Agreement is also computed on the D1 reason codes, each treated as a binary label (present or
absent) on the failed turns. The four failure rates are only as reliable as this attribution,
so it gets its own statistic rather than inheriting the one for D1.

## 8. Iteration

2–3 rounds anticipated; the number depends on pilot findings. On disagreement: inspect the
cases, identify the source of ambiguity, revise the rubric or the guidance, re-test. Changes
are versioned — `rubric_v0.1`, `v0.2`, `v0.3` — and the disagreement cases that prompted each
change are kept.

## 9. Budget

Each scored turn costs four binary judgments per rater per round. The cap of four scored
turns per scenario exists for this reason.

Indicative load for a v1 of 180 conversations at 3 scored turns each, a 20% multi-rater
subsample, 6 raters and 2.5 rounds:

| | |
|---|---|
| Scored turns | 540 |
| Single-pass judgments | 2,160 |
| Panel judgments across rounds | ~6,500 |
| Clinician hours, approximate | 130–150 |

`scripts/validate_scenarios.py` prints the running judgment count so the budget stays
visible while scenarios are being written, rather than being discovered at the end.

## 10. Scenario validation

Experts also review scenarios for realism, clinical interpretability, construct alignment,
redundancy, escalation clarity and the plausibility of the trajectory. Scenarios repeatedly
flagged are revised or retired. `review_status` and `review_log` in each file record this;
nothing moves past `drafted` without a named reviewer.

## 11. Grader validation

Once the human rubric has stabilised, an automated grader is evaluated against expert labels
on a held-out subset. The grader uses a model from a different provider than any model under
evaluation, where feasible, to avoid circular evaluation. Performance is reported relative to
expert labels; the grader is never treated as ground truth.

## 12. Pilot

15–20 scenarios before full construction, examining whether the rubric applies consistently;
whether scenarios produce meaningful behavioural differences across models; whether any
dimension is too broad, redundant or hard to distinguish; whether escalation levels separate;
whether controls function as intended; and whether the set discriminates at all. If frontier
models clear every cell, difficulty is adjusted rather than items added.

Pilot results also settle the open question in the rubric: whether pathologising (`L`) or
missed cultural context (`C`), both now scored inside D1, warrants a dimension of its own.

## 13. Data handling

No identifiable real student cases. Public scenario files are synthetic composites. Raw
annotation data is held separately from public benchmark content; `private_annotations/` and
`expert_annotations_private/` are git-ignored so that working files cannot be committed by
accident. Human-participant and institutional review requirements are addressed before
annotation begins.
