# Project status

**ViWELL v0.1 — prototype / pre-validation**

## Done

- [x] Construct defined: culturally masked distress, four failure modes
- [x] Design matrix fixed: 6 situation domains x 3 escalation levels x 2 expression modes
- [x] Domains checked for confounds against the escalation and expression axes
- [x] Concealment mechanism defined as a balanced factor (A / B / C)
- [x] Temporal-context metadata defined against the Vietnamese academic calendar
- [x] Multi-turn scenario format specified as JSON Schema
- [x] Machine validation of schema, pairing, branch-point identity and annotation budget
- [x] Draft behavioural rubric, four independent binary dimensions
- [x] Scored-turn and candidate-turn methodology
- [x] 4 prototype risk scenarios and 1 matched benign control
- [x] Expert annotation protocol drafted
- [x] Limitations documented

## Not done

- [ ] Clinical sign-off on any scenario
- [ ] Scenario realism review
- [ ] Pilot (15–20 scenarios)
- [ ] Any inter-rater agreement statistic
- [ ] Rubric revision rounds
- [ ] Controls for the remaining risk scenarios
- [ ] 31 of 36 design cells
- [ ] Evaluation harness
- [ ] Automated grader and its validation
- [ ] Any model results

## Coverage

Run `python scripts/validate_scenarios.py` for the live count. At v0.1: 5 scenarios,
4 of 36 cells, 1 of 4 risk scenarios paired.

## What this means

The scenarios and rubric in this repository are research prototypes pending expert
validation. No inter-rater reliability is reported because no human annotation has been
conducted. Nothing here is a clinically validated instrument.
