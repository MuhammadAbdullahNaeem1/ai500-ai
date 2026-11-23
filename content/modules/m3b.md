# M3 · Notes B — Visualization, descriptive statistics, feature engineering (§3.3–3.5)

Module 3 notes, pp. 366–435 (PDF pages 56–125) · **Quiz 3 syllabus** (with Notes A)

<div class="pdf-links">
<a href="pdfs/notes/Module-3-Notes.pdf">Module 3 notes (PDF)</a>
<a href="quiz3-guide.html">Quiz 3 guide</a>
<a href="assignments.html#computational-training-module-2-in-code">Code: computational scripts 15–25</a>
</div>

In order, this page covers: why numbers alone are not enough (Anscombe's quartet) and how to choose a chart (3.3.1); the plot types — histograms, boxplots, scatterplots, correlation heatmaps, pair plots, time-series plots and categorical summaries — each with what it reveals, its limitations and its fixes (3.3.2–3.3.8); responsible visualization (3.3.9); descriptive statistics from the mean to Spearman correlation (3.4); and feature engineering, from the "fit on training data only" rule to scaling, binning, encoding, interactions, polynomial, time-window and cyclical features and their risks (3.5).

## 3.3.1 Why visualizations are necessary

Summary statistics **compress** data, and compression can hide non-linearity, clusters, gaps, outliers, heteroscedasticity, multimodality, temporal change, data-entry errors and subgroup patterns. Visualization is an **analytical instrument** for asking questions, not just decoration for results.

:::figs
m3-p057|Figure 34 — Anscombe's quartet: identical summaries, different structures
:::

**Anscombe's quartet** (1973): four datasets with nearly identical means, variances, correlations and fitted regression lines, yet completely different plots — one linear, one curved, one a line with a single outlier, one vertical cluster with one high-leverage point. Lesson: never rely on numerical summaries alone.

**Choosing a chart** starts with a **question**, not a chart type. The choice depends on the **variable types**, the **analytical goal**, the **sample size**, the **number of groups**, whether there is a **meaningful order** (time), and the **audience**. The aim is not many charts, but the ones that make relevant structure visible.

:::remember
Numbers compress and can hide structure (Anscombe); pick the chart from the question and the variable types.
:::

## 3.3.2 Histograms

:::figs
m3-p059|Figure 35 — Histogram shapes
:::

A histogram splits a numerical variable's range into bins $B_k$ and shows the count $h_k=\#\{x_i:x_i\in B_k\}$ (or proportion) in each. It reveals **symmetry/skewness, modality, gaps, extremes, range** and where values concentrate.

**Bin choice matters.** Too few bins hide structure (over-smoothing); too many make noise look like signal. Try **several reasonable bin widths** and keep only features that survive. Best for continuous variables and counts with many distinct values, in moderate-to-large samples. **Comparing groups:** use common bin boundaries, common axes, normalised proportions when group sizes differ, and separate (faceted) panels when overlapping bars get confusing.

:::remember
Histogram = shape at a glance, but its picture depends on bins: check more than one bin width, and compare groups on common bins and axes.
:::

## 3.3.3 Boxplots

:::figs
m3-p061|Figure 36 — Boxplots as compact summaries
:::

A boxplot shows the **median**, **$Q_1$**, **$Q_3$**, the **IQR** $=Q_3-Q_1$, **whiskers**, and points beyond the whiskers. Conventional fences:
$$
\big[\,Q_1-1.5\times\text{IQR},\ \ Q_3+1.5\times\text{IQR}\,\big],
$$
with whiskers reaching the most extreme observations inside the fences. *(The notes print the upper fence as $Q_1+1.5\,\text{IQR}$; the standard rule, and the notes' own footnote 281, use $Q_3$.)*

:::warn
Points beyond the whiskers are **not automatically errors** — just observations past a conventional line. Retain, investigate, transform or remove depending on context and provenance.
:::

| strengths | limitations |
|---|---|
| comparing **many groups** on centre, spread, asymmetry and extremes | hides **multimodality, gaps, clusters, small-sample behaviour** and detailed shape |

Fix: overlay the individual points, or pair with a **violin plot** (box + density, Hintze & Nelson 1998).

:::remember
Boxplot: median, IQR, fences at $1.5\times$IQR; great for comparing groups, blind to modes and gaps; outliers are prompts to investigate.
:::

## 3.3.4 Scatterplots

:::figs
m3-p063|Figure 37 — Scatterplots
:::

A scatterplot of pairs $(x_i,y_i)$ shows the **direction**, apparent **strength** and **form** (linear or not) of a relationship, plus **clusters, outliers, influential points, changing variance** and **subgroup structure**. Look at it **before** trusting a correlation coefficient or fitted line.

- **Heteroscedasticity:** $\operatorname{Var}(Y\mid X=x)$ changes with $x$ — a **funnel** shape. Matters because many methods assume constant variance.
- **Overplotting:** with many points, marks overlap and hide the pattern. Fixes: **transparency, jittering, hexagonal binning, density contours, random subsampling, aggregation** — depending on whether individual points or overall density matter.
- **Extra variables** via colour, marker shape, size or faceting reveal subgroups — but too many encodings make the plot harder to read.

:::remember
Scatterplot first, statistic second: it shows form, clusters, outliers and funnels; use transparency/hexbin against overplotting.
:::

## 3.3.5 Correlation heatmaps

:::figs
m3-p065|Figure 38 — Correlation heatmaps
:::

A heatmap colours the correlation matrix $R_{jk}=\operatorname{Corr}(X_j,X_k)$. **Uses:** highly related features, groups of variables behaving alike, possible **multicollinearity**, **redundant** measurements, unexpected associations — a **screening** tool for a moderate number of numerical variables.

:::figs
m3-p071|Figure 39 — Instructive limitations of correlation heatmaps
:::

| limitation | notes' example | consequence | fix |
|---|---|---|---|
| **non-linear relationship** | U-shaped age vs blood pressure | $r\approx0$ though strongly related | scatterplot; Spearman for monotonic relations |
| **outliers** | one \$5 M executive among \$30–100 k salaries | correlation driven by one point | scatterplot, outlier checks; Spearman or biweight midcorrelation |
| **categorical treated as numerical** | education coded 1–4 | implies equal gaps between levels | Spearman for ordinal; polychoric correlation |
| **different $n$ per pair** (missing data) | age–education on 5,000 rows, income–health on 2,000 | cells shown together with very different precision | listwise deletion or multiple imputation for a consistent $n$ |
| **temporal dependence** | daily ad spend vs daily sales over 2 years | shared trend/seasonality inflates $r$ | detrend (use changes, $\Delta X_t=X_t-X_{t-1}$), cross-correlation |
| **too many correlations** | 100 variables → 4,950 pairs | some strong values by pure chance | Bonferroni or FDR corrections; validate |
| **misleading colour scale** | narrow scale makes 0.05 vs 0.15 look dramatic | over-interpretation | symmetric scale from $-1$ to $1$ |
| **causation** | ice-cream sales vs drownings | both driven by hot weather | experiments (A/B tests), causal methods (DAGs, instrumental variables) |

:::remember
A correlation heatmap is a screening tool for linear association — confirm striking cells with scatterplots, robust/rank correlations and a sensible colour scale.
:::

## 3.3.6 Pair plots

:::figs
m3-p072|Figure 40 — Pair plots
:::

A pair plot puts **univariate distributions on the diagonal** and **scatterplots off the diagonal**, optionally coloured by group/class. Useful for low-to-moderate dimensions: **class separation, non-linear associations, clusters, comparing marginals, joint behaviour**. But panels grow like $p^2$ (10 variables → ~100 panels), so choose a **hypothesis-driven, domain-informed subset** rather than plotting hundreds of features.

## 3.3.7 Time-series plots

:::figs
m3-p074|Figure 41 — Time-series plots
:::

A time-series plot keeps the order $(t_i,x_i)$ and can show **trend, seasonality, cycles, abrupt changes, regime shifts, missing periods, anomalies, changing variability** and **sensor drift**. Observations close in time are usually **not independent**.

- **Raw + smoothed:** overlay a moving average $\text{MA}_t=\frac1w\sum_{j=0}^{w-1}x_{t-j}$ — but smoothing can hide short events, abrupt changes and local anomalies, so keep the raw series.
- **Don't connect unrelated observations:** a line implies continuity and order.
- **Temporal leakage:** prediction features may only use the past, $\text{Feature}_t=g(x_{t-1},x_{t-2},\dots)$. A **centred** rolling average (which uses future values) is fine for describing the past but leaks for prediction.

## 3.3.8 Categorical summaries

:::figs
m3-p075|Figure 42 — Categorical summaries
:::

For a categorical $C$: counts $n_k=\#\{i:C_i=k\}$ and proportions $p_k=n_k/n$, shown as count/proportion plots, grouped or stacked bars, mosaic plots or contingency tables. **Counts** answer "how many?", **proportions** "what fraction?" — prefer proportions when groups differ in size. **Order:** keep the natural order of ordinal categories; for nominal ones sort by frequency, outcome rate or domain importance to make comparison easy.

## 3.3.9 Principles of responsible visualization

:::figs
m3-p077|Figure 43 — Responsible visualization (air-quality example)
:::

A chart is an **argument**: scales, axes, colours, aggregation, filtering and annotation steer what viewers see. A responsible visualization:

- uses a chart type that fits the variables and the question;
- labels axes, units and categories; states $n$ when it matters;
- avoids misleading or distorted scales;
- shows **uncertainty** when the claim depends on it;
- discloses filtering, exclusions, transformations and aggregation;
- distinguishes raw data from fitted trends/model output;
- uses **consistent scales** for intended comparisons;
- avoids 3-D and decorative distortion;
- stays readable for colour-vision limitations and in greyscale.

:::remember
Each plot type has a job and blind spots; responsible charts are honest about scales, $n$, uncertainty and what was filtered.
:::

## 3.4 Descriptive statistics

Numbers that quantify location, spread, relative position, asymmetry and association — complements to plots, never interpreted in isolation.

### 3.4.1–3.4.4 Mean, weighted mean, median

- **Mean** $\bar x=\frac1n\sum x_i$: uses every value, so it is pulled by extremes. $\{2,3,3,4,100\}$: $\bar x=22.4$, although four of five values lie between 2 and 4.
- **Weighted mean** $\bar x_w=\sum w_ix_i/\sum w_i$: when observations count unequally — survey weights, class weights, exposure durations, combining groups with different representation. Document what the weights mean.
- **Median** $\tilde x$: the middle ordered value ($x_{((n+1)/2)}$ for odd $n$; average of the two middle values for even $n$). Resistant: the median of $\{2,3,3,4,100\}$ is $3$, unchanged by the 100.
- **Mean vs median:** a big gap signals **skewness, extremes, mixtures or data problems**. Mean for roughly symmetric data without heavy outliers; median for skewed data; reporting **both** is often most informative (household income: mean ≫ median).

:::figs
m3-p080|Figure 44 — Mean vs median for household income
:::

### 3.4.5 Variance and standard deviation

$$
s^2=\frac{1}{n-1}\sum_{i=1}^n(x_i-\bar x)^2,\qquad s=\sqrt{s^2}.
$$
Dividing by $n-1$ makes $s^2$ an **unbiased** estimator of the population variance ($\mathbb E[s^2]=\sigma^2$ for independent samples). Variance is in **squared units**; the SD is in the original units and easier to read. Both are **sensitive to outliers** (squared deviations). **Robust** alternatives: $\text{IQR}=Q_{0.75}-Q_{0.25}$ (spread of the middle 50%) and $\text{MAD}=\operatorname{median}(|x_i-\operatorname{median}(x)|)$.

:::figs
m3-p082|Figure 45 — Classical vs robust spread for salaries
:::

### 3.4.6 Quantiles

The $q$-quantile $Q_q$ has about a fraction $q$ of observations below it: $Q_{0.25}$ (first quartile), $Q_{0.5}$ (median), $Q_{0.75}$, $Q_{0.90}$, $Q_{0.95}$. **Percentiles** are quantiles on a 0–100 scale; **quartiles** are the 25th/50th/75th. Quantiles need no distributional assumption and serve skewed data, operational/clinical thresholds, service levels, tails, screening extremes and group comparisons.

**Estimation conventions differ** between software, which matters for small $n$:

:::example The 80th-percentile SLA (Example 91)
Latencies $[120,135,142,150,165]$ ms; the SLA requires $Q_{0.8}\le155$.
- **Type 7** (NumPy default): position $1+(n-1)p=1+4(0.8)=4.2$ → $150+0.2(165-150)=153$ ms → **passes**.
- **Type 6** (Excel PERCENTILE.EXC, R type 6): position $(n+1)p=6(0.8)=4.8$ → $150+0.8(15)=162$ ms → **fails**.

Same data, opposite verdicts — a 9 ms difference from software defaults alone. Flag quantiles from small samples ($n<30$), and **state the method** in reports and contracts.
:::

:::figs
m3-p084|Figure 46 — Quantiles for emergency-department waiting times
:::

### 3.4.7 Skewness

$$
\gamma_1=\frac{\mathbb E[(X-\mu)^3]}{\sigma^3}:\qquad \gamma_1>0\ \text{long right tail},\quad \gamma_1<0\ \text{long left tail},\quad \gamma_1\approx0\ \text{roughly symmetric (not necessarily normal)}.
$$
Right-skewed examples: income, waiting times, transaction amounts, healthcare costs, follower counts. The statistic itself is **sensitive to extremes** — read it with a histogram or boxplot. A **log transform** $x'=\log(1+x)$ reduces right skew for non-negative variables (house prices), but only if the transformed scale still makes sense for the task.

:::figs
m3-p087|Figure 47 — Right-skewed healthcare costs
m3-p088|Figure 48 — Log-transforming house prices
:::

### 3.4.8–3.4.9 Covariance and correlation

$$
s_{XY}=\frac1{n-1}\sum(x_i-\bar x)(y_i-\bar y),\qquad
r_{XY}=\frac{s_{XY}}{s_Xs_Y}=\frac{\sum(x_i-\bar x)(y_i-\bar y)}{\sqrt{\sum(x_i-\bar x)^2}\sqrt{\sum(y_i-\bar y)^2}}\in[-1,1].
$$

- **Covariance:** sign gives the direction of co-movement; its units are the product of the two variables' units, so magnitudes are **not comparable** across pairs (and change when you rescale).
- **Pearson $r$:** unit-free strength of **linear** association. $r=\pm1$ perfect linear; $r=0$ means **no linear** association — not no relationship: $Y=X^2$ with $X$ symmetric about 0 gives $r=0$.
- **Pearson is affected by** outliers, restricted ranges, mixtures of groups, non-linearity, selection effects and temporal trends; a common trend can make two unrelated series correlate.
- **Spearman** $\rho_S=\operatorname{Corr}(\operatorname{rank}X,\operatorname{rank}Y)$, $=1-\dfrac{6\sum d_i^2}{n(n^2-1)}$ without ties: measures **monotonic** association; suits ordinal data and non-linear monotonic relations, and is less (not totally) sensitive to outliers.
- Neither establishes causation.

:::figs
m3-p089|Figure 49 — The covariance matrix in a portfolio
m3-p092|Figure 50 — Correlation and its limits (cardiovascular health)
:::

:::remember
Report centre with mean *and* median, spread with SD *and* IQR/MAD, tails with quantiles (state the method), association with a scatterplot plus Pearson or Spearman — and none of it proves cause.
:::

## 3.5.1 What is feature engineering?

**Feature engineering** turns raw inputs into representations that make relevant structure easier for a model to use: $\phi(x_{\text{raw}})=x_{\text{model}}$, through scaling, encoding, aggregation, transformation, selection or new variables. It can improve numerical stability, encode domain knowledge, express non-linearity, represent history, reduce dimension, encode categories, and improve interpretability. Examples: timestamp → hour/day-of-week/time since last event; date of birth → age at observation; transactions → recent frequency. It usually **re-represents** information rather than adding new information, and is part of the modelling process (Kuhn & Johnson).

## 3.5.2 Feature engineering must occur inside the modelling pipeline

:::def The training-only rule
Any transformation whose parameters $\psi$ are learned from data is fitted on the **training** data only, $\hat\psi=\text{Fit}(X_{\text{train}})$, then applied unchanged to every split:
$$
X'_{\text{train}}=T(X_{\text{train}};\hat\psi),\qquad X'_{\text{val}}=T(X_{\text{val}};\hat\psi),\qquad X'_{\text{test}}=T(X_{\text{test}};\hat\psi).
$$
:::

This covers scaling, imputation, categorical and **target** encoding, feature selection, dimensionality reduction, vocabulary building and any data-driven transform. Standardising with the mean and SD of the **whole** dataset before splitting lets test data shape the features, so evaluation is **optimistically biased**. Safest: put all data-dependent preprocessing **inside the pipeline** so each fit (including each CV fold) learns its own parameters.

## 3.5.3–3.5.4 Scaling, standardization and normalization

| transform | formula | use | caution |
|---|---|---|---|
| **standardization** (z-score, mean–variance normalization) | $z=\dfrac{x-\mu_{\text{train}}}{\sigma_{\text{train}}}$ | logistic regression, SVMs, neural nets, PCA, kNN, regularised regression, gradient methods | sensitive to outliers |
| **robust scaling** | $\dfrac{x-\operatorname{median}(x)}{\text{IQR}(x)}$ | data with extreme values | — |
| **min–max** | $\dfrac{x-x_{\min}}{x_{\max}-x_{\min}}\in[0,1]$ | bounded inputs | one extreme value sets the range and squashes the rest; fit min/max on training data |
| **unit-vector** | $x/\|x\|_2$ | when direction matters: documents, embeddings, cosine similarity | $x\neq0$ |
| **distributional** | $\log(1+x)$, $\sqrt x$ | reduce skew, stabilise variance, linearise | changes interpretation (log → relative changes) |

**Why scale?** Income (0 to $10^7$) next to a debt ratio (0 to 1) dominates any distance just because of its units; ridge/lasso penalties also only make sense on comparable scales. **Tree-based models** split on thresholds and are much less scale-sensitive. "Normalization" means different things in different fields — say exactly which operation.

:::example Choosing transformations (Example 96)
Log-income (skewed, but now not in dollars — explain it); $\log(1+\text{length of stay})$ (handles zeros, helps constant-variance models); log–log website visits vs sales (now linear, coefficients read as percentage changes); age$^2$/splines/age bands for mortality risk (non-linear effect); fraud model trained on log(amount) but fed raw amounts in production (**train–serving inconsistency**); a transform that lifts accuracy from 82% to 84% but can't be explained or reproduced (not worth it).
:::

## 3.5.5 Binning

Binning maps a continuous $x$ to intervals via thresholds $c_1<\dots<c_{K-1}$. Types: **equal-width**, **equal-frequency (quantile)**, **domain-defined**, **supervised** (outcome-based).

| benefits | risks |
|---|---|
| captures thresholds; less sensitive to tiny measurement noise; interpretable and easy to communicate; lets simple models capture some non-linearity | discards information; artificial jumps at cut-points; unstable predictions near boundaries; hides variation within bins; **target leakage** if outcome-based cut-points use evaluation data |

Prefer **domain thresholds** (AQI bands, clinical blood-pressure categories); fit data-driven or supervised bins inside training only.

:::figs
m3-p101|Figure 51 — Binning AQI into risk categories
m3-p102|Figure 52 — Risks of binning blood pressure
:::

## 3.5.6 Encoding categorical variables

- **Ordinal encoding** (low = 1, medium = 2, high = 3) — only for genuinely ordered categories; on nominal ones (colours, countries) it invents an order.
- **One-hot encoding** $x_{ik}=\mathbf 1\{C_i=k\}$ — simple and safe, but **high cardinality** (40,000 US ZIP codes) gives huge sparse matrices and overfitting. With an intercept, **drop one category** (the reference) to avoid perfect collinearity: for {Male, Female, Other}, $y=\beta_0+\beta_1\text{Male}+\beta_2\text{Female}$, so $\beta_0$ is Other's level and $\beta_1,\beta_2$ are differences from Other.
- **Frequency encoding** $f_k=n_k/n$ — one compact column for high cardinality (cities: LHR 0.4, KHI 0.3, ISL 0.2, PEW 0.1), but categories with equal frequencies become indistinguishable even if they behave very differently.
- **Target encoding** $\hat\mu_k=\mathbb E[Y\mid C=k]$ — powerful for high cardinality, but **leaks the target**: a row's own outcome feeds its own feature; a category with one row (a lone Engineer who defaulted) is encoded as exactly its label, 1.00. Remedies: **out-of-fold / cross-fitting** (encode each fold with the other folds' targets), **smoothing** towards the global mean
$$
\text{TE}(c)=\frac{n_c\bar y_c+\lambda\bar y}{n_c+\lambda}\quad\Big(\text{lone Engineer: }\frac{1(1)+10(0.5)}{11}=0.455\Big),
$$
and an explicit rule (global mean) for categories unseen in training.
- **Rare and unseen categories** — merge rare levels into "Other"; **hashing** into a fixed number of buckets; **hierarchical grouping** (employer → industry → sector); **learned embeddings** (neural nets); an explicit **unknown** category or global default at deployment. A *rare* category has little data; an *unseen* one has none.

## 3.5.7–3.5.8 Interaction and polynomial features

**Interaction:** the effect of one variable depends on another,
$$
\hat y=\beta_0+\beta_1x_1+\beta_2x_2+\beta_3x_1x_2,\qquad \frac{\partial\hat y}{\partial x_1}=\beta_1+\beta_3x_2 .
$$
Examples: a drug's effect depending on age, rainfall × soil type, income × household size for expenditure. They add domain knowledge but also complexity — justify and validate them.

**Polynomial features** $x,x^2,\dots,x^d$ (and $x_1^2,x_2^2,x_1x_2$ for two inputs) let linear models fit curves; low degrees stay interpretable. **Risks:** feature count explodes, multicollinearity, scale sensitivity, wild behaviour outside the training range, overfitting at high degree — use scaling, regularisation and cross-validation.

:::figs
m3-p115|Figure 53 — Income × household size interaction
m3-p117|Figure 55 — Risks of polynomial expansion
:::

## 3.5.9 Time-window features

| feature | formula |
|---|---|
| lag | $L_k(t)=x_{t-k}$ |
| rolling mean | $M_w(t)=\frac1w\sum_{j=1}^wx_{t-j}$ |
| rolling SD | $S_w(t)=\sqrt{\frac{1}{w-1}\sum_{j=1}^w(x_{t-j}-M_w(t))^2}$ |
| difference / % change | $\Delta x_t=x_t-x_{t-1}$, $\ r_t=(x_t-x_{t-1})/x_{t-1}$ |
| event count | $C_w(t)=\sum_{j=1}^w\mathbf 1\{\text{event at }t-j\}$ |
| time since event | $t-t_{\text{last event}}$ |

**Calendar features:** hour, day of week, month, holiday flag, season, working-day flag (e.g. Saturday 15 August, 7 PM → hour 19, day 5 with Monday = 0, month 8, holiday 0, season 2, working day 0). **Every feature must use only information available before the prediction time** — note that all the windows above start at $t-1$. Centred windows leak the future; use chronological splits and document feature timestamps.

:::figs
m3-p118|Figure 56 — Time-window features for fraud detection
m3-p120|Figure 57 — Temporal availability and leakage
:::

## 3.5.10 Cyclical feature encoding

Hour 23 and hour 0 are neighbours, but as integers they are 23 apart. Encode a cyclical variable with period $P$ as two features:
$$
x_{\sin}=\sin\frac{2\pi x}{P},\qquad x_{\cos}=\cos\frac{2\pi x}{P}\qquad(P=24\ \text{hours},\ 7\ \text{days},\ 12\ \text{months}),
$$
which places the values on a circle, so the end and start of the cycle are close (electricity demand by hour, restaurant demand by weekday). The same sine/cosine idea gives **positional encodings** in Transformers, letting them tell "the cat chased the mouse" from "the mouse chased the cat".

:::figs
m3-p122|Figure 58 — Cyclical encoding on the unit circle
:::

## 3.5.11 Feature-engineering risks

:::figs
m3-p124|Figure 59 — Eight major risks in feature engineering
:::

The eight risks: **target leakage**, **temporal leakage**, **identity leakage**, **proxy discrimination** (ZIP code standing in for race or income in lending), **unstable high-cardinality features** (customer ID memorised, useless for new customers), **train–serving inconsistency**, **excessive dimensionality**, and **spurious interactions**. Every engineered feature should be specified by its definition, unit, source variables, computation window, availability time, missing-value rule, version, and justification. Judge a feature not only by validation score but by whether it is valid, reproducible, interpretable where needed, **available at prediction time**, and robust in deployment.

:::remember
Fit every data-driven transform on training data only, choose scaling/encoding to fit the model and variable, use only past information in time features, and watch for leakage, proxies and high-cardinality traps.
:::
