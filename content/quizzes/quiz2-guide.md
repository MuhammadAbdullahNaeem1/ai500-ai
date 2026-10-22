# Quiz 2 guide — Module 2

**Quiz 2: Saturday 24 October 2026, in class.** Module 2: *Data Collection, Curation, Cleaning, Governance, and Ethics*. Syllabus: everything up to the class of **17 October**. **No programming, no numerical problems** — case study, assessment, descriptive analysis, fundamental concepts and practice. **Same style as Quiz 1.** Practice questions: notes pages **130–145**.

<div class="pdf-links">
<a href="quiz2-mock-a.html">Mock Quiz 2A</a>
<a href="quiz2-mock-b.html">Mock Quiz 2B</a>
<a href="quiz2-mock-c.html">Mock Quiz 2C</a>
<a href="quiz1-solved.html">Real Quiz 1 (solved)</a>
<a href="pdfs/quizzes/Quiz-1-Solution.pdf">Quiz 1 solution PDF</a>
</div>

## 1. What "the style of Quiz 1" means

Quiz 1 (3 October 2026): **50 points, 60 minutes**, four sections, all marked with a rubric that gives a point for **naming** a concept and a point for **explaining it in context**.

| Section | Quiz 1 | Marks | What to expect in Quiz 2 |
|---|---|---|---|
| **Basic definitions** [CLO 1] — "compact response" | (a) Define AI (3) · (b) Define temporal leakage + why results unreliable (3) · (c) Define calibration + distinguish from discrimination (3) | **9** | 3 definitions, each with a twist ("…and explain why…", "…distinguish from…") |
| **Short conceptual** | (a) AI ≠ ML + non-learning example (4) · (b) 0.62 is a prediction not a decision + 3 considerations (4) · (c) Why not pick the more accurate model + 3 criteria (4) | **12** | 3 × 4-mark "explain why / give three…" |
| **Scenario** | Water-pipe failure: formulation (5), data risks incl. leakage (4), why 95% accuracy is inadequate (4), threshold 0.5 vs costs & capacity (4), abstain/monitor (4) | **21** | One Module 2 case like S1–S5 with 5 parts |
| **Identify biases** | Hiring ranker: 4 distinct bias/feedback mechanisms, 2 pts each | **8** | Name & explain 4 **distinct** problems (biases, leakage types, quality failures, governance failures) |

:::warn Rubric lessons from Quiz 1
- "Do not reduce AI to ML" — **don't reduce an answer to one word**. Name it *and* tie it to the case.
- **Avoid double counting**: two symptoms of one mechanism earn marks once. In a "four distinct biases" question, choose mechanisms from **different stages** (data → label → evaluation → deployment → feedback).
- Temporal leakage was worth **1.5/3** just for "uses post-index/future information" — learn the exact phrasing: *information not available at the time the prediction is made*.
- Beyond accuracy, the same evaluation checklist kept scoring: **class imbalance, FP vs FN, calibration, subgroup performance, robustness, temporal validation, baseline, decision utility**.
:::

## 2. Coverage checklist — Module 2

Tick when you can explain it **without notes**, with one example from the notes.

| Topic | Notes | Must be able to… |
|---|---|---|
| Data are produced, not found | [2.1](m2a-notes.html#1-data-are-produced-not-simply-found-2-1-1) | Give the 5 components (Figure 14); explain "raw data is an oxymoron" |
| $Q(D,T,C)$ fitness for purpose | [2.1.2](m2a-notes.html#2-fitness-for-purpose-2-1-2) | Define D, T, C for a case and judge; the 4 tasks of Example 38 |
| 8 data sources | [2.2](m2a-notes.html#3-data-sources-and-their-inherent-realities-2-2) | One characteristic error per source; six survey errors; four log timestamps; platform as instrument; admin = institutional behaviour |
| Synthetic-data validation | [2.2.8](m2a-notes.html#3-8-synthetic-data) | Fidelity, utility, privacy, fairness, coverage, realism |
| 6 quality dimensions | [2.3](m2a-notes.html#4-the-six-dimensions-of-data-quality-2-3) | Define each; completeness types; consistency types; timeliness concepts; 3 shifts; random/systematic/differential error; construct validity |
| Curation workflow | [2.4](m2b-notes.html#2-the-eight-stage-curation-workflow-2-4-2-figure-15) | 8 stages; curation vs cleaning; audit-trail fields |
| Missing data | [2.5.1](m2b-notes.html#3-missing-values-2-5-1) | MCAR/MAR/MNAR with examples; informative missingness (lactate); costs of mean imputation |
| Outliers, duplicates, labels, units | [2.5.2–2.5.3](m2b-notes.html#4-outliers-2-5-2) | Investigate not delete; exact/near duplicates; false merge/split; κ concept; acceptable alternative labels; unit schemas |
| Imbalance & calibration | [2.5.4](m2b-notes.html#6-class-imbalance-2-5-4) | Accuracy paradox; split before resampling; recalibration; Platt vs isotonic; SMOTE vs SMOTENC |
| Leakage | [2.6](m2b-notes.html#7-data-leakage-2-6) | Target, train–test, temporal, group, site; CV variants; prevention checklist |
| Documentation | [2.7](m2c-notes.html#1-data-documentation-2-7) | Datasheet areas; data dictionary elements; provenance vs lineage; consent ≠ licence; copyright ≠ privacy; licence compatibility |
| Governance & ethics | [2.8](m2c-notes.html#2-governance-and-ethics-2-8) | Privacy risks; de-identification limits; minimization rule; proxies; sensitive attributes for auditing; 7 biases; 4 fairness metrics & incompatibility; secondary use; roles |
| Good data, misleading AI | [2.9–2.10](m2c-notes.html#3-how-a-quot-good-quot-dataset-produces-a-misleading-ai-system-2-9) | Construct → process → proxy → target; suitability audit (6 lenses); 6 acceptance gates |
| Case studies | [2.11](m2c-notes.html#5-three-case-studies-2-11) | Gender Shades, cost proxy (Obermeyer), label errors (Northcutt) — diagnosis, redesign, lesson |

## 3. Most likely questions (ranked)

1. **Define and distinguish** — MCAR/MAR/MNAR; provenance vs lineage; consent vs licence; random vs systematic error; covariate/label/concept shift; curation vs cleaning; datasheet vs data dictionary; demographic parity vs equal opportunity.
2. **Leakage hunting in a case** — S3, S4, R3 shapes: name each leak (target, contamination, temporal, group, site), explain, fix.
3. **$Q(D,T,C)$ on a case** — S1/R1 shape.
4. **Proxy / construct validity** — cost for need, arrests for crime, clicks for satisfaction; "why can't a better model fix it?"
5. **Four distinct biases** — historical, representation, measurement, aggregation, evaluation, deployment, feedback (+ proxy, selective labels).
6. **Governance case** — S5/R5 shape: consent, licence, de-identification, model weights, roles.
7. **Why not just remove the sensitive attribute?** — proxies + need for fairness auditing.
8. **Synthetic data claims** — challenge "synthetic = anonymous/fair".

## 4. One-line answers — in the notes' exact words

Sir prioritizes the wording of the notes. Write these sentences **as they are**, then add the mechanism and an example. The full list of 108 is on [Notes-exact definitions](m2-definitions.html).

| Term | Notes wording (exact) | § |
|---|---|---|
| Raw data | The phrase raw data is a dangerous oxymoron. | 2.1 |
| Fitness for purpose | There is no such thing as a universally good or high-quality dataset in a vacuum. A dataset is only good for a specific purpose under specific conditions. | 2.1.2 |
| Coverage error | The sampling frame misses parts of the target population. | 2.2.1 |
| Nonresponse bias | Respondents differ systematically from those who refuse to participate. | 2.2.1 |
| Platform as measurement | Observed web behavior is not a direct measure of stable human preference. It is a reaction within an engineered environment, defined by a combination of user, interface, ranking algorithm, moderation, and platform incentives. | 2.2.3 |
| Event time | When the real-world action actually occurred. | 2.2.4 |
| Recording time | When the local system logged it. | 2.2.4 |
| Arrival time | When it reached the central data pipeline. | 2.2.4 |
| Processing time | When the pipeline actually handled it. | 2.2.4 |
| Administrative data | Administrative data encodes institutional behavior not objective reality. | 2.2.5 |
| Completeness | Completeness measures whether all required data is actually present. | 2.3.1 |
| Accuracy | Accuracy measures how closely recorded values correspond to the true or accepted reference values. | 2.3.2 |
| Consistency | Consistency asks whether data values agree logically across formats, records, systems, and established rules. | 2.3.3 |
| Timeliness | Timeliness concerns whether data is sufficiently current and available exactly when it is needed for a decision. | 2.3.4 |
| Representativeness | Representativeness asks whether the data adequately reflects the intended target population and the actual operating conditions of deployment. | 2.3.5 |
| Measurement error | Measurement error is the fundamental difference between an observed value and the true underlying construct or quantity it is intended to measure. | 2.3.6 |
| Construct validity | The most dangerous measurement error occurs before the instrument is even used: the chosen variable simply does not measure the intended concept. | 2.3.6 |
| Data curation | Data curation is the systematic process of acquiring, organizing, validating, documenting, preserving, and maintaining data to ensure that they remain accurate, accessible, and suitable for their intended purposes throughout their lifecycle. | 2.4 |
| MCAR | Under MCAR, the probability of missingness is unrelated to either observed or unobserved data. | 2.5.1 |
| MAR | Here, missingness may depend on observed variables but not on the missing values themselves after conditioning on the observed data. | 2.5.1 |
| MNAR | Under MNAR, the probability of missingness continues to depend on the unobserved values even after accounting for observed information. | 2.5.1 |
| Outlier | An outlier is an observation that differs substantially from the expected pattern of the data. | 2.5.2 |
| Duplicate records | Duplicate records occur when multiple entries represent the same observation or entity. | 2.5.3 |
| Class imbalance | Class imbalance occurs when one or more classes are substantially less frequent than others. | 2.5.4 |
| Data leakage | Data leakage occurs when information that would not legitimately be available at the intended prediction or evaluation time is inadvertently used during model development. | 2.6.1 |
| Target leakage | Target leakage occurs when one or more input features directly or indirectly reveal the outcome that the model is intended to predict. | 2.6.2 |
| Train–test contamination | Train-test contamination occurs when information from the evaluation dataset influences model development, parameter estimation, or model selection. | 2.6.3 |
| Temporal leakage | Temporal leakage occurs when information from the future is used to predict an earlier outcome. | 2.6.5 |
| Group leakage | Group leakage occurs when related observations from the same entity appear in multiple data partitions. | 2.6.6 |
| Data provenance | Data provenance describes the origin of data and the processes used to generate them. | 2.7.3 |
| Data lineage | Data lineage records how data evolve as they move through processing pipelines. | 2.7.3 |
| Data governance | Data governance is the framework of policies, roles, processes, and technical controls through which data are managed, protected, and used throughout their lifecycle. | 2.8.1 |
| Privacy | Privacy concerns an individual's ability to control, understand, and be protected from inappropriate collection, processing, inference, sharing, or disclosure of information about them. | 2.8.2 |
| De-identification | de-identification should be viewed as a risk-reduction strategy rather than a guarantee of anonymity. | 2.8.3 |
| Data minimization | Data minimization is the principle that organizations should collect, retain, and process only the information reasonably necessary to achieve a clearly defined and legitimate purpose. | 2.8.5 |
| Sensitive attributes | Sensitive attributes are variables whose misuse may expose individuals to discrimination, privacy violations, or other forms of harm. | 2.8.6 |
| Demographic parity | Predicted positive rates are equal across groups. | 2.8.8 |
| Equal opportunity | True positive rates are equal across groups. | 2.8.8 |
| Equalized odds | Equalized odds require equality of both true positive rates and false positive rates across demographic groups. | 2.8.8 |
| Predictive parity | The probability that a positive prediction is correct is equal across groups. | 2.8.8 |

## 5. Exam strategy (60 minutes, 50 points)

- **≈1 minute per point.** Definitions 9 min, conceptual 12 min, scenario 21 min, biases 8 min, 10 min buffer.
- For "identify $n$": number them, **bold the term**, one sentence of mechanism tied to the case.
- In scenarios, always add the **fix** — rubrics for "integrate into a sensible policy" reward it.
- Use the module's words: *constructed target, fitness for purpose, informative missingness, train–test contamination, availability time, group-level split, site hold-out, proxy, construct validity, recalibration, consent conditions, licence compatibility, data minimization, fairness auditing*.
