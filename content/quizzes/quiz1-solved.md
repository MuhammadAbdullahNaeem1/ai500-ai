# Real Quiz 1 (solved) — 3 October 2026

**50 points · 60 minutes · Module 1.** The instructor's solution scheme, condensed, with what each question tested. Quiz 2 "will follow the style of Quiz #1", so this is the template for everything on the [Quiz 2 guide](quiz2-guide.html).

<div class="pdf-links">
<a href="pdfs/quizzes/Quiz-1-Solution.pdf">Quiz 1 solution scheme (PDF)</a>
<a href="m1a-notes.html">Module 1 notes</a>
<a href="quiz2-guide.html">Quiz 2 guide</a>
</div>

| Q | Marks | Topic | Module |
|---|---|---|---|
| 1(a) | 3 | Define AI (science **and** engineering, not just ML) | M1 §1.3 |
| 1(b) | 3 | Define temporal leakage; why it makes strong results unreliable | M1 §1.9.3 / **M2 §2.6.5** |
| 1(c) | 3 | Define calibration; distinguish from discrimination | M1 §1.5.5 |
| 2(a) | 4 | AI ≠ ML; a non-learning AI example | M1 §1.4.1 |
| 2(b) | 4 | 0.62 readmission risk is a prediction, not a decision; 3 considerations | M1 §1.5.6 |
| 2(c) | 4 | Why the more accurate model isn't automatically deployed; 3 criteria | M1 §1.5.4 |
| 3(a–e) | 21 | Water-pipe failure: formulation, data risks, evaluation, threshold vs capacity, fallback & monitoring | M1 §1.5–1.9 |
| 4 | 8 | Hiring ranker: four distinct biases / feedback mechanisms | M1 §1.1, §1.2 / **M2 §2.8.7** |

## Basic Definitions

:::question 1(a) [3 points] Define artificial intelligence. Your definition should capture both the scientific and engineering character of AI rather than equating AI only with machine learning.
:::solution Official answer
AI is the **scientific and engineering discipline** concerned with developing computational systems that can **receive or perceive information, construct useful representations, reason or learn from evidence, and generate actions or outputs in pursuit of specified objectives under uncertainty and constraints.**
*Rubric:* discipline (science + engineering) 1 · capabilities (representation, reasoning, learning, perception, action) 1 · objectives + uncertainty/constraints, not reduced to ML 1.
:::
:::

:::question 1(b) [3 points] Define temporal leakage in an AI or machine-learning system. Why does the presence of temporal leakage make an apparently strong evaluation result unreliable?
:::solution Official answer
Temporal leakage occurs when a model uses **information that would not have been available at the time the prediction is supposed to be made**, usually because the feature was measured or recorded later. The model effectively gains information **from the future**, so test performance appears **artificially high** though that information won't exist during real-world prediction.
*Rubric:* post-index/future information 1.5 · unavailable at prediction time 0.5 · inflated evaluation / fails to reflect deployment 1.
:::
:::

:::question 1(c) [3 points] Define probabilistic calibration. In one additional sentence, distinguish calibration from discrimination.
:::solution Official answer
A model is **well calibrated** when predictions assigned probability $p$ occur approximately a proportion $p$ of the time (of cases given 0.8, about 80% have the outcome). **Discrimination** is how well the model **ranks/separates** cases with and without the outcome.
*Rubric:* definition 1.5 · predicted probability ↔ observed frequency 0.5 · distinction 1.
:::
:::

## Short Conceptual Questions

:::question 2(a) [4 points] Explain why artificial intelligence is not synonymous with machine learning. Give one example of an AI system or technique that does not need to learn from data and explain briefly why it can still legitimately be regarded as part of AI.
:::solution Official answer
ML is **one approach within** AI. AI also includes search, symbolic reasoning, planning, constraint satisfaction, optimization, expert systems and rule-based control. Example: a **shortest-path search** explores a state space to choose a route without learning from data — still AI because it performs **goal-directed computational reasoning**.
*Rubric:* ML ⊂ AI 1.5 · valid non-learning example 1 · why it is AI 1 · clear distinction (automation alone ≠ AI) 0.5.
:::
:::

:::question 2(b) [4 points] A model estimates that a patient has a probability of 0.62 of being readmitted to hospital within 30 days. Explain why this number is a prediction rather than a decision. Identify three considerations that should influence whether an intervention is actually triggered.
:::solution Official answer
0.62 is an **estimated risk**; it specifies no action. A decision needs a **rule/threshold/policy** linking prediction to action. Considerations (any three): relative costs of **FP vs FN**; **capacity** to intervene; expected **benefit** of intervention; **calibration**/reliability; uncertainty; **fairness** and subgroup consequences; availability of **human review**; costs and workflow; alternative interventions/thresholds.
:::
:::

:::question 2(c) [4 points] Two models solve the same prediction task. Model A has slightly higher test-set accuracy, whereas Model B is simpler, faster, easier to interpret, and considerably cheaper to maintain. Explain why Model A should not automatically be selected for deployment. Discuss any three criteria other than raw predictive accuracy that should influence the choice.
:::solution Official answer
Higher test accuracy ≠ greater real-world utility. Criteria: **interpretability**, **latency**, **compute requirements**, **maintenance burden**, **robustness** to missing/shifted data, **calibration**, **governance/auditability**, data requirements, team expertise, **lifecycle cost**.
:::
:::

## Scenario — AI-assisted water-pipe failure management (21 points)

:::orig AI-Assisted Water-Pipe Failure Management — Quiz 1, Question 3 [21 points]
A city water utility maintains 40,000 underground water pipes. It wants to use AI to identify pipes at risk of failure so that inspection teams can intervene before a major leak occurs. The available historical data include:

- pipe age and material;
- pipe diameter;
- recent water-pressure sensor readings;
- rainfall measurements;
- previous maintenance records;
- customer complaints about low pressure;
- date and time at which an emergency repair was completed;
- neighborhood;
- recorded pipe failures.

The data science team trains a machine-learning model using a random 80/20 train-test split and reports 95% overall accuracy. Management proposes the following policy: *For every pipe whose predicted probability of failure exceeds 0.5, automatically shut the corresponding valve and dispatch an inspection team.* However,

- some pressure sensors report intermittently;
- sensor coverage is much poorer in older neighborhoods;
- the emergency-repair-completed field is generally recorded only after a pipe has already failed;
- the city has capacity to inspect only 20 pipes per day;
- unnecessarily shutting a pipe interrupts water supply to homes and businesses;
- failing to identify an actual imminent failure can cause flooding, infrastructure damage, and substantial repair costs.
:::

:::question 3(a) [5 points; Problem Formulation] The statement *build an AI model to predict pipe failure* is inadequately formulated. Specify: an appropriate unit of analysis; an index time; a reasonable prediction horizon; the decision-maker; and the action that the prediction is intended to support.
:::solution Official answer
**Unit:** one pipe at an index time. **Index time:** start of each day, before inspection assignment. **Horizon:** failure within next 24 h / 48 h / 7 days (justified operationally). **Decision-maker:** maintenance/operations manager or dispatch team. **Action:** prioritize pipes for inspection, preventive maintenance, monitoring, or (very high risk) controlled shutdown. *"At the beginning of each day, estimate for every operating pipe the probability of failure in the next seven days using only information available then, so the team can prioritize its limited daily capacity."* 1 mark each.
:::
:::

:::question 3(b) [4 points; Data and representation risks] Identify and explain two distinct risks in the available data. At least one of your answers must consider the emergency-repair-completed variable. Identify two additional aspects of evaluation that should be investigated before deployment.
:::solution Official answer
**Temporal leakage:** repair-completed is recorded **after** failure → future information → unrealistically high performance (2). Plus one of: **intermittent sensors/missingness** (possibly related to condition); **unequal sensor coverage / representation bias** in older neighbourhoods; **neighbourhood as proxy**; **selection/measurement bias**; **random split** doesn't test future deployment (2).
:::
:::

:::question 3(c) [4 points; Evaluation] Explain why the statement *the model achieved 95% accuracy, therefore it is ready for deployment* is inadequate. Identify two additional aspects of evaluation that should be investigated before deployment.
:::solution Official answer
Accuracy ignores FP vs FN, misleads under **class imbalance** (failures rare), says nothing about **calibration**, hides **neighbourhood subgroup** differences, robustness to missing sensors, operational usefulness, and came from a random split. Add: **recall/FNR**, **calibration**, **subgroup performance**, **robustness**, **temporal validation**, **decision utility/cost**, **baseline** comparison.
:::
:::

:::question 3(d) [4 points; From prediction to action] Why is the proposed threshold of 0.5 not automatically appropriate? Explain how both: the different consequences of false positives versus false negatives, and the capacity limit of 20 inspections per day, should affect the decision policy.
:::solution Official answer
0.5 is just a number. **Asymmetric costs:** missed failures (flooding) may justify a lower threshold, but false positives interrupt water supply. **Capacity:** 20 inspections/day — a threshold yielding 200 alerts is useless. Best: **rank pipes by risk and select the top cases within capacity**, with triage and human review before any shutdown.
:::
:::

:::question 3(e) [4 points; Deployment and monitoring] State: one condition under which the system should abstain or fall back to another procedure, and one quantity or behavior that should be continuously monitored after deployment.
:::solution Official answer
**Abstain** if critical sensor values are missing/invalid, inputs violate schema/ranges or are out of distribution, confidence inadequate, pipeline failure, or the pipe is from an unvalidated population → fall back to **manual engineering review / legacy rules / intensified monitoring**. **Monitor:** missing-sensor rate, input drift, calibration, sensitivity/FNR, FPR, missed failures, subgroup performance, alert volume, inspection yield, latency, override rate, real failures after deployment — and say why it matters.
:::
:::

## Identifying Biases in an AI System (8 points)

:::question 4 [8 points] A company uses an AI system to rank job applicants. The model is trained on ten years of historical hiring data. Applicants from a small set of universities were hired more frequently in the past, and the model consequently assigns them higher scores. The recruitment dashboard prominently highlights the top-ranked applicants, and recruiters rarely inspect candidates ranked lower down. After one year, the model is retrained using the hiring decisions made with assistance from the system. Identify and briefly explain four distinct sources or forms of bias/problematic feedback present in this scenario.
:::solution Official answer
**Historical bias** (past preferences encoded) · **Proxy bias** (university as proxy for socioeconomic opportunity — only if mechanism explained) · **Automation/interface bias** (highlighting changes recruiter behaviour) · **Self-reinforcing feedback loop** (retraining on decisions the model influenced). Also: selective exposure, **selective labels** (outcomes observed only for hired candidates), sampling/representation bias, measurement bias. **Avoid double counting** — "recruiters look at the top" and "lower candidates are rarely reviewed" are one mechanism.
:::
:::
