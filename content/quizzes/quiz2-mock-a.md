# Mock Quiz 2A — Module 2

**50 points · 60 minutes · closed book.** Same four sections as the real Quiz 1. Solutions include a Quiz-1-style rubric — mark yourself strictly.

<div class="pdf-links">
<a href="quiz2-guide.html">Quiz 2 guide</a>
<a href="quiz2-mock-b.html">Mock 2B</a>
<a href="quiz2-mock-c.html">Mock 2C</a>
</div>

## Basic Definitions [CLO 4] — 9 points

:::question 1(a) [3 points] Explain why "raw data" is described as an oxymoron. Your answer should name the three kinds of decisions that shape a dataset before any row is recorded.
:::solution Solution & marking
Data are never raw: every dataset is **produced** through human, technical and institutional choices before it is recorded. **Conceptualization** — what phenomenon matters and how variables/labels are defined; **observation** — unit of analysis, inclusion/exclusion, instruments, frequency; **engineering** — what is recorded, how missingness is encoded, how data are stored, linked and transformed. Hence a dataset is an engineered artifact, not a passive reflection of reality.

| Rubric | |
|---|---|
| States data are produced/constructed, not objective or pre-existing | 1 |
| Names all three decision types (½ each for two, 1 for three) | 1 |
| Links to consequence: models inherit these choices / dataset is an artifact | 1 |
:::
:::

:::question 1(b) [3 points] Define Missing Not at Random (MNAR). Why can't the missingness mechanism usually be verified from the dataset itself?
:::solution Solution & marking
**MNAR:** the probability that a value is missing depends on the **unobserved value itself**, even after conditioning on observed variables (e.g. high earners withhold income even after accounting for age, education, occupation). It cannot usually be verified because testing it would require knowing the **missing values** — which are, by definition, not observed; the mechanism is an **assumption about the data-generating process** justified by domain knowledge.

| Rubric | |
|---|---|
| Missingness depends on the missing value itself | 1 |
| …even after conditioning on observed data (distinguishes from MAR) | 0.5 |
| Not verifiable because missing values are unobserved / assumption about data-generating process | 1.5 |
:::
:::

:::question 1(c) [3 points] Define data provenance. In one additional sentence, distinguish provenance from data lineage.
:::solution Solution & marking
**Provenance** is the documented **origin, history and chain of custody** of data — how, when, where and by whom they were collected, processed and maintained. **Lineage** records **how data evolve through processing steps** — the chain of dataset versions $D_0\to D_1\to\cdots\to D_{\text{training}}$ and the transformations between them.

| Rubric | |
|---|---|
| Correct definition of provenance (origin/history/custody) | 1.5 |
| Mentions how/when/where/by whom or collection & processing context | 0.5 |
| Correct distinction: lineage = transformations/versions through the pipeline | 1 |
:::
:::

## Short, Conceptual Questions [CLO 4] — 12 points

:::question 2(a) [4 points] A bank removes race from its loan-approval model and claims the model is therefore fair. Explain why this claim is inadequate, and explain why the bank might nevertheless need to *retain* race data.
:::solution Solution & marking
Removing a sensitive attribute does not remove bias because other variables act as **proxies**: postal code (historical residential segregation), income, occupation, school or language correlate with race, so the model can reproduce disparities (Example 59). Historical approval labels may themselves encode discrimination. The bank should **retain race under restricted access for fairness auditing and monitoring** — without it, it cannot measure whether approval or error rates differ across groups (Example 60: 91/90/74% accuracy). Governance separates use for **prediction** from use for **evaluation**, with strict access controls.

| Rubric | |
|---|---|
| Proxy mechanism explained | 1.5 |
| Concrete proxy example (postal code etc.) or biased labels | 0.5 |
| Retain for fairness auditing/monitoring — can't detect disparity otherwise | 1.5 |
| Restricted access / separation of prediction vs audit use | 0.5 |
:::
:::

:::question 2(b) [4 points] A research team oversamples the minority class to a 50/50 balance and then splits the data 80/20 into training and test sets. They report 98% accuracy. Explain two distinct problems with this procedure and how to fix them.
:::solution Solution & marking
1. **Train–test contamination:** oversampled/synthetic minority cases are copies or interpolations of originals, so near-identical cases appear in both sets → over-optimistic results. **Fix:** split first, oversample only the training set (inside each CV training fold), keep the test set untouched.
2. **Unrealistic evaluation/calibration:** the test set now has 50% prevalence, unlike deployment, so accuracy (and any probability) is uninformative; balanced training also inflates predicted probabilities. **Fix:** evaluate on the natural prevalence with recall, precision, F1/PR-AUC; recalibrate (Platt scaling or isotonic regression).
(Accept also: accuracy is misleading under imbalance.)

| Rubric | |
|---|---|
| Problem 1 named + explained | 1.5 |
| Fix for problem 1 | 0.5 |
| Problem 2 named + explained | 1.5 |
| Fix for problem 2 | 0.5 |
:::
:::

:::question 2(c) [4 points] "Synthetic data contain no real people, so privacy and fairness concerns do not apply." Critically evaluate this statement using any three validation dimensions for synthetic data.
:::solution Solution & marking
The statement is **false**. **Privacy:** generators can memorize training records; near-copies enable membership inference and reconstruction — synthetic ≠ anonymous. **Fairness:** the generator learns historical bias and under-representation from the source data and can reproduce or amplify it. **Coverage:** rare but critical cases and small subgroups are often missing, so models fail on them. (Also fidelity, utility on real data, realism.) Synthetic data must be **validated** on all six dimensions before use.

| Rubric | |
|---|---|
| Rejects claim with justification | 1 |
| First dimension correctly applied | 1 |
| Second dimension | 1 |
| Third dimension | 1 |
:::
:::

## Scenario-based Question [CLO 3, 4] — 21 points

:::orig Smart-meter energy-theft detection
A power-distribution company wants an AI system to flag households likely to be **stealing electricity** so that inspection teams can visit them. Available data: monthly smart-meter consumption (for areas with smart meters), billing and payment history, number of past inspections, **"theft confirmed" flags from past inspections**, neighbourhood, household size from an old census, customer complaints, and the **date a fine was issued**.
- Smart meters were installed mainly in **newer, wealthier neighbourhoods**; older areas use manual readings recorded by meter readers, often **estimated** when the reader cannot access the meter, and estimates are stored like real readings.
- Inspections were historically concentrated in **low-income neighbourhoods**, so most "theft confirmed" labels come from there.
- Several households appear many times (monthly rows), and rows were randomly split 80/20; the model reports **96% accuracy**.
- Theft is present in about **3%** of households. The company plans to **automatically disconnect** any household with predicted probability above 0.7.
:::

:::question 3(a) [4 points; Data sources and quality] Identify two data-quality problems arising from the meter readings. Name the quality dimension each violates.
:::solution Solution & marking
- **Estimated readings stored as real readings** → **accuracy** (values aren't measured) and **consistency/structural** (two different kinds of value in one column without a flag); estimation is more common where access is hard → systematic error.
- **Smart meters only in newer/wealthier areas** → **representativeness/completeness of subgroups** (monthly digital data missing for older areas) and **measurement error differing by area (differential)**: manual readings are noisier.
- (Also: household size from an **old census** → **timeliness/staleness**.)

| Rubric | per problem |
|---|---|
| Problem identified from the case | 1 |
| Correct dimension + explanation | 1 |
:::
:::

:::question 3(b) [5 points; Labels and construct validity] Is "theft confirmed" a valid measure of actual electricity theft? Explain using the chain *true construct → institutional process → recorded proxy → training target*, and name the bias that results.
:::solution Solution & marking
- **True construct:** whether a household actually steals electricity.
- **Institutional process:** the company decides **where to inspect** — historically low-income neighbourhoods; inspectors' judgement; access to premises.
- **Recorded proxy:** "theft confirmed" — exists **only for inspected households**; uninspected thieves are labelled "no theft" (**selective labels**).
- **Training target:** the model learns **who gets inspected and caught**, not who steals.
- Result: **historical/feedback bias** (and selective labels) — low-income areas look high-risk; if new inspections follow the model, more theft is found there → **feedback loop**; wealthier thieves remain invisible. The label has **poor construct validity**.

| Rubric | |
|---|---|
| Construct vs proxy distinguished | 1 |
| Institutional process (inspection allocation) explained | 1 |
| Selective labels (uninspected = negative) | 1 |
| Bias named (historical/feedback) with mechanism | 1 |
| Consequence for model/decision | 1 |
:::
:::

:::question 3(c) [4 points; Leakage] Identify two distinct forms of leakage in the development process and explain how each inflates the 96%.
:::solution Solution & marking
- **Target/temporal leakage — "date fine was issued":** a fine is issued **after** theft is confirmed, so the feature reveals the outcome and wouldn't exist at prediction time.
- **Group leakage:** monthly rows of the **same household** are randomly split across train and test → the model recognizes households rather than theft patterns.
- (Also acceptable: number of past inspections counting the inspection that generated the label; random split ignores time.)

| Rubric | per leak |
|---|---|
| Correct leak type named with case evidence | 1 |
| How it inflates performance / fix (household-level, time-based split; drop post-outcome fields) | 1 |
:::
:::

:::question 3(d) [4 points; Evaluation] Why is 96% accuracy inadequate here? State two further evaluation analyses required before deployment.
:::solution Solution & marking
With **3% prevalence**, "no theft" for everyone gives **97%** — 96% is worse than the trivial baseline. Accuracy hides FP/FN, is inflated by leakage, and says nothing about calibration or groups. Required: **precision/recall (PR-AUC) at the operating threshold** — false accusations vs missed theft; **subgroup performance** by neighbourhood/income and smart vs manual meters; **calibration** at the true prevalence; **household-level and temporal** validation; comparison with a **baseline**.

| Rubric | |
|---|---|
| Base-rate/imbalance argument | 1 |
| Another reason (leakage, FP/FN, calibration) | 1 |
| First additional analysis | 1 |
| Second additional analysis | 1 |
:::
:::

:::question 3(e) [4 points; Governance and ethics] Evaluate the automatic-disconnection policy. Propose a governance-appropriate alternative.
:::solution Solution & marking
Automatic disconnection is a **high-harm, punitive decision** made on an unreliable, biased score: false positives cut power to innocent (often low-income) households; the score inherits **inspection bias**; there is no human review or appeal; 0.7 is arbitrary and probabilities are uncalibrated. **Alternative:** use the score only to **prioritize inspections** within team capacity (ranking), with **human verification** before any action, notice and **appeal**; restrict to validated meter types; audit subgroup flag and confirmation rates; monitor feedback effects (randomized share of inspections outside high-score areas); a named model owner and oversight body.

| Rubric | |
|---|---|
| Harms of automation/false positives explained | 1 |
| Links to bias/unreliable score | 1 |
| Alternative: score → inspection prioritization + human verification | 1 |
| Safeguards: appeal, audit, monitoring, accountability | 1 |
:::
:::

## Identifying Problems in a Data Pipeline [CLO 4] — 8 points

:::question 4 [8 points] A city builds a model predicting which restaurants will fail hygiene inspections. It trains on five years of inspection records. Inspectors historically visited restaurants in tourist districts more often. Customer-complaint counts from a review app are used as a feature; most app users are young and urban. Restaurant names are matched across years by fuzzy string matching. Each year the model is retrained on the outcomes of inspections it recommended. Identify and explain **four distinct** problems (2 points each).
:::solution Solution & marking
Award 1 for the correct name, 1 for the mechanism tied to the scenario.
1. **Selective labels / historical (inspection) bias:** outcomes exist mainly where inspectors went (tourist districts); uninspected restaurants look "clean".
2. **Representation / platform bias in web data:** complaint counts reflect **app users** (young, urban) and app visibility, not hygiene; neighbourhoods with older or non-app customers generate fewer complaints.
3. **Entity-resolution errors:** fuzzy name matching causes **false merges** (two restaurants combined) and **false splits** (renamed restaurant treated as new) → wrong histories and duplicates.
4. **Feedback loop:** retraining on outcomes of inspections the model recommended means the model's past choices generate its future labels, reinforcing its initial focus.
Also acceptable: construct validity of "failed inspection" vs actual hygiene; temporal drift in inspection standards. *No double counting* of 1 and 4 unless the student distinguishes past human allocation from model-driven retraining.
:::
:::
