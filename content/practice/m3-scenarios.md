# M3 · Scenarios S1–S4 and Reflections R1–R3 (Quiz 3)

Model answers to the scenario and reflection questions at the end of the Module 3 notes (PDF pp. 210–221). These are the closest match to the announced Quiz 3 question types: choose tools for a scenario, analyse findings, say what else is needed and why. **S5, R4 and R5** are mainly about hypothesis tests, effect sizes and analytical flexibility (§3.6 onwards) and are not in Quiz 3; their EDA parts are covered by the answers below.

<div class="pdf-links">
<a href="m3-answers-1.html">Answers Q1–36</a>
<a href="m3-answers-2.html">Answers Q37–72</a>
<a href="quiz3-guide.html">Quiz 3 guide</a>
<a href="pdfs/notes/Module-3-Notes.pdf#page=210">Scenarios in the PDF (p.210)</a>
</div>

<div class="hl-legend">
<span><mark class="hl">Yellow</mark> the one line to remember</span>
<span><span class="key">Blue</span> keywords a rubric looks for</span>
<span><mark class="trap">Coral</mark> a common trap</span>
</div>

## S1 · University student performance prediction

> 12,000 student-course records from 2,000 students over three years (attendance, study hours, sleep, previous grades, online activity). EDA: 7–8 h sleepers score higher, but the relationship weakens within undergraduate and postgraduate groups; some students report > 18 h of daily study; low-attendance students have disproportionately missing sleep records. The team tries many predictors and models, keeps the one with the strongest sleep–score relationship, and reports significance on the same data.

:::question S1(a). Identify the unit of observation, unit of prediction, and appropriate unit of evaluation.
:::solution Answer
- @@Observation@@: a **student-course record** (one student in one course in one term) — 12,000 rows.
- @@Prediction@@: a student's examination performance **in a course** (a student-course), made for an individual student.
- @@Evaluation@@: the student-course prediction, but ==grouped by student== — all of a student's records in the same split, and uncertainty computed at the student level, because the 12,000 rows come from only 2,000 students and are not independent.
:::
:::

:::question S1(b). Which graphical techniques would help examine the relationship between sleep duration and examination performance?
:::solution Answer
- A @@scatterplot@@ of sleep (x) against score (y), with transparency or hexbin (12,000 points) and a smooth trend line — to see whether the relation is linear, peaks at 7–8 h (inverted U), or has thresholds.
- The same scatterplot @@coloured or faceted by undergraduate/postgraduate@@ — the pattern changes by group.
- @@Side-by-side boxplots@@ of scores by sleep band (< 5, 5–7, 7–8, > 8 h) with $n$ per band.
- @@Histograms@@ of sleep and score to check skew, heaping (self-reported whole hours) and impossible values.

Pair with **Spearman/Pearson** per group — but only after looking at the plots.
:::
:::

:::question S1(c). Why might the aggregate relationship differ from the relationships within undergraduate and postgraduate groups?
:::solution Answer
The two groups may differ in **both** sleep and scores (e.g. postgraduates sleep differently and are graded differently). The pooled correlation then mixes the **between-group** difference with the **within-group** relationship (@@aggregation effect / confounding by programme level@@, Simpson-style). If one group both sleeps more and scores higher, pooling creates a stronger overall relationship than exists inside either group. ==An aggregate pattern need not describe any subgroup== — report both.
:::
:::

:::question S1(d). How should the unusually high reported study hours and subgroup-specific missingness be investigated?
:::solution Answer
**> 18 h/day of study:** follow the anomaly workflow — @@flag@@ (histogram/boxplot), @@verify@@ (is the field daily or weekly? units? data-entry error? self-report exaggeration?), @@explain@@, then correct (e.g. a weekly figure entered as daily) or set to missing, and @@document@@; check whether results change with/without them. Do not delete automatically.

**Missing sleep for low-attendance students:** compute $P(\text{sleep missing}\mid\text{attendance band})$ — the missingness is **related to** a predictor and plausibly to the outcome, so it is not random. Complete-case analysis keeps mainly high-attenders (who also score higher), biasing the sleep–score relationship. Use a @@missingness indicator@@, consider imputation fitted on training data, and report performance separately for low-attendance students.
:::
:::

:::question S1(e). What is problematic about discovering a relationship, selecting a model, and confirming the resulting hypothesis using the same dataset?
:::solution Answer
The same data were used to **search** for a pattern, **select** the hypothesis, **choose** variables and model, and **test** it, so the final p-value ==does not account for the selection==: trying many predictors and models and keeping the strongest makes a chance pattern look significant (data-dependent decisions). The reported association is exploratory, not confirmed.
:::
:::

:::question S1(f). Propose an appropriate exploratory and confirmatory analysis strategy for this project.
:::solution Answer
1. Define units (student-course rows, students as the independence unit); split **by student** (and by academic year if predicting future years): an exploration set and an untouched confirmation/test set.
2. On the exploration set: distributions, anomaly checks (study hours), missingness by subgroup, scatterplots of sleep vs score overall and by programme level, other relationships.
3. Write down the hypothesis, variables, model and subgroups (**pre-register**) based on exploration.
4. Run that single pre-specified analysis on the held-out set (or next year's data), controlling for study time, previous grades and programme level.
5. Report effect sizes, uncertainty at the student level, subgroup results, and all exploratory choices transparently.
:::
:::

## S2 · Hospital readmission prediction and data quality

> 50,000 admissions from five hospitals. Hospital B's older BP devices read higher than Hospital A's calibrated ones; labs missing for 60% of low-risk patients (not routinely ordered); length of stay strongly right-skewed; some extreme BP values are confirmed emergencies; some patients have several admissions. The team proposes mean imputation for labs, deleting points beyond the boxplot whiskers, and a random split of admissions.

:::question S2(a). Identify the measurement bias and missingness problems in the dataset.
:::solution Answer
- @@Measurement bias@@: BP is measured with different devices — Hospital B's older devices **systematically read higher**, so B's patients look more hypertensive and "hospital" becomes confounded with BP; a model may learn device differences, not physiology.
- @@Missingness@@: labs missing for 60% of low-risk patients — **not random**, it depends on clinicians' judgement of risk (subgroup-specific, related to the outcome). Mean imputation would give low-risk patients an average lab value computed mostly from sicker patients, distorting distributions and hiding the information in "not ordered".
:::
:::

:::question S2(b). Why might the missing laboratory values contain clinically meaningful information?
:::solution Answer
A test is missing because a clinician ==judged it unnecessary==, which reflects an assessment of the patient as low-risk. "Not ordered" is therefore itself a signal correlated with readmission risk. Represent it with a **missingness indicator** feature rather than hiding it under an imputed mean, and check missingness rates by hospital and risk group.
:::
:::

:::question S2(c). Which descriptive statistics and visualizations would be appropriate for examining hospital length of stay?
:::solution Answer
LOS is strongly right-skewed with a few very long stays. **Numbers:** @@median@@ and @@IQR@@ (or MAD) for the typical stay and spread; @@upper percentiles@@ (90th, 95th) for long stays; mean reported alongside (its gap from the median quantifies the skew). **Plots:** @@histogram@@ (several bin widths, or on a $\log(1+x)$ scale) and @@ECDF@@ (proportion discharged by day $k$; integer days show as steps); @@boxplots by hospital@@ or diagnosis group with $n$. Consider $\log(1+\text{LOS})$ for modelling.
:::
:::

:::question S2(d). Why should observations beyond the boxplot whiskers not automatically be deleted?
:::solution Answer
Clinical experts confirmed that some extreme BP values are **genuine emergencies** — exactly the high-risk patients the model must handle. In skewed variables like LOS, long stays beyond $Q_3+1.5\,\text{IQR}$ are real and clinically important. The whisker rule is a ==convention for flagging, not a test for errors==: deleting these points removes true risk, biases estimates and makes the model fail on the most severe cases. Investigate each (verify, explain), correct only confirmed errors, and document.
:::
:::

:::question S2(e). What statistical and modelling problems may arise from randomly partitioning admissions belonging to the same patient?
:::solution Answer
Admissions of the same patient share characteristics (chronic conditions, demographics, history), so they are **not independent**. A random admission-level split puts the same patient in train and test — @@identity leakage@@: the model recognises patients instead of learning general risk, so test performance is **optimistic**. Statistically, the effective sample size is overstated and standard errors are too small. Split **by patient** (and preferably by time, and check by hospital).
:::
:::

:::question S2(f). Propose a more reliable EDA, preprocessing, and evaluation workflow for this project.
:::solution Answer
1. Define units: admission (observation), patient (independence/grouping), discharge as the prediction time; use only information available at discharge.
2. Split **by patient** (and by time); keep a final test set untouched; ideally also test on a held-out hospital.
3. EDA on training data: distributions by hospital (boxplots of BP by hospital to expose device offsets), LOS with median/IQR/percentiles, missingness by variable, pattern and subgroup, anomaly workflow for extremes.
4. Preprocessing **fitted on training data inside the pipeline**: handle device bias (device/hospital indicator or calibration), missingness indicators plus training-fitted imputation for labs, $\log(1+\text{LOS})$ or robust scaling; keep confirmed extremes.
5. Evaluate with metrics suited to readmission (recall, precision, calibration), **per hospital and subgroup**, with patient-level uncertainty; document every decision.
:::
:::

## S3 · Credit default prediction and feature engineering

> Income ranges from 20,000 to several million; debt ratio from 0 to 1; a distance-based classifier is used unscaled. Occupation has hundreds of categories, some with one customer, target-encoded with default rates from the complete dataset. A feature "total defaults during the next 12 months" is used at application time. At deployment a new occupation appears, and production supplies raw income to a model trained on log income.

:::question S3(a). Why can the difference in numerical scale between income and debt ratio affect a distance-based classifier?
:::solution Answer
Distances sum squared differences across features. Two applicants differing by 10,000 in income and by 0.9 in debt ratio have a distance dominated by income ($10{,}000^2$ vs $0.81$), so ==debt ratio is effectively ignored== — not because it is uninformative but because of its units. The classifier's neighbours are decided almost entirely by income. Scale the features (fitted on training data) before using distances.
:::
:::

:::question S3(b). Compare standardization, robust scaling, and logarithmic transformation as possible treatments for the income variable.
:::solution Answer
- @@Standardization@@ $(x-\mu)/\sigma$: puts income on a comparable scale, but the few multi-million incomes inflate $\mu$ and $\sigma$, squeezing typical incomes together.
- @@Robust scaling@@ $(x-\text{median})/\text{IQR}$: centre and spread unaffected by extremes, so typical incomes stay spread out; extremes remain large values.
- @@Log@@ $\log(1+x)$: compresses the right tail and reduces skew; differences become relative (a 10% rise means the same at any income level) — often the most natural for income. Can be followed by standardization.

Whichever is chosen: ==fit on training data and apply the identical transform in production==.
:::
:::

:::question S3(c). What are the risks of using ordinary target encoding for occupations represented by very few customers?
:::solution Answer
For a one-customer occupation, the encoding **equals that customer's own outcome** (1.00 if they defaulted): the feature leaks the label (@@target leakage@@). Small categories give @@noisy, unstable@@ rates that the model over-trusts (@@overfitting@@). Computing the rates on the complete dataset also leaks **test** outcomes into training features. The result: excellent development performance that collapses on new customers.
:::
:::

:::question S3(d). Explain how out-of-fold target encoding and smoothing can reduce leakage and overfitting.
:::solution Answer
- @@Out-of-fold@@ (cross-fitting): split the training data into folds; each customer's occupation encoding is computed from the **other folds only**, so no customer's own outcome enters their feature. Test data never contribute.
- @@Smoothing@@: $\text{TE}(c)=\frac{n_c\bar y_c+\lambda\bar y}{n_c+\lambda}$ pulls small categories towards the global default rate — a lone defaulter with $\bar y=0.5$, $\lambda=10$ gets $6/11\approx0.55$ instead of 1.00 — reducing noise and overfitting. Use both together; smoothing alone does not fully remove a row's own influence.
:::
:::

:::question S3(e). Identify the temporal leakage and train-serving inconsistency problems in this project.
:::solution Answer
- @@Temporal leakage@@: "total defaults during the **next** 12 months" is not known at application time — it is essentially the outcome itself. The model will look nearly perfect in development and be impossible to use. Only information available **at the application date** may be used (e.g. defaults in the **previous** 12 months).
- @@Train–serving inconsistency@@: the revised model was trained on $\log(\text{income})$ but production supplies raw income, so inputs arrive on a completely different scale and predictions become unreliable. The transformation must be part of the deployed pipeline.
:::
:::

:::question S3(f). How should the system handle occupation categories that were not observed during training?
:::solution Answer
Define the rule **before deployment**: map unseen occupations to an "unknown/other" category or to the global training default rate (or a smoothed prior), possibly using a hierarchy (occupation → industry → sector) so a new job title inherits its industry's information. Log and monitor how often unseen categories occur, and retrain periodically. ==The system must never fail or assign an arbitrary value.==
:::
:::

## S4 · Smart-city air quality and statistical visualization

> Most daily PM2.5 values are moderate but occasional severe episodes are extreme, so the mean is well above the median. Some sensors report identical values for hours; data missing during power outages; peaks at morning and evening traffic; abrupt changes after a firmware update; industrial areas more variable. The dashboard shows a 3-D bar chart with a truncated axis, silently drops missing data, and reports only the citywide mean.

:::question S4(a). What distributional characteristics would explain the difference between mean and median PM2.5 concentrations?
:::solution Answer
A strongly @@right-skewed, heavy-tailed@@ distribution: most days are moderate (where the median sits) while rare severe episodes create a long right tail that pulls the mean up. The gap may also reflect a @@mixture@@ — industrial areas, more variable and extreme, pooled with residential ones.
:::
:::

:::question S4(b). Which graphical methods would help investigate temporal trends, unusual observations, and differences across monitoring stations?
:::solution Answer
- **Temporal:** @@time-series plots@@ of raw readings with a moving average; average by **hour of day** and day of week (traffic peaks); mark missing periods (outages) and firmware-update dates.
- **Unusual observations:** time-series plots per sensor to spot **flat runs** (identical values for hours = stuck sensor) and abrupt level shifts; boxplots/ECDFs for extremes.
- **Stations:** @@side-by-side boxplots@@ (or violins) by station and by land use with $n$; a map; scatterplots/correlations between neighbouring stations to detect sensors that disagree with their neighbours.
:::
:::

:::question S4(c). How can sensor firmware changes introduce measurement bias or apparent distribution shifts?
:::solution Answer
New firmware can change calibration, averaging or filtering, so the **same** air produces different readings. The series then shows a level shift or a change in variability at the update date — an @@apparent distribution shift@@ caused by the @@measurement process@@, not by pollution. A model or trend analysis would treat it as real change. Detect it by aligning shifts with update dates and comparing with neighbouring unchanged sensors; correct with calibration or a device-version feature; document.
:::
:::

:::question S4(d). Why might reporting only the citywide mean conceal important information about pollution exposure?
:::solution Answer
The mean blends all stations and hours into one number: it hides @@spatial differences@@ (industrial neighbourhoods far worse than residential), @@temporal peaks@@ (rush hours, severe episodes), the @@frequency of hazardous days@@, and the skew (it is inflated by a few extremes yet says nothing about how many people face them). Excluding missing data silently can bias it further (outages may coincide with particular conditions). ==People are exposed to local, hourly levels, not to a city average.==
:::
:::

:::question S4(e). How could the median, interquartile range, and upper percentiles complement the mean in describing pollution?
:::solution Answer
- @@Median@@: the typical day, robust to rare extremes.
- @@IQR@@: the usual range of variation (compare industrial vs residential spread).
- @@Upper percentiles@@ (90th/95th/99th) and the **number of days above health thresholds**: the severity and frequency of dangerous episodes — what matters for warnings.
- @@Mean@@: still useful for total/average exposure, and its gap from the median shows skew.

Report them **by station/area and time of day**, not only citywide.
:::
:::

:::question S4(f). Identify the problems with the proposed dashboard and recommend appropriate principles of responsible visualization.
:::solution Answer
**Problems:** 3-D bars distort heights; a @@truncated vertical axis@@ exaggerates differences; @@missing data excluded without disclosure@@; only the @@citywide mean@@ (hides areas, peaks and extremes); no uncertainty or sample sizes.

**Recommendations:** simple 2-D bars or line charts with a full, labelled axis and units; time-series with hourly/daily values and health-threshold lines; maps or small multiples by area with **consistent scales**; median, IQR and upper percentiles alongside the mean; show and explain missing periods; state $n$ and uncertainty; mark firmware changes; colour-blind-safe palettes.
:::
:::

## R1 · Air-quality early warnings (reflection — EDA parts)

:::question R1. Design a comprehensive EDA strategy, investigate unusual observations, select descriptive statistics, and explain why the winter association between PM2.5 and hospital admissions is not causal.
:::solution Answer
**EDA strategy.** Units: station-hour readings (observation), station/area and time (prediction). For each station: histograms/ECDFs (right skew), time-series plots with moving averages (traffic peaks, seasonality, firmware shifts), missingness by station, hour and weather (outages, storms — not random), boxplots by land use (industrial variability), maps and neighbour correlations. Numbers: median, IQR, 90th/95th percentiles, days above thresholds, missingness rates per station.

**Unusual observations.** Compare a spike with neighbouring stations and weather (a real episode affects many stations; a fault affects one); check device logs, flat runs and firmware dates. Genuine extreme episodes are **exactly what a warning system must predict** — ==removing them would train a model that never warns==.

**Statistics.** Mean for average exposure; median for the typical day; upper percentiles and exceedance counts for warnings; IQR/SD for variability by area — different operational questions need different summaries.

**Causation.** Hospital admissions and PM2.5 both rise in winter: shared **seasonality** (cold, respiratory infections, heating) confounds the association. Detrend/deseasonalise and use causal designs before concluding PM2.5 drives admissions.

**Evaluation (beyond EDA):** hourly readings are temporally dependent, so a random hour split leaks neighbouring hours; split chronologically and hold out whole stations.
:::
:::

## R2 · Multihospital clinical deterioration (reflection — EDA and features)

:::question R2. Define the statistical units, plan subgroup analysis, explain the weak aggregate age effect, design preprocessing and identify leakage.
:::solution Answer
**Units.** Observation: an admission/record; prediction: a patient-admission at a time point (next 12 h); sampling: hospital (eight hospitals); evaluation: patient-admission, with patients as the independence unit. Repeated admissions are correlated → split by patient, compute uncertainty at patient level.

**Subgroups.** Pre-specify meaningful groups — hospital, age band, clinical category, rural/urban and a few justified intersections — with adequate $n$; compare distributions, missingness, outcome prevalence and model recall per group; adjust for multiple comparisons.

**Weak aggregate age effect.** Hospitals serve different populations (older multimorbid vs younger), so pooling mixes between-hospital differences with within-group relationships (aggregation, confounding); age may also **interact** with clinical category. Stratify.

**Preprocessing.** Skewed biomarkers: $\log(1+x)$ or robust scaling; standardization for others; imputation plus missingness indicators (tests are ordered for sicker patients). All fitted **on training data inside the pipeline** — the team's plan to impute and scale before partitioning is leakage.

**Leakage.** Medication orders placed **after** deterioration (temporal/target leakage); preprocessing on the full dataset; repeated patients across splits (identity leakage). Each inflates reported performance.

**Unequal recall in rural hospitals.** Check population differences, missingness, measurement practices and data volume per hospital before blaming the model.
:::
:::

## R3 · Credit-card fraud and feature engineering (reflection)

:::question R3. Critique 99.6% accuracy, design an EDA protocol, a leakage-safe feature pipeline, encoding for merchants, and temporal representations.
:::solution Answer
**Accuracy.** Fraud is 0.4%, so predicting "never fraud" already scores 99.6% — ==accuracy says nothing here==. Use recall, precision, PR-AUC, cost-weighted metrics at a chosen threshold.

**EDA.** Histogram/ECDF of amounts on a log scale (right skew), fraud rate by merchant category with counts (rare categories), activity by hour/day (time-series and hour-of-day profiles), per-customer behaviour distributions, scatterplots of amount vs customer average; anomaly workflow for unusual transactions.

**Leakage-safe features.** Every window must end **before** the transaction being scored: transactions in the previous 24 h; average amount over the previous 7 days; locations in the previous month; time since the previous transaction; current amount minus the customer's **historical** average. The merchant fraud rate must use only past, training-period data, out-of-fold and smoothed. The team's rolling features that include later transactions, and merchant rates from the full dataset, are leakage; the random split ignoring customers and time adds identity and temporal leakage.

**Encoding merchants.** One-hot: too many sparse columns; frequency: compact but rare merchants collide; target encoding: powerful but needs out-of-fold estimates, smoothing for rare merchants, and an "unknown" rule for new merchants.

**Temporal.** Hour as an integer puts 23:00 and 00:00 far apart — use $\sin/\cos$ with $P=24$ (and $P=7$ for weekday), combined with lags and customer history features.

**Evaluation.** Chronological split (train on earlier months, test on later), grouped by customer when testing generalisation to new customers.
:::
:::
