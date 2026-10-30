# Mock Mid A — Modules 1 and 2

**95 points · 2 hours 30 minutes · closed book.** Part I: 15 MCQs (15 points, 30 minutes). Part II: 80 points, 2 hours. Module 3 is not examined. Sit it timed, then mark yourself strictly against the rubrics.

<div class="pdf-links">
<a href="mid-guide.html">Mid guide</a>
<a href="mid-mock-b.html">Mock Mid B</a>
<a href="mid-mock-c.html">Mock Mid C</a>
</div>

## Part I — MCQs [15 points, 30 minutes]

Each question has one correct answer.

:::question 1 [1 point] Which statement best captures the relation between AI and machine learning?
(a) AI and ML are the same field under two names
(b) ML is one major approach within AI
(c) AI is one approach within ML
(d) ML includes search, planning and logic
:::answer
**(b)** AI also includes search, planning, logic, constraint satisfaction, expert systems and control.
:::
:::

:::question 2 [1 point] A thermostat switches the heating on and off with no human input. In the notes' terms it is:
(a) Autonomous but not intelligent
(b) Intelligent but not autonomous
(c) A decision-support system
(d) Generative AI
:::answer
**(a)** Autonomy is not the same as intelligence.
:::
:::

:::question 3 [1 point] "What would happen if every student were required to attend every lecture?" is:
(a) A prediction question
(b) A clustering question
(c) An intervention (causal) question
(d) A ranking question
:::answer
**(c)** Prediction says who is likely to succeed. Causal reasoning says which actions improve success.
:::
:::

:::question 4 [1 point] In the NIST AI RMF, which function means prioritizing and acting on risks (mitigate, transfer or accept)?
(a) Govern
(b) Map
(c) Measure
(d) Manage
:::answer
**(d)** Govern sets culture and accountability, Map contextualizes, Measure assesses, Manage acts.
:::
:::

:::question 5 [1 point] Which claim requires temporal validation?
(a) "It works for everyone"
(b) "It works in the future"
(c) "Its probabilities are meaningful"
(d) "It works at other hospitals"
:::answer
**(b)** Train on the past and test strictly on the future. Everyone → subgroup evaluation; probabilities → calibration; other sites → external validation.
:::
:::

:::question 6 [1 point] Many models fit the training data equally well but behave differently in deployment. This failure mode is:
(a) Distribution shift
(b) Underspecification
(c) Data leakage
(d) Weak evaluation
:::answer
**(b)**
:::
:::

:::question 7 [1 point] Google Flu Trends mainly teaches that:
(a) Volume removes measurement bias
(b) A proxy is useful only while its relation to the target stays stable
(c) Search data should never be used
(d) Larger models always beat simple baselines
:::answer
**(b)** The combined GFT + lagged CDC model beat either alone.
:::
:::

:::question 8 [1 point] Mean age is computed on the full dataset before the train–test split. This is:
(a) Group leakage
(b) Target leakage
(c) Train–test contamination
(d) Site leakage
:::answer
**(c)** Real Quiz 2 tested exactly this. Compute it on the training data only.
:::
:::

:::question 9 [1 point] Men withhold income more often than women, but within each gender missingness is unrelated to income. This is:
(a) MCAR
(b) MAR
(c) MNAR
(d) Informative labels
:::answer
**(b)** Missingness depends on an observed variable, not on the missing value after conditioning.
:::
:::

:::question 10 [1 point] A hospital's "lactate" is missing mostly for patients doctors judged healthy. Dropping this signal by imputing the mean loses:
(a) Provenance
(b) Informative missingness
(c) Licence compatibility
(d) Construct validity of the model
:::answer
> **Notes wording** — “Missingness itself can be informative.” (M2 p.53)

**(b)** The absence itself carries information. Add a missingness indicator.
:::
:::

:::question 11 [1 point] Which is a *false merge*?
(a) Two different people combined into one record
(b) One person split into two records
(c) A record dropped by mistake
(d) A duplicated transaction
:::answer
> **Notes wording** — “Because matching is imperfect, entity resolution may introduce both false merges (combining different entities) and false splits (failing to combine identical entities), particularly when records are incomplete or inconsistent.” (M2 p.60)

**(a)** A false split is (b).
:::
:::

:::question 12 [1 point] Oversampling should be applied:
(a) Before splitting, so all partitions are balanced
(b) To the test set only
(c) Only inside the training partition or training folds
(d) Never
:::answer
> **Notes wording** — “Resampling should therefore be performed only within the training partition or within each training fold during cross-validation” (§2.5.4)

**(c)**
:::
:::

:::question 13 [1 point] Demographic parity requires equal:
(a) True positive rates across groups
(b) Predicted positive rates across groups
(c) Precision across groups
(d) Accuracy across groups
:::answer
> **Notes wording** — “Predicted positive rates are equal across groups.” (§2.8.8)

**(b)**
:::
:::

:::question 14 [1 point] Which statement about de-identification matches the notes?
(a) It guarantees anonymity
(b) It removes the need for governance
(c) It is a risk-reduction strategy, not a guarantee
(d) It applies only to images
:::answer
> **Notes wording** — “de-identification should be viewed as a risk-reduction strategy rather than a guarantee of anonymity.” (§2.8.3)

**(c)**
:::
:::

:::question 15 [1 point] A pathology dataset is "good" for research but poor for a rural screening tool. This illustrates:
(a) Data lineage
(b) Fitness for purpose $Q(D,T,C)$
(c) Concept shift
(d) Equalized odds
:::answer
> **Notes wording** — “There is no such thing as a universally good or high-quality dataset in a vacuum. A dataset is only good for a specific purpose under specific conditions.” (§2.1.2)

**(b)** Quality is judged for a dataset, a task and a context.
:::
:::

## Part II — Basic Definitions [12 points]

:::question 1(a) [3 points] Define artificial intelligence so that both its scientific and engineering character are captured.
:::solution Solution & marking
AI is the **scientific and engineering discipline** concerned with constructing computational systems that **perceive or receive information, form useful representations, reason or learn from evidence, and select actions or outputs in pursuit of specified objectives under uncertainty and constraints.**

| Rubric | |
|---|---|
| Discipline: science and engineering | 1 |
| Capabilities: representation, reasoning, learning, perception, action | 1 |
| Objectives under uncertainty/constraints; not reduced to ML | 1 |
:::
:::

:::question 1(b) [3 points] Define prediction horizon and index time. Why must the horizon fit the decision?
:::solution Solution & marking
> **Notes wording** — “Index time: (or prediction origin) is the exact, specific moment in the real world at which the model is required to make its prediction.” (M1 p.100) “The prediction horizon defines the exact temporal window into the future within which the target outcome must occur.” (M1 p.100) “the prediction horizon must strictly align with the operational window available to act.” (M1 p.101)

**Index time** is the exact moment the prediction is made; every feature must be available at or before it. **Prediction horizon** is how far ahead the prediction looks. It must fit the window in which someone can act: for the turbine gearbox (Example 36) a 24-hour warning is useless, while 14–30 days allows parts and crews to be arranged.

| Rubric | |
|---|---|
| Index time | 1 |
| Horizon | 1 |
| Must match the time needed to act, with an example | 1 |
:::
:::

:::question 1(c) [3 points] Define target leakage and give one example.
:::solution Solution & marking
> **Notes wording** — “Target leakage occurs when one or more input features directly or indirectly reveal the outcome that the model is intended to predict.” (§2.6.2)

Example: using "antibiotic administered" to predict sepsis, because treatment follows the diagnosis. The model looks excellent in evaluation and then fails live.

| Rubric | |
|---|---|
| Feature reveals the outcome | 1.5 |
| Valid example | 1 |
| Consequence: inflated evaluation | 0.5 |
:::
:::

:::question 1(d) [3 points] Define construct validity. Why is it described as the most dangerous measurement error?
:::solution Solution & marking
> **Notes wording** — “The most dangerous measurement error occurs before the instrument is even used: the chosen variable simply does not measure the intended concept.” (§2.3.6)

It is dangerous because the data can be precise, complete and consistent and still answer the wrong question. More data or a better model cannot fix it. Example: healthcare **cost** used for healthcare **need** (Obermeyer).

| Rubric | |
|---|---|
| Variable does not measure the intended concept | 1.5 |
| Why dangerous: survives cleaning and modelling | 1 |
| Example | 0.5 |
:::
:::

## Part II — Short Conceptual Questions [16 points]

:::question 2(a) [4 points] “Optimization solves the objective that was specified.” Explain what this means and why it is a limitation, using one example from the notes.
:::solution Solution & marking
> **Notes wording** — “Optimization solves the objective that was specified.” (M1 p.46)

Training minimizes empirical risk $\hat R(\theta)=\tfrac1n\sum_i L(f_\theta(x_i),y_i)$ for whichever target $y$ and loss $L$ were chosen. It cannot tell whether those were right. Example 20: an algorithm that predicts healthcare **cost** as a stand-in for **need** can be perfectly optimized and still under-serve patients who had less access to care, because lower spending is read as lower need.

| Rubric | |
|---|---|
| Optimizer takes the objective as given | 1.5 |
| Objective may be the wrong target or loss | 1 |
| Valid example with mechanism | 1.5 |
:::
:::

:::question 2(b) [4 points] Explain why "the same algorithm" can lead to different outcomes in two organizations. Name the five parts of a socio-technical composite.
:::solution Solution & marking
> **Notes wording** — “a deployed AI system is not merely an isolated algorithm, but an integrated composite of the Model, Data Infrastructure, Interface, Human Workflow, and Institutional Rules.” (M1 p.26)

A deployed system is **Model + Data infrastructure + Interface + Human workflow + Institutional rules**. Example 12: the same ranking algorithm differs with historical hiring data, whether the dashboard shows a ranking, whether its output is final or advisory, and what law or fairness policy applies. Outcomes come from the composite, not from the model alone.

| Rubric | |
|---|---|
| Five components (1 mark for 3–4, 2 for all five) | 2 |
| Explains how a non-model component changes outcomes | 2 |
:::
:::

:::question 2(c) [4 points] Distinguish covariate shift, label shift and concept shift. Give one example of each.
:::solution Solution & marking
> **Notes wording** — “The input variables have changed.” (covariate shift, M2 p.36) “The mapping from X to Y changes.” (concept shift, M2 p.36)

- **Covariate shift:** the input distribution $P(X)$ changes while the relation to the outcome holds. Example: a hospital starts treating older patients.
- **Label shift:** outcome prevalence $P(Y)$ changes. Example: flu rises in winter.
- **Concept shift:** the relation $P(Y\mid X)$ changes. Example: a new treatment changes which patients deteriorate.

| Rubric | per shift |
|---|---|
| Correct definition | 0.75 |
| Example | 0.5 |
| Clear contrast across the three (overall) | 0.25 |
:::
:::

:::question 2(d) [4 points] Why may a duplicate record harm a model? What should be done before deleting it?
:::solution Solution & marking
> **Notes wording** — “Duplicate records occur when multiple entries represent the same observation or entity.” (§2.5.3)

Harms: inflates sample size, distorts frequencies and class rates, gives some records too much influence, and places the same case in training and test, which inflates performance.
Before deleting, **verify** that they are true duplicates by checking transaction or patient IDs, timestamps, source-system logs and record details, then resolve them with a **documented, reproducible rule**. In real Quiz 2, writing "check the duplicates" without saying what to check earned only 0.5.

| Rubric | |
|---|---|
| Two valid harms | 2 |
| Verify before deleting, naming what is checked | 1.5 |
| Documented, reproducible rule | 0.5 |
:::
:::

## Part II — Scenario 1: Bus breakdown prediction [18 points, Module 1 focus]

:::orig Metro bus fleet
A city transit authority runs 900 buses and wants AI to flag buses at risk of breaking down on the road. Data include bus age and model, engine sensor readings, driver fault reports, route, past maintenance logs, the **workshop job-closed timestamp**, and recorded breakdowns. The team builds a model with a random 80/20 split of daily rows and reports **97% accuracy**. Management proposes: *any bus with predicted probability above 0.5 is automatically withdrawn from service that morning.* Facts:
- newer buses have sensors; older buses rely on driver reports;
- the workshop can inspect only **15 buses per day**;
- a withdrawn bus cancels trips on low-income routes where no spare bus exists;
- a roadside breakdown strands passengers and blocks traffic.
:::

:::question 3(a) [5 points; Problem formulation] Rewrite "predict bus breakdowns" using the problem-framing worksheet: unit, index time, horizon, decision-maker, action.
:::solution Solution & marking
> **Notes wording** — “Every machine learning project must begin by explicitly defining the unit of analysis” (M1 p.99)

*"At 05:00 each day (index time), for each bus scheduled for service (unit), using only information available by then, estimate the probability of an in-service breakdown within the next 7 days (horizon), so that the maintenance supervisor (decision-maker) can prioritize the 15 available inspection slots (action). Compare with the current inspection schedule (baseline)."*

| Rubric | 1 mark each |
|---|---|
| Unit · index time · horizon · decision-maker · action | 5 |
:::
:::

:::question 3(b) [4 points; Data risks] Identify two distinct data risks. One must concern the workshop timestamp.
:::solution Solution & marking
> **Notes wording** — “If a model relies on data that has not yet occurred at the index time, it is leaking the future, not demonstrating intelligence.” (M1 p.100)

1. **Temporal/target leakage:** the job-closed timestamp is recorded **after** a fault was repaired, so it reveals the outcome and will not exist at index time. Drop it.
2. **Unequal measurement:** sensors on new buses, driver reports on old buses. Missingness and quality differ by bus age, so the model is less reliable for old buses (representation and differential measurement error).
Also acceptable: driver reporting habits; group leakage (next part is separate, award once).

| Rubric | per risk |
|---|---|
| Named | 1 |
| Explained in the case | 1 |
:::
:::

:::question 3(c) [4 points; Evaluation] Explain why 97% accuracy does not show readiness. Name a defect in the split and two further analyses.
:::solution Solution & marking
> **Notes wording** — “If a model is intended to predict future events, it should be evaluated using temporal validation (trained on past data and evaluated on strictly future data), rather than using randomly shuffled cross-validation that would leak future information into the training process.” (M1 p.64)

Breakdowns are rare, so "no breakdown" may already score about this high, and accuracy hides false negatives. **Split defect:** daily rows of one bus sit in both partitions (**group leakage**) and random splitting ignores time. Use bus-level and temporal validation. Further: **recall/precision or AUPRC**, **calibration**, **subgroup performance** by bus age and route, **baseline** comparison.

| Rubric | |
|---|---|
| Base rate/FP–FN argument | 1 |
| Split defect with fix | 1 |
| Two analyses, 1 each | 2 |
:::
:::

:::question 3(d) [5 points; Decision] Evaluate the 0.5 automatic-withdrawal policy, considering error costs, capacity and fairness. Propose a better policy.
:::solution Solution & marking
> **Notes wording** — “A machine learning prediction is not a decision.” (M1 p.68) “Abstention is a risk-control mechanism that allows a system to defer difficult cases to human review or an alternative process rather than producing potentially unreliable outputs.” (M1 p.79)

- 0.5 is arbitrary; a threshold must reflect **FP vs FN costs**. Here a false alarm cancels trips while a miss strands passengers.
- **Capacity:** a threshold that flags 60 buses cannot be served by 15 inspections.
- **Fairness:** withdrawals fall on routes with no spare bus, and old buses have poorer data, so harm concentrates on low-income riders.
- **Better:** **rank buses and inspect the top 15 each day**, with a supervisor's review before any withdrawal; prefer inspection over withdrawal; **fall back** to scheduled checks when sensor data is missing; **monitor** missed breakdowns, alert yield, calibration and subgroup rates.

| Rubric | |
|---|---|
| Error costs | 1 |
| Capacity → ranking | 1.5 |
| Fairness/route consequence | 1 |
| Human review and fallback or monitoring | 1.5 |
:::
:::

## Part II — Scenario 2: Student dropout early warning [18 points, Module 2 focus]

:::orig University early-warning system
A university wants to predict which first-year students will **drop out**, so advisors can contact them. It merges admissions records, LMS logins, library card swipes, a voluntary wellbeing survey, fee payments, and the field **"withdrawal form submitted"**. Facts:
- 28% of survey responses are missing; students under financial stress respond least;
- students on one campus log in through an older LMS that records only weekly totals;
- student names are matched across systems by fuzzy matching;
- imputation and scaling were fitted on all the data, then rows were split randomly;
- dropout is 8%, and the model scores 92% accuracy.
:::

:::question 4(a) [4 points; Quality] Identify two data-quality problems and name the quality dimension each violates.
:::solution Solution & marking
> **Notes wording** — “Because matching is imperfect, entity resolution may introduce both false merges (combining different entities) and false splits (failing to combine identical entities), particularly when records are incomplete or inconsistent.” (M2 p.60)

- **Weekly LMS totals on one campus** → **consistency** (different granularity across sources) and possibly timeliness.
- **Fuzzy name matching** → **accuracy/consistency**, with false merges and false splits producing wrong histories.
- Also: voluntary survey → **completeness**; a sample of responders → **representativeness**.

| Rubric | per problem |
|---|---|
| Problem from the case | 1 |
| Dimension with reason | 1 |
:::
:::

:::question 4(b) [4 points; Missingness] Is the survey missingness MCAR, MAR or MNAR? Justify. Why is overall mean imputation problematic here?
:::solution Solution & marking
> **Notes wording** — “Under MNAR, the probability of missingness continues to depend on the unobserved values even after accounting for observed information.” (§2.5.1) “These mechanisms describe assumptions about the data-generating process rather than properties that can usually be verified directly from the dataset.” (§2.5.1) “Missingness itself can be informative.” (M2 p.53)

Most plausibly **MNAR**: students under stress, the very quantity the survey measures, respond least. If stress were fully explained by observed fee payments and grades it would be MAR; this cannot be verified from the data, since it is an assumption about the data-generating process.
Mean imputation **shrinks variance**, **distorts relationships**, removes **informative missingness**, and here was fitted on all data, causing **contamination**.

| Rubric | |
|---|---|
| Mechanism with justification | 1.5 |
| Notes that it cannot be verified | 0.5 |
| Two problems with imputation | 2 |
:::
:::

:::question 4(c) [5 points; Leakage] Identify three distinct leakage or contamination problems and give the fix for each.
:::solution Solution & marking
> **Notes wording** — “Group leakage occurs when related observations from the same entity appear in multiple data partitions.” (§2.6.6) “Train-test contamination occurs when information from the evaluation dataset influences model development, parameter estimation, or model selection.” (§2.6.3)

| Problem | Fix |
|---|---|
| **Target/temporal leakage:** "withdrawal form submitted" appears at or after dropout | Define the index time; keep only features available then |
| **Preprocessing contamination:** imputer and scaler fitted on all data | Split first; fit on training data; apply to test |
| **Group leakage:** repeated rows of a student across partitions | Split by student so $G_{\text{train}}\cap G_{\text{test}}=\emptyset$ |

| Rubric | |
|---|---|
| Each problem with fix | 1.5 each |
| Links leakage to optimistic evaluation | 0.5 |
:::
:::

:::question 4(d) [5 points; Governance] Recommend four improvements before deployment. For each, say why it is needed.
:::solution Solution & marking
> **Notes wording** — “Data minimization is the principle that organizations should collect, retain, and process only the information reasonably necessary to achieve a clearly defined and legitimate purpose.” (§2.8.5) “Consent explains what participants agreed to, while licensing defines what users are legally permitted to do with the data.” (M2 p.89)

Any four, 0.5 for the action and 0.5 for the reason, plus 1 for tying them to a specific harm: **split by student**; **remove post-outcome fields**; **fit preprocessing on training data**; **audit subgroups** by campus and financial background; **minimize** data, since library swipes and wellbeing answers may not be necessary; **consent** check, because a voluntary wellbeing survey was not collected for risk scoring (secondary use); **document** with a datasheet and lineage; **human advisors decide**, with no automatic penalty; **monitor** after deployment.
:::
:::

## Part II — Identify Distinct Problems [8 points]

:::question 5 [8 points] A city ranks neighbourhoods for housing-repair grants using complaints made through a mobile app. The app is in English only. Past grants went mainly to wards with active councillors. The dashboard shows the top ten wards in bold, and officers rarely scroll. Each year the model is retrained on which wards received grants. Identify four **distinct** problems (2 points each).
:::solution Solution & marking
1 mark for the name, 1 for the mechanism in the case.
1. **Representation/platform bias:** the app reflects English-speaking smartphone users, not housing need.
2. **Historical bias:** past grants reflect councillor influence, not need.
3. **Interface/automation bias:** bold top-ten placement narrows officers' attention.
4. **Feedback loop:** retraining on grants the system influenced reinforces its first choices.
Also: **construct validity** (complaints ≠ need), **selective labels**. *No double counting* of two symptoms of one mechanism.
:::
:::

## Part II — Calculation [8 points]

:::question 6 [8 points] A screening model gives these test results. Group A: TP 40, FN 10, FP 30, TN 120. Group B: TP 15, FN 15, FP 10, TN 160. (a) Compute overall accuracy and the accuracy of always predicting negative. (b) Compute the selection rate, TPR, FPR and precision for each group. (c) Which fairness criteria fail? Why might fixing all of them at once be impossible?
:::solution Solution & marking
> **Notes wording** — “These fairness criteria may be mutually incompatible, particularly when outcome prevalence differs between populations.” (M2 p.98)

**(a)** Accuracy $=\frac{40+120+15+160}{400}=\frac{335}{400}=0.8375$. Positives $=50+30=80$, so all-negative gives $\frac{320}{400}=0.80$. The gain over the trivial model is small.

**(b)**

| | Selection rate | TPR | FPR | Precision |
|---|---|---|---|---|
| A | $70/200=0.35$ | $40/50=0.80$ | $30/150=0.20$ | $40/70=0.571$ |
| B | $25/200=0.125$ | $15/30=0.50$ | $10/170=0.059$ | $15/25=0.60$ |

**(c)** **Demographic parity** fails (0.35 vs 0.125). **Equal opportunity** fails (0.80 vs 0.50). **Equalized odds** fails (TPR and FPR differ). **Predictive parity** nearly holds (0.57 vs 0.60). Base rates differ (0.25 vs 0.15), and when they differ these criteria generally cannot all hold at once, so the choice is a value decision tied to which harm matters most.

| Rubric | |
|---|---|
| (a) both values | 1.5 |
| (b) table | 4 |
| (c) criteria and incompatibility | 2.5 |
:::
:::
