# M2 · Practice answers Q51–100

Answers to practice questions 51–100 (Module 2 notes, PDF pages 132–135): curation, cleaning, units, imbalance, calibration, leakage, documentation, governance and ethics.

<div class="pdf-links">
<a href="m2b-notes.html">Part B notes (2.4–2.6)</a>
<a href="m2c-notes.html">Part C notes (2.7–2.11)</a>
<a href="m2-answers-1.html">Answers Q1–50</a>
<a href="pdfs/notes/Module-2-Notes.pdf#page=132">Questions in the PDF (p.132)</a>
</div>

## Data Profiling and Curation

:::question Q51. Define data curation and explain how it differs from data cleaning.
:::solution Answer
> **Data curation** (notes §2.4): “Data curation is the systematic process of acquiring, organizing, validating, documenting, preserving, and maintaining data to ensure that they remain accurate, accessible, and suitable for their intended purposes throughout their lifecycle.”
>
> **Data cleaning (vs curation)** (notes §2.4): “Data cleaning focuses primarily on identifying and correcting errors, inconsistencies, and missing values.”

**Data curation** is the systematic process of **acquiring, organizing, validating, documenting, preserving and maintaining** data so they remain accurate, accessible and suitable for their purpose **throughout their lifecycle**. **Data cleaning** is one component: identifying and correcting errors, inconsistencies and missing values. Curation is broader — it adds **scope and governance** (what belongs, definitions, access, legal basis), **integrity and lineage** (duplicates, provenance, documented exclusions, reproducibility) and **lifecycle management** (versioning, retiring obsolete data). Cleaning fixes a dataset once; curation keeps it trustworthy and reusable over time.
:::
:::

:::question Q52. What activities are included in a complete data-curation lifecycle?
:::solution Answer
Deciding which data belong in the collection; defining variables, coding schemes and metadata standards; identifying and resolving duplicates; documenting provenance and collection history; maintaining version histories; controlling access and permissions; recording exclusions and transformation decisions; preserving reproducibility through documentation; and archiving or retiring obsolete datasets while keeping historical records.
:::
:::

:::question Q53. Describe the eight stages of the data governance and quality workflow.
:::solution Answer
1. **Inventory** — manifest of sources, owners, purpose, coverage, sensitivity, legal basis before any change.
2. **Profile** — statistical/structural characteristics (types, missingness, distributions, duplicates, subgroups).
3. **Validate** — schema, ranges, keys, referential integrity, logic, chronology, cross-source agreement.
4. **Clean** — correct identified defects.
5. **Reconcile** — resolve inconsistencies across sources.
6. **Document** — definitions and provenance.
7. **Version** — version-control approved artifacts.
8. **Approve** — formal release approval.
Together they give reproducibility, accountability, traceability and dependable downstream AI (Figure 15).
:::
:::

:::question Q54. What information should be recorded in a data inventory before any modification begins?
:::solution Answer
Data **source**; data **owner or custodian**; **purpose** of collection; **temporal coverage**; **file format and storage location**; **unit of analysis**; approximate **size**; **sensitive or protected fields**; **access permissions and restrictions**; **legal or regulatory basis**; expected **update schedule** — i.e. provenance & ownership, scope & structure, and governance.
:::
:::

:::question Q55. What is data profiling, and why should it be performed before cleaning?
:::solution Answer
> **Data profiling** (notes §2.4.4): “Data profiling examines the statistical and structural characteristics of a dataset to identify potential quality issues before cleaning begins.”

**Profiling** examines the statistical and structural characteristics of a dataset — metrics, quality indicators, distributions, composition — to **find potential quality issues**. It comes first because you cannot fix what you have not characterized: it reveals anomalies, unexpected missingness patterns, impossible values, imbalance, duplicates and subgroup gaps, and tells you *which* cleaning steps are justified. Cleaning without profiling risks deleting meaningful rare cases or imputing informative missingness.
:::
:::

:::question Q56. Which statistical, structural, temporal and subgroup characteristics should be examined during profiling?
:::solution Answer
**Structural:** number of rows/columns, data types, unique-value counts, duplicate records. **Statistical:** proportion missing, distributions, min/max, class/label balance. **Temporal:** temporal coverage (gaps, period). **Subgroup:** demographic or subgroup composition.
:::
:::

:::question Q57. Distinguish among schema validation, relational validation, logical validation and domain validation.
:::solution Answer
> **Validation** (notes §2.4.5): “Validation determines whether the dataset satisfies predefined structural, logical, and domain-specific requirements.”

- **Schema (structural):** columns, types and formats conform to the declared schema; primary keys unique.
- **Relational:** **referential integrity** between tables (every visit's patient ID exists in the patient table); cross-source agreement.
- **Logical:** internal consistency among variables — discharge ≥ admission, correct chronological order of timestamps.
- **Domain:** values satisfy subject-matter rules and ranges — $0\le p\le1$, plausible BP, probabilities sum to one.
Many can be automated; resolving violations needs domain expertise.
:::
:::

:::question Q58. Why must original source data be preserved in an immutable state?
:::solution Answer
> **Immutable raw data** (notes §2.4.6): “Data cleaning must never overwrite raw data without absolute traceability.”

So that every change is **traceable, reproducible and reversible**. If raw data are overwritten, nobody can check whether a correction was right, re-run the pipeline with a different rule, roll back an error, or audit how the curated dataset was produced. Immutable raw data plus a change log let future users see exactly what was altered and why.
:::
:::

:::question Q59. What information should be recorded in an audit trail for every correction or transformation?
:::solution Answer
The **original value**, the **corrected value**, the **rule or procedure** used, the **date and time**, the **software/tool version**, the **person responsible**, and the **justification**.
:::
:::

:::question Q60. How do version control, release approval, archiving and retirement support long-term dataset reliability?
:::solution Answer
**Version control** ties every model and paper to an exact dataset version and lets corrections be released without breaking comparability. **Release approval** is a formal gate ensuring only validated, documented versions are used. **Archiving** preserves historical versions for reproducibility and audit. **Retirement** withdraws obsolete or flawed data so it isn't reused, while keeping records of why. Together they keep the dataset trustworthy over its life (lifecycle management).
:::
:::

## Missing Values, Outliers, Duplicates and Labels

:::question Q61. List common reasons why values may be missing from real-world datasets.
:::solution Answer
> **Missing values** (notes §2.5.1): “Missing values occur when one or more observations are unavailable.”

Measurement never taken; respondent declined; **sensor/equipment failure**; clinical test deemed **unnecessary**; system failed to record; unsuccessful **record linkage**; deliberate removal for **privacy**; field **not applicable**.
:::
:::

:::question Q62. Define MCAR, MAR and MNAR.
:::solution Answer
> **MCAR** (notes §2.5.1): “Under MCAR, the probability of missingness is unrelated to either observed or unobserved data.”
>
> **MAR** (notes §2.5.1): “Here, missingness may depend on observed variables but not on the missing values themselves after conditioning on the observed data.”
>
> **MNAR** (notes §2.5.1): “Under MNAR, the probability of missingness continues to depend on the unobserved values even after accounting for observed information.”

- **MCAR:** $P(R\mid X_{obs},X_{mis})=P(R)$ — missingness unrelated to any data (box of questionnaires lost in transport).
- **MAR:** $P(R\mid X_{obs},X_{mis})=P(R\mid X_{obs})$ — explained by **observed** variables (younger people skip income; age observed).
- **MNAR:** missingness depends on the **unobserved value itself** even after conditioning (high earners hide income; severely depressed patients skip the questionnaire).
:::
:::

:::question Q63. Why are missingness mechanisms assumptions about the data-generating process rather than directly observable properties?
:::solution Answer
> **Mechanisms are assumptions** (notes §2.5.1): “These mechanisms describe assumptions about the data-generating process rather than properties that can usually be verified directly from the dataset.”

Distinguishing MAR from MNAR requires knowing whether missingness depends on the **missing values themselves** — which, by definition, we **do not observe**. The data show *which* values are missing and their relation to observed variables, but not what the missing values were. So the mechanism must be **argued from domain knowledge** (why would a lactate test not be ordered?) and handled with sensitivity analyses, not tested definitively.
:::
:::

:::question Q64. Compare deletion, simple imputation, groupwise imputation, multiple imputation, model-based imputation and missing-value indicators.
:::solution Answer
| Approach | Idea | Use / risk |
|---|---|---|
| **Deletion** (rows/variables) | Drop incomplete cases or variables with excessive missingness | Simple; loses data; biased unless MCAR |
| **Simple** (mean/median/mode) | One fill value | Fast; reduces variance, distorts relationships, creates spikes |
| **Groupwise** | Fill with subgroup statistic (e.g. by age band/ward) | Preserves subgroup differences better |
| **Multiple** | Several plausible imputations, results pooled | Reflects imputation uncertainty; more complex |
| **Model-based** (k-NN, regression) | Predict from other features (BMI from height, weight, age, gender) | Preserves relationships; can **hide informative missingness** |
| **Indicator** (`is_missing`) | Add a flag | Keeps the signal when absence is informative (lactate, skipped fields) |
No single approach is universally optimal; fit all on the **training data only**.
:::
:::

:::question Q65. Why must imputation parameters be estimated only from the training partition?
:::solution Answer
> **Imputation without leakage** (notes §2.5.1): “imputation parameters must be estimated using only the training data and then applied unchanged to validation and test datasets.”

Statistics computed on the full dataset (means, medians, k-NN neighbours, regression imputers) contain information from the **validation/test** data, so the test set influences training — **train–test contamination**, producing optimistic estimates. At deployment there is no future test data to borrow from. Estimate on training, then apply **unchanged** to validation, test and production (and inside each CV training fold).
:::
:::

:::question Q66. How can mean imputation reduce variance and distort relationships among variables?
:::solution Answer
Every missing value becomes the **same number**, so the spread shrinks (variance understated, confidence over-stated) and an **artificial cluster/spike** appears at the mean. The filled values ignore other variables, so **correlations are weakened** (a high-BP patient with missing BP gets the average) and subgroup differences are obscured. If missingness is informative (lactate), the mean also **erases the signal** that the test was not needed.
:::
:::

:::question Q67. Why should an outlier be investigated rather than automatically removed?
:::solution Answer
> **Outlier** (notes §2.5.2): “An outlier is an observation that differs substantially from the expected pattern of the data.”
>
> **Outlier handling** (notes §2.5.2): “outliers should be investigated rather than automatically removed.”
>
> **Cleaning principle** (notes §2.5.2): “Data cleaning should remove errors, not meaningful complexity.”

An outlier may be a **genuine rare observation**, a data-entry mistake, a **unit error**, sensor malfunction, a previously unseen population, **fraud**, or distribution change. Auto-deletion removes errors *and* the most important cases — fraud, failures, ICU deterioration live in the tails. In Scenario S3, BP > 300 included both typos and **real emergencies**. "Cleaning should remove errors, not meaningful complexity" — verify the source, correct documented errors, convert units, keep valid rare cases with robust methods, exclude only by predefined documented criteria.
:::
:::

:::question Q68. Compare the z-score rule, IQR rule, Winsorization, transformations and robust loss functions.
:::solution Answer
- **z-score** $z=(x-\bar x)/s$: flags points far from the mean in SD units; mean and SD are themselves pulled by outliers; assumes roughly normal data.
- **IQR rule:** flag outside $[Q_1-1.5\,\text{IQR},\ Q_3+1.5\,\text{IQR}]$; **robust** to extremes and skew. (Both detect *for investigation*.)
- **Winsorization/clipping:** cap extremes at thresholds — keeps the row, limits influence (cap > \$10,000).
- **Transformations** (log, Box–Cox): compress large values and reduce skew (log income).
- **Robust losses** (Huber, quantile): change the **loss** not the data — Huber is squared for small, linear for large residuals; quantile loss weights asymmetrically. More stable but need tuning, slower, may **underfit** if outliers are signal.
:::
:::

:::question Q69. Distinguish exact duplicates, near duplicates, false merges and false splits.
:::solution Answer
> **Exact duplicates** (notes §2.5.3): “Exact duplicates are identical across all relevant fields.”
>
> **Near duplicates** (notes §2.5.3): “Near duplicates differ only slightly because of spelling variations, formatting differences, timestamps, abbreviations, or minor recording inconsistencies.”
>
> **False merges / false splits** (notes §2.5.3): “false merges (combining different entities) and false splits (failing to combine identical entities) …”

**Exact duplicates:** identical on all relevant fields (two "101, Ali Khan, 45, Male, Diabetes" rows). **Near duplicates:** same entity with small differences (Sara Ahmed vs Sara A. Ahmed) — need approximate matching. In entity resolution: **false merge** = records of *different* entities wrongly combined; **false split** = records of the *same* entity left separate. Both arise because matching on names, DOB, addresses, IDs is imperfect.
:::
:::

:::question Q70. Why should annotation systems preserve original labels, consensus labels, adjudication decisions, uncertainty and acceptable alternative labels?
:::solution Answer
> **Majority voting** (notes §2.5.3): “Majority voting provides a practical method for producing consensus labels but may suppress legitimate expert disagreement or overlook genuinely ambiguous cases.”

Because **consensus does not always equal truth**: majority voting can suppress legitimate expert disagreement and hide genuinely ambiguous cases. Keeping originals, annotator expertise, consensus, adjudication and uncertainty supports **transparency and future re-evaluation** — e.g. the lesion labelled dysplastic nevus by consensus keeps *benign nevus* as an acceptable alternative (Example 51), so better imaging or new guidelines can revisit it. It also enables class-specific disagreement analysis and soft labels $p_{ik}$.
:::
:::

## Unit Errors, Class Imbalance and Probability Calibration

:::question Q71. Why should every numerical variable include metadata about units, valid ranges, precision and conversion rules?
:::solution Answer
Numbers are meaningless without their **physical quantity and unit**. Metadata lets validation catch impossible values (range), prevents mixing units, records how precisely something was measured, and makes conversions explicit and reproducible. It also documents source-system conventions when merging hospitals or devices. **Unit-aware schemas** greatly reduce silent unit errors.
:::
:::

:::question Q72. How can mixing kilograms and pounds in one variable produce serious analytical errors?
:::solution Answer
A column with 70 (kg) and 155 (lb?) looks like two very different weights. Means, BMI, dose calculations and model coefficients become wrong; heavy-looking "outliers" may be deleted or genuine extremes hidden; the model learns site/unit artefacts. Pounds are ×2.2 kilograms, so the error is large and **systematic** for one source. Convert explicitly ($x_{kg}=0.45359237\,x_{lb}$) using recorded units — never infer.
:::
:::

:::question Q73. What is dimensional consistency, and why is it important when combining physical quantities?
:::solution Answer
**Dimensional consistency** means every operation respects units: you only add like quantities and the units of derived variables are known and documented (BMI = kg/m²). Combining inconsistent dimensions (kg + lb, mg/dL with mmol/L, seconds with milliseconds) silently produces meaningless features. Explicit dimensional analysis catches these errors before modelling.
:::
:::

:::question Q74. Define class prevalence and class imbalance.
:::solution Answer
> **Class imbalance** (notes §2.5.4): “Class imbalance occurs when one or more classes are substantially less frequent than others.”

**Class prevalence** $\pi_k=n_k/n$ — the proportion of observations in class $k$. **Class imbalance** — one or more classes substantially less frequent than others (fraud, rare disease, equipment failure, safety incidents, cyber-attacks).
:::
:::

:::question Q75. Why can a classifier that always predicts the majority class achieve high accuracy while having no practical value?
:::solution Answer
Accuracy weights all cases equally, so the majority dominates. With 99% legitimate transactions, "always legitimate" gets **99% accuracy** yet **detects zero fraud** — recall for the minority class is 0, which is the whole purpose. Use recall/sensitivity, precision, F1, PR-AUC, and cost-weighted metrics instead.
:::
:::

:::question Q76. Compare class weighting, threshold adjustment, oversampling, undersampling, minority-class collection and cost-sensitive learning.
:::solution Answer
- **Class weighting:** bigger loss weight on minority errors; no data duplication.
- **Threshold adjustment:** move the decision cutoff to trade FP vs FN; model unchanged.
- **Oversampling** (duplicate/SMOTE): more minority examples; risk of overfitting/leakage if done before splitting.
- **Undersampling:** drop majority examples; loses information.
- **Collect more minority data:** best evidence, but slow/costly.
- **Cost-sensitive learning:** optimize expected cost with explicit FP/FN costs.
Also: stratified splits, anomaly-detection framing. Choose by the **relative cost of errors**.
:::
:::

:::question Q77. Why must oversampling be performed only within the training partition or within each training fold?
:::solution Answer
> **Resampling rule** (notes §2.5.4): “Resampling should therefore be performed only within the training partition or within each training fold during cross-validation …”

Oversampled/synthetic minority cases are copies or interpolations of **original** cases. If you oversample first and then split, near-copies of the same patient fall in **both training and test** — the model is tested on what it has effectively seen → **train–test contamination** and over-optimistic results (Example 52: 99% accuracy). Split first, resample only training; in k-fold CV, resample inside each training fold; leave validation/test at the natural prevalence.
:::
:::

:::question Q78. What leakage can occur when synthetic minority observations are generated before train–test partitioning?
:::solution Answer
**Train–test contamination:** SMOTE interpolates between neighbouring minority cases, so synthetic training points are built *from* test records (and synthetic test points from training records). The model is evaluated on interpolations of its own training data; the test minority class also no longer reflects real cases or real prevalence. Reported recall/accuracy inflate and fail on new patients.
:::
:::

:::question Q79. Why can a model trained on an artificially balanced dataset produce poorly calibrated probabilities at deployment?
:::solution Answer
> **Balancing vs prevalence** (notes §2.5.4): “Balancing the training data improves learning but does not alter the underlying frequencies of events in real-world applications.”

The model learns the **training prevalence** (e.g. 50%) as its base rate. If real prevalence is 5%, its probabilities are systematically **too high** (Example 53: predicted 70% may really be ~22%). Balancing helps learning but **does not change real-world frequencies**, so probabilities must be **recalibrated** to the deployment prevalence on representative validation data.
:::
:::

:::question Q80. Compare Platt scaling and isotonic regression as approaches to probability calibration.
:::solution Answer
> **Platt scaling** (notes §2.5.4): “Platt scaling is performed by training a logistic regression model on a classifier's output scores (not the original features) to convert those scores into calibrated probabilities.”

**Platt scaling:** fits a **logistic regression on the classifier's scores** (not features) using a validation set: $P(y=1\mid s)=1/(1+\exp(As+B))$. Parametric (2 parameters), works with little data, assumes a sigmoid-shaped relation (SVM score 1.6 → 0.84 with $A=-1.3,B=0.4$). **Isotonic regression:** fits any **monotonically increasing** step function from scores to probabilities — non-parametric, more flexible, but needs more validation data and can overfit with small samples (0.85 → 0.63). Both are fitted on held-out data, never the test set.
:::
:::

## Data Leakage and Evaluation Design

:::question Q81. Define data leakage and explain why it creates overly optimistic estimates of model performance.
:::solution Answer
> **Data leakage** (notes §2.6.1): “Data leakage occurs when information that would not legitimately be available at the intended prediction or evaluation time is inadvertently used during model development.”

**Data leakage** occurs when information **not legitimately available at the intended prediction or evaluation time** is used during model development. The model exploits signals (future data, the outcome itself, test-set statistics, the same entity) that will **not exist for new cases**, so evaluation scores are inflated and real-world performance drops.
:::
:::

:::question Q82. What practical question should be asked when evaluating whether a feature introduces leakage?
:::solution Answer
> **Leakage test question** (notes §2.6.1): “Could this feature, preprocessing statistic, or related record genuinely be available in the same form at the time a prediction is made for a new observation?”

*"Could this feature, preprocessing statistic, or related record genuinely be available **in the same form at the time a prediction is made** for a new observation?"* If no, it must not be used for training or evaluation.
:::
:::

:::question Q83. Define target leakage and give an example involving sepsis prediction.
:::solution Answer
> **Target leakage** (notes §2.6.2): “Target leakage occurs when one or more input features directly or indirectly reveal the outcome that the model is intended to predict.”

**Target leakage:** input features directly or indirectly reveal the outcome — generated from $Y$ or after the prediction point ($Y\to X_j$). **Sepsis:** "broad-spectrum antibiotics prescribed" is ordered *after* clinicians suspect sepsis, so it is an almost perfect proxy for the label; the model reaches **AUC 0.99** without learning early risk factors and fails when used six hours earlier.
:::
:::

:::question Q84. What is train–test contamination, and through which preprocessing or modeling activities can it occur?
:::solution Answer
> **Train–test contamination** (notes §2.6.3): “Train-test contamination occurs when information from the evaluation dataset influences model development, parameter estimation, or model selection.”

Information from the evaluation data influences development, parameter estimation or model selection. Sources: identical records in both sets; **near-duplicate images** across partitions; **preprocessing fitted on the whole dataset** (scaling, imputation); **feature selection using test labels**; **repeated tuning against the test set**; pretraining on benchmark test examples; **synthetic observations generated from test records** (SMOTE before splitting).
:::
:::

:::question Q85. Why must scaling, imputation, encoding, feature selection, dimensionality reduction and resampling occur inside each CV training fold?
:::solution Answer
Each is **data-dependent**: it estimates something (means/SDs, imputation values, category maps, selected features, PCA axes, synthetic samples) from the data it sees. Fitting on all data before creating folds lets each validation fold influence its own preprocessing → leakage and biased CV estimates. Fitting inside each training fold (a pipeline) simulates deployment, where the preprocessing never sees the new case.
:::
:::

:::question Q86. Compare standard k-fold, stratified k-fold, grouped CV and time-series CV.
:::solution Answer
- **Standard k-fold:** for **i.i.d.** samples; k folds, each validates once; average metrics (mean ± SD).
- **Stratified k-fold:** classification, especially **imbalanced** — each fold keeps the class proportions, so no fold lacks positives (stable precision/recall/F1).
- **Grouped CV** (GroupKFold): rows from the same **patient/user/device/household** stay in one fold — prevents group leakage, tests generalization to new entities.
- **Time-series CV** (TimeSeriesSplit): training always **precedes** validation in time — prevents seeing the future.
:::
:::

:::question Q87. What is temporal leakage, and why is information-availability time more important than event time?
:::solution Answer
> **Temporal leakage** (notes §2.6.5): “Temporal leakage occurs when information from the future is used to predict an earlier outcome.”
>
> **Availability time** (notes §2.6.5): “The relevant timestamp is the moment at which the information became available, not necessarily when the underlying event occurred.”

**Temporal leakage:** using information from the future to predict an earlier outcome. Each feature must satisfy $t_{\text{availability},j}\le t$. A lab result may describe a sample taken *before* $t$ (event time) but be **finalized after** $t$; using event time lets the model use it although it would not be in the system at prediction time. Availability time reflects what the deployed system can actually know. Examples: labs finalized later, revised economic statistics, maintenance records entered after failure, random past/future mixing.
:::
:::

:::question Q88. What is group leakage, and why must all records from one patient, customer, household or device remain in one partition?
:::solution Answer
> **Group leakage** (notes §2.6.6): “Group leakage occurs when related observations from the same entity appear in multiple data partitions.”

**Group leakage:** correlated observations from the **same entity** appear in multiple partitions. The model can recognize **entity-specific characteristics** (a patient's anatomy, a customer's usage level) instead of general patterns, inflating test scores (Example 55: C001 in train and test → 95% accuracy). Requirement $G_{\text{train}}\cap G_{\text{test}}=\varnothing$ so evaluation reflects **new entities**, as in deployment.
:::
:::

:::question Q89. When should an entire institution or site be held out during evaluation?
:::solution Answer
When the model is intended for **previously unseen institutions** (new hospitals, schools, regions). Random patient-level splits within the same hospitals share equipment, protocols, coding and populations, so they overestimate transfer. **Hold out whole sites** (leave-one-site-out) so testing reflects genuinely new environments (Scenario S4, Reflection R3).
:::
:::

:::question Q90. What checks should be included in a comprehensive data-leakage prevention checklist?
:::solution Answer
Define the **prediction time**; construct the **data timeline**; identify **grouping variables** and dependent entities; **partition before** any preprocessing; search for **duplicates and near-duplicates**; exclude **targets and derived fields** from predictors; fit preprocessing on **training only**; **resample only within training** partitions/folds; keep an **untouched test set**; **investigate unexpectedly powerful variables**; document **when each feature becomes available**; make the evaluation design **mirror deployment** (future periods, new sites, unseen populations).
:::
:::

## Documentation, Governance, Privacy, Fairness and Ethics

:::question Q91. What information should be included in a comprehensive Datasheet for Datasets?
:::solution Answer
- **Motivation:** why created, funder, task/gap, intended users.
- **Composition:** what an instance is, count, populations/periods, labels, sensitive information.
- **Collection process:** who, instruments, sampling, **consent**, compensation, limitations.
- **Preprocessing/cleaning:** removals, imputation, transformations, label review, de-identification.
- **Intended and discouraged uses:** tasks, users, limitations, prohibited uses, unreliable contexts.
- **Distribution and licensing:** access procedure, licence, redistribution, commercial limits, attribution, privacy/security.
- **Maintenance:** owners, error reporting, update schedule, withdrawal, versioning, revision tracking.
:::
:::

:::question Q92. How does a data dictionary differ from a dataset-level datasheet?
:::solution Answer
> **Data dictionary** (notes §2.7.2): “A data dictionary provides field-level documentation describing the meaning, structure, and interpretation of individual variables.”

A **datasheet** documents the **whole dataset** — motivation, composition, collection, uses, licensing, maintenance. A **data dictionary** documents **each field**: variable name, human-readable label, definition, data type, unit, allowed values, missing-value codes, source, time semantics, transformation, sensitivity, quality notes. One tells you *whether* to use the data; the other tells you *what each column means*.
:::
:::

:::question Q93. Distinguish between data provenance and data lineage.
:::solution Answer
> **Data provenance** (notes §2.7.3): “Data provenance describes the origin of data and the processes used to generate them.”
>
> **Data lineage** (notes §2.7.3): “Data lineage records how data evolve as they move through processing pipelines.”

**Provenance** — the documented **origin** and history/chain of custody: how, when, where and by whom data were collected and processed. **Lineage** — how data **evolve through processing pipelines**: the chain $D_0\to D_1\to D_2\to D_{\text{training}}$ with the transformation that produced each version. Provenance answers "where did this come from?"; lineage answers "what was done to it?".
:::
:::

:::question Q94. What information should be recorded for every transformation in a data-lineage chain?
:::solution Answer
**Input dataset version; code or software version; processing parameters; output dataset version; execution timestamp; responsible person or system; validation results.**
:::
:::

:::question Q95. Why should consent documentation describe permitted purposes, linkage, commercial use, international transfer, withdrawal and vulnerable populations?
:::solution Answer
> **Consent documentation** (notes §2.7.4): “Consent should not be represented merely as a binary indicator such as consent obtained: Yes/No.”

Because "Consent obtained: Yes" says nothing about **what** was agreed. A new use (commercial product, transfer abroad, linkage with other datasets, AI development) may violate the participants' actual agreement (Example 57). Withdrawal terms decide what happens to records and **derived models**; vulnerable populations need extra protection; broad vs specific consent determines secondary use. Detailed records let reviewers judge whether a proposed use is **ethically and legally acceptable**.
:::
:::

:::question Q96. How do consent, licensing, copyright and privacy impose different constraints on dataset use?
:::solution Answer
> **Consent vs licensing** (notes §2.7 Ex. 57): “Consent explains what participants agreed to, while licensing defines what users are legally permitted to do with the data.”
>
> **Copyright vs privacy** (notes §2.7.6): “Legal permission to access a dataset does not automatically mean that every possible use is acceptable.”

- **Consent** — what **participants agreed to** (purposes, commercial, transfer, withdrawal).
- **Licensing** — what **users are legally permitted** to do (research-only, no redistribution, attribution, no re-identification).
- **Copyright** — **intellectual-property** rights in the content/compilation.
- **Privacy** — obligations to protect **personal information**, regardless of licence.
They are independent: an openly licensed dataset can still contain personal data; de-identified data can still be under copyright or contract. Satisfying one does not satisfy the others.
:::
:::

:::question Q97. Why should de-identification be treated as risk reduction rather than a guarantee of anonymity?
:::solution Answer
> **De-identification** (notes §2.8.3): “de-identification should be viewed as a risk-reduction strategy rather than a guarantee of anonymity.”

Removing names and IDs leaves **quasi-identifiers** — age, location, dates, rare diagnoses — whose **combinations** can be unique and linked to external data (**linkage attacks**, re-identification). Models trained on the data can also leak membership. So de-identification **lowers** risk but does not eliminate it; it must be combined with access control, minimization, aggregation and possibly differential privacy.
:::
:::

:::question Q98. Explain how data minimization, access control, encryption, retention limits, audit logs, differential privacy and federated learning reduce privacy risks.
:::solution Answer
> **Data minimization** (notes §2.8.5): “Data minimization is the principle that organizations should collect, retain, and process only the information reasonably necessary to achieve a clearly defined and legitimate purpose.”

- **Minimization** — collect only what's necessary (Benefit > Risk), so less can leak.
- **Access control** — role-based restriction to authorized users.
- **Encryption** — protects stored and transmitted data from interception/theft.
- **Retention limits** — delete data when no longer needed; avoid indefinite exposure.
- **Audit logs** — record who accessed what, deterring and detecting misuse.
- **Differential privacy** — adds calibrated noise so outputs reveal little about any individual.
- **Federated learning** — trains where data live; raw data are not centralized.
Together they protect across the whole lifecycle (OECD: purpose limitation, minimization, security, accountability).
:::
:::

:::question Q99. Why might sensitive attributes be excluded from prediction but retained under restricted access for fairness auditing?
:::solution Answer
> **Removing sensitive attributes** (notes §2.8.6): “Excluding a sensitive variable from a predictive model does not necessarily prevent discriminatory outcomes.”

Excluding them from inputs avoids **direct** use in decisions, but bias can persist through **proxies** (postal code, school, utilization). Without recording the attribute you **cannot measure** subgroup disparities — Example 60's accuracy of 91/90/**74%** for Group C would be invisible. So governance separates **use for prediction** from **use for fairness evaluation and monitoring**, with strict access, retention and security controls.
:::
:::

:::question Q100. How should data owners, stewards, ethics committees, review bodies, technical teams, domain experts and leaders share responsibility?
:::solution Answer
> **Data owner** (notes §2.8.11): “Holds formal authority and ultimate responsibility for the data resource.”
>
> **Data steward** (notes §2.8.11): “Maintains data definitions, quality standards, documentation, metadata, and access policies.”
>
> **Data custodian** (notes §2.8.11): “Manages the technical infrastructure supporting data storage, security, backup, and access.”
>
> **Data producer** (notes §2.8.11): “Creates, measures, or collects the original observations.”
>
> **Data consumer** (notes §2.8.11): “Uses the data for research, analysis, reporting, or predictive modeling.”
>
> **Model owner** (notes §2.8.11): “Assumes responsibility for the development, deployment, monitoring, and operational performance of predictive models.”

- **Data owner** — formal authority and **ultimate accountability**; approves uses.
- **Data steward** — definitions, quality standards, documentation, metadata, access policies.
- **Data custodian/technical teams** — secure infrastructure, access, lineage, leakage-safe pipelines, monitoring.
- **Domain experts** — validate constructs, proxies, labels and clinical/operational meaning.
- **Ethics committees / IRBs / data-protection offices** — review consent, privacy, fairness, vulnerable groups, secondary use.
- **Model owner** — deployment, monitoring, performance.
- **Organizational leaders** — resources, policy, final accountability, escalation.
Clear assignment prevents the failure where *everyone uses the data but no one is responsible*; it operationalizes lawful, fair, transparent and accountable use.
:::
:::
