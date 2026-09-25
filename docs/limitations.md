# Limitations and scope

**1. Pre-validation.** The rubric and scenarios have not been through the planned expert
validation. No inter-rater agreement is reported in v0.1.

**2. Construct scope.** ViWELL evaluates four conversational behaviours: recognition,
clarification, connection, support transition. It does not measure overall psychological
safety, clinical competence or therapeutic quality. Other dimensions may prove necessary
during validation: pathologising and missed cultural context are both scored inside D1 through
reason codes, and the pilot decides whether either needs a dimension of its own.

**3. No diagnostic inference.** The benchmark diagnoses nothing. Scenario labels are design
conditions, not clinical categories.

**4. Synthetic scenarios.** Public scenarios are composites. This protects privacy and
reproducibility at some cost to ecological validity relative to naturally occurring
conversation.

**5. Scripted turns.** The simulated user's later turns do not adapt to the quality of the
model's reply, whereas a good reply may in reality cause a student to disclose *more* rather
than retreat. A smaller supplementary set will use an adaptive simulated user to test this.

**6. Coverage.** A finite benchmark cannot represent the full diversity of Vietnamese
psychological experience. Regional, socioeconomic and developmental variation are
underrepresented in v1.

**7. Language variation.** Vietnamese varies by region, age, education, online community and
formality. Informal register and code-switching age quickly; scenarios will need periodic
refresh on that ground alone.

**8. Access surface.** Vietnamese young people reach these systems mainly through consumer
applications; the harness uses APIs. System instructions, safety policies, memory, tool
availability and model version may all differ. Every evaluation report must state the access
method and model version rather than claim equivalence.

**9. Run-to-run variability.** Repeated runs estimate variability; they are not averaged
away into a single number. Aggregation is decided from pilot data, not fixed in advance.

**10. Automated grading.** A grader introduces its own errors. It is evaluated against expert
labels and is never treated as ground truth.

**11. Saturation.** If frontier models clear every cell easily, the benchmark carries no
information. This is checked at pilot and answered by adjusting difficulty, not by adding
items.

**12. Contamination.** Publishing scenarios openly risks their entering training corpora,
after which the benchmark measures recall rather than capability. Mitigation: publish the
majority, retain a held-out subset for formal evaluation, include canary strings, refresh a
portion periodically within the same cell matrix.

**13. Cross-session behaviour.** Within-session only. No long-term memory, repeated
interaction over weeks, persistent profiles or longitudinal change.

**14. Generalisation.** Performance on ViWELL is evidence about the constructs and scenarios
represented here. It does not establish general safety.
