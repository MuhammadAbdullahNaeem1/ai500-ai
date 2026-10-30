# Mid guide — Modules 1 and 2

**Examined: Module 1 and Module 2. Module 3 is not examined on the mid.** The syllabus states closed books, closed notes, in person, and 25% of the grade.

<div class="pdf-links">
<a href="mid-mock-a.html">★ Mock Mid A</a>
<a href="mid-mock-b.html">Mock Mid B</a>
<a href="mid-mock-c.html">Mock Mid C</a>
<a href="quiz2-solved.html">Real Quiz 2 (solved)</a>
<a href="quiz1-solved.html">Real Quiz 1 (solved)</a>
<a href="m2-definitions.html">Notes-exact definitions</a>
</div>

:::warn The real format is not confirmed
No 2026 mid paper or format announcement is in the course folder. The mocks borrow their layout from the **Fall 2025 mid** (Part I: 14 MCQs in 30 minutes; Part II: 50 points in 2 hours) and their question style and rubrics from this year's **Quiz 1 and Quiz 2**. Last year's syllabus was different, so use it for layout only. Follow any instruction from class over this page.
:::

## 1. What the real papers show

| Paper | Marks | Time | Structure |
|---|---|---|---|
| Fall 2025 mid | 15 + 50 | 30 min + 2 h | MCQs, then worked problems |
| 2026 Quiz 1 | 50 | 60 min | Definitions 9, conceptual 12, scenario 21, four biases 8 |
| 2026 Quiz 2 | 20 | 30 min | One case, parts (a)–(e) |

## 2. Rubric lessons

- **Name it, then tie it to the case.** Quiz 1 and 2 both award one part for the name and one for the explanation.
- **"Without explanation" earns half.** In Quiz 2, a metric with no explanation earned 0.5 of 1, and "check the duplicates" with no detail earned 0.5.
- **Say what is wrong and how to fix it.** Quiz 2 Q(c) required a correction for each leak.
- **Do not double count.** Choose mechanisms from different stages: data, label, evaluation, deployment, feedback.
- **Connect leakage to its effect:** unrealistically optimistic evaluation. Quiz 2 gave 0.5 for this sentence.
- **Accuracy trap:** state that always predicting the majority class already achieves the same score and detects nothing.

## 3. Ten things to get right

1. Problem-framing sentence: unit, index time, horizon, decision-maker, action, baseline.
2. Calibration vs discrimination.
3. A prediction is not a decision: costs, capacity, fairness, human review.
4. Claims and validations: future → temporal; elsewhere → external; everyone → subgroup; probabilities → calibration; decisions → workflow trial.
5. Leakage types with fixes: target, temporal, group, site, preprocessing contamination.
6. MCAR, MAR, MNAR, and why the mechanism cannot usually be verified from the data.
7. $Q(D,T,C)$ and the six quality dimensions.
8. Proxies and why sensitive attributes are kept for auditing.
9. Fairness metrics and why they conflict when base rates differ.
10. Case studies: Google Flu Trends, Epic Sepsis, TFX, Gender Shades, Obermeyer, Northcutt.

## 4. Revision order for tonight

1. [Real Quiz 2](quiz2-solved.html) and [real Quiz 1](quiz1-solved.html): read the rubrics.
2. [Mock Mid A](mid-mock-a.html), timed. Mark it strictly.
3. Revise the weak topics in [M1 Part B](m1b-notes.html), [M2 Part B](m2b-notes.html) and [definitions](m2-definitions.html).
4. Use Mocks B and C for scenarios and MCQs if time allows, then sleep.

## 5. Formulas for the calculation section

Quiz 2 was announced as having no numerical problems, and the mid may be the same. Assignment 2 did include calculations, so they are worth 15 minutes.

| Item | Formula |
|---|---|
| Accuracy | $(TP+TN)/N$ |
| Precision | $TP/(TP+FP)$ |
| Recall / TPR | $TP/(TP+FN)$ |
| FPR | $FP/(FP+TN)$ |
| Selection rate | $(TP+FP)/N$ |
| Cohen's $\kappa$ | $(p_o-p_e)/(1-p_e)$ |
| IQR fences | $[Q_1-1.5\,\text{IQR},\ Q_3+1.5\,\text{IQR}]$ |
| z-score | $(x-\bar x)/s$ |
| Platt scaling | $P=1/(1+\exp(As+B))$ |
| Threshold cost | $c_{FP}\cdot FP+c_{FN}\cdot FN$ |
| Alert volume | $\#\text{encounters}\times P(\hat p\ge t)$ |

The notes print the upper IQR fence with a minus sign in §2.5.2. The plus sign above is correct, as footnote 213 confirms.

## 6. Exact lines from the notes

Write these as they are, then add the mechanism and an example. The Module 2 list is on [Notes-exact definitions](m2-definitions.html).

| Topic | Notes wording | Source |
|---|---|---|
| Prediction vs decision | A machine learning prediction is not a decision. | M1 p.68 |
| Optimization | Optimization solves the objective that was specified. | M1 p.46 |
| Index time | Index time: (or prediction origin) is the exact, specific moment in the real world at which the model is required to make its prediction. | M1 p.100 |
| Feature availability | every single input feature must be strictly available at or before this index time. | M1 p.100 |
| Horizon | The prediction horizon defines the exact temporal window into the future within which the target outcome must occur. | M1 p.100 |
| Unit of analysis | the fundamental, independent entity the model is evaluating, predicting for, or learning from. | M1 p.99 |
| Rational agent | A rational agent selects actions expected to advance its objectives, given its information and constraints. | M1 p.35 |
| Model choice | the most complex model is not automatically the best model. | M1 p.59 |
| Deployment | Ultimately, a highly accurate model sitting in a Jupyter notebook is not a deployed AI system. | M1 p.75 |
| Abstention | Abstention is a risk-control mechanism that allows a system to defer difficult cases to human review or an alternative process rather than producing potentially unreliable outputs. | M1 p.79 |
| Temporal validation | If a model is intended to predict future events, it should be evaluated using temporal validation (trained on past data and evaluated on strictly future data), rather than using randomly shuffled cross-validation that would leak future information into the training process. | M1 p.64 |
| Missingness | Not all missing values indicate poor data quality; in many situations, they are expected and informative. | M2 p.50 |
| Outliers | Consequently, outliers should be investigated rather than automatically removed. | M2 p.55 |
| Resampling | Resampling should therefore be performed only within the training partition or within each training fold during cross-validation | §2.5.4 |
| Consent vs licence | Consent explains what participants agreed to, while licensing defines what users are legally permitted to do with the data. | M2 p.89 |
| Fairness conflict | These fairness criteria may be mutually incompatible, particularly when outcome prevalence differs between populations. | M2 p.98 |
