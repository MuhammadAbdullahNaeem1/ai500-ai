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

## 4. One-line answers to memorize

| Term | One line |
|---|---|
| Raw data | An oxymoron — data are produced through conceptualization, observation and engineering choices. |
| $Q(D,T,C)$ | Fitness of dataset D for task T under context C — quality is relative to purpose. |
| Coverage error | The sampling frame misses part of the target population. |
| Nonresponse bias | Respondents differ systematically from those who refuse. |
| Platform as instrument | Web behaviour is a reaction inside an engineered environment (algorithm, interface, moderation, incentives). |
| Event/recording/arrival/processing time | When it happened / was logged / reached the pipeline / was processed. |
| Administrative data | Observed outcome = f(condition, access, policy, institutional practice). |
| Completeness | $1-m_j/n$ per cell; complete records / total per record. |
| Accuracy | Closeness to an independent trusted reference — internal agreement is not enough. |
| Staleness | $\Delta t=t-t_{\text{last update}}$ beyond a task threshold. |
| Representativeness | $P_{\text{data}}(X,Y)\ne P_{\text{target}}(X,Y)$ in consequential ways. |
| Differential measurement error | $P(X^*\ne X\mid A=a)$ varies by group — a fairness problem. |
| Construct validity | Does the variable measure the concept we care about? |
| MCAR / MAR / MNAR | Unrelated to data / explained by observed data / depends on the missing value itself. |
| Data leakage | Using information not available at prediction time → optimistic evaluation. |
| Target leakage | A feature reveals the outcome (antibiotics → sepsis). |
| Group leakage | Same entity in train and test; require $G_{\text{train}}\cap G_{\text{test}}=\varnothing$. |
| Provenance / lineage | Where data came from / how they changed through processing. |
| Data minimization | Collect $X_j$ only if Benefit > Risk. |
| De-identification | Risk reduction, not a guarantee of anonymity. |
| Equal opportunity | Equal true-positive rates across groups. |
| Predictive parity | Equal precision (PPV) across groups. |

## 5. Exam strategy (60 minutes, 50 points)

- **≈1 minute per point.** Definitions 9 min, conceptual 12 min, scenario 21 min, biases 8 min, 10 min buffer.
- For "identify $n$": number them, **bold the term**, one sentence of mechanism tied to the case.
- In scenarios, always add the **fix** — rubrics for "integrate into a sensible policy" reward it.
- Use the module's words: *constructed target, fitness for purpose, informative missingness, train–test contamination, availability time, group-level split, site hold-out, proxy, construct validity, recalibration, consent conditions, licence compatibility, data minimization, fairness auditing*.
