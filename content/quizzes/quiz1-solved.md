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

:::question 1(a) [3] Define artificial intelligence (scientific and engineering character, not just ML).
:::solution Official answer
AI is the **scientific and engineering discipline** concerned with developing computational systems that can **receive or perceive information, construct useful representations, reason or learn from evidence, and generate actions or outputs in pursuit of specified objectives under uncertainty and constraints.**
*Rubric:* discipline (science + engineering) 1 · capabilities (representation, reasoning, learning, perception, action) 1 · objectives + uncertainty/constraints, not reduced to ML 1.
:::
:::

:::question 1(b) [3] Define temporal leakage. Why does it make an apparently strong evaluation unreliable?
:::solution Official answer
Temporal leakage occurs when a model uses **information that would not have been available at the time the prediction is supposed to be made**, usually because the feature was measured or recorded later. The model effectively gains information **from the future**, so test performance appears **artificially high** though that information won't exist during real-world prediction.
*Rubric:* post-index/future information 1.5 · unavailable at prediction time 0.5 · inflated evaluation / fails to reflect deployment 1.
:::
:::

:::question 1(c) [3] Define probabilistic calibration; distinguish from discrimination.
:::solution Official answer
A model is **well calibrated** when predictions assigned probability $p$ occur approximately a proportion $p$ of the time (of cases given 0.8, about 80% have the outcome). **Discrimination** is how well the model **ranks/separates** cases with and without the outcome.
*Rubric:* definition 1.5 · predicted probability ↔ observed frequency 0.5 · distinction 1.
:::
:::

## Short Conceptual Questions

:::question 2(a) [4] Why is AI not synonymous with ML? Give a non-learning AI example.
:::solution Official answer
ML is **one approach within** AI. AI also includes search, symbolic reasoning, planning, constraint satisfaction, optimization, expert systems and rule-based control. Example: a **shortest-path search** explores a state space to choose a route without learning from data — still AI because it performs **goal-directed computational reasoning**.
*Rubric:* ML ⊂ AI 1.5 · valid non-learning example 1 · why it is AI 1 · clear distinction (automation alone ≠ AI) 0.5.
:::
:::

:::question 2(b) [4] Why is a 0.62 readmission probability a prediction, not a decision? Three considerations for triggering an intervention.
:::solution Official answer
0.62 is an **estimated risk**; it specifies no action. A decision needs a **rule/threshold/policy** linking prediction to action. Considerations (any three): relative costs of **FP vs FN**; **capacity** to intervene; expected **benefit** of intervention; **calibration**/reliability; uncertainty; **fairness** and subgroup consequences; availability of **human review**; costs and workflow; alternative interventions/thresholds.
:::
:::

:::question 2(c) [4] Model A slightly more accurate; Model B simpler, faster, interpretable, cheaper. Why not automatically pick A? Three criteria.
:::solution Official answer
Higher test accuracy ≠ greater real-world utility. Criteria: **interpretability**, **latency**, **compute requirements**, **maintenance burden**, **robustness** to missing/shifted data, **calibration**, **governance/auditability**, data requirements, team expertise, **lifecycle cost**.
:::
:::

## Scenario — AI-assisted water-pipe failure management (21 points)

:::orig Case
40,000 pipes; data: age, material, diameter, pressure-sensor readings, rainfall, maintenance records, complaints, **date/time emergency repair completed**, neighbourhood, recorded failures. Random 80/20 split, **95% accuracy**. Policy: probability > 0.5 → **automatically shut valve and dispatch**. Sensors intermittent; coverage poorer in **older neighbourhoods**; repair-completed recorded **after failure**; capacity **20 inspections/day**; shut-offs disrupt supply; missed failures cause flooding and damage.
:::

:::question 3(a) [5] Formulate: unit of analysis, index time, horizon, decision-maker, action.
:::solution Official answer
**Unit:** one pipe at an index time. **Index time:** start of each day, before inspection assignment. **Horizon:** failure within next 24 h / 48 h / 7 days (justified operationally). **Decision-maker:** maintenance/operations manager or dispatch team. **Action:** prioritize pipes for inspection, preventive maintenance, monitoring, or (very high risk) controlled shutdown. *"At the beginning of each day, estimate for every operating pipe the probability of failure in the next seven days using only information available then, so the team can prioritize its limited daily capacity."* 1 mark each.
:::
:::

:::question 3(b) [4] Two data risks (one must use emergency-repair-completed).
:::solution Official answer
**Temporal leakage:** repair-completed is recorded **after** failure → future information → unrealistically high performance (2). Plus one of: **intermittent sensors/missingness** (possibly related to condition); **unequal sensor coverage / representation bias** in older neighbourhoods; **neighbourhood as proxy**; **selection/measurement bias**; **random split** doesn't test future deployment (2).
:::
:::

:::question 3(c) [4] Why is "95% accuracy, ready to deploy" inadequate? Two more evaluations.
:::solution Official answer
Accuracy ignores FP vs FN, misleads under **class imbalance** (failures rare), says nothing about **calibration**, hides **neighbourhood subgroup** differences, robustness to missing sensors, operational usefulness, and came from a random split. Add: **recall/FNR**, **calibration**, **subgroup performance**, **robustness**, **temporal validation**, **decision utility/cost**, **baseline** comparison.
:::
:::

:::question 3(d) [4] Why is 0.5 not automatically appropriate? Use FP/FN costs and the 20/day capacity.
:::solution Official answer
0.5 is just a number. **Asymmetric costs:** missed failures (flooding) may justify a lower threshold, but false positives interrupt water supply. **Capacity:** 20 inspections/day — a threshold yielding 200 alerts is useless. Best: **rank pipes by risk and select the top cases within capacity**, with triage and human review before any shutdown.
:::
:::

:::question 3(e) [4] One abstention/fallback condition; one quantity to monitor.
:::solution Official answer
**Abstain** if critical sensor values are missing/invalid, inputs violate schema/ranges or are out of distribution, confidence inadequate, pipeline failure, or the pipe is from an unvalidated population → fall back to **manual engineering review / legacy rules / intensified monitoring**. **Monitor:** missing-sensor rate, input drift, calibration, sensitivity/FNR, FPR, missed failures, subgroup performance, alert volume, inspection yield, latency, override rate, real failures after deployment — and say why it matters.
:::
:::

## Identifying biases (8 points)

:::question 4 [8] Hiring ranker trained on ten years of decisions; favoured universities score higher; dashboard highlights top candidates; recruiters rarely look lower; retrained on system-assisted decisions. Four distinct mechanisms.
:::solution Official answer
**Historical bias** (past preferences encoded) · **Proxy bias** (university as proxy for socioeconomic opportunity — only if mechanism explained) · **Automation/interface bias** (highlighting changes recruiter behaviour) · **Self-reinforcing feedback loop** (retraining on decisions the model influenced). Also: selective exposure, **selective labels** (outcomes observed only for hired candidates), sampling/representation bias, measurement bias. **Avoid double counting** — "recruiters look at the top" and "lower candidates are rarely reviewed" are one mechanism.
:::
:::
