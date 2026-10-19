# Mock Quiz 2C — Module 2

**50 points · 60 minutes · closed book.** Emphasis: quality dimensions, cleaning decisions, fairness metrics and the case studies.

<div class="pdf-links">
<a href="quiz2-guide.html">Quiz 2 guide</a>
<a href="quiz2-mock-a.html">Mock 2A</a>
<a href="quiz2-mock-b.html">Mock 2B</a>
</div>

## Basic Definitions [CLO 4] — 9 points

:::question 1(a) [3 points] Define differential measurement error and explain why it is a fairness issue.
:::solution Solution & marking
Measurement error whose rate **differs across subgroups**: $P(X^*\neq X\mid A=a)$ varies with a sensitive attribute $A$ (heart-rate sensor ±2 bpm on light skin, ±10 bpm on dark skin). It is a fairness issue because the model receives systematically **worse data for one group**, producing unequal performance that the model **cannot correct** from the data alone.

| Rubric | |
|---|---|
| Error differs by subgroup | 1.5 |
| Example | 0.5 |
| Unequal performance / cannot be corrected | 1 |
:::
:::

:::question 1(b) [3 points] Define concept shift and distinguish it from covariate shift.
:::solution Solution & marking
**Concept shift:** the relationship between inputs and outputs, $P(Y\mid X)$, changes (purchasing behaviour after a recession). **Covariate shift:** the input distribution $P(X)$ changes while the mapping is stable (a model moved to a hospital with different demographics).

| Rubric | |
|---|---|
| Concept shift definition | 1.5 |
| Distinction from covariate shift | 1.5 |
:::
:::

:::question 1(c) [3 points] Define equal opportunity as a fairness criterion, and state when the notes recommend it.
:::solution Solution & marking
**Equal opportunity:** true-positive rates are equal across groups, $P(\hat Y=1\mid Y=1,A=a)=P(\hat Y=1\mid Y=1,A=b)$. Recommended when **false negatives are the most harmful error** — e.g. sepsis detection with different prevalence across groups (Example 62), where missing a true case is worse than an extra test.

| Rubric | |
|---|---|
| Equal TPR definition | 1.5 |
| When it is appropriate (FN harm) | 1 |
| Example | 0.5 |
:::
:::

## Short, Conceptual Questions [CLO 4] — 12 points

:::question 2(a) [4 points] A dataset is 99% complete at the cell level. Give two reasons why it could still be unfit for a deployment task.
:::solution Solution & marking
(1) Cell completeness ignores **missing records and missing subgroups** — it may exclude an entire vulnerable population (rural patients, online students) → representativeness failure. (2) Present values may be **inaccurate, inconsistent or stale**: complete but wrong (miscalibrated monitor), mixed units, or too old for real-time prediction; or labels may measure the wrong construct. Completeness is only one of six dimensions and is judged relative to the task, $Q(D,T,C)$.

| Rubric | per reason |
|---|---|
| Reason | 1 |
| Explanation tied to task | 1 |
:::
:::

:::question 2(b) [4 points] Why should outliers be investigated rather than automatically removed? Give two appropriate responses other than deletion.
:::solution Solution & marking
Outliers may be **genuine rare cases** (emergencies, fraud, failures — often the most important events) as well as errors (entry mistakes, wrong units, sensor faults). Automatic deletion removes the tails the model most needs and biases it towards normal cases. Responses: verify against the source and **correct documented errors**; **convert wrong units**; **retain valid extremes with robust methods** (Huber/quantile loss); **winsorize/clip** with justification; **log/Box–Cox transform**; separate category; exclude only by predefined documented criteria.

| Rubric | |
|---|---|
| Outliers can be meaningful | 1 |
| Consequence of deletion | 1 |
| Two valid responses | 2 |
:::
:::

:::question 2(c) [4 points] Using Gender Shades, explain why aggregate accuracy can conceal severe subgroup failure, and why data cleaning alone could not have fixed the problem.
:::solution Solution & marking
$E_{\text{overall}}=\sum_g P(G=g)E_g$: if easy groups (lighter-skinned men, error ≤0.8%) dominate the data, overall error is low even when a small group (darker-skinned women, up to 34.7%) has unacceptable error; reporting by gender or skin type **separately** also hides the worst **intersection**. Cleaning could not fix it because nothing was "dirty" — the problem was **who was sampled and in what proportions, which metrics were reported, and how categories were defined**; a perfectly formatted dataset can still be inequitable.

| Rubric | |
|---|---|
| Weighted-average / dominance argument | 1.5 |
| Intersectional point | 1 |
| Why cleaning can't fix it | 1.5 |
:::
:::

## Scenario-based Question [CLO 3, 4] — 21 points

:::orig Early-childhood malnutrition screening
A provincial health department wants an AI tool that flags children under five at risk of **severe acute malnutrition in the next three months**, so lady health workers can schedule extra visits. Data: monthly records from **basic health units** (weight, height, age, vaccination, illness episodes), household income from a **survey** done five years ago, distance to the nearest health unit, and a label **"admitted to a nutrition rehabilitation centre"**.
- Weights are recorded on different scales; some units record kilograms, some pounds; several units' scales were found to read **0.5 kg high**.
- Children who **never visit** a health unit have no records.
- Missing height is common in remote units without measuring boards; the team plans to **delete all records with missing height**.
- The department considers using the score to **prioritize food-supplement rations**, with no appeal.
:::

:::question 3(a) [4 points] Is "admitted to a nutrition rehabilitation centre" a valid label for severe malnutrition? Explain using construct validity.
:::solution Solution & marking
No — it is a **proxy** shaped by an **institutional process**: admission requires being detected, referred, having transport and a bed, and family acceptance. Children far from centres (distance!) or from poorer households may be severely malnourished but **never admitted** → recorded as negative. The model learns **access to care** (who gets admitted), not malnutrition — the same pattern as cost-for-need. A better label: anthropometric criteria (weight-for-height z-score, MUAC) measured by health workers.

| Rubric | |
|---|---|
| Identifies proxy vs construct | 1 |
| Institutional process/access explanation | 1.5 |
| Consequence (bias against remote/poor) | 1 |
| Better target | 0.5 |
:::
:::

:::question 3(b) [5 points] Identify three distinct data-quality problems in the weight and survey data and name the dimension each violates.
:::solution Solution & marking
1. **kg and lb mixed** → **consistency (structural)**/unit error; needs unit-aware schema and explicit conversion.
2. **Scales reading 0.5 kg high** → **accuracy/systematic measurement error** ($b\ne0$); averaging won't remove it — recalibrate/correct per unit.
3. **Five-year-old income survey** → **timeliness/staleness** ($\Delta t$ = 5 years).
(Also: differential measurement error if faulty scales cluster in certain districts; children never visiting → completeness of subgroups/representativeness.)

| Rubric | |
|---|---|
| Three problems × (identification ½ + dimension & explanation 1) | 4.5 |
| Any fix mentioned | 0.5 |
:::
:::

:::question 3(c) [4 points] Evaluate the plan to delete records with missing height. What missingness mechanism is plausible and what is the consequence?
:::solution Solution & marking
Height is missing where units **lack measuring boards — remote units** → missingness depends on location/remoteness (**MAR** given unit; effectively systematic), and remote children likely have **higher malnutrition risk** (possibly MNAR-like with respect to outcome). Deleting them removes the **most vulnerable population**, biasing the model towards urban children and making it least accurate where risk is highest (representativeness failure). Better: keep records with a `height_missing` indicator, use weight-for-age/MUAC, impute with training-only models, and **fix data collection** (provide boards).

| Rubric | |
|---|---|
| Mechanism (systematic, not MCAR) | 1 |
| Deletion removes high-risk remote children | 1.5 |
| Alternative handling | 1.5 |
:::
:::

:::question 3(d) [4 points] Children who never visit a health unit have no records. Explain the consequence and how evaluation should account for it.
:::solution Solution & marking
The data cover **healthcare users only** (utilization, not burden — like administrative records). Non-visiting children — often poorest and most remote — are absent, so the model cannot be validated for them and its outputs ignore them (**representation bias / coverage error**). Evaluation must state the covered population, compare dataset composition with census/survey figures, report performance by district and distance band, and pair the tool with **community outreach** data (e.g. door-to-door MUAC screening) to reach unseen children.

| Rubric | |
|---|---|
| Missing population identified | 1 |
| Consequence (bias, invalid for them) | 1 |
| Two evaluation/mitigation steps | 2 |
:::
:::

:::question 3(e) [4 points] Should the score be used to prioritize food rations with no appeal? Discuss and recommend a policy.
:::solution Solution & marking
Rations are a **scarce, high-stakes allocation**; an unreliable, access-biased score would systematically under-serve remote and non-visiting children (**feedback**: fewer rations → worse outcomes but fewer recorded admissions → lower predicted risk). No appeal removes **contestability**. Recommend: use the score to **schedule extra health-worker visits** (supportive, low-harm), allocate rations based on **direct measurement** (MUAC/weight-for-height) confirmed by workers, keep an appeal and override process, audit allocations by district/income/sex, and monitor outcomes.

| Rubric | |
|---|---|
| Harm/bias of the proposed use | 1.5 |
| Contestability/human review | 1 |
| Concrete alternative policy + monitoring | 1.5 |
:::
:::

## Identify the Problems [CLO 4] — 8 points

:::question 4 [8 points] A team reports AUC 0.97 for a credit-default model. Identify four **distinct** problems from the description: standardization used the mean of all 50,000 records; features include "collections agency assigned"; each customer has several monthly rows split randomly; feature selection kept the 20 variables most correlated with default on the full dataset.
:::solution Solution & marking
1. **Preprocessing contamination** — standardization with full-data statistics (test data influenced training). Fix: fit on training only.
2. **Target leakage** — "collections agency assigned" happens **after** default. Fix: drop post-outcome fields.
3. **Group leakage** — same customer in train and test. Fix: customer-level (GroupKFold) split.
4. **Feature-selection contamination** — selection used test labels. Fix: select inside training folds.
(2 points each: 1 name, 1 mechanism/fix.)
:::
:::
