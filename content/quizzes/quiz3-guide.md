# Quiz 3 guide — Module 3, §3.1–3.5 (Saturday 28 November, in class)

<div class="pdf-links">
<a href="quiz3-numericals.html">★ Quiz 3 numericals</a>
<a href="pdfs/quizzes/Quiz-3-Practice-Set-shared.pdf">★ Shared practice set (PDF)</a>
<a href="m3-answers-1.html">★ Back questions Q1–36</a>
<a href="m3-answers-2.html">★ Back questions Q37–72</a>
<a href="m3-scenarios.html">★ Scenarios S1–S4 · R1–R3</a>
<a href="m3a-notes.html">M3 Notes A (§3.1–3.2)</a>
<a href="m3b-notes.html">M3 Notes B (§3.3–3.5)</a>
<a href="quiz3-mock-a.html">Mock Quiz 3A</a>
<a href="quiz3-mock-b.html">Mock Quiz 3B</a>
<a href="quiz3-mock-c.html">Mock Quiz 3C</a>
</div>

**Syllabus:** Module 3, *Exploratory Data Analysis, Feature Engineering, and Statistical Thinking*, sections **3.1 to 3.5**: what EDA is and the unit of analysis (3.1), the core goals of EDA (3.2), data visualization (3.3), descriptive statistics (3.4) and feature engineering (3.5). Sections 3.6 onwards (sampling, confidence intervals, hypothesis tests, effect sizes, pitfalls) are **not** in this quiz.

The announcement lists the question types. Every one of them is a **judgement** question: you are given a scenario, a tool or a plot, and asked to choose, criticise or interpret. Definitions alone will not earn the marks; **tool → what it reveals → what it hides → what to do next** will.

## 1. The six question types, and how to answer each

| type in the announcement | what the examiner wants | answer skeleton |
|---|---|---|
| **Which exploratory tool(s) would you prefer?** (numerical, graphical, hybrid) | the right tool for the *variable types* and the *question*, and a reason | 1. name the variable types and the question; 2. pick the tool(s) — usually a **hybrid** (plot + matching numbers); 3. say what it will reveal; 4. one caveat |
| **Advantages and limitations of a tool** | balanced pros and cons tied to the notes' lists | 2–3 things it reveals well · 2–3 things it hides or distorts · one fix for each limitation |
| **Analyse a plot/summary in a scenario** | read the evidence, then interpret it *in context* | describe (shape, centre, spread, tails, unusual points, groups) → interpret (what it means for the scenario) → caution (what it cannot tell you) |
| **Is one analysis enough? What else, and why?** | almost always **no**: name the missing checks | what the given analysis shows · what it cannot show · 2–3 named follow-ups, each with *why* |
| **Pathological visualizations** | recognise the pathology and its likely cause | name the pattern → list real vs artefact explanations → how to tell them apart → what to do |
| "Questions of this sort" | the same reasoning on new scenarios | unit of analysis, missingness, bias, subgroups, leakage are the recurring hidden traps |

:::exam The habits that earn marks
1. **Start with the unit of analysis** whenever the scenario has repeated rows (patients with many visits, customers with many transactions): "one row is a ___; the unit of prediction is a ___".
2. **Prefer hybrid answers.** A plot shows shape; numbers quantify it. "Histogram *and* median/IQR", "scatterplot *and* Spearman's $\rho$".
3. **Never conclude causation** from EDA. Name the alternatives: reverse causation, confounding, selection, chance.
4. **Never delete outliers automatically.** Flag → verify → explain → correct or retain → document.
5. **Check subgroups.** An overall pattern may weaken, strengthen or reverse within groups (Simpson's-paradox style).
6. **Fit preprocessing on training data only.** Any statistic used to transform features (mean, SD, min/max, target means, bin edges) comes from the training split.
:::

## 2. Choosing a tool: the decision table

| what you want to know | variable types | graphical | numerical | hybrid answer |
|---|---|---|---|---|
| shape of one distribution | 1 numerical | histogram (try ≥2 bin widths), density, ECDF, Q–Q plot | mean, median, SD, IQR, quantiles, skewness | histogram + median/IQR (+ mean if roughly symmetric) |
| compare a numerical variable across groups | numerical × categorical | side-by-side boxplots / violin plots, faceted histograms (common bins and axes) | group medians, IQRs, $n$ per group | boxplots with points overlaid + group $n$, medians, IQRs |
| relationship between two numerical variables | 2 numerical | scatterplot (transparency/hexbin if large $n$) | Pearson $r$ (linear), Spearman $\rho_S$ (monotonic), covariance | scatterplot **first**, then $r$ or $\rho_S$ |
| screen many numerical variables | many numerical | correlation heatmap ($-1$ to $1$ symmetric colour scale), pair plot of a chosen subset | correlation matrix | heatmap to screen → scatterplots for the striking pairs |
| behaviour over time | time-ordered | time-series line plot (raw + moving average) | rolling mean/SD, differences | raw series + smoothed line + note of missing periods |
| one categorical variable | categorical | bar chart (counts or proportions) | counts $n_k$, proportions $p_k$ | proportions bar chart + counts table |
| two categorical variables | categorical × categorical | grouped/stacked bars, mosaic plot | contingency table, row proportions | contingency table + proportion bars |
| missingness | any | missingness heatmap/bar chart | $r_j$ (per variable), $r_i$ (per record), $P(\text{missing}\mid G=g)$ | all four levels: variable, record, pattern, subgroup |
| tails and thresholds (SLAs, waiting times) | 1 numerical | ECDF, boxplot | quantiles ($Q_{0.9}$, $Q_{0.95}$) | ECDF + stated quantile method |

:::remember
Match the tool to the variable types and the question, pair every plot with the numbers that quantify it, and say what the tool cannot show.
:::

## 3. Advantages and limitations, tool by tool

| tool | reveals well | hides or distorts | fix |
|---|---|---|---|
| **Histogram** | shape, skew, modes, gaps, range, concentration | depends on bin width/boundaries: too few bins hide structure, too many create noise; outliers can compress the scale | try several bin widths; common bins and normalised proportions when comparing groups; log scale or zoom for long tails |
| **Density (KDE) plot** | smooth shape, modes | bandwidth: over-smoothing erases peaks, under-smoothing invents them; boundary bias (mass outside $[0,1]$ or below 0) | vary bandwidth; boundary-aware KDE; show with raw data/rug |
| **Boxplot** | median, IQR, asymmetry, extreme points; **comparing many groups** | multimodality, gaps, clusters, small-$n$ behaviour, detailed shape; "outliers" beyond $1.5\times$IQR are not errors | overlay points, add violin/density, report $n$ |
| **ECDF** | no bins or smoothing; steps (repeated values), flat stretches (gaps), truncation, censoring, mixtures; quantiles read directly | less intuitive to read than a histogram | pair with a histogram |
| **Q–Q plot** | departures from a reference (normal): heavy/light tails, skew, mixtures, outliers | only compares with one reference distribution; needs care with small $n$ | add a histogram; try a transformation and re-check |
| **Scatterplot** | direction, strength, form (linear/curved), clusters, outliers, influential points, heteroscedasticity (funnel), subgroups | overplotting with large $n$; too many encodings (colour, size, shape) clutter it; shows association, not cause | transparency, jitter, hexbin, density contours, subsampling; facet by group |
| **Correlation heatmap** | many pairwise linear associations at once; redundancy, multicollinearity, blocks of related variables | non-linear relations (U-shape gives $r\approx0$), outliers, ordinal codes treated as numbers, different $n$ per pair from missing data, time trends, thousands of pairs → chance findings, misleading colour scales, causation | scatterplots for key pairs; Spearman; consistent $n$; detrend; multiple-comparison correction; symmetric $-1$…$1$ scale |
| **Pair plot** | all pairwise scatterplots + marginals; class separation, clusters, non-linearity | grows as $p^2$ panels: unreadable beyond ~8–10 variables | hypothesis-driven subset of variables |
| **Time-series plot** | trend, seasonality, cycles, abrupt changes, regime shifts, missing periods, drift, changing variance | smoothing hides short events; lines imply continuity (do not connect unrelated points); observations are not independent | show raw and smoothed; mark gaps; use only past data for features |
| **Bar chart / categorical summaries** | counts and proportions per category | counts mislead when group sizes differ; arbitrary category order hides patterns | proportions for unequal groups; keep ordinal order; sort nominal by frequency or rate |
| **Mean** | uses every value; efficient for symmetric data | pulled by outliers and skew ($\{2,3,3,4,100\}$: mean $22.4$) | report with the median |
| **Median** | resistant to extremes; the "typical" value for skewed data | ignores the size of extremes | report with mean, quantiles |
| **SD / variance** | spread in original (SD) or squared (variance) units | squared deviations → very sensitive to outliers | IQR, MAD |
| **Quantiles** | position, tails, thresholds; no distributional assumption | small-$n$ values depend on the software's interpolation rule | state the method (e.g. NumPy Type 7 vs Excel Type 6) |
| **Skewness** $\gamma_1$ | direction and degree of asymmetry | itself very sensitive to extreme values; $\gamma_1\approx0$ is not normality | read with the plot |
| **Covariance** | direction of co-movement | unit-dependent, so magnitudes are not comparable | use correlation |
| **Pearson $r$** | strength of **linear** association, unit-free, in $[-1,1]$ | $r=0$ ≠ no relation ($Y=X^2$); outliers, restricted range, mixed groups, trends, selection | scatterplot; Spearman for monotonic/ordinal |

## 4. "Is this analysis enough?" — the checklist

When a scenario offers **one** histogram, scatterplot, correlation or mean, ask:

1. **Unit of analysis.** Are rows independent? (images per patient, transactions per customer, days per counter)
2. **Missingness.** How much, where, which variables together, which subgroups? Who is missing the data?
3. **Subgroups.** Does the pattern hold within age groups, sites, devices, time periods? Could it reverse?
4. **Outliers / anomalies.** Investigate before removing; check if one point drives a correlation.
5. **Form of the relationship.** Linear or not? (Scatterplot before $r$.) Heteroscedastic?
6. **Time.** Trends, seasonality, drift, leakage from future data.
7. **Bias.** Sampling, measurement, label, survivorship, selection, historical.
8. **Exploration vs confirmation.** A pattern found here is a hypothesis; confirm on new data, a held-out split, or a pre-registered analysis.
9. **Causation.** Association only — confounding, reverse causation, selection, chance.

:::warn
"No — I would also do X" without **why** earns little. Every follow-up needs its reason: "…because the overall correlation could be driven by the difference between age groups (confounding)".
:::

## 5. Pathological visualizations — a diagnosis table

:::figs
m3-p021|Figure 26 — Pathological distributions
m3-p022|Figure 27 — Pathological histograms
:::

| you see | genuine explanation | artefact explanation | what to do |
|---|---|---|---|
| long right tail (histogram, boxplot with many upper points) | skewed process: income, costs, waiting times, length of stay | a few data-entry errors (extra zeros), unit mix-ups | median/IQR; log$(1+x)$; check the extreme records |
| two or more peaks | a mixture of subpopulations (sites, scanners, disease types, demographics) | bin choice creating false peaks; KDE bandwidth too small | stratify by the suspected group; vary bins/bandwidth |
| tall spike at zero | zero-inflation: many people with no visits/claims | missing values coded as 0 | separate "zero" from "missing"; model zeros separately |
| spikes at round numbers (multiples of 5 or 10, 9.99) | pricing conventions | heaping from self-report, rounding, digit preference | treat as measurement resolution; avoid over-reading peaks |
| sharp cut-off / pile-up at a limit | natural bound (0, 100%) | censoring/detection limits, truncation at a study end | record the limit; methods for censored data |
| gaps | genuinely impossible values | device range, downtime, recording rules | check the measurement process and timeline |
| histogram compressed into one bar | heavy tail | a single huge value dominating the axis | zoom, log scale, inspect that value |
| many boxplot "outliers" | skewed/heavy-tailed data (legitimate) | errors | investigate; do not delete automatically |
| step-like ECDF | discrete scale (Likert 1–5), rounding | — | treat as ordinal/discrete |
| Q–Q points bending away at both ends | heavy tails (finance returns) | outliers | robust methods; check extremes |
| Q–Q curved one way / S-shape | skewness / mixture of groups | — | transform; stratify |
| scatterplot funnel | heteroscedasticity: spread grows with $X$ | — | transform; methods without constant-variance assumption |
| strong $r$ driven by one point | — | one influential observation | Spearman/robust correlation; refit without it and compare |
| near-zero $r$ but clear U-shape | non-linear relationship | — | scatterplot; non-linear features |
| correlation from two separate clusters | relationship between groups, not within | — | colour by group; analyse within groups |

:::remember
For any odd-looking plot: name the pattern, give a genuine and an artefact explanation, say how you would tell them apart, and what you would do next — without deleting data automatically.
:::

## 6. Numbers you should be able to compute

- **Mean, median, effect of an outlier:** $\{2,3,3,4,100\}$ → mean $22.4$, median $3$.
- **IQR and boxplot fences:** $\text{IQR}=Q_3-Q_1$; fences $Q_1-1.5\,\text{IQR}$ and $Q_3+1.5\,\text{IQR}$.
- **MAD:** $\operatorname{median}(|x_i-\operatorname{median}(x)|)$.
- **Sample variance:** $s^2=\frac1{n-1}\sum(x_i-\bar x)^2$; SD $=s$.
- **Weighted mean:** $\bar x_w=\sum w_ix_i/\sum w_i$.
- **Covariance, Pearson $r$** (unit-free, $[-1,1]$), **Spearman** $\rho_S=1-\dfrac{6\sum d_i^2}{n(n^2-1)}$ (no ties).
- **Missingness rates:** $r_j$ per variable, $r_i$ per record, $P(\text{missing}\mid G=g)$.
- **Standardisation** $z=(x-\mu_{\text{train}})/\sigma_{\text{train}}$, **min–max** $(x-x_{\min})/(x_{\max}-x_{\min})$, **robust** $(x-\text{median})/\text{IQR}$.
- **Target encoding with smoothing:** $\dfrac{n_c\bar y_c+\lambda\bar y}{n_c+\lambda}$ (notes: $n_c=1$, $\bar y_c=1$, $\bar y=0.5$, $\lambda=10$ → $\frac{1+5}{11}=0.545$; !!the notes print 0.455, an arithmetic slip!!).
- **Cyclical encoding:** $\big(\sin\frac{2\pi x}{P},\cos\frac{2\pi x}{P}\big)$ with $P=24,7,12$.
- **Big Data paradox:** error $=\rho_{R,X}\sqrt{(N-n)/n}\;\sigma_X$ — a 10× bigger biased sample only shrinks the error by $\sqrt{10}\approx3.16$.
- **Quantile conventions (notes Q42):** latencies $[120,135,142,150,165]$, SLA $Q_{0.8}\le155$. Type 7: position $1+4(0.8)=4.2$ → $153$ ms (pass). Type 6: position $6(0.8)=4.8$ → $162$ ms (fail).
- **Missingness rate (notes Q19):** income missing for 450 of 2,000 patients → $r_j=0.225$; to see whether it is concentrated in groups you need $P(\text{missing}\mid G=g)$ by age, insurance, site, etc.

## 7. The notes' back questions — answered

The end of the Module 3 notes (PDF pp. 203–221) has 100 practice questions, five scenarios and five reflections. For Quiz 3 (§3.1–3.5) the relevant ones are **Q1–Q72**, **S1–S4**, and the EDA and feature-engineering parts of **R1–R3**; Q73–Q100, S5, R4 and R5 are mainly about sampling, confidence intervals and hypothesis tests (§3.6 onwards).

- **[Answers Q1–36](m3-answers-1.html)** — EDA foundations, distributions and anomalies, missingness and bias, visualization.
- **[Answers Q37–72](m3-answers-2.html)** — descriptive statistics, correlation and causation, feature engineering.
- **[Scenarios S1–S4 and Reflections R1–R3](m3-scenarios.html)** — the closest match to the announced question types.
- **[Quiz 3 numericals](quiz3-numericals.html)** — every calculation in §3.1–3.5, worked, plus practice.

## 8. Shared practice set (PDF)

**[Quiz 3 EDA practice set with model answers](pdfs/quizzes/Quiz-3-Practice-Set-shared.pdf)** (28 pages) — 40 exam-style questions with model answers and drawn plots to analyse, grouped by the announced question types. Shared by a classmate; **not official course material**. One correction: in Q21, income is missing for **23.5%** overall, not 22% ((480 + 900 + 1,440) / 12,000). Its strength is the plots: use Q15–Q21 and Q29–Q35 to practise reading a given plot and diagnosing odd-looking visualizations.
