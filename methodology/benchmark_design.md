# ViWELL benchmark design

## 1. Objective

ViWELL is a behavioural evaluation benchmark, not a collection of ideal-response prompts.

> Can an AI model recognise and respond appropriately when psychological distress changes in
> meaning or severity across a realistic Vietnamese multi-turn conversation?

An **item is a conversation trajectory, not a prompt**. A single twelve-turn item tests
recognition, clarification, escalation sensitivity, maintenance of contact and transition to
support at once — which is why item count is a poor proxy for coverage here, and why the
design prioritises controlled variation over raw size.

## 2. Situation domains

`academic_performance` — academic and performance pressure
`family_expectation` — family expectation and conflict
`social_exclusion` — exclusion, bullying, peer rejection
`belonging_new_environment` — belonging and isolation in a new setting, including the move
from home to university
`loss_life_disruption` — bereavement, parental separation, family illness, financial shock
`close_relationship_conflict` — romantic or close-peer conflict

These are conversational situations, not diagnostic categories.

**Why not "self-worth and hopelessness" or "mental-health disclosure" as domains.** Both
appeared in an earlier draft and both were removed, because each duplicates another axis.
Hopelessness and collapse of self-worth are what escalation level 3 consists of in every
domain — a hopeless conversation about family pressure belongs in `family_expectation` at
level 3, not in a separate domain. Direct disclosure of a mental-health problem is what the
direct expression mode consists of. Keeping either as a domain would let one conversation
belong to two cells, which is not a taxonomy problem only: it surfaces later as rater
disagreement that looks like rubric ambiguity and is actually matrix ambiguity, costing a
revision round to diagnose.

Expansion domains for phase 2: identity and direction after school; online social life and
comparison; work and money pressure among those who have left education.

## 3. Escalation

**Level 1 — context and early signal.** Distress or vulnerability present; no clearly
elevated risk established.

**Level 2 — emerging or ambiguous concern.** Meaningful indicators, with interpretation or
severity still uncertain.

**Level 3 — clearly concerning.** A substantially more concerning signal requiring a
materially different response. Carried by statements of hopelessness, worthlessness or
expendability — never by graphic content.

Levels are design conditions, not clinical severity categories.

## 4. Expression mode and concealment mechanism

**Direct** — distress stated relatively explicitly.

**Masked** — the signal travels indirectly. Every masked variant is tagged with the
mechanism carrying it:

- **A — concealed inside a permitted subject.** The distress travels under a topic that is
  socially acceptable to raise: schoolwork, a friend's problem, mental-health advocacy about
  a family member.
- **B — withheld, fragmented, retracted.** Released in pieces, each followed by a pullback
  ("giờ thì cũng đỡ rồi").
- **C — reinterpreted by the speaker as not-distress.** Relabelled as maturity, as a personal
  flaw, as nothing worth mentioning ("nvm chắc do mình delulu"; "bố mẹ bận nên mình cần
  trưởng thành hơn").

Mechanism is a **balanced factor, not a fourth axis**. Construction requires all three within
each domain across its variants; results can then be reported by mechanism without turning 36
cells into 108. The distinction matters: a benchmark organised by topic tests coverage, while
a benchmark organised by mechanism tests the thing English-calibrated safeguarding is
actually likely to miss.

We keep the term *masked* rather than the softer *contextually indirect*. The construct named
in the project title is cultural masking, and the benchmark should not disclaim its own
claim in its design document. The caution behind the softer term is real and belongs in
`docs/limitations.md`: no linguistic form is universally disguising, and what counts as
masked is a property of the conversation, not of a word list.

## 5. Matrix

6 domains x 3 levels x 2 modes = **36 cells**, 2–3 controlled variants each → roughly 90 risk
conversations. Matched benign controls double the pool: **~180 conversations for the
validated v1 release**, extending toward 300–400 in phase 2.

Variation within a cell changes surface realisation while preserving the construct: wording,
directness, register, slang, code-switching, contextual detail, setting, disclosure order,
minimisation, topic shifts. The point is that the benchmark must not be solvable from a small
set of lexical cues.

## 6. Temporal context

Every scenario carries `temporal_context`: where in the Vietnamese academic year the
conversation sits, an approximate date, one sentence on why that period raises or lowers the
weight of the signal, and whether the user states the period or the model must infer it.

`stated_by_user: false` is the more informative condition and the default preference. The
same sentence is not the same signal in the university entrance window, in the days before
Tết when relatives ask about grades, and in an unremarkable week in October.

## 7. Multi-turn structure

6–14 turns. An illustrative shape: opening context; first signal; elaboration; an opening for
clarification; minimisation or topic shift; further disclosure; escalation or resolution.
Illustrative, not mandatory.

## 8. Scored turns

Pre-specified clinical decision points, set when the scenario is written: where a signal
first appears, an ambiguous statement needs clarification, the apparent level changes, the
user minimises a previous disclosure, a context shift tests retention, or support transition
becomes appropriate. They are fixed before any model is run and never selected afterwards by
looking at where models disagreed; choosing them that way would build the results into the
instrument.

The recognition threshold (`expected_recognition_turn`) is proposed by the scenario author and
confirmed or moved by the clinical panel during scenario validation, with disagreement
recorded.

**Capped at four per scenario**, typically two or three. Each scored turn costs four binary
judgments per rater per round; at a 5–7 person panel and 2–3 rounds, a scenario scoring nine
turns costs roughly three times one scoring three. Turns of interest beyond the cap go in
`candidate_turns`, outside the annotation budget.

## 9. Benign controls

A control resembles its risk twin in surface context and lacks the clinical signal. It is
identical up to a declared branch point, after which only the signal differs. This is what
allows under-response and over-response to be measured on one instrument, and it is the
element we consider methodologically distinctive. `scripts/validate_scenarios.py` checks that
the arms are identical in text and annotation before the branch point and record the same
design cell, so a control cannot drift from its twin unnoticed.

Where a control can reuse a *surface-identical move* from the risk arm with different
clinical meaning, it should, and at the same turn so that both arms score it. In
`VW-FAM3-M-01b` turn 10 the speaker dismisses the comparison with her sister in the same
throwaway register in which her twin, at turn 10, dismisses herself. That is precisely the
discrimination the pair exists to test.

## 10. Phasing

**Phase 1 (months 1–6).** Construct and validate ~180 conversations across the full matrix,
including controls; stabilise the rubric against expert labels.

**Phase 2 (months 7–12).** Extend to further domains and indirect expression patterns —
code-switching and youth register, somatic framing, trajectories that resolve late — toward
300–400 conversations, with the validated scoring framework unchanged.

We phase deliberately rather than committing to a final count. Expanding a benchmark whose
rubric has not stabilised produces more items of unknown quality. This is a measurement
problem before it is a scale problem.
