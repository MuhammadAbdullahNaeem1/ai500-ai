# M2 · Part B — Curation, Cleaning and Data Leakage

Module 2 notes, Sections 2.4–2.6 (PDF pages 46–80, printed pages 214–248). Profiling and curation, missing values, outliers, duplicates, labels, units, class imbalance, calibration, and every form of leakage.

<div class="pdf-links">
<a href="pdfs/notes/Module-2-Notes.pdf">Module 2 notes (PDF)</a>
<a href="m2-answers-2.html">Answers Q51–100</a>
<a href="m2-scenarios.html">Scenarios S3, S4</a>
<a href="pdfs/tutorials/Computational-Tutorial-2026.pdf">Computational tutorial (topics 1–14)</a>
</div>

Part A showed that data are constructed and that quality has six faces. Part B is about **what to do with a real dataset**: curate it in a traceable workflow, clean it without destroying meaningful information, and — above all — make sure the evaluation is not quietly fed information from the future or from the test set. Quiz 1 already asked to *define temporal leakage* (3 marks); Module 2 is where leakage is treated in full.

## 1. Data curation vs data cleaning (2.4, 2.4.1)

:::def Data curation
> **Data curation** (notes §2.4): “Data curation is the systematic process of acquiring, organizing, validating, documenting, preserving, and maintaining data to ensure that they remain accurate, accessible, and suitable for their intended purposes throughout their lifecycle.”
>
> **Data cleaning (vs curation)** (notes §2.4): “Data cleaning focuses primarily on identifying and correcting errors, inconsistencies, and missing values.”

The systematic process of **acquiring, organizing, validating, documenting, preserving and maintaining** data so they stay accurate, accessible and suitable for their purpose throughout their **lifecycle**.
**Data cleaning** is only one part: identifying and correcting errors, inconsistencies and missing values. Curation adds: **scope and governance** (what belongs, definitions, access, legal basis), **integrity and lineage** (duplicates, provenance, explicit exclusions, reproducibility), **lifecycle management** (version control, retiring obsolete data).
:::

Curation activities: decide inclusion; define variables, coding schemes and metadata standards; resolve duplicates; document provenance and collection history; maintain versions; control access; record exclusions and transformations; preserve reproducibility; archive/retire obsolete data while keeping history.

## 2. The eight-stage curation workflow (2.4.2, Figure 15)

:::figs
m2-p047|Figure 15 — Inventory → Profile → Validate → Clean → Reconcile → Document → Version → Approve
:::

| # | Stage | What happens |
|---|---|---|
| 1 | **Inventory** | Manifest *before touching a cell*: source, owner/custodian, purpose, temporal coverage, format & location, unit of analysis, size, sensitive fields, access restrictions, legal basis, update schedule |
| 2 | **Profile** | Rows/columns, types, unique counts, % missing, distributions, min/max, class balance, duplicates, temporal coverage, subgroup composition |
| 3 | **Validate** | Schema conformity, value ranges, primary-key uniqueness, **referential integrity**, logical consistency, chronological order, cross-source agreement (structural, relational, logical tests — many automatable) |
| 4 | **Clean** | Correct identified defects (missing values, outliers, duplicates, units, labels) |
| 5 | **Reconcile** | Resolve inconsistencies across sources |
| 6 | **Document** | Definitions and provenance |
| 7 | **Version** | Version approved artifacts |
| 8 | **Approve** | Formal release approval |

Together: reproducibility, accountability, traceability, dependable downstream AI.

:::def Immutable audit trail (2.4.6)
> **Immutable raw data** (notes §2.4.6): “Data cleaning must never overwrite raw data without absolute traceability.”

Never overwrite raw data without traceability; keep the original **immutable**. For every change record: **original value, corrected value, rule/procedure, date & time, software/tool version, person responsible, justification.**
:::

:::remember
Curation ⊃ cleaning. Inventory before you touch, profile before you clean, validate with rules, and log every change against an immutable raw copy.
:::

## 3. Missing values (2.5.1)

Causes: measurement never taken; respondent declined; sensor failure; test clinically unnecessary; system failed to record; failed record linkage; deliberate removal for privacy; not applicable. **Not all missingness is poor quality — often it is expected and informative.**

:::def Missingness indicator matrix
$$R_{ij}=\begin{cases}1,&X_{ij}\text{ observed}\\0,&X_{ij}\text{ missing}\end{cases}$$
The pattern of $R$ can itself carry information (patients with more lab tests differ systematically from those with fewer).
:::

:::def MCAR, MAR, MNAR
> **MCAR** (notes §2.5.1): “Under MCAR, the probability of missingness is unrelated to either observed or unobserved data.”
>
> **MAR** (notes §2.5.1): “Here, missingness may depend on observed variables but not on the missing values themselves after conditioning on the observed data.”
>
> **MNAR** (notes §2.5.1): “Under MNAR, the probability of missingness continues to depend on the unobserved values even after accounting for observed information.”
>
> **Mechanisms are assumptions** (notes §2.5.1): “These mechanisms describe assumptions about the data-generating process rather than properties that can usually be verified directly from the dataset.”

- **MCAR** — $P(R\mid X_{\text{obs}},X_{\text{mis}})=P(R)$: missingness unrelated to anything. *Box of 30 of 500 questionnaires falls off a truck; instrument glitch on 5% of samples.*
- **MAR** — $P(R\mid X_{\text{obs}},X_{\text{mis}})=P(R\mid X_{\text{obs}})$: explained by **observed** variables. *Younger people skip income (age observed); older patients miss follow-up cholesterol.*
- **MNAR** — depends on the **unobserved value itself**, even after conditioning. *High earners hide income; severely depressed patients don't complete the questionnaire.*

These are **assumptions about the data-generating process**, usually **not verifiable** from the data alone (you cannot see the values you are missing).
:::

**Approaches:** keep missing values if the method supports it; **missing-value indicators**; simple (mean/median) imputation; **groupwise** imputation; **multiple** imputation; **model-based** imputation; drop variables with excessive missingness; collect more data. No single method is universally optimal.

| Method | When |
|---|---|
| **Mean** | Numeric, roughly symmetric, missingness not tied to extremes |
| **Median** | Outliers/skew (income, lab values, session durations) |
| **Mode** | Categorical (Example 48: `device_type` 2% missing → "Android") |
| **Indicator** `is_missing` | Missingness informative (absent log event, skipped optional form field) |
| **Model-based** (k-NN, regression imputer) | Moderate missingness, predictable from other features (Example 49: BMI from height, weight, age, gender) |

:::warn Lactate — the module's favourite trap
Lactate is ordered mainly when critical illness is suspected, so **its absence signals lower severity**. Mean or model-based imputation **erases that clinical signal**. Keep an indicator.
:::

:::warn Costs of simple imputation
Mean imputation **reduces variance**, **distorts relationships** between variables, creates **artificial clusters** of identical values, and obscures subgroup differences. And: **imputation parameters must be estimated on the training data only**, then applied unchanged to validation/test — otherwise it is leakage.
:::

## 4. Outliers (2.5.2)

An outlier may be a genuine rare observation, entry mistake, wrong unit, sensor malfunction, new population, fraud, or distribution change → **investigate, don't auto-delete.**

:::def Detection rules
> **Outlier** (notes §2.5.2): “An outlier is an observation that differs substantially from the expected pattern of the data.”
>
> **Outlier handling** (notes §2.5.2): “outliers should be investigated rather than automatically removed.”

- **z-score:** $z_i=\dfrac{x_i-\bar x}{s}$.
- **IQR (robust):** $\text{IQR}=Q_3-Q_1$; flag outside $[Q_1-1.5\,\text{IQR},\ Q_3+1.5\,\text{IQR}]$. *(The notes' main text prints $Q_3-1.5\,$IQR — a typo; the footnote gives $+$.)* Example: $Q_1=22,Q_3=30\Rightarrow$ IQR $=8$, fences $10$ and $42$.
- **Multivariate outliers:** ordinary on each variable, impossible jointly — a young person with a very long employment history; transactions in an impossible geographic sequence; physiologically incompatible lab combinations.

These flag cases **for investigation**, not automatic deletion.
:::

**Responses:** verify the source; correct documented errors; convert wrong units; keep valid rare cases and use robust methods; **Winsorize** when justified; separate category; exclude only by **predefined, documented** criteria.

| Strategy | Idea |
|---|---|
| **Clipping/Winsorization** | Cap extremes (e.g. amounts above \$10,000) — limit influence without deleting |
| **Log / Box–Cox** | $x^{(\lambda)}=\dfrac{x^\lambda-1}{\lambda}$ ($\lambda\ne0$), $\ln x$ ($\lambda=0$), for $x>0$; shifted version uses $x+c$. $\lambda=1$ unchanged, $0.5$ square-root-like, $0$ log, $2$ stretches large values |
| **Huber loss** | $\tfrac12e^2$ if $\lvert e\rvert\le\delta$, else $\delta(\lvert e\rvert-\tfrac12\delta)$: squared for small, linear for large residuals |
| **Quantile (pinball) loss** | $\tau(y-\hat y)$ if $y\ge\hat y$, $(1-\tau)(\hat y-y)$ otherwise — asymmetric, targets a quantile |

Robust losses: more stable, but slower convergence, need tuning ($\delta$), may **underfit when outliers are the signal**.

:::warn The tail is often the point
Fraud, rare equipment failures and ICU deterioration live in the **tails**. *Cleaning should remove errors, not meaningful complexity.*
:::

## 5. Duplicates, entity resolution, labels, units (2.5.3)

:::figs
m2-p059|Table 18 — exact duplicate (101 Ali Khan ×2) and near duplicate (Sara Ahmed vs Sara A. Ahmed)
:::

- **Exact duplicates:** identical on all relevant fields. **Near duplicates:** differ slightly (spelling, format, timestamps, abbreviations) → need approximate matching (string similarity, record linkage).
- Causes: repeated ingestion, repeated submissions, merging systems, manual entry, copied benchmarks, entity-resolution errors.
- **Why they matter:** bias frequencies, over-weight some observations, inflate apparent sample size, **contaminate train/test**, optimistic evaluation.

:::def Entity resolution
> **Entity resolution** (notes §2.5.3): “Entity resolution seeks to determine whether multiple records refer to the same underlying entity.”

Deciding whether records refer to the same entity using IDs, names, DOB, addresses, phones, device IDs, behaviour. Errors in both directions: **false merge** (two different entities combined) and **false split** (one entity left as two).
:::

**Inconsistent labels** arise from annotator disagreement, evolving criteria, institutional differences, ambiguous cases, taxonomy changes (e.g. splitting Diabetes into Type 1/2), automated-labelling errors, multiple valid labels.

:::def Inter-annotator agreement
- **Raw agreement:** e.g. 90 of 100 → 90% (no chance correction).
- **Cohen's κ (2 raters):** $\kappa=\dfrac{P_o-P_e}{1-P_e}$, $P_e=\sum_{i=1}^k P_{Ai}P_{Bi}$.
- **Fleiss' κ (≥3 raters):** $\kappa=\dfrac{\bar P-\bar P_e}{1-\bar P_e}$, $P_i=\dfrac{1}{n(n-1)}\big(\sum_j n_{ij}^2-n\big)$, $\bar P_e=\sum_j p_j^2$.
- Adjudication outcomes; class-specific disagreement rates (8% Diabetes vs 25% Pre-diabetes).
:::

*(No numerical problems in Quiz 2 — know what κ corrects for: agreement expected **by chance**.)*

:::example Example 51 — Acceptable alternative labels
Three dermatologists: Benign nevus, Dysplastic nevus, Dysplastic nevus. Consensus **dysplastic nevus**; **benign nevus kept as acceptable alternative** — preserving legitimate diagnostic uncertainty for future re-evaluation. *Consensus does not always equal truth*: majority voting can suppress legitimate expert disagreement. Preserve original annotations, annotator expertise, consensus labels, adjudication decisions, uncertainty, acceptable alternatives.
:::

:::figs
m2-p062|Table 19 — three experts disagree
:::

**Test-set label quality** matters most: rankings depend on it (Northcutt et al.).

**Unit-aware schemas:** every numeric variable needs quantity, **units**, valid ranges, precision, conversion rules, source conventions. **Dimensional analysis:** keep operations dimensionally consistent; convert explicitly, e.g. $x_{\text{kg}}=0.45359237\,x_{\text{lb}}$ — never infer silently.

## 6. Class imbalance (2.5.4)

:::def Class prevalence
> **Class imbalance** (notes §2.5.4): “Class imbalance occurs when one or more classes are substantially less frequent than others.”

$\pi_k=n_k/n$. **Imbalance:** one or more classes far rarer (fraud, rare disease, equipment failure, safety incidents, cyber-attacks). With 99% legitimate, "always legitimate" scores **99% accuracy and catches zero fraud**.
:::

**Strategies:** imbalance-appropriate metrics; class-weighted learning; threshold adjustment; over/under-sampling; collect more minority data; stratified partitioning; reformulate as anomaly detection; cost-sensitive learning. Choice depends on the relative cost of errors.

:::example Example 52 — Resample after splitting (950 Healthy / 50 Cancer)
**Wrong:** oversample to 950/950, then split 80/20 → train 760/760, test 190/190. Duplicated or synthetic cancer cases derived from the same originals land in both sets → e.g. **99% accuracy**, over-optimistic.
**Right:** split first (train 760/40, test 190/10), oversample **only the training set** (760/760), leave the test set untouched (190/10). *(The notes label both approaches "Incorrect" — the second heading is a typo for "Correct".)* In k-fold CV, oversample **inside each training fold**.
:::

:::figs
m2-p066a|Table 20 — oversample then split (wrong)
m2-p066b|Table 21 — split then oversample training only (right)
:::

:::def Recalibration after balancing (Example 53)
> **Balancing vs prevalence** (notes §2.5.4): “Balancing the training data improves learning but does not alter the underlying frequencies of events in real-world applications.”
>
> **Platt scaling** (notes §2.5.4): “Platt scaling is performed by training a logistic regression model on a classifier's output scores (not the original features) to convert those scores into calibrated probabilities.”

Balancing helps learning but **does not change real-world frequencies**. Trained at 50% prevalence (real 5%), a predicted 70% cancer risk is too high; after recalibration it might be ~22%.
- **Platt scaling:** fit a logistic regression on the classifier's **scores** (not original features) on validation data: $P(y=1\mid s)=\dfrac{1}{1+\exp(As+B)}$. With $A=-1.3,B=0.4$ and score $1.6$: $1/(1+e^{-1.68})\approx0.84$.
- **Isotonic regression:** non-parametric monotone mapping from scores to probabilities (e.g. 0.85 → 0.63).
:::

:::figs
m2-p069|Table 22 — SVM scores 2.5, 1.8 (Cancer), 0.4, −1.2 (Healthy)
:::

**SMOTE** (Chawla 2002) creates synthetic minority points by **interpolating between neighbouring minority samples** — continuous features only. **SMOTENC** handles **mixed** numeric + categorical features. Variants: Borderline-SMOTE, **ADASYN** (more samples for harder minority points).

:::remember
Accuracy lies under imbalance. Split first, resample only the training fold, keep the test set untouched, and recalibrate probabilities to the true prevalence.
:::

## 7. Data leakage (2.6)

:::def Data leakage
> **Data leakage** (notes §2.6.1): “Data leakage occurs when information that would not legitimately be available at the intended prediction or evaluation time is inadvertently used during model development.”

Information **not legitimately available at the intended prediction (or evaluation) time** is used during model development → **overly optimistic** performance that does not generalize. Kaufman et al. (2012): a major, overlooked threat.
**Practical test:** *Could this feature, preprocessing statistic or related record genuinely be available, in the same form, when a prediction is made for a new observation?* If **no**, don't use it.
:::

### 7.1 Target leakage

Features that directly or indirectly reveal the outcome. Predicting in-hospital mortality **at admission** must not use discharge disposition, post-mortem procedures, final diagnoses after death, treatment decisions just before the outcome, or variables computed from the outcome. Formally if $Y\to X_j$ after prediction time, using $X_j$ violates temporal/causal order.

Subtle proxies: invoice status after default; cancellation codes after churn; interventions started after recognition; notes written after the outcome.

:::example Example 54 — Sepsis and antibiotics
"Broad-spectrum antibiotics prescribed (Yes/No)" is given **after** clinicians suspect sepsis → near-perfect proxy → **AUC 0.99**, misleading. *Unexpectedly high performance should trigger investigation, not confidence.*
:::

### 7.2 Train–test contamination

Information from evaluation data influences development: identical records in both sets; near-duplicate images across partitions; preprocessing fitted on the whole dataset; feature selection using test labels; repeated tuning on the test set; pretraining on benchmark test examples; synthetic records generated from test records.

:::def Preprocessing contamination
> **Train–test contamination** (notes §2.6.3): “Train-test contamination occurs when information from the evaluation dataset influences model development, parameter estimation, or model selection.”

Wrong: $\mu=\frac{1}{n_{\text{all}}}\sum_{\text{all}}x_i$. Right: $\mu_{\text{train}}=\frac{1}{n_{\text{train}}}\sum_{i\in\text{train}}x_i$, then apply $x_i'=\dfrac{x_i-\mu_{\text{train}}}{\sigma_{\text{train}}}$ to **every** partition.
:::

### 7.3 Cross-validation (2.6.4)

Inside CV, **every data-dependent step is fitted inside each training fold**: imputation, scaling, encoding, feature selection, over/under-sampling, dimensionality reduction, threshold optimization. CV averages over splits → more reliable comparisons and a sense of **variance across folds**.

:::figs
m2-p074|Figure 16 — five-fold CV for model selection, plus a final hold-out test set
:::

| Scheme | Use when | Tools |
|---|---|---|
| **Standard k-fold** | Samples ≈ **i.i.d.** (no time order, groups, dependencies) | KFold, RepeatedKFold |
| **Stratified k-fold** | Classification, esp. **imbalanced** — each fold keeps class proportions (else folds with zero positives → unstable precision/recall/F1) | StratifiedKFold, StratifiedShuffleSplit |
| **Grouped** | Rows belong to patients, users, devices, sessions, households → whole group in one side | GroupKFold, StratifiedGroupKFold |
| **Time-series** | Temporally ordered data → train always **before** validation | TimeSeriesSplit |
| Others | LeaveOneOut; ShuffleSplit (random repeated splits, no folds) | |

### 7.4 Temporal leakage (2.6.5)

Future information used to predict an earlier outcome. At prediction time $t$, every feature must satisfy $t_{\text{availability},j}\le t$ — **availability time, not event time**. Examples: lab results finalized after prediction time; random mixing of past and future in splitting; revised economic statistics; maintenance records entered after failure; summary statistics using future data. → Evaluate **chronologically** (train earlier, validate middle, test future).

:::figs
m2-p077|Figure 17 — temporal evaluation: information flows forward in time only
:::

### 7.5 Group leakage (2.6.6) and site leakage (2.6.7)

Related observations of the same entity (patient, household, student, customer, device, hospital, region, video, document source, repeated measurements) in several partitions inflate performance — the model recognizes the **entity**, not the pattern. Require $G_{\text{train}}\cap G_{\text{test}}=\varnothing$.

:::example Example 55 — Churn: split by customer
C001's January and March in training, February in testing → model learns C001's personal usage → **95% accuracy**, misleading. Correct: all of C001's records together (C001, C002 train; C003 test).
:::

:::figs
m2-p078|Table 23 — record-level split leaks C001
m2-p079|Table 24 — customer-level split
:::

**Site leakage:** if deployment is to **unseen hospitals/institutions**, hold out **whole sites**; random patient splits within the same hospitals don't test that.

### 7.6 Leakage-prevention checklist (2.6.8)

Define the **prediction time**; build the **data timeline**; identify **grouping variables**; **partition before** any preprocessing; search for duplicates/near-duplicates; exclude targets and derived fields; fit preprocessing on **training only**; resample **only within training** partitions/folds; keep an **untouched test set**; **investigate suspiciously strong features**; document **when each feature becomes available**. Evaluation design must **mirror deployment** (future time, new institutions, unseen populations).

:::exam How leakage is examined
Quiz 1 Q1(b) (define temporal leakage + why it makes results unreliable, 3 pts) and Q3(b) (the "emergency-repair-completed" field) were both leakage. Module 2 Scenarios **S3** (mean imputation before split), **S4** (SMOTE before split, image-level split, full-data standardization) and Reflection **R3** (sepsis: antibiotics, ICU transfer, firmware, sites) are leakage-hunting cases. Name the type, explain the mechanism, state the fix.
:::

:::remember
Four leaks + one: **target** (feature encodes the outcome), **train–test contamination** (test info shapes training — duplicates, full-data preprocessing, resampling before split), **temporal** (future info; use availability time), **group** (same entity on both sides), and **site** (hold out whole institutions). Fix: split first, fit everything inside training folds, group and time-aware splits, untouched test set.
:::
