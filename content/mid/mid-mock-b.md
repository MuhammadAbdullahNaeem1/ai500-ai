# Mock Mid B — Modules 1 and 2

**95 points · 2 hours 30 minutes · closed book.** Part I: 15 MCQs (15 points, 30 minutes). Part II: 80 points, 2 hours. Module 3 is not examined.

<div class="pdf-links">
<a href="mid-guide.html">Mid guide</a>
<a href="mid-mock-a.html">Mock Mid A</a>
<a href="mid-mock-c.html">Mock Mid C</a>
</div>

## Part I — MCQs [15 points, 30 minutes]

Each question has one correct answer.

:::question 1 [1 point] Who proposed the imitation game as an operational test of machine intelligence?
(a) Norbert Wiener
(b) Claude Shannon
(c) Alan Turing
(d) John McCarthy
:::answer
**(c)** Wiener: cybernetics. Shannon: information theory. McCarthy: Dartmouth, the name "artificial intelligence".
:::
:::

:::question 2 [1 point] Shannon's information theory shows that:
(a) Information equals meaning
(b) Information is measurable, but information is not meaning
(c) Machines can understand language
(d) Entropy measures model fairness
:::answer
**(b)** See Example 6: pixels are encoded easily, yet "happy" remains a contested label.
:::
:::

:::question 3 [1 point] Which is a limitation of symbolic AI?
(a) Opaque decisions
(b) Needs large labelled datasets
(c) Brittleness under ambiguity and combinatorial explosion
(d) Cannot encode domain rules
:::answer
**(c)**
:::
:::

:::question 4 [1 point] In the four classical views, a rational agent:
(a) Must imitate humans
(b) Is always perfect
(c) Selects actions expected to advance its objectives given its information and constraints
(d) Uses only formal logic
:::answer
> **Notes wording** — “A rational agent selects actions expected to advance its objectives, given its information and constraints.” (M1 p.35) “Rational action does not mean perfect action.” (M1 p.35)

**(c)** Rational does not mean perfect.
:::
:::

:::question 5 [1 point] A fraud system blocks clear fraud and routes borderline cases to staff. Its autonomy level is:
(a) Passive analytical
(b) Decision support
(c) Semi-autonomous
(d) Fully autonomous
:::answer
**(c)** See Example 16.
:::
:::

:::question 6 [1 point] Training uses a median for missing blood pressure while production uses 0. This is:
(a) Proxy encoding
(b) Aggregation bias
(c) Train–serving mismatch
(d) Identity error
:::answer
**(c)** See the six representation risks in §1.5.
:::
:::

:::question 7 [1 point] The main framing error in forecasting is:
(a) Random splits of time-ordered data
(b) Ignoring position in the list
(c) Treating clusters as real categories
(d) Equating fluency with truth
:::answer
**(a)**
:::
:::

:::question 8 [1 point] A good evaluation plan should be:
(a) Chosen after seeing which metric looks best
(b) Locked before training
(c) Based only on accuracy
(d) Written by the vendor alone
:::answer
**(b)** This prevents metric shopping.
:::
:::

:::question 9 [1 point] The Epic Sepsis Model's external validation showed that:
(a) It reached AUROC near 0.95
(b) AUROC was about 0.63 and most sepsis cases were missed at the chosen score
(c) It raised no alerts
(d) It was validated at one site only
:::answer
**(b)** AUROC ≈ 0.63, 67% of sepsis cases missed at score ≥ 6.
:::
:::

:::question 10 [1 point] Administrative data encodes:
(a) Objective reality
(b) Institutional behaviour
(c) Only financial records
(d) Survey responses
:::answer
> **Notes wording** — “Administrative data encodes institutional behavior not objective reality.” (§2.2.5)

**(b)**
:::
:::

:::question 11 [1 point] A sampling frame misses homes without telephones. This is:
(a) Nonresponse bias
(b) Coverage error
(c) Measurement error
(d) Concept shift
:::answer
> **Notes wording** — “The sampling frame misses parts of the target population.” (§2.2.1)

**(b)** Nonresponse bias is when those who refuse differ from those who respond.
:::
:::

:::question 12 [1 point] "When the real-world action actually occurred" defines:
(a) Recording time
(b) Arrival time
(c) Processing time
(d) Event time
:::answer
> **Notes wording** — “When the real-world action actually occurred.” (§2.2.4)

**(d)**
:::
:::

:::question 13 [1 point] Which is true of synthetic data?
(a) It is automatically anonymous
(b) It removes historical bias
(c) It must be validated for fidelity, utility, privacy, fairness, coverage and realism
(d) It cannot be memorized by a generator
:::answer
> **Notes wording** — “Synthetic data can substantially improve privacy, experimentation, and model development, but it is not automatically safe or representative.” (M2 p.30)

**(c)**
:::
:::

:::question 14 [1 point] A consent form allows research use only. A company wants to train a commercial model. The issue is:
(a) Secondary use beyond consent conditions
(b) Group leakage
(c) Random error
(d) Label shift
:::answer
> **Notes wording** — “Consent explains what participants agreed to, while licensing defines what users are legally permitted to do with the data.” (M2 p.89)

**(a)** A licence and consent are separate checks, and neither replaces the other.
:::
:::

:::question 15 [1 point] Gender Shades mainly demonstrated:
(a) Better overall accuracy solves fairness
(b) Aggregate accuracy can hide large intersectional error disparities
(c) Cost is a good proxy for need
(d) Label errors do not affect benchmarks
:::answer
> **Notes wording** — “commercial facial recognition systems, which performed well on overall gender and overall skin type, failed catastrophically when evaluated at the intersection of darker skin and female gender.” (M2 p.37)

**(b)**
:::
:::

## Part II — Basic Definitions [12 points]

:::question 1(a) [3 points] Define machine learning and data science. State one way in which data science is broader than "training a model".
:::solution Solution & marking
> **Notes wording** — “Machine learning, conversely, is fundamentally rooted in prediction – seeking to accurately map inputs to outputs.” (M1 p.42)

**Machine learning** studies how a system can improve a task by learning patterns or parameters from data or experience; it is a major approach within AI. **Data science** covers how data are acquired, prepared, analysed, modelled, interpreted and communicated. It is broader: framing, collection, cleaning, EDA, communication and decisions are all part of it, and it may use no AI.

| Rubric | |
|---|---|
| ML | 1 |
| Data science | 1 |
| Breadth | 1 |
:::
:::

:::question 1(b) [3 points] Define class imbalance. Explain the accuracy paradox.
:::solution Solution & marking
> **Notes wording** — “Overall accuracy may provide an overly optimistic assessment of performance when classes are highly imbalanced.” (M2 p.64)

> **Notes wording** — “Class imbalance occurs when one or more classes are substantially less frequent than others.” (§2.5.4)

**Accuracy paradox:** when positives are rare, predicting the majority class for everyone gives high accuracy while detecting none. At 6% prevalence the trivial model scores 94% (real Quiz 2).

| Rubric | |
|---|---|
| Definition | 1 |
| Trivial majority model has high accuracy | 1 |
| Detects no positives | 1 |
:::
:::

:::question 1(c) [3 points] Define data provenance and data lineage. Why do both matter for an audit?
:::solution Solution & marking
> **Notes wording** — “Data provenance describes the origin of data and the processes used to generate them.” “Data lineage records how data evolve as they move through processing pipelines.” (§2.7.3)

They allow an auditor to reproduce results, trace a defect to its step, verify permitted use, and roll back.

| Rubric | |
|---|---|
| Provenance | 1 |
| Lineage | 1 |
| Audit value | 1 |
:::
:::

:::question 1(d) [3 points] Define data minimization and say how it conflicts with the urge to "collect everything".
:::solution Solution & marking
> **Notes wording** — “Data minimization is the principle that organizations should collect, retain, and process only the information reasonably necessary to achieve a clearly defined and legitimate purpose.” (§2.8.5)

"Collect everything" widens privacy risk, breach impact and proxy leakage without a stated purpose. Each variable must be justified against the task.

| Rubric | |
|---|---|
| Definition | 2 |
| Conflict explained | 1 |
:::
:::

## Part II — Short Conceptual Questions [16 points]

:::question 2(a) [4 points] Explain what a model card records and how it differs from a datasheet.
:::solution Solution & marking
> **Notes wording** — “By documenting critical aspects such as data sources, performance metrics, and fairness considerations, the Model Card helps users understand the model's behavior, its potential biases, and its limitations.” (M1 p.85) “this practice recommends comprehensive documentation of a dataset's motivation, composition, collection methods, preprocessing steps, recommended uses, and inherent limitations.” (M1 p.53)

A **model card** documents a **model**: intended use, evaluation procedure, conditions of good performance, subgroup results, limitations. A **datasheet** documents a **dataset**: motivation, composition, collection, preprocessing, uses, distribution and maintenance.

| Rubric | |
|---|---|
| Two or more model-card items | 1.5 |
| Two or more datasheet items | 1.5 |
| Clear distinction model vs dataset | 1 |
:::
:::

:::question 2(b) [4 points] A high-AUROC model is badly calibrated. Why can this still harm decisions? Name a way to fix it.
:::solution Solution & marking
> **Notes wording** — “They check discrimination (the model successfully ranks high-risk patients above low-risk ones) but also check calibration.” (M1 p.63)

AUROC measures **ranking** only. If the model says 0.8 and only 40% of those cases have the outcome, staff act on inflated risk, thresholds lose meaning, and capacity and cost planning go wrong. Fix: **recalibrate** with Platt scaling or isotonic regression on a validation set, then check with a calibration curve at the true prevalence.

| Rubric | |
|---|---|
| Discrimination vs calibration | 1.5 |
| Decision harm | 1.5 |
| Fix | 1 |
:::
:::

:::question 2(c) [4 points] Why might removing an outlier be wrong? What is the correct procedure?
:::solution Solution & marking
> **Notes wording** — “An outlier is an observation that differs substantially from the expected pattern of the data.” (§2.5.2) “Consequently, outliers should be investigated rather than automatically removed.” (M2 p.55) “These methods identify observations for further investigation rather than providing automatic criteria for deletion.” (M2 p.55)

An outlier may be a **true rare event**, such as fraud or a critical patient, and deleting it removes the cases the model most needs. It may also be an error. **Procedure:** investigate the cause (domain check, source records); classify it as error, rare valid value or different population; then correct, retain or exclude under a **documented rule**. z-scores and IQR flag observations for investigation; they are not automatic criteria for deletion.

| Rubric | |
|---|---|
| Rare but valid | 1.5 |
| Investigate cause | 1.5 |
| Documented decision | 1 |
:::
:::

:::question 2(d) [4 points] Differentiate site leakage from group leakage and name the correct validation for each.
:::solution Solution & marking
> **Notes wording** — “Group leakage occurs when related observations from the same entity appear in multiple data partitions.” (§2.6.6) “When deployment is intended for previously unseen institutions, random patient-level partitioning within the same hospitals does not adequately evaluate generalization.” (M2 p.79)

**Group leakage:** related observations from one entity (patient, customer) appear in several partitions. Use **group k-fold** or an entity-level split. **Site leakage:** the model learns site-specific signals (scanner, hospital protocol, label habits), so results do not transfer. Use **leave-one-site-out** or site hold-out.

| Rubric | |
|---|---|
| Each definition | 1 |
| Each validation | 1 |
:::
:::

## Part II — Scenario 1: Flood early warning [18 points, Module 1 focus]

:::orig River-flood warning system
A provincial disaster authority wants AI to warn villages along a river about flooding. Data: rainfall gauges, upstream dam releases, satellite imagery, river-level sensors, and past flood records. Past records come mainly from villages near the district headquarters. The team shuffles hourly rows, splits 80/20 and reports an **RMSE of 4 cm**. Facts:
- evacuation takes **36 hours**;
- two river gauges are offline for weeks during monsoon;
- a false evacuation costs families income and reduces trust in later warnings;
- a missed flood can cost lives.
:::

:::question 3(a) [5 points; Type and framing] What type of AI problem is this? State the unit, index time, horizon, decision-maker and action.
:::solution Solution & marking
> **Notes wording** — “the prediction horizon must strictly align with the operational window available to act.” (M1 p.101)

**Forecasting** (with a decision layer). **Unit:** a village or river segment. **Index time:** each 6-hour update, using data available then. **Horizon:** at least 36 hours, e.g. 48 hours, since evacuation takes 36. **Decision-maker:** district disaster officer. **Action:** issue a staged alert and begin evacuation.

| Rubric | |
|---|---|
| Type | 1 |
| Each of four elements, 1 mark; horizon must be ≥ 36 h for full credit | 4 |
:::
:::

:::question 3(b) [4 points; Evaluation] Why does the RMSE of 4 cm not show the model is fit for use?
:::solution Solution & marking
> **Notes wording** — “Random splitting leaked this future knowledge into the past; temporal validation exposed the flaw.” (M1 p.66)

Shuffled hourly rows of a **time series** let neighbouring hours sit on both sides of the split, which is temporal leakage. Use a forward-chaining split. RMSE averages over calm days; what matters is **performance on rare flood peaks**, detection delay, false alarms, and performance at distant villages. Also compare with a **baseline** such as persistence or the existing bulletin.

| Rubric | |
|---|---|
| Random split leak | 1.5 |
| Average hides flood events | 1.5 |
| Baseline or event metrics | 1 |
:::
:::

:::question 3(c) [4 points; Data risks] Identify two distinct data risks and how to handle each.
:::solution Solution & marking
> **Notes wording** — “Not all missing values indicate poor data quality; in many situations, they are expected and informative.” (M2 p.50)

- **Representation/selection bias:** records near headquarters leave distant villages under-represented. Collect local records; evaluate by region.
- **Missing sensors in monsoon:** missingness is tied to the conditions of interest (not MCAR). Add indicators; use a fallback, not silent imputation.
- Also: flood-record **label quality**, and dam-release **availability time**.

| Rubric | per risk |
|---|---|
| Risk named and explained | 1 |
| Handling | 1 |
:::
:::

:::question 3(d) [5 points; Deployment] Propose a decision policy, one abstention condition, and two monitored quantities.
:::solution Solution & marking
> **Notes wording** — “Abstention is a risk-control mechanism that allows a system to defer difficult cases to human review or an alternative process rather than producing potentially unreliable outputs.” (M1 p.79)

**Policy:** missed floods cost lives, so tolerate more false alarms but stage them: *watch → prepare → evacuate*, with an officer confirming evacuation. A staged alert protects trust. **Abstain/fallback:** when key gauges are offline or inputs are out of range, fall back to the hydrologist's manual bulletin. **Monitor:** sensor-missing rate, calibration of warnings, lead time achieved, missed floods, false-alarm rate by district, and input drift.

| Rubric | |
|---|---|
| Asymmetric costs justify the policy | 1.5 |
| Human confirmation/staging | 1 |
| Abstain with fallback | 1.5 |
| Two monitored quantities | 1 |
:::
:::

## Part II — Scenario 2: Phone-data microloans [18 points, Module 2 focus]

:::orig Mobile-phone credit scoring
A fintech lender wants to score applicants with no credit history. It buys a telecom dataset containing call patterns, top-up behaviour, location history and contacts, and merges it with its past loan outcomes. The vendor's licence allows "internal analytics only". Names and phone numbers were removed before transfer. Facts:
- labels exist only for applicants who were approved;
- women in the data often share a phone with relatives;
- postal area, top-up amount and contact count are strong predictors;
- the model will be sold to two other lenders;
- the product team says: "We removed gender, so the model is fair."
:::

:::question 4(a) [4 points; Licence and consent] Identify two legal or ethical problems with how the data are being used.
:::solution Solution & marking
> **Notes wording** — “A data license specifies the conditions under which a dataset may be accessed, used, modified, or redistributed.” (M2 p.87) “Consent explains what participants agreed to, while licensing defines what users are legally permitted to do with the data.” (M2 p.89)

- **Licence:** "internal analytics only" does not permit selling a model trained on the data; licence compatibility extends to derived models.
- **Consent/secondary use:** subscribers agreed to phone service, not to credit scoring. Consent does not transfer to a new purpose.
- Also: **minimization**, as location history and contacts may not be necessary.

| Rubric | per problem |
|---|---|
| Problem named | 1 |
| Applied to the case | 1 |
:::
:::

:::question 4(b) [4 points; Privacy] "We removed names and numbers, so the data is anonymous." Evaluate this.
:::solution Solution & marking
> **Notes wording** — “de-identification should be viewed as a risk-reduction strategy rather than a guarantee of anonymity.” (§2.8.3)

Location traces and contact graphs are **quasi-identifiers**: a few home–work points can re-identify a person, especially via linkage with other data. So the claim fails; add access controls, aggregation and minimization.

| Rubric | |
|---|---|
| Rejects the claim, with notes' idea | 1.5 |
| Quasi-identifiers/linkage in the case | 1.5 |
| Mitigation | 1 |
:::
:::

:::question 4(c) [5 points; Bias] Explain why removing gender does not give fairness. Name a label problem and a measurement problem in this case.
:::solution Solution & marking
> **Notes wording** — “Other variables may function as proxies for the omitted attribute” (M2 p.94)

> **Notes wording** — “Excluding a sensitive variable from a predictive model does not necessarily prevent discriminatory outcomes.” (§2.8.6)

**Proxies:** postal area, top-ups and contacts can stand in for gender and income. **Keep** gender under restricted access to audit outcomes. **Label problem:** selective labels, because repayment is known only for approved applicants, and rejected applicants are unseen. **Measurement:** shared phones mean behaviour is attributed to one woman but produced by several people, a differential measurement error.

| Rubric | |
|---|---|
| Proxy mechanism | 1.5 |
| Retain for auditing | 1 |
| Selective labels | 1.25 |
| Shared-phone measurement error | 1.25 |
:::
:::

:::question 4(d) [5 points; Audit] Apply $Q(D,T,C)$ and give a verdict on using this data for this task.
:::solution Solution & marking
> **Notes wording** — “There is no such thing as a universally good or high-quality dataset in a vacuum. A dataset is only good for a specific purpose under specific conditions.” (§2.1.2)

**D:** telecom behaviour with approved-only labels. **T:** credit scoring. **C:** multi-lender deployment in a regulated, high-stakes setting. **Verdict:** not fit as it stands. The licence and consent do not permit the use, labels are selective, and groups are measured unequally. **Conditions:** renegotiate the licence and consent; reduce the variables; evaluate subgroup error; test on applicant populations for each lender; provide a route to appeal and human review.

| Rubric | |
|---|---|
| D, T and C, 1 each | 3 |
| Reasoned verdict | 1 |
| Conditions | 1 |
:::
:::

## Part II — Identify Distinct Problems [8 points]

:::question 5 [8 points] A hospital predicts which patients will miss appointments and double-books them. Training data come from the wealthiest of its four clinics. "Missed" is recorded differently at each clinic. The model is 89% accurate overall but much worse for patients who need interpreters. Double-booked patients wait longer, and more of them then stop attending, which enters the next training data. Identify four **distinct** problems (2 points each).
:::solution Solution & marking
1. **Representation bias:** one wealthy clinic does not represent all four.
2. **Measurement/label inconsistency:** "missed" differs across clinics (consistency, construct validity).
3. **Aggregation/evaluation bias:** an overall 89% hides failure for patients needing interpreters.
4. **Feedback loop/performative effect:** double-booking worsens the waits that cause missed visits, and this feeds retraining.
Also accepted: **deployment harm**, because the action penalizes those predicted to miss.
:::
:::

## Part II — Calculation [8 points]

:::question 6 [8 points] (a) Two nurses label 200 notes as urgent or not. Both say urgent: 60. Only nurse 1 says urgent: 20. Only nurse 2 says urgent: 10. Both say not urgent: 110. Compute observed agreement and Cohen's $\kappa$. Why is $\kappa$ preferred to raw agreement? (b) Resting heart rates have $Q_1=48$, $Q_3=64$, mean 56, $s=10$. Compute the IQR and the screening fences. Are 95 and 20 flagged? Give their z-scores. What should happen next?
:::solution Solution & marking
> **Notes wording** — “These methods identify observations for further investigation rather than providing automatic criteria for deletion.” (M2 p.55)

**(a)** $p_o=\frac{60+110}{200}=0.85$. Nurse 1 urgent $=\frac{80}{200}=0.40$, nurse 2 urgent $=\frac{70}{200}=0.35$. $p_e=0.40(0.35)+0.60(0.65)=0.14+0.39=0.53$.
$$\kappa=\frac{p_o-p_e}{1-p_e}=\frac{0.85-0.53}{0.47}\approx0.68$$
$\kappa$ corrects for agreement expected by chance, which raw agreement ignores.

**(b)** IQR $=64-48=16$. Fences $=[48-24,\ 64+24]=[24,\ 88]$. Both 95 and 20 are flagged. $z_{95}=\frac{95-56}{10}=3.9$ and $z_{20}=\frac{20-56}{10}=-3.6$. Next: **investigate**. 95 could be a real tachycardic reading in a resting record, and 20 could be a sensor fault. Do not delete automatically.

:::warn Typo in the notes
§2.5.2 prints the upper fence as $Q_3-1.5\,\text{IQR}$. The correct upper fence is $Q_3+1.5\,\text{IQR}$, as the notes' own footnote 213 shows.
:::

| Rubric | |
|---|---|
| $p_o$, $p_e$ | 2 |
| $\kappa$ with reason | 2 |
| IQR, fences, flags | 2 |
| z-scores and investigation | 2 |
:::
:::
