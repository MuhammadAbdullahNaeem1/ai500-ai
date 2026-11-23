# M3 · Back questions Q37–72 (Quiz 3)

Answers to the end-of-module practice questions in the Module 3 notes (PDF pp. 205–208), sections **3.4–3.5**. Each is sized for a **3–4 mark** quiz part. Numerical questions are worked in full on the [numericals page](quiz3-numericals.html).

<div class="pdf-links">
<a href="m3-answers-1.html">Answers Q1–36</a>
<a href="m3-scenarios.html">Scenarios S1–S4 · Reflections R1–R3</a>
<a href="quiz3-numericals.html">Quiz 3 numericals</a>
<a href="pdfs/notes/Module-3-Notes.pdf#page=205">Questions in the PDF (p.205)</a>
</div>

<div class="hl-legend">
<span><mark class="hl">Yellow</mark> the one line to remember</span>
<span><span class="key">Blue</span> keywords a rubric looks for</span>
<span><mark class="trap">Coral</mark> a common trap</span>
</div>

## Descriptive Statistics and Distributional Summaries

:::question Q37. Define the arithmetic mean, weighted mean, and median. Under what distributional characteristics might each provide a useful summary?
:::solution Answer
- @@Mean@@ $\bar x=\frac1n\sum x_i$ — uses every value; efficient for ==roughly symmetric data without strong outliers==; pulled by extremes.
- @@Weighted mean@@ $\bar x_w=\sum w_ix_i/\sum w_i$ — when observations count unequally: survey weights, class weights, exposure durations, combining groups of different sizes. Its meaning depends on what the weights represent, so document them.
- @@Median@@ — middle ordered value; resistant to extremes; best for **skewed** data or data with influential outliers (income, waiting times, costs).

Neither is universally better; reporting mean **and** median shows skew through their gap.
:::
:::

:::question Q38. Consider the observations {2, 3, 3, 4, 100}. Calculate the mean and median. Explain why the two statistics provide substantially different descriptions of the same dataset.
:::solution Answer
Mean $=112/5=$ **22.4**; median $=$ **3**. The mean incorporates the single extreme value 100, which pulls it far above the four values between 2 and 4 — so 22.4 describes none of the observations. The median depends only on the middle position and is ==resistant to the extreme value==. The large gap signals @@right skew@@ or an @@extreme observation@@ (possibly an error) that should be investigated; here the median better represents the typical value.
:::
:::

:::question Q39. Define sample variance and sample standard deviation. Why is the denominator $(n-1)$ conventionally used when estimating population variance from independent sample observations?
:::solution Answer
$s^2=\dfrac{1}{n-1}\sum(x_i-\bar x)^2$ and $s=\sqrt{s^2}$ (same units as the data; variance is in squared units).

Deviations are measured from $\bar x$, which is itself fitted to the sample, so they are on average **smaller** than deviations from the true mean $\mu$. Dividing by $n$ would under-estimate $\sigma^2$; dividing by $n-1$ (the @@degrees of freedom@@) corrects this, making $s^2$ an ==unbiased estimator==: $\mathbb E[s^2]=\sigma^2$ for independent observations (notes' footnote: $\mathbb E\sum(X_i-\bar X)^2=n\sigma^2-n\cdot\sigma^2/n=(n-1)\sigma^2$).
:::
:::

:::question Q40. Distinguish among variance, standard deviation, interquartile range, and median absolute deviation. Which measures are more resistant to extreme observations?
:::solution Answer
- @@Variance@@: average squared deviation from the mean (squared units).
- @@SD@@: square root of the variance (original units).
- @@IQR@@ $=Q_{0.75}-Q_{0.25}$: spread of the middle 50%.
- @@MAD@@ $=\operatorname{median}|x_i-\operatorname{median}(x)|$.

Variance and SD **square** deviations, so one extreme value can dominate them. ==IQR and MAD are robust== — they ignore how far the extremes are — and are preferred for skewed or heavy-tailed data (e.g. 10 waiting times: SD 23.9 with one 95-minute value vs 7.4 without; MAD 6 either way).
:::
:::

:::question Q41. Explain the relationship among quantiles, quartiles, and percentiles. What information do the 25th, 50th, 90th, and 95th percentiles provide about a distribution?
:::solution Answer
A @@quantile@@ $Q_q$ has about a fraction $q$ of values below it. A @@percentile@@ is a quantile on a 0–100 scale (90th percentile $=Q_{0.90}$). @@Quartiles@@ are the three quantiles splitting data into four parts ($Q_{0.25},Q_{0.5},Q_{0.75}$) — all quartiles are quantiles, not vice versa.
- 25th and 75th: the middle 50% (their difference is the IQR).
- 50th: the median — typical value.
- 90th and 95th: the **upper tail** — the worst 10%/5% (service levels, waiting-time targets, screening extremes).

They need no distributional assumption, which suits skewed data.
:::
:::

:::question Q42. Latencies [120, 135, 142, 150, 165] ms. Calculate the 80th percentile using Hyndman and Fan Type 7 and Type 6. If the SLA requires the 80th percentile to remain below 155 ms, determine the outcome under each method.
:::solution Answer
- **Type 7** (NumPy): position $1+(n-1)p=1+4(0.8)=4.2$ → $150+0.2(165-150)=$ **153 ms → passes**.
- **Type 6** (Excel PERCENTILE.EXC): position $(n+1)p=6(0.8)=4.8$ → $150+0.8(15)=$ **162 ms → fails**.

The 9 ms difference is ==purely an artefact of software defaults==. With small samples, flag quantiles for review, state the method in every report, and define the interpolation rule in the contract itself.
:::
:::

:::question Q43. Define skewness mathematically and explain the interpretation of positive, negative, and approximately zero skewness.
:::solution Answer
$\gamma_1=\dfrac{\mathbb E[(X-\mu)^3]}{\sigma^3}$ — the standardised third moment.
- $\gamma_1>0$: longer/heavier **right** tail (income, waiting times, healthcare costs); typically mean > median.
- $\gamma_1<0$: longer/heavier **left** tail.
- $\gamma_1\approx0$: approximately symmetric — ==but not necessarily normal== (could be bimodal or heavy-tailed).

Because deviations are cubed, the statistic is itself @@sensitive to extreme observations@@ — read it with a histogram or boxplot.
:::
:::

:::question Q44. Why can logarithmic transformations be useful for strongly right-skewed variables? Discuss their effects on distributional shape, interpretation, and subsequent statistical modeling.
:::solution Answer
- **Shape:** $\log(1+x)$ compresses large values (each tenfold increase adds ≈2.3), so a long right tail becomes more symmetric and extremes lose dominance; $+1$ handles zeros.
- **Interpretation:** the variable is no longer in original units; effects become ==relative/percentage changes== — results must be explained or back-transformed.
- **Modelling:** can stabilise variance, make relationships closer to linear (log–log visits vs sales), and reduce the influence of extremes — helpful for models assuming constant variance or linearity.

Use it only when the transformed scale is meaningful for the task, not merely to make a histogram look nicer; and apply the **same** transform at deployment (train–serving consistency).
:::
:::

:::question Q45. Define covariance and explain how its sign and magnitude should be interpreted. Why are covariance values not directly comparable across variables measured in different units?
:::solution Answer
$s_{XY}=\dfrac{1}{n-1}\sum(x_i-\bar x)(y_i-\bar y)$. **Sign:** positive — large $X$ tends to come with large $Y$; negative — large $X$ with small $Y$; near zero — little **linear** co-movement. **Magnitude:** measured in the @@product of the units@@ (kg·cm), so it depends on scale — converting cm to m divides it by 100 although the association is unchanged. ==Covariance magnitudes cannot be compared across pairs==; use correlation for strength. (Diagonal of a covariance matrix = variances.)
:::
:::

:::question Q46. Define Pearson correlation and explain how standardizing covariance produces a dimensionless measure of linear association.
:::solution Answer
$r_{XY}=\dfrac{s_{XY}}{s_Xs_Y}=\dfrac{\sum(x_i-\bar x)(y_i-\bar y)}{\sqrt{\sum(x_i-\bar x)^2}\sqrt{\sum(y_i-\bar y)^2}}$. Dividing the covariance by both standard deviations **cancels the units** (kg·cm ÷ kg ÷ cm), giving a pure number in $[-1,1]$ that is unchanged by rescaling either variable. $r=\pm1$: perfect linear relationship; $r=0$: ==no linear association — not necessarily no relationship==. This makes strength comparable across variable pairs.
:::
:::

## Relationships, Correlation, and Causal Interpretation

:::question Q47. Distinguish among positive linear, negative linear, nonlinear, monotonic, threshold-based, interaction-driven, and outlier-driven relationships.
:::solution Answer
- **Positive / negative linear:** $Y$ rises / falls at a roughly constant rate with $X$.
- **Non-linear:** changes at a varying rate or direction (U-shape: age vs BP).
- **Monotonic:** always increasing (or decreasing), though not at a constant rate (doubling curves) — captured by Spearman.
- **Threshold-based:** little effect until $X$ passes a cut-off, then a jump (AQI above a level).
- **Interaction-driven:** the $X$–$Y$ relationship depends on a third variable (medication effect depends on age).
- **Outlier-driven:** an apparent relationship created by one or a few extreme points.

Telling them apart needs a ==scatterplot, overall and within subgroups== (Figure 32).
:::
:::

:::question Q48. Why can Pearson correlation be close to zero even when two variables are strongly related? Illustrate using $Y=X^2$ for a distribution of $X$ symmetric around zero.
:::solution Answer
Pearson measures only **linear** association. With $X=-2,-1,0,1,2$ and $Y=X^2=4,1,0,1,4$: the left half slopes down, the right half up, and the products $(x_i-\bar x)(y_i-\bar y)$ cancel exactly, so $r=0$ — yet $Y$ is ==perfectly determined by $X$==. A zero correlation means no linear association, not independence. Always plot first; use non-linear terms or other measures for such shapes.
:::
:::

:::question Q49. Compare Pearson correlation and Spearman rank correlation in terms of the relationships they measure and their sensitivity to extreme observations.
:::solution Answer
| | Pearson $r$ | Spearman $\rho_S$ |
|---|---|---|
| measures | **linear** association | **monotonic** association (Pearson on ranks) |
| suits | continuous, roughly linear | monotonic non-linear, ordinal data, non-comparable scales |
| extremes | very sensitive — one point can create or destroy $r$ | less sensitive (ranks cap the influence), but not immune |

Example: $y=10,20,40,80$ against $x=1,2,3,4$ gives $r\approx0.96$ but $\rho_S=1$. Neither establishes causation.
:::
:::

:::question Q50. Why might calculating Pearson correlation for ordinal categories encoded as integers produce a misleading interpretation?
:::solution Answer
Coding education as 1 = high school, 2 = bachelor's, 3 = master's, 4 = doctorate ==assumes equal distances between levels== — that going from 1 to 2 is the same "amount" as from 3 to 4 — which the categories do not justify. Pearson then treats these arbitrary spacings as real numbers, so the coefficient's value depends on the coding. Use @@Spearman@@ (only order matters) or @@polychoric correlation@@ for ordinal variables; match the method to the measurement scale.
:::
:::

:::question Q51. How can the correlation between two time-dependent variables be influenced by shared trends, seasonality, or temporal dependence?
:::solution Answer
If both series grow over time, or both peak in the same season, they correlate strongly ==even with no direct relationship== — daily ad spend and sales both rise in holiday periods; ice-cream sales and drownings both rise in summer. Consecutive observations are also **not independent**, so the effective sample size is smaller than the row count and the correlation looks more certain than it is. Fix: @@detrend@@ (correlate changes $\Delta X_t=X_t-X_{t-1}$, or remove fitted trends/seasonality) and use time-series methods such as cross-correlation.
:::
:::

:::question Q52. Explain why an aggregate association may become weaker, stronger, or reversed after stratifying the data into relevant subgroups.
:::solution Answer
The pooled association mixes two things: the relationship **within** each group and the differences **between** groups. If groups differ in both variables, the between-group difference can create, inflate, hide or reverse the within-group pattern (@@confounding@@, @@aggregation effects@@, @@Simpson's paradox@@). *Example 68:* exercise vs blood pressure is strongly negative overall, but weak in young adults, moderate in middle age and strong in older adults — partly because older adults both exercise less and have higher BP. ==An aggregate relationship need not describe any subgroup==, so examine relationships overall and within meaningful groups.
:::
:::

:::question Q53. Distinguish among confounding, reverse causation, selection effects, and chance as possible explanations for an observed association.
:::solution Answer
For an association between exercise ($X$) and blood pressure ($Y$):
- @@Confounding@@: a third variable drives both (diet, stress, healthcare access, age).
- @@Reverse causation@@: $Y$ causes $X$ (people with high BP exercise less because of their condition).
- @@Selection effects@@: how units entered the data creates the association (people who choose to exercise differ systematically; only hospital patients studied).
- @@Chance@@: random sampling variation, especially after examining many variables.

EDA can show the association but ==cannot tell which explanation is correct==.
:::
:::

:::question Q54. Why does correlation not establish causation? Explain how randomized interventions, causal models, and explicit causal assumptions can strengthen causal conclusions.
:::solution Answer
Correlation only shows that two variables move together; the same pattern is produced by causation, reverse causation, confounding, selection, measurement artefacts or chance (ice-cream sales and drownings both follow hot weather). Stronger evidence comes from:
- @@Randomised interventions@@ (RCTs, A/B tests): random assignment balances observed and unobserved factors, so outcome differences can be attributed to the intervention.
- @@Causal models@@ (DAGs): make assumed causal paths explicit, identifying confounders to adjust for and colliders not to.
- @@Explicit assumptions@@ (e.g. instrumental-variable conditions, no unmeasured confounding): state what must hold for an observational estimate to be causal, so it can be scrutinised.
:::
:::

## Feature Engineering, Scaling, Normalization, and Categorical Encoding

:::question Q55. Define feature engineering and explain the meaning of $\phi(x_{\text{raw}})=x_{\text{model}}$. How can feature engineering improve the representation of information without necessarily introducing new information?
:::solution Answer
Feature engineering converts raw data into representations more useful for modelling. $\phi$ is the transformation (scaling, encoding, aggregation, mathematical transforms, new variables) mapping raw inputs $x_{\text{raw}}$ to the model's inputs $x_{\text{model}}$. It often ==re-expresses information already present in a form the model can use==: a timestamp → hour of day or time since last event; date of birth → age at the observation; many transactions → recent transaction frequency. Nothing new is measured, but patterns (daily cycles, ageing, bursts of activity) become accessible — improving stability, encoding domain knowledge, expressing non-linearity and history.
:::
:::

:::question Q56. Why must transformations whose parameters are learned from data be fitted using the training partition rather than the complete dataset?
:::solution Answer
If means, SDs, min/max, imputation values, category encodings, selected features or PCA directions are computed from the **whole** dataset, ==information from the test set influences the features used to build the model== (leakage). The model is then evaluated on data that helped shape it, so performance is **optimistically biased** and will not hold on truly new data. Rule: $\hat\psi=\text{Fit}(X_{\text{train}})$, then apply $T(\cdot;\hat\psi)$ unchanged to train, validation and test — ideally inside a modelling pipeline so each CV fold re-fits its own preprocessing.
:::
:::

:::question Q57. Explain standardization and derive the transformation used to convert a numerical feature into a standardized representation using the training mean and standard deviation.
:::solution Answer
Standardization rescales a feature to mean 0 and SD 1. Subtracting the mean centres it: $x-\mu_{\text{train}}$ has mean 0. Dividing by the SD rescales its spread: $\operatorname{SD}\big((x-\mu)/\sigma\big)=\sigma/\sigma=1$. So
$$
z_i=\frac{x_i-\mu_{\text{train}}}{\sigma_{\text{train}}},
$$
with $\mu_{\text{train}},\sigma_{\text{train}}$ from the training data only (also called mean–variance normalization). Example: training ages $20,\dots,60$ ($\mu=40$, $s=15.81$) → a test patient of 70 gets $z=1.90$. Useful for logistic regression, SVMs, neural nets, PCA, kNN, regularised regression and gradient methods.
:::
:::

:::question Q58. Compare standardization, robust scaling, min-max normalization, and unit-vector normalization. Identify an appropriate application for each.
:::solution Answer
| method | formula | application | weakness |
|---|---|---|---|
| @@Standardization@@ | $(x-\mu)/\sigma$ | SVM, logistic regression, kNN, PCA, neural nets | outliers inflate $\sigma$ |
| @@Robust scaling@@ | $(x-\text{median})/\text{IQR}$ | features with extreme values (incomes, charges) | — |
| @@Min–max@@ | $(x-x_{\min})/(x_{\max}-x_{\min})$ | bounded inputs, e.g. pixel intensities, neural-net inputs in $[0,1]$ | one extreme sets the range and squashes the rest |
| @@Unit vector@@ | $x/\|x\|_2$ | when direction matters: documents, embeddings, cosine similarity | discards magnitude |

All fitted parameters come from the training data.
:::
:::

:::question Q59. Why are distance-based algorithms, regularized regression, and gradient-based optimization generally more sensitive to feature scaling than many tree-based models?
:::solution Answer
- @@Distance-based@@ (kNN, SVM, clustering): distances add squared differences, so a feature on a big scale (income up to $10^7$) dominates one on $[0,1]$ (debt ratio) ==purely because of its units==.
- @@Regularised regression@@: penalties act on coefficient sizes, and a coefficient's size depends on its feature's scale, so the same penalty affects features unequally.
- @@Gradient-based optimisation@@: very different scales make the loss surface elongated, slowing or destabilising convergence.

**Trees** split on thresholds within one feature at a time ("is income > 50,000?"); rescaling a feature moves the threshold but not the split, so they are largely scale-invariant.
:::
:::

:::question Q60. Distinguish among logarithmic transformations, square-root transformations, and nonlinear feature construction. How can each influence model behavior and interpretability?
:::solution Answer
- @@Log@@ $\log(1+x)$: strong compression of large values; reduces heavy right skew; coefficients become relative (percentage) effects.
- @@Square root@@ $\sqrt x$: milder compression; useful for moderately skewed counts; stabilises variance of count data; interpretation in "root units" is less intuitive.
- @@Non-linear feature construction@@ (age², splines, age bands, interactions): lets a model represent curvature or thresholds (mortality rising steeply in old age), improving fit but making individual coefficients harder to explain and increasing overfitting risk.

All must be applied identically in training and deployment; prefer transformations whose scale stays meaningful.
:::
:::

:::question Q61. Define binning and compare equal-width, equal-frequency, domain-defined, and supervised binning.
:::solution Answer
**Binning** maps a continuous variable to intervals using thresholds $c_1<\dots<c_{K-1}$.
- @@Equal-width@@: intervals of the same width — simple, but skewed data leave most points in one bin and some bins empty.
- @@Equal-frequency (quantile)@@: each bin holds about the same number of points — balanced, but boundaries have no meaning and can be very uneven in width.
- @@Domain-defined@@: thresholds with real meaning (AQI bands, clinical BP categories, policy limits) — ==preferred when such thresholds exist==.
- @@Supervised@@: cut-points chosen using the outcome — can capture thresholds well but risks **target leakage**; must be fitted on training data only.
:::
:::

:::question Q62. What information can be lost when a continuous variable is converted into categories? Explain how artificial discontinuities arise near bin boundaries.
:::solution Answer
Binning throws away **within-bin variation**: systolic BP of 121 and 139 become the same category although clinically different, and fine gradients of risk disappear. It also creates @@artificial discontinuities@@: values just either side of a cut-point (139 vs 140) fall into different categories, so the model's prediction **jumps** at the boundary even though the underlying quantity barely changed — and small measurement noise near the boundary can flip the category (unstable predictions). ==Use bins only when thresholds are meaningful==, and keep the continuous variable otherwise.
:::
:::

:::question Q63. Compare ordinal encoding, one-hot encoding, frequency encoding, and target encoding. Discuss their suitability for nominal, ordinal, and high-cardinality variables.
:::solution Answer
| encoding | idea | nominal | ordinal | high cardinality |
|---|---|---|---|---|
| @@Ordinal@@ | integers in order | ✗ invents an order | ✓ | — |
| @@One-hot@@ | one 0/1 column per category (drop one with an intercept) | ✓ simple, safe | ✓ (loses order) | ✗ huge sparse matrices (40,000 ZIPs), overfitting |
| @@Frequency@@ | category → its proportion | usable | usable | ✓ compact (one column); but equal frequencies collide |
| @@Target@@ | category → mean outcome | usable | usable | ✓ powerful, but ==leakage and overfitting risk== — needs out-of-fold estimates and smoothing |
:::
:::

:::question Q64. Why is target encoding especially vulnerable to target leakage? Explain how cross-fitting, out-of-fold estimates, smoothing, and explicit handling of unseen categories can reduce this risk.
:::solution Answer
Each row's encoded value is computed from outcomes that **include its own**, so ==the feature carries the label==. For a category with one row, the encoding equals that row's outcome (lone Engineer who defaulted → 1.00). Training performance looks excellent and collapses on new data.
- @@Cross-fitting / out-of-fold@@: split training data into folds; encode each fold using only the **other** folds' outcomes, so no row sees its own target.
- @@Smoothing@@: shrink small categories towards the global mean, $\frac{n_c\bar y_c+\lambda\bar y}{n_c+\lambda}$ (lone Engineer, $\lambda=10$: $6/11\approx0.545$) — reduces noise but does not fully remove the row's influence, so combine with out-of-fold.
- @@Unseen categories@@: a predefined fallback (global training mean or "unknown") for categories absent from training.
:::
:::

## Advanced Feature Construction and Feature-Engineering Risks

:::question Q65. Define an interaction feature and explain the interpretation of the interaction coefficient in $\hat y=\beta_0+\beta_1x_1+\beta_2x_2+\beta_3x_1x_2$.
:::solution Answer
An **interaction** exists when ==the effect of one variable depends on the value of another==. The feature $x_1x_2$ captures it. Differentiating, $\partial\hat y/\partial x_1=\beta_1+\beta_3x_2$: $\beta_1$ is the effect of $x_1$ when $x_2=0$, and $\beta_3$ is **how much that effect changes per unit of $x_2$**. If $\beta_3\neq0$ the model is no longer additive. Example: expenditure with an income × household-size term — the same extra income raises spending more in bigger households. Justify and validate interactions; many of them add complexity and overfitting.
:::
:::

:::question Q66. What are polynomial features, and how can they allow a model that is linear in its parameters to represent nonlinear relationships?
:::solution Answer
Polynomial features add powers (and products) of inputs: $\hat y=\beta_0+\beta_1x+\beta_2x^2+\dots+\beta_dx^d$; for two inputs at degree 2: $x_1,x_2,x_1^2,x_2^2,x_1x_2$. The model is ==still linear in the coefficients $\beta$==, so ordinary least squares and regularisation work unchanged, but the fitted function of $x$ is a curve — capturing diminishing returns (spending vs income) or curvature. Low degrees remain interpretable.
:::
:::

:::question Q67. Why can increasing the degree of polynomial features create problems involving multicollinearity, excessive dimensionality, unstable extrapolation, and overfitting?
:::solution Answer
- @@Multicollinearity@@: $x$, $x^2$, $x^3$ are highly correlated, making coefficients unstable.
- @@Excessive dimensionality@@: terms grow rapidly with variables and degree (degree 2 on 10 variables already gives 65 features).
- @@Unstable extrapolation@@: high-degree polynomials swing wildly outside the training range.
- @@Overfitting@@: a flexible curve fits noise; validation error rises.
- @@Scale sensitivity@@: $x^5$ of large values explodes numerically.

Remedies: scale inputs, keep degrees low, regularise, and choose the degree by (cross-)validation.
:::
:::

:::question Q68. Define lag features, rolling means, rolling standard deviations, differences, percentage changes, event counts, and time-since-event features.
:::solution Answer
For a series $x_t$, using only past values:
- **Lag** $L_k(t)=x_{t-k}$ — value $k$ steps ago (persistence).
- **Rolling mean** $M_w(t)=\frac1w\sum_{j=1}^wx_{t-j}$ — recent average level.
- **Rolling SD** $S_w(t)$ — recent variability.
- **Difference** $\Delta x_t=x_t-x_{t-1}$ — change.
- **Percentage change** $(x_t-x_{t-1})/x_{t-1}$ — relative change.
- **Event count** $C_w(t)=\sum_{j=1}^w\mathbf 1\{\text{event at }t-j\}$ — e.g. transactions in the last 24 h.
- **Time since event** $t-t_{\text{last event}}$ — e.g. minutes since previous transaction.

==Every window must end before the prediction time.==
:::
:::

:::question Q69. A fraud detection system generates a prediction at time $t$. Explain why a rolling average constructed using observations from $(t+1)$ or later would introduce temporal leakage.
:::solution Answer
At time $t$ the system can only know transactions up to $t$. A rolling average that includes $t+1$ or later uses ==information that will not exist when the prediction is made== — e.g. the burst of fraudulent transactions *after* the card was compromised. The model learns from the future, so development performance is artificially high, but the feature **cannot be computed in deployment**, so real performance collapses. Use backward-looking windows ending at $t$ (or $t-1$), chronological splits, and documented feature timestamps; centred windows are only for retrospective description.
:::
:::

:::question Q70. Why should cyclical variables such as hour of day, day of week, and month of year not always be represented using ordinary integer encoding?
:::solution Answer
Integer encoding puts the ends of the cycle far apart: hour 23 and hour 0 differ by 23, Sunday (7) and Monday (1) by 6, December (12) and January (1) by 11 — although they are ==adjacent in time==. Distance-based and linear models then treat late night and early morning as opposites and cannot represent smooth patterns that wrap around midnight or the new year. A cyclical encoding preserves this circular proximity.
:::
:::

:::question Q71. Explain how sine and cosine transformations preserve circular proximity when encoding cyclical variables. Write the formulas and identify the appropriate period for hour-of-day encoding.
:::solution Answer
$$
x_{\sin}=\sin\frac{2\pi x}{P},\qquad x_{\cos}=\cos\frac{2\pi x}{P},
$$
with $P=24$ for hour of day (7 for day of week, 12 for month). Each value becomes a point on the **unit circle**; the cycle's end and start meet. Hour 0 → $(0,1)$, hour 23 → $(-0.259,0.966)$: distance $\approx0.26$, as close as any two consecutive hours, while hours 0 and 12 are opposite (distance 2). **Both** features are needed — sine alone gives the same value to hours 3 and 9.
:::
:::

:::question Q72. Identify and explain eight major feature-engineering risks: target leakage, temporal leakage, identity leakage, proxy discrimination, unstable high-cardinality features, train-serving inconsistency, excessive dimensionality, and spurious interactions.
:::solution Answer
- @@Target leakage@@: a feature contains the outcome (target encoding on full data; "total defaults in the next 12 months").
- @@Temporal leakage@@: a feature uses information from after the prediction time (centred rolling windows).
- @@Identity leakage@@: rows of the same person/device in train and test, so the model recognises entities rather than learning patterns.
- @@Proxy discrimination@@: a feature stands in for a sensitive attribute (ZIP code for race or income in lending).
- @@Unstable high-cardinality features@@: IDs or rare categories memorised (customer ID) — no use for new entities.
- @@Train–serving inconsistency@@: features computed differently in production (log income in training, raw income served).
- @@Excessive dimensionality@@: too many engineered features (one-hot, polynomials) → overfitting and cost.
- @@Spurious interactions@@: interactions that fit noise in training and do not replicate.

Document each feature's definition, unit, sources, window, availability time, missing-value rule, version and justification.
:::
:::
