# Mock Mid C — Modules 1 and 2

**95 points · 2 hours 30 minutes · closed book.** Part I: 15 MCQs (15 points, 30 minutes). Part II: 80 points, 2 hours. Module 3 is not examined.

<div class="pdf-links">
<a href="mid-guide.html">Mid guide</a>
<a href="mid-mock-a.html">Mock Mid A</a>
<a href="mid-mock-b.html">Mock Mid B</a>
</div>

## Part I — MCQs [15 points, 30 minutes]

Each question has one correct answer.

:::question 1 [1 point] Predictive policing data becoming "self-confirming" because more patrols record more incidents is an example of:
(a) Train–serving mismatch
(b) A feedback loop
(c) Label shift only
(d) Data minimization
:::answer
> **Notes wording** — “This can produce self-reinforcing bias, selective labels, performative effects, and feedback loops.” (M1 p.12)

**(b)** See Example 5, which also covers selective labels and performative effects.
:::
:::

:::question 2 [1 point] Which is NOT one of the eight pipeline stages?
(a) Representation
(b) Decision
(c) Monitoring
(d) Publication
:::answer
**(d)** Problem formulation, data, representation, model, evaluation, decision, deployment, monitoring.
:::
:::

:::question 3 [1 point] In $a(x)=$ intervene if $\hat p\ge t$, the threshold $t$ should reflect:
(a) Always 0.5
(b) Error costs, capacity, uncertainty, fairness and human review
(c) Only the AUROC
(d) Only the training loss
:::answer
> **Notes wording** — “A machine learning prediction is not a decision.” (M1 p.68)

**(b)**
:::
:::

:::question 4 [1 point] “Ultimately, a highly accurate model sitting in a Jupyter notebook is not a deployed AI system.” This stresses:
(a) Latency, fallback, rollback, ownership
(b) Better hyperparameters
(c) More training data
(d) Symbolic reasoning
:::answer
> **Notes wording** — “Ultimately, a highly accurate model sitting in a Jupyter notebook is not a deployed AI system.” (M1 p.75)

**(a)**
:::
:::

:::question 5 [1 point] Undeclared consumers, glue code and entanglement describe:
(a) Hidden technical debt
(b) Coverage error
(c) Data provenance
(d) Generative AI risk
:::answer
**(a)** From Sculley et al. (2015).
:::
:::

:::question 6 [1 point] The problem type with output $\tau=\mathbb E[Y(1)-Y(0)]$ is:
(a) Ranking
(b) Causal estimation
(c) Clustering
(d) Control
:::answer
**(b)** Common framing error: reading correlation as an intervention effect.
:::
:::

:::question 7 [1 point] A generative model fabricating legal citations illustrates:
(a) Confabulation
(b) Covariate shift
(c) Group leakage
(d) Isotonic regression
:::answer
**(a)** Example 22.
:::
:::

:::question 8 [1 point] TensorFlow Extended's main lesson is that:
(a) Training scripts are production systems
(b) Production needs schema validation, shared transforms, gates and rollback
(c) Monitoring is optional
(d) Deep learning is required
:::answer
**(b)**
:::
:::

:::question 9 [1 point] The eight-stage curation workflow differs from cleaning because curation:
(a) Is only about deleting bad rows
(b) Spans the data lifecycle: acquiring, organizing, validating, documenting, preserving, maintaining
(c) Happens only after deployment
(d) Applies only to images
:::answer
> **Notes wording** — “Although data cleaning is an important component of curation, the two concepts are not synonymous.” (M2 p.46)

**(b)** Cleaning is one activity within curation.
:::
:::

:::question 10 [1 point] Survey respondents overstate voting. This is mainly:
(a) Social desirability (a response error)
(b) Coverage error
(c) Timeliness
(d) Site leakage
:::answer
**(a)**
:::
:::

:::question 11 [1 point] A sensor reads 2 °C too high everywhere. This error is:
(a) Random
(b) Systematic
(c) Differential only
(d) Unmeasurable
:::answer
**(b)** It is differential if it varies by group or site.
:::
:::

:::question 12 [1 point] SMOTENC differs from SMOTE because it:
(a) Handles mixed numerical and categorical features
(b) Undersamples the majority class
(c) Calibrates probabilities
(d) Only copies rows
:::answer
**(a)**
:::
:::

:::question 13 [1 point] Two radiologists have $\kappa=0.82$. This means:
(a) They agree on 82% of images
(b) Strong agreement beyond chance
(c) The model has accuracy 0.82
(d) Labels are correct
:::answer
**(b)** Two experts can agree and both be wrong.
:::
:::

:::question 14 [1 point] Equal opportunity requires equal:
(a) Predicted positive rates
(b) True positive rates
(c) False positive and true positive rates
(d) Precision
:::answer
> **Notes wording** — “True positive rates are equal across groups.” (§2.8.8)

**(b)** Equalized odds is (c).
:::
:::

:::question 15 [1 point] Northcutt et al.'s label-error study showed that:
(a) Common benchmarks contain label errors that can change which model looks best
(b) Benchmarks are error-free
(c) Errors affect only small datasets
(d) Calibration fixes label errors
:::answer
**(a)**
:::
:::

## Part II — Basic Definitions [12 points]

:::question 1(a) [3 points] Define probabilistic calibration and distinguish it from discrimination.
:::solution Solution & marking
A model is **well calibrated** when, among cases given probability $p$, about a proportion $p$ have the outcome (of cases given 0.8, about 80%). **Discrimination** is how well the model **ranks or separates** cases with and without the outcome.

| Rubric | |
|---|---|
| Definition | 1.5 |
| Predicted ↔ observed frequency | 0.5 |
| Distinction | 1 |
:::
:::

:::question 1(b) [3 points] Define temporal leakage. Why does it make a strong result unreliable?
:::solution Solution & marking
> **Notes wording** — “Temporal leakage occurs when information from the future is used to predict an earlier outcome.” (§2.6.5)

The model uses **information not available at the time the prediction is made**. Test performance appears artificially high, and the information will not exist in deployment.

| Rubric | |
|---|---|
| Post-index/future information | 1.5 |
| Unavailable at prediction time | 0.5 |
| Inflated evaluation | 1 |
:::
:::

:::question 1(c) [3 points] Define data governance and name two roles it assigns.
:::solution Solution & marking
> **Notes wording** — “Data governance is the framework of policies, roles, processes, and technical controls through which data are managed, protected, and used throughout their lifecycle.” (§2.8.1)

Roles: data owner and data steward, for example.

| Rubric | |
|---|---|
| Definition | 2 |
| Two roles | 1 |
:::
:::

:::question 1(d) [3 points] Define completeness. Why is a "complete" dataset not automatically representative?
:::solution Solution & marking
> **Notes wording** — “Completeness measures whether all required data is actually present.” (§2.3.1)

Every cell may be filled, yet whole populations may be absent. Representativeness asks whether the data reflect the intended target population and operating conditions.

| Rubric | |
|---|---|
| Definition | 1.5 |
| Contrast, with reason | 1.5 |
:::
:::

## Part II — Short Conceptual Questions [16 points]

:::question 2(a) [4 points] Two models perform similarly. Model A is complex and slightly more accurate; Model B is simple and interpretable. Argue why Model A should not be chosen automatically, using three criteria.
:::solution Solution & marking
> **Notes wording** — “Ultimately, a foundational principle of applied machine learning is that the most complex model is not automatically the best model.” (M1 p.59)

Higher test accuracy does not mean greater real-world utility. Criteria: **interpretability/auditability** in regulated settings, **latency and compute**, **maintenance burden**, **robustness** to shift and missing data, **calibration**, **lifecycle cost**.

| Rubric | |
|---|---|
| Accuracy ≠ utility | 1 |
| Three criteria, 1 each | 3 |
:::
:::

:::question 2(b) [4 points] Explain the difference between a poor problem statement and a good one, with an example.
:::solution Solution & marking
Poor: "Build an AI model to predict hospital readmission." It names no decision. Better: *"At the time of discharge, estimate the probability of an unplanned 30-day readmission among adult medical patients so that the discharge team can allocate a limited number of follow-up appointments, while measuring calibration, subgroup performance, preventability and the consequences of false alerts."*

| Rubric | |
|---|---|
| Good statement names decision, time and population | 2 |
| Valid rewritten example | 2 |
:::
:::

:::question 2(c) [4 points] "Big data fixes bias." Evaluate, referring to one Module 1 case.
:::solution Solution & marking
False. Volume reduces random noise, not **systematic** error. In **Google Flu Trends**, about 50 million candidate terms against 1,152 weekly observations produced chance correlations, and estimates ran high in 100 of 108 weeks. Larger samples of a biased process give a more confident wrong answer.

| Rubric | |
|---|---|
| Rejects claim | 1 |
| Random vs systematic | 1 |
| Case details | 2 |
:::
:::

:::question 2(d) [4 points] Why do oversampling and SMOTE require recalibration?
:::solution Solution & marking
> **Notes wording** — “When this occurs, predicted probabilities often require recalibration to reflect the true prevalence of outcomes in the target population.” (M2 p.66) “After recalibration, the same patient might receive a probability of 22% instead of 70%, providing a more realistic estimate of cancer risk.” (M2 p.67)

Rebalancing changes the class prior seen in training, so predicted probabilities become inflated relative to the true prevalence. Example: a patient rated 70% risk might truly be about 22%. Ranking may survive but the probabilities do not. Recalibrate with **Platt scaling** or **isotonic regression** on data at natural prevalence.

| Rubric | |
|---|---|
| Prior changed | 1.5 |
| Inflated probabilities | 1.5 |
| Recalibration | 1 |
:::
:::

## Part II — Scenario 1: Support assistant [18 points, Module 1 focus]

:::orig Telecom support assistant
A telecom company builds an LLM assistant to answer customer questions and to **issue refunds of up to Rs 5,000 automatically**. Success is measured by the number of chats closed without a human. Facts:
- the assistant sometimes invents policy terms;
- Urdu questions perform worse than English ones;
- a rule-based menu already resolves 60% of billing questions;
- customers who get a wrong answer often give up and do not complain;
- the policy document is updated monthly.
:::

:::question 3(a) [4 points; Framing] What autonomy level does this system have? Is AI needed for every part? Explain.
:::solution Solution & marking
Issuing refunds alone makes it **autonomous** for that action, or semi-autonomous if edge cases escalate. Answering questions alone would be decision support for the customer. The canvas asks about **necessity of AI and simpler alternatives**: the rule menu already handles 60%, so it should be the **baseline**, with the LLM used only where rules fail.

| Rubric | |
|---|---|
| Autonomy level, justified | 2 |
| Simpler alternative as baseline | 2 |
:::
:::

:::question 3(b) [5 points; Objective] Critique "chats closed without a human" as a success measure.
:::solution Solution & marking
It is a **proxy** with poor construct validity for "customer problem solved". A customer who gives up counts as success, so failures look like wins (**solving the wrong problem**). Optimizing it rewards deflection, not help. Replace it with **verified resolution**, repeat contact within 7 days, refund accuracy, and satisfaction, with **guardrail** metrics for wrong refunds and by-language error.

| Rubric | |
|---|---|
| Proxy/construct validity | 1.5 |
| Silent failure counted as success | 1.5 |
| Better primary metric | 1 |
| Guardrail | 1 |
:::
:::

:::question 3(c) [4 points; Risks] Identify two risks specific to generative AI here, with a mitigation for each.
:::solution Solution & marking
- **Confabulation:** invented policy. Use retrieval from the current policy and show sources; refuse if unsupported.
- **Information integrity/fluency mistaken for truth:** confident wrong answers mislead customers. Label AI use; give a human route.
- Also: privacy of customer data in prompts.

| Rubric | per risk |
|---|---|
| Risk | 1 |
| Mitigation | 1 |
:::
:::

:::question 3(d) [5 points; Lifecycle] Name a fairness check, an abstention condition, a monitored quantity, a governance owner, and a rollback trigger.
:::solution Solution & marking
> **Notes wording** — “Abstention is a risk-control mechanism that allows a system to defer difficult cases to human review or an alternative process rather than producing potentially unreliable outputs.” (M1 p.79)

- **Fairness:** compare resolution and wrong-refund rates in Urdu and English.
- **Abstain:** low retrieval support, a policy-disputed case, or a refund near the limit → pass to a human.
- **Monitor:** wrong-refund rate, repeat contacts, drift after each policy update.
- **Owner:** named product and risk lead.
- **Rollback:** wrong refunds above an agreed rate → return to the rule menu.

| Rubric | 1 mark each |
|---|---|
| All five | 5 |
:::
:::

## Part II — Scenario 2: Chest X-ray TB triage [18 points, Module 2 focus]

:::orig Multi-hospital TB screening
A consortium trains a model to flag tuberculosis from chest X-rays. It has 40,000 images from three city hospitals. Facts:
- patients have several X-rays, and images were randomly split;
- Hospital A uses portable scanners for its sickest patients;
- labels came from one radiologist per image; a sample check gave $\kappa=0.55$;
- children are 2% of the images but 15% of target patients;
- the tool will be deployed in rural clinics with older machines;
- hospital logos appear in image corners;
- the model reports AUROC 0.97.
:::

:::question 4(a) [5 points; Leakage] Identify three distinct leakage or shortcut problems and their fixes.
:::solution Solution & marking
> **Notes wording** — “Group leakage occurs when related observations from the same entity appear in multiple data partitions.” (§2.6.6) “When deployment is intended for previously unseen institutions, random patient-level partitioning within the same hospitals does not adequately evaluate generalization.” (M2 p.79)

| Problem | Fix |
|---|---|
| **Group leakage:** one patient's images across partitions | Split by patient |
| **Site leakage/shortcut:** logos and scanner signature reveal the hospital, and so its prevalence | Crop logos; leave-one-site-out validation |
| **Shortcut via portable scanner:** scanner type marks severity, not disease | Stratify by scanner; test within scanner type |

| Rubric | |
|---|---|
| Each with fix | 1.5 each |
| Links to inflated AUROC | 0.5 |
:::
:::

:::question 4(b) [4 points; Labels] What does $\kappa=0.55$ imply? Propose a labelling redesign.
:::solution Solution & marking
Agreement beyond chance is only moderate, so labels are noisy. One reader per image hides uncertainty, and the model inherits this ceiling. **Redesign:** at least two independent readers, adjudication for disagreement, a written label protocol, stored uncertainty and acceptable alternative labels, and microbiological confirmation where available.

| Rubric | |
|---|---|
| Interpretation | 1.5 |
| Two independent readers/adjudication | 1.5 |
| Protocol or reference standard | 1 |
:::
:::

:::question 4(c) [4 points; Representativeness] Evaluate representativeness for the rural deployment. What validation is required?
:::solution Solution & marking
> **Notes wording** — “Representativeness asks whether the data adequately reflects the intended target population and the actual operating conditions of deployment.” (§2.3.5) “External validation is therefore necessary before local deployment.” (M1 p.131)

Two gaps: **children** are 2% of images against 15% of target patients, and data come from **city hospitals with newer machines**, which is covariate shift for rural clinics. Required: **external validation** at rural sites on their machines, **subgroup** results for children, **calibration** at rural prevalence, and a **silent trial** before use.

| Rubric | |
|---|---|
| Two gaps | 2 |
| Two validations | 2 |
:::
:::

:::question 4(d) [5 points; Fairness] Should the team target demographic parity or equal opportunity here? Justify, and describe how you would use the tool responsibly.
:::solution Solution & marking
> **Notes wording** — “True positive rates are equal across groups.” (§2.8.8) “These fairness criteria may be mutually incompatible, particularly when outcome prevalence differs between populations.” (M2 p.98)

**Equal opportunity** suits this best, since a missed TB case is the harm. All groups should have similar sensitivity. Demographic parity is unsuitable because true prevalence may differ across groups. Use: the tool **prioritizes** films for readers rather than ruling out disease; low-confidence cases and children get human review; sensitivity is monitored by age and site. Note the incompatibility of fairness criteria when base rates differ.

| Rubric | |
|---|---|
| Choice | 1 |
| Justification from harm | 1.5 |
| Why not parity | 1 |
| Responsible use | 1.5 |
:::
:::

## Part II — Identify Distinct Problems [8 points]

:::question 5 [8 points] A food-delivery platform predicts which riders are "low performers". Ratings come from customers. Riders in rain-prone zones have longer delivery times. Time is measured from the order placed, including restaurant delay. Riders flagged as low performers receive fewer orders, so their monthly data becomes sparse and their rating worse. Women riders are few in the data. Identify four **distinct** problems (2 points each).
:::solution Solution & marking
1. **Measurement/construct validity:** delivery time includes restaurant delay, so it does not measure rider performance.
2. **Rating bias:** customer ratings can reflect prejudice (historical/measurement bias).
3. **Context/aggregation:** zones differ, and comparing riders across rain-prone zones treats unlike conditions as alike.
4. **Feedback loop:** fewer orders → sparse data → worse score.
Also: **representation bias** for women riders.
:::
:::

## Part II — Calculation [8 points]

:::question 6 [8 points] (a) A model screens 10,000 encounters, with 5% prevalence. Threshold $t_1$ flags 8% of encounters at 25% precision. Threshold $t_2$ flags 3% at 50% precision. Reviews are capped at 400. Costs: false positive 20, false negative 500. For each threshold compute TP, FP, FN, recall and total cost, then choose. (b) Platt scaling has $A=-1.5$, $B=0.5$. Compute $P$ for scores 2 and 0.
:::solution Solution & marking
> **Notes wording** — “The optimal threshold keeps the manual search lines moving, preserves the physical workflow, and ensures that the AI's predictions are actually actionable in the real world.” (M1 p.73)

**(a)** Positives $=500$.

| | Flagged | TP | FP | FN | Recall | Cost |
|---|---|---|---|---|---|---|
| $t_1$ | 800 | 200 | 600 | 300 | 0.40 | $600(20)+300(500)=162{,}000$ |
| $t_2$ | 300 | 150 | 150 | 350 | 0.30 | $150(20)+350(500)=178{,}000$ |

$t_1$ costs less but flags 800, twice the capacity of 400. $t_2$ fits. **Choice:** $t_1$ is not feasible. Use $t_2$, or better, **rank and review the top 400**, which sits between them and uses all capacity.

**(b)** $P=\frac{1}{1+\exp(As+B)}$.
Score 2: $\exp(-3+0.5)=\exp(-2.5)=0.082$, so $P=\frac{1}{1.082}\approx0.92$.
Score 0: $\exp(0.5)=1.649$, so $P=\frac{1}{2.649}\approx0.38$.

| Rubric | |
|---|---|
| Counts | 2 |
| Recall and cost | 2 |
| Capacity reasoning | 2 |
| Platt values | 2 |
:::
:::
