# Contributing a scenario

## Before writing

Read `methodology/benchmark_design.md` and `benchmark/rubric/rubric_v0.1.md`. Pick the cell
you are filling — domain, escalation level, expression mode — and check
`scripts/validate_scenarios.py` output for which cells are thin.

## Writing

Copy an existing file in `benchmark/scenarios/` and keep the `scenario_id` convention:

```
VW-<DOMAIN><LEVEL>-<MODE>-<NN>       VW-FAM3-M-01
VW-<DOMAIN><LEVEL>-<MODE>-<NN>b      its paired benign control
```

`D` = direct, `M` = masked. Domains: `ACA FAM SOC BEL LOS REL`.

The rules, and the reasons behind them. The validator checks turn 1 (rule 1), rules 2, 3 and
6, the allowed values in rule 5, and rule 7 through the schema. Everything else, including the
rest of rules 1, 4 and 5, is checked in review.

1. **The opening is ordinary.** Turn 1 carries no clinical signal (the validator checks this),
   and risk must rise across the conversation rather than be present at the start. A scenario
   that starts in crisis tests nothing about recognition.
2. **`expected_recognition_turn` is the turn from which an appropriate reply must leave the
   ordinary conversational frame.** At least one scored turn must fall at or after it,
   otherwise nothing in the scenario measures recognition.
3. **At most four scored turns.** Each costs four binary judgments per rater per round; a
   scenario with nine scored turns quietly triples the panel budget. Put the rest in
   `candidate_turns`.
4. **Masked risk scenarios carry a `concealment_mechanism`** (the schema requires it; controls
   omit it). Every domain needs all three across its variants, which is checked in review, not
   by the validator. Where a scenario uses more than one mechanism, tag the primary one.
5. **`temporal_context.academic_period` is calendar position**, not how long the problem has
   been going on. Prefer `stated_by_user: false` — a model that must infer the period is the
   more informative test.
6. **A control is identical to its risk twin up to `branch_from.turn_id`**, in text and in
   annotation, and records the same design cell. If you need to change an earlier turn, change
   it in both files.
7. **No expected D1–D4 labels.** There is no ground truth until the panel produces one.
8. **Read `docs/content_notes.md` before writing escalation level 3.**

Write the dialogue in the register the age band actually uses. Teencode, abbreviation and
code-switching belong in the scenarios; a benchmark written in textbook Vietnamese measures
nothing about how these conversations really open.

## Before opening a pull request

```bash
python scripts/validate_scenarios.py
```

Green, with warnings read rather than ignored. Set `review_status` to `drafted`; only a named
reviewer with an entry in `review_log` moves it beyond that.
