# M3 · Back questions Q1–36 (Quiz 3)

Answers to the end-of-module practice questions in the Module 3 notes (PDF pp. 203–205), sections **3.1–3.3**. Each is sized for a **3–4 mark** quiz part: point → reason → example from the notes. Q73–Q100 cover §3.6 onwards and are **not** in Quiz 3.

<div class="pdf-links">
<a href="m3-answers-2.html">Answers Q37–72</a>
<a href="m3-scenarios.html">Scenarios S1–S4 · Reflections R1–R3</a>
<a href="quiz3-numericals.html">Quiz 3 numericals</a>
<a href="pdfs/notes/Module-3-Notes.pdf#page=203">Questions in the PDF (p.203)</a>
</div>

<div class="hl-legend">
<span><mark class="hl">Yellow</mark> the one line to remember</span>
<span><span class="key">Blue</span> keywords a rubric looks for</span>
<span><mark class="trap">Coral</mark> a common trap</span>
</div>

## Foundations of Exploratory Data Analysis

:::question Q1. Define exploratory data analysis (EDA) and explain its role in the end-to-end AI and machine learning pipeline.
:::solution Answer
EDA is ==the systematic investigation of a dataset before formal modelling, hypothesis testing or confirmatory inference== (Tukey, 1977). In the pipeline it sits between data collection/cleaning and modelling: it reveals the @@structure@@ and @@distributions@@ of the variables, @@relationships@@, @@missing, duplicated or erroneous values@@, @@outliers@@ and @@bias@@; it checks whether model @@assumptions@@ look reasonable; it decides @@transformations and preprocessing@@; it judges whether the task is @@feasible@@; and it @@generates hypotheses@@ and guides the choice of models. Catching these problems early stops them being carried into the model and its conclusions. *Example 65:* EDA shows students sleeping 7–8 h score higher — a hypothesis to test, not a finding.
:::
:::

:::question Q2. What are the principal objectives of EDA, and how do numerical summaries and graphical methods complement one another?
:::solution Answer
**Objectives** (NIST): maximise insight, uncover underlying structure, detect outliers and anomalies, test assumptions, develop parsimonious models, determine good factor settings. The core goals in §3.2: understand @@distributions@@, @@relationships@@, @@anomalies@@, @@missingness@@, @@bias@@ and @@subgroups@@.

**Complementarity:** @@graphical methods@@ (histograms, boxplots, scatterplots, density, time-series plots) show shape, clusters, gaps, non-linearity and outliers that ==numbers compress away==; @@numerical summaries@@ (mean, median, SD, IQR, quantiles, correlation) quantify what the plots show and make comparisons precise. Anscombe's quartet is the proof: identical summaries, completely different plots. So a good EDA answer is **hybrid** — the plot and the matching number.
:::
:::

:::question Q3. Why should EDA be treated as an iterative process rather than a fixed sequence of statistical operations?
:::solution Answer
Because each finding raises the next question: ==question → visualize/summarize → unexpected pattern → new hypothesis → refined question== (Figure 22). A scatterplot may show a relationship *and* some odd points; summaries of those points raise a new question — genuine cases, measurement errors, or data-entry problems? A fixed checklist would never ask that follow-up. The analyst looks at the data from several perspectives and lets what is found steer what is examined next; the exact sequence depends on the question, the dataset and how it was generated. (The recommended workflow in §3.1.7 gives structure, but it is still iterative.)
:::
:::

:::question Q4. Distinguish between exploratory analysis and confirmatory analysis in terms of their objectives, analytical procedures, and interpretation of findings.
:::solution Answer
| | exploratory | confirmatory |
|---|---|---|
| **objective** | @@discover@@ what the data may reveal; generate hypotheses | @@evaluate@@ a specific claim specified in advance |
| **procedure** | flexible, iterative, data-driven choices | design, variables, model and decision rule @@fixed before@@ seeing the data |
| **interpretation** | patterns are **candidates** that may reflect chance, selection or this dataset's quirks | evidence (p-values, intervals) with its stated meaning |

==Exploration finds what might be interesting; confirmation tests whether it is likely to be genuine==, using independent or properly controlled evidence.
:::
:::

:::question Q5. Why should a hypothesis discovered through EDA not automatically be treated as independently confirmed evidence when tested using the same dataset?
:::solution Answer
Because the data were used **twice** — to find the result and to prove it. The sequence *search for pattern → select hypothesis → choose variables → choose model → test* makes @@data-dependent decisions@@ at every step, so the final p-value or interval ==does not account for the selection that preceded it== and the result looks stronger than it is. *Example 66:* after scanning sleep, exercise, screen time, breakfast, caffeine and study time, one relationship may look strong **by chance**; testing only that one on the same 500 students exaggerates it. The exploration was still useful — it produced a hypothesis — but it should be tested on new data, a held-out sample, or a pre-registered analysis.
:::
:::

:::question Q6. Explain how separate exploratory and confirmatory datasets, preregistration, replication, and transparent reporting can improve the credibility of statistical findings.
:::solution Answer
- @@Separate datasets@@ (or train/validation/test partitions): one part to discover, an untouched part to test, so the evidence is independent of the discovery.
- @@Preregistration@@: hypotheses, variables, outcomes and analysis fixed **before** the confirmatory analysis, so results cannot steer the method.
- @@Replication@@: the finding is checked on a new, independent sample — chance patterns rarely replicate.
- @@Transparent reporting@@: documenting variable selection, exclusions, transformations and model choice lets readers judge how much flexibility was used.

Together they make clear which analyses were exploratory and which were confirmatory, giving ==more credible and reproducible conclusions==.
:::
:::

:::question Q7. Distinguish among the unit of observation, unit of prediction, unit of sampling, and unit of evaluation. Illustrate the differences using a medical imaging application.
:::solution Answer
- @@Unit of observation@@ — what one record is: **one image**.
- @@Unit of prediction@@ — the entity a prediction is for: often **the patient** (does this patient have the disease?).
- @@Unit of sampling@@ — what was selected into the data: **patients** (or hospitals, if hospitals were chosen first and then patients).
- @@Unit of evaluation@@ — where performance is assessed: **the patient** (patient-level sensitivity), not each image.

In a 50,000-image dataset from 2,000 patients the units differ, so splits and summaries must be made at the **patient** level: ==all images of a patient go in the same split==.
:::
:::

:::question Q8. A medical imaging dataset contains 50,000 images from 2,000 patients. Why would treating the dataset as 50,000 independent patient-level observations potentially produce misleading statistical conclusions?
:::solution Answer
Images from the same patient share anatomy, disease state, scanner and acquisition settings, so they are **not independent** — ==row count is not sample size==. Treating them as 50,000 independent patients causes:
- @@overstated sample size@@ (effective $n$ is closer to 2,000);
- @@underestimated standard errors@@ and over-confident p-values/intervals;
- @@data leakage@@ if images of one patient fall in both train and test, so the model is tested on patients it has effectively seen;
- @@misleading summaries@@ when some patients contribute many more images than others.
:::
:::

## Understanding Distributions and Detecting Anomalies

:::question Q9. Explain the five complementary characteristics of a numerical distribution: location, spread, shape, tails, and unusual observations.
:::solution Answer
- @@Location@@ — where values centre (mean, median).
- @@Spread@@ — how widely they vary (range, variance, SD, IQR).
- @@Shape@@ — symmetry, skewness, modality, concentration (histogram, density, skewness).
- @@Tails@@ — behaviour far from the centre: heavy or light (Q–Q plot, upper quantiles).
- @@Unusual observations@@ — legitimate extremes **or** data-quality problems (boxplot, inspection).

They are complementary: two variables can share a mean and SD yet differ in shape and tails, so ==summarise all five, with plots as well as numbers== (Figure 24).
:::
:::

:::question Q10. Distinguish among symmetric, positively skewed, negatively skewed, unimodal, bimodal, and multimodal distributions.
:::solution Answer
- **Symmetric:** mirror image around the centre; mean ≈ median.
- **Positively (right) skewed:** long right tail; ==mean > median== (income, waiting times, costs).
- **Negatively (left) skewed:** long left tail; mean < median (scores near a maximum).
- **Unimodal:** one peak. **Bimodal:** two peaks. **Multimodal:** several peaks.

Two or more peaks usually signal a @@mixture of subpopulations@@ (sites, scanners, disease types, demographic groups) — stratify by the suspected group. Skewness concerns asymmetry; modality concerns the number of peaks — a distribution can be both skewed and bimodal.
:::
:::

:::question Q11. What are heavy-tailed distributions, and why can they create difficulties for statistical models that assume approximately normal observations?
:::solution Answer
A **heavy-tailed** distribution produces extreme values far from the centre **much more often** than a normal distribution would (insurance claims, financial losses and returns). Difficulties: the @@mean and SD@@ are dominated by a few extremes and become unstable or misleading; methods assuming @@normality or constant variance@@ give wrong p-values and intervals and poor predictions; a Q–Q plot bends away at the ends; and boxplots flag many legitimate points as "outliers". Remedies: robust summaries (median, IQR, MAD), transformations such as $\log(1+x)$, and models suited to heavy tails — and never delete the extremes automatically.
:::
:::

:::question Q12. Explain the meaning and practical significance of zero inflation, truncation, and heterogeneous mixtures in real-world datasets.
:::solution Answer
- @@Zero inflation@@: far more zeros than the rest of the distribution implies (many people with no hospital visits or claims in a period). A single model may fit neither the zeros nor the positive values; consider modelling "any vs none" separately, and check zeros are not **missing values coded as 0**.
- @@Truncation@@ (or censoring): values cut off or piled up at a limit — physical bounds, detection limits, study end. Means are biased and the true tail is unseen; record and handle the limit.
- @@Heterogeneous mixtures@@: data pooled from distinct groups (hospitals, scanners, regimes) give multiple peaks or shoulders; one summary or model may describe no group well — ==stratify==.
:::
:::

:::question Q13. How can inappropriate histogram bin widths and bin boundaries conceal genuine structure or create misleading distributional patterns?
:::solution Answer
- @@Too few (wide) bins@@ over-smooth: two peaks merge into one, gaps disappear — real structure is hidden.
- @@Too many (narrow) bins@@ make random noise look like many peaks and gaps.
- @@Bin boundaries@@ can split a cluster across two bins or create false spikes and dips — especially with **heaping** (values at multiples of 5 or 10, prices at 9.99).
- An extreme value stretches the axis so all ordinary values fall into one bar.

Fix: ==try several reasonable bin widths and keep only features that persist==; use common bins and axes (and proportions) when comparing groups; add an ECDF, which needs no bins.
:::
:::

:::question Q14. Why can excessive smoothing or insufficient smoothing in kernel density estimation produce incorrect interpretations of distributional shape?
:::solution Answer
A KDE's shape depends on its **bandwidth**. @@Over-smoothing@@ (bandwidth too large) erases genuine peaks, shoulders and subpopulations, making a bimodal variable look unimodal. @@Under-smoothing@@ (too small) produces spurious wiggles that look like real modes. Near a boundary the kernel also spills density outside the possible range (@@boundary bias@@ — mass below 0 or outside $[0,1]$). So ==a density plot is an estimate of shape, not the data==: vary the bandwidth, use boundary-aware methods, and check with the raw data, a histogram or an ECDF.
:::
:::

:::question Q15. Define an anomaly and distinguish among a legitimate extreme observation, measurement error, data-entry error, and evidence of distribution shift.
:::solution Answer
An **anomaly** is ==an observation, combination or pattern that differs substantially from what the data-generating process would normally produce==.
- **Legitimate extreme:** real but rare (a genuine 900-minute ED wait, a confirmed hypertensive emergency) — keep it.
- **Measurement error:** the instrument failed or was miscalibrated (a sensor jump, a body temperature of 350 °C).
- **Data-entry error:** a human or system recording mistake (extra zero, negative age, wrong units).
- **Distribution shift:** many values change together because the process changed (new device, firmware update, new population) — not one bad point but a new regime.

Distinguish them by checking source records, units, devices and timing, and whether nearby/related values changed too.
:::
:::

:::question Q16. Why should observations beyond the conventional boxplot whiskers not automatically be removed from a dataset?
:::solution Answer
Points beyond $Q_1-1.5\,\text{IQR}$ or $Q_3+1.5\,\text{IQR}$ are just past a @@conventional line@@ — ==not automatically errors==. In skewed or heavy-tailed variables (hospital charges, waiting times, length of stay) many legitimate observations lie beyond the whiskers, and they are often the most important cases (rare events, fraud, emergencies). Deleting them biases means and variances downwards, hides real risk, and can remove the very cases a model must detect. Retention, investigation, transformation or removal should depend on **context and provenance**, with the decision documented.
:::
:::

:::question Q17. Describe a structured anomaly-investigation workflow covering flagging, verification, explanation, correction or retention, and documentation.
:::solution Answer
1. @@Flag@@ — mark candidates with plots (boxplot, scatterplot, time series) and rules; don't act yet.
2. @@Verify@@ — check the source record, units, device logs, timestamps and duplicates.
3. @@Explain@@ — decide the cause: entry/unit error, equipment failure, rare legitimate case, fraud, discovery, or distribution shift.
4. @@Correct or retain@@ — fix confirmed errors (or set to missing); ==keep valid rare observations==.
5. @@Document@@ — record the decision, its rationale, and the observation's influence on later analyses (e.g. results with and without it).
:::
:::

## Missingness, Bias, Representativeness, and Subgroup Behavior

:::question Q18. Distinguish among variable-level, record-level, pattern-level, and subgroup-specific missingness.
:::solution Answer
- @@Variable-level@@: proportion missing per feature, $r_j=\#\text{missing in }j/n$ — which features are badly incomplete.
- @@Record-level@@: proportion of features missing per row, $r_i=\#\text{missing in }i/p$ — unusually incomplete records (system failures, particular people).
- @@Pattern-level@@: which variables are missing **together** — a shared cause (failed monitor → BP and heart rate; declined sensitive questions → income and employment).
- @@Subgroup-specific@@: $P(R_j=0\mid G=g)$ — whether some groups have much more missing data. ==An overall rate can hide large group differences.==
:::
:::

:::question Q19. A dataset contains 2,000 patient records, and income is missing for 450 patients. Calculate the variable-level missingness rate. What additional information would be needed to determine whether missingness is concentrated within particular patient groups?
:::solution Answer
$r_{\text{income}}=450/2000=0.225$, i.e. **22.5%**.

To see whether it is concentrated, we need @@subgroup-specific rates@@ $P(\text{income missing}\mid G=g)$ by relevant groups — age, insurance type, hospital, region, risk level, time period — plus the group sizes. Example 71 shows why: an overall figure can hide 55% missing in one group and 10% in another, which changes effective sample sizes, imputation accuracy and model reliability per group. Also check pattern-level co-missingness (income with employment).
:::
:::

:::question Q20. How can missingness itself contain useful information about the underlying data-generating process? Explain using an example involving laboratory tests ordered selectively by clinicians.
:::solution Answer
Clinicians order tests when they suspect a problem. So a lab value is missing mostly for patients who looked well — ==the absence of a test is a clinical judgement==, recorded implicitly. Missingness is then related to the patient's condition, not random — in scenario S2, labs are missing for 60% of low-risk patients because clinicians do not routinely order them. Consequences: complete-case analysis keeps mostly sicker patients; mean-imputation invents normal-looking values with the wrong meaning. Use it instead: add a @@missingness indicator@@ ("test not ordered") as a feature, report missingness by subgroup, and evaluate the model separately by group.
:::
:::

:::question Q21. Explain the consequences of subgroup-specific missingness for effective sample size, imputation uncertainty, feature distributions, and model reliability.
:::solution Answer
Using Example 71 (income missing 55% Medicare, 10% Medicaid, 25% private):
- @@Unequal effective sample sizes@@: dropping incomplete rows keeps 45% / 90% / 75% → the model learns the income relationship mostly from Medicaid patients.
- @@Differential imputation error@@: imputation is least reliable where most is missing (Medicare), possibly biased (under-estimating retirement income).
- @@Distorted feature distributions@@: the observed Medicare incomes come from a self-selected 45% — not representative.
- @@Unequal model reliability@@: predictions are least reliable for Medicare patients, hidden behind one overall AUC.

Remedies: report missingness by subgroup, use missingness indicators, evaluate per subgroup.
:::
:::

:::question Q22. Distinguish among sampling bias, measurement bias, label bias, selection bias, survivorship bias, and historical bias.
:::solution Answer
- @@Sampling bias@@ — the sample differs systematically from the target population (online survey misses people without internet).
- @@Measurement bias@@ — a variable is measured differently across groups, sites, devices or time (older BP device reads higher at Hospital B).
- @@Label bias@@ — the recorded outcome is an imperfect proxy for the construct (transfer recorded as "dropout"; no complaint ≠ satisfied).
- @@Selection bias@@ — inclusion depends on variables related to the outcome, distorting associations (only hospitalised patients; only admitted students).
- @@Survivorship bias@@ — only units that "survived" a process remain (studying only companies still operating, only graduates).
- @@Historical bias@@ — data accurately record an unequal past process (hiring, lending, policing records).
:::
:::

:::question Q23. How can a dataset be internally consistent and accurately recorded while still reproducing historical inequalities?
:::solution Answer
Because accuracy describes how well the data record **what happened**, not whether what happened was fair. If certain groups historically received fewer job offers, loans, treatments or admissions — or more police attention — the records faithfully capture those decisions. A model trained on them ==learns past unequal opportunity as if it were merit or risk==: e.g. arrest data reflect where police patrolled, so areas look "high-crime" and attract more patrols (a feedback loop); lending data contain few successful borrowers from communities that were denied credit. This is @@historical bias@@: the problem is in the process, not the recording.
:::
:::

:::question Q24. Explain the Big Data Paradox and why increasing the number of observations does not necessarily eliminate systematic bias.
:::solution Answer
The **Big Data paradox** (Meng, 2018): a very large dataset can give ==precise but wrong== estimates when inclusion in the data is related to the quantity measured. More data reduces @@random sampling error@@, not @@systematic bias@@; worse, when a huge non-random dataset is analysed as if it were a random sample, the confidence intervals become **deceptively narrow** around a biased value. Example: about 2.3 million self-reported 2016 US voting records (≈1% of voters) had error comparable to a genuine random sample of only **about 400** people. Data quality (representativeness) is not guaranteed by quantity.
:::
:::

:::question Q25. Interpret the three components of the decomposition $\bar X_S-\bar X_U=\rho_{R,X}\sqrt{\frac{N-n}{n}}\,\sigma_X$. What does each represent, and what does the equation reveal?
:::solution Answer
- $\rho_{R,X}$ — @@data quality@@: the correlation between being included ($R=1$) and the value $X$. Zero for a random sample; non-zero when, e.g., high earners are likelier to appear.
- $\sqrt{(N-n)/n}$ — @@data quantity@@: shrinks as $n$ grows, but only like $1/\sqrt n$ (10× more data → error ÷ $\sqrt{10}\approx3.16$), and grows with population size $N$ (Law of Large Populations).
- $\sigma_X$ — @@problem difficulty@@: the population SD; the more $X$ varies, the more a given bias translates into error. It is not the source of the bias.

**What it reveals:** ==collecting more data shrinks only the middle term; if $\rho_{R,X}\neq0$ the bias remains==. A tiny correlation times a huge $N$ can outweigh a large $n$.
:::
:::

:::question Q26. Why should subgroup analysis be guided by domain knowledge, substantive relevance, and adequate sample sizes rather than by repeatedly searching for statistically significant findings?
:::solution Answer
Because searching many arbitrary subgroups (birth month, shoe size, favourite food) ==guarantees some "significant" results by chance==, and small subgroups give @@unstable estimates@@. Subgroups chosen by @@domain knowledge@@ (age for a blood-pressure treatment, undergraduate vs postgraduate for study habits) are plausible a priori, can be @@pre-specified@@, and answer meaningful questions — including where a model performs worse. Good practice: few, justified subgroups; adequate $n$ in each; multiple-comparison adjustments when many are tested; and a clear separation of pre-specified (confirmatory) from post-hoc (exploratory) findings.
:::
:::

## Data Visualization and Responsible Statistical Graphics

:::question Q27. Why is visualization necessary even when a dataset has already been summarized using means, variances, correlations, and regression coefficients?
:::solution Answer
Because ==summaries compress information, and a compact description is not a complete one==. Very different datasets can share the same mean, variance, correlation and regression line. Visualization reveals what the numbers hide: @@non-linearity, clusters, gaps, outliers, heteroscedasticity, multimodality, temporal change, data-entry errors@@ and @@subgroup patterns@@. It is an analytical instrument for asking questions and detecting problems, not decoration — e.g. a correlation of 0.8 may come from one influential point, or $r\approx0$ may hide a strong U-shape.
:::
:::

:::question Q28. What is the central lesson of Anscombe's quartet, and how does it demonstrate the limitations of relying exclusively on numerical summaries?
:::solution Answer
Anscombe (1973) built four datasets with nearly identical @@means, variances, correlations and fitted regression lines@@, yet their scatterplots differ completely: one roughly linear with noise; one a smooth **curve**; one a tight line with **one outlier**; one a vertical cluster with **one high-leverage point** creating the whole slope. The lesson: ==identical summaries can describe totally different structures==, so numerical summaries must always be checked with an appropriate plot before interpreting or modelling.
:::
:::

:::question Q29. Explain how histograms, kernel density plots, boxplots, empirical cumulative distribution functions, and Q-Q plots provide complementary perspectives on numerical distributions.
:::solution Answer
- @@Histogram@@: overall shape, skew, modes, gaps — but depends on bins.
- @@Kernel density@@: smooth shape and modes — but depends on bandwidth; boundary bias.
- @@Boxplot@@: median, IQR, asymmetry, flagged extremes; best for comparing groups — but hides modes and gaps.
- @@ECDF@@: proportion $\le$ each value with no bins or smoothing; shows steps (repeated values), flat stretches (gaps), truncation, quantiles directly.
- @@Q–Q plot@@: departures from a reference distribution — tails, skew, mixtures, outliers.

Each one's weakness is covered by another, so ==using several reveals features any single plot could miss== (Figure 25).
:::
:::

:::question Q30. What information can be obtained from an empirical cumulative distribution function that may be difficult to identify from a histogram?
:::solution Answer
Because the ECDF ==needs no bins and no smoothing==, it shows: @@large vertical steps@@ = many identical values (Likert scales, rounding, heaping); @@long flat stretches@@ = ranges with no data (gaps); @@changes of slope@@ = mixtures or thresholds (two service regimes); @@abrupt ends or pile-ups@@ = truncation, censoring, detection limits. It also gives any quantile or "proportion below $x$" directly (e.g. proportion of patients waiting ≤ 4 h) and lets several groups be compared on one plot without binning choices.
:::
:::

:::question Q31. How can a Q-Q plot be used to identify heavy tails, light tails, skewness, heterogeneous mixtures, and unusual observations?
:::solution Answer
Plot observed quantiles against reference (usually normal) quantiles; a good match lies on a **straight line**. Then:
- @@Heavy tails@@: ends bend **away** from the line (both tails too extreme) — financial returns.
- @@Light tails@@: ends bend **towards** the line/flatten — bounded test scores.
- @@Skewness@@: a curve bending one way (convex/concave) — right-skewed concentrations.
- @@Mixtures@@: changes in slope or clusters/steps — data from different subpopulations (S-shaped residuals).
- @@Outliers@@: isolated points far from the line at the ends — e.g. defective products.
:::
:::

:::question Q32. What does heteroscedasticity mean, and how might it appear in a scatterplot?
:::solution Answer
@@Heteroscedasticity@@: the conditional variance $\operatorname{Var}(Y\mid X=x)$ ==changes with $x$== instead of being constant. In a scatterplot the vertical spread **fans out** (a funnel or cone) or narrows as $x$ increases — e.g. expenditure varies far more among high earners than low earners; industrial-area pollution varies more than residential. It matters because many methods (ordinary regression intervals and tests) assume constant variance. Remedies: transform $Y$ (log), or use methods that allow changing variance.
:::
:::

:::question Q33. What is overplotting, and how can transparency, jittering, hexagonal binning, density contours, and aggregation help address it?
:::solution Answer
@@Overplotting@@: with many observations, points overlap so heavily that density and pattern disappear (one dark blob).
- @@Transparency@@: dense regions become darker, revealing concentration.
- @@Jittering@@: small random noise separates points stacked on identical (discrete/rounded) values.
- @@Hexagonal binning@@: counts points in hexagonal cells and colours by count.
- @@Density contours@@: draw contour lines of point density.
- @@Random subsampling / aggregation@@: plot a sample, or summaries per bin.

Choice depends on whether ==individual points or overall density== is the focus.
:::
:::

:::question Q34. What is a correlation heatmap? Explain its uses and limitations when relationships are nonlinear, outliers are influential, or correlations are estimated using different effective sample sizes.
:::solution Answer
A colour-coded display of the correlation matrix $R_{jk}=\operatorname{Corr}(X_j,X_k)$. **Uses:** screening many variables for @@highly related or redundant features@@, groups of similar variables, possible @@multicollinearity@@ and unexpected associations.

**Limitations:**
- @@Non-linear@@ relationships: Pearson measures linear association, so a strong U-shape (age vs BP) can show $r\approx0$. Fix: scatterplots; Spearman for monotonic.
- @@Influential outliers@@: one \$5 M salary can create a strong-looking correlation. Fix: scatterplots, outlier checks, Spearman/biweight midcorrelation.
- @@Different effective $n$@@: with missing data, one cell may use 5,000 rows and another 2,000, displayed as if equally precise. Fix: consistent $n$ (listwise deletion or multiple imputation) and report $n$.

==A heatmap screens; it does not prove a relationship or causation.==
:::
:::

:::question Q35. What is a pair plot, and why does its usefulness diminish as the number of variables becomes large?
:::solution Answer
A matrix of plots with @@univariate distributions on the diagonal@@ and @@pairwise scatterplots off the diagonal@@, optionally coloured by class. It reveals class separation, non-linear associations, clusters, marginal differences and joint behaviour for low-to-moderate dimensions. But the number of panels grows like $p^2$ (10 variables → ~100 panels; 100 variables → ~10,000), so each panel becomes tiny and the display overwhelming; it also shows only **pairs**, not higher-order structure. Use a ==hypothesis-driven, domain-informed subset== of variables.
:::
:::

:::question Q36. Explain how chart selection, axis scaling, category ordering, color, aggregation, uncertainty display, and disclosure of exclusions contribute to responsible data visualization.
:::solution Answer
A chart is an **argument**; each design choice changes what viewers conclude.
- @@Chart selection@@: match the chart to the variable types and question (no lines joining unrelated categories; no 3-D bars).
- @@Axis scaling@@: honest, labelled axes with units; no truncated axes exaggerating differences; consistent scales across compared panels.
- @@Category ordering@@: keep natural order for ordinal categories; sort nominal ones by frequency or rate to aid comparison.
- @@Colour@@: meaningful, symmetric scales (correlations $-1$ to $1$), readable with colour-vision deficiency and in greyscale.
- @@Aggregation@@: say what was averaged; a citywide mean can hide high-exposure areas.
- @@Uncertainty@@: show intervals or $n$ when claims depend on precision.
- @@Disclosure@@: state filtering, exclusions, missing data and transformations.

==Good visualization makes evidence easier to see without misleading cues.==
:::
:::
