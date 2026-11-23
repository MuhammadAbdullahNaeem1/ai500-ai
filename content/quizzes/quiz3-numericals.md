# Quiz 3 numericals — Module 3, §3.1–3.5

Every calculation Module 3 (3.1–3.5) supports, worked step by step with the notes' own examples where they exist, then practice with hidden answers. All numbers were checked by computer.

<div class="pdf-links">
<a href="quiz3-guide.html">Quiz 3 guide</a>
<a href="m3-answers-1.html">Back questions Q1–36</a>
<a href="m3-answers-2.html">Back questions Q37–72</a>
<a href="m3b-notes.html">M3 Notes B</a>
</div>

<div class="hl-legend">
<span><mark class="hl">Yellow</mark> the one line to remember</span>
<span><span class="key">Blue</span> keywords a rubric looks for</span>
<span><mark class="trap">Coral</mark> a common trap</span>
</div>

:::exam Which numericals can appear
The notes' back questions that ask for a number are **Q19** (missingness rate), **Q38** (mean vs median of $\{2,3,3,4,100\}$) and **Q42** (80th percentile, Type 7 vs Type 6). The sections also define, with formulas, the mean, weighted mean, median, sample variance/SD, IQR and boxplot fences, MAD, quantiles, skewness, covariance, Pearson and Spearman correlation, the missingness rates $r_j$ and $r_i$, standardization, min–max, robust and unit-vector scaling, $\log(1+x)$, frequency and target encoding (with smoothing), interaction effects, time-window features, cyclical encoding and the Big Data paradox. Each of these is worked below. Always **show the formula, the substitution and the interpretation** — the interpretation is usually worth a mark on its own.
:::

## 1. Centre: mean, weighted mean, median

$$
\bar x=\frac1n\sum_{i=1}^nx_i,\qquad \bar x_w=\frac{\sum w_ix_i}{\sum w_i},\qquad \tilde x=\text{middle ordered value (average of the two middle values if }n\text{ is even)}.
$$

:::example Notes Q38: $\{2,3,3,4,100\}$
$\bar x=\dfrac{2+3+3+4+100}{5}=\dfrac{112}{5}=22.4$, and $\tilde x=3$ (the 3rd of 5 ordered values).

**Interpretation:** four of the five values lie between 2 and 4; the single 100 drags the mean to 22.4, which describes none of the observations. The median is ==resistant to the extreme value==. A large mean–median gap signals @@right skew@@, an @@extreme observation@@, a @@mixture@@, or a @@data-quality problem@@ — check which before choosing a summary.
:::

:::example Weighted mean
Two sections: 30 students average 70, 10 students average 80. The overall mean is **not** $(70+80)/2=75$:
$$
\bar x_w=\frac{30(70)+10(80)}{30+10}=\frac{2100+800}{40}=72.5 .
$$
The weights are the group sizes; !!averaging group means without weights over-counts the small group!!.
:::

## 2. Spread: variance, SD, IQR, fences, MAD

$$
s^2=\frac{1}{n-1}\sum(x_i-\bar x)^2,\quad s=\sqrt{s^2},\quad \text{IQR}=Q_3-Q_1,\quad \text{fences } Q_1-1.5\,\text{IQR},\ Q_3+1.5\,\text{IQR},\quad \text{MAD}=\operatorname{median}|x_i-\tilde x|.
$$

:::example Sample variance of $\{4,8,6,5,7\}$
$\bar x=30/5=6$. Deviations $-2,2,0,-1,1$; squares $4,4,0,1,1$, sum $10$.
$$
s^2=\frac{10}{5-1}=2.5,\qquad s=\sqrt{2.5}\approx1.58 .
$$
(Dividing by $n=5$ would give $2$ — the population formula. !!Quizzes on sample data expect $n-1$!!, which makes $s^2$ unbiased.) Variance is in **squared units**; the SD is in the original units.
:::

:::example Ten ED waiting times (minutes): $12,15,18,20,22,25,28,30,35,95$
1. **Centre:** $\bar x=300/10=30$; median $=(22+25)/2=23.5$. Mean > median → right skew.
2. **Quartiles** (NumPy/Type 7, position $1+(n-1)q$): $Q_1$ at position $3.25$ → $18+0.25(20-18)=18.5$; $Q_3$ at position $7.75$ → $28+0.75(30-28)=29.5$. $\text{IQR}=11$.
3. **Fences:** $18.5-1.5(11)=2$ and $29.5+1.5(11)=46$. Only **95** lies outside → plotted as an individual point.
4. **SD:** $s\approx23.9$ with the 95, but $\approx7.4$ without it — ==one value triples the SD==.
5. **MAD:** absolute deviations from 23.5 are $11.5,8.5,5.5,3.5,1.5,1.5,4.5,6.5,11.5,71.5$; their median is $(5.5+6.5)/2=6$. The MAD barely notices the 95.

**Interpretation:** report median 23.5 and IQR 11 (or MAD 6) as the robust summary; investigate the 95-minute wait (genuine long wait or a recording error?) **before** deciding anything — do not delete it because it is past the fence.

*Note:* other quartile conventions give slightly different values (Type 6: $Q_1=17.25$, $Q_3=31.25$). State the method you use.
:::

## 3. Quantiles: the method matters (notes Q42 / Example 91)

For sorted data $x_{(1)}\le\dots\le x_{(n)}$ and a position $h$ between two ranks, interpolate: $Q=x_{(\lfloor h\rfloor)}+(h-\lfloor h\rfloor)\big(x_{(\lfloor h\rfloor+1)}-x_{(\lfloor h\rfloor)}\big)$.

| method | position $h$ for quantile $p$ | software |
|---|---|---|
| **Type 7** | $1+(n-1)p$ | NumPy, pandas, R default, Excel PERCENTILE.INC |
| **Type 6** | $(n+1)p$ | Excel PERCENTILE.EXC, R type 6, Minitab |

:::example Latencies $[120,135,142,150,165]$ ms; SLA: $Q_{0.8}\le155$
- **Type 7:** $h=1+4(0.8)=4.2$ → $150+0.2(165-150)=153$ ms → ==passes==.
- **Type 6:** $h=6(0.8)=4.8$ → $150+0.8(15)=162$ ms → **fails**.

Same five numbers, opposite verdicts, a 9 ms gap caused only by the software default. With small $n$ (notes: flag $n<30$), state the quantile method in the report and in the contract.
:::

## 4. Shape: skewness

$$
\gamma_1=\frac{\mathbb E[(X-\mu)^3]}{\sigma^3}\quad\text{(sample version: replace }\mathbb E,\mu,\sigma\text{ by averages over the data)}.
$$

:::example $\{1,2,2,3,3,3,4,12\}$
Mean $=30/8=3.75$, median $=3$. Cubed deviations are dominated by $(12-3.75)^3\approx561.5$, so $\gamma_1\approx1.96>0$: a **long right tail**, caused by one value. This is why the notes warn that ==skewness statistics are themselves sensitive to extremes== — read them with a histogram or boxplot. $\gamma_1\approx0$ means roughly symmetric, **not** necessarily normal.
:::

## 5. Association: covariance, Pearson, Spearman

$$
s_{XY}=\frac{1}{n-1}\sum(x_i-\bar x)(y_i-\bar y),\qquad r=\frac{s_{XY}}{s_Xs_Y},\qquad \rho_S=1-\frac{6\sum d_i^2}{n(n^2-1)}\ \ (\text{no ties}).
$$

:::example $x=(1,2,3,4,5)$, $y=(2,4,5,3,6)$
$\bar x=3$, $\bar y=4$. Products of deviations: $(-2)(-2)+(-1)(0)+(0)(1)+(1)(-1)+(2)(2)=4+0+0-1+4=7$.
- $s_{XY}=7/4=1.75$ (units: units of $x$ × units of $y$).
- $s_X^2=10/4$, $s_Y^2=10/4$, so $r=\dfrac{7}{\sqrt{10}\sqrt{10}}=0.70$ — moderately strong positive **linear** association.
- **Spearman:** ranks of $y$ are $1,3,4,2,5$; differences from the ranks of $x$ are $0,-1,-1,2,0$, $\sum d_i^2=6$, so $\rho_S=1-\dfrac{6(6)}{5(24)}=1-0.3=0.70$.
:::

:::example $r=0$ but a perfect relationship (notes Q48)
$X=(-2,-1,0,1,2)$, $Y=X^2=(4,1,0,1,4)$. $\bar X=0$, and $\sum X_i(Y_i-\bar Y)=\sum X_iY_i-\bar Y\sum X_i=(-8-1+0+1+8)-0=0$, so $r=0$. $Y$ is completely determined by $X$, but the relationship is **symmetric and non-linear**. ==$r=0$ means no *linear* association, not no relationship== — always look at the scatterplot.
:::

:::example One outlier creates a correlation
Ten points with no relation ($r\approx-0.01$); add one point far out at $(40,40)$ and Pearson jumps to $r\approx0.95$, while Spearman is only $\approx0.34$. This is the notes' "influence of outliers" limitation of heatmaps: !!a strong $r$ may be one observation!! — inspect the scatterplot and compare with Spearman.
:::

**Covariance is unit-dependent:** measuring $X$ in cm instead of m multiplies $s_{XY}$ by 100 but leaves $r$ unchanged — which is why covariances are not comparable across pairs and correlation is.

## 6. Missingness rates

$$
r_j=\frac{\#\text{ missing in feature }j}{n},\qquad r_i=\frac{\#\text{ missing features in record }i}{p},\qquad P(\text{feature }j\text{ missing}\mid G=g).
$$

:::example Notes Q19 and Example 71
- Income missing for 450 of 2,000 patients: $r_j=450/2000=0.225$ (22.5%). To see whether it is concentrated in groups, compute $P(\text{missing}\mid G=g)$ by age band, insurance, hospital, etc. — the overall 22.5% can hide one group at 60%.
- A record missing 3 of 12 features has $r_i=3/12=0.25$.
- **Example 71:** 10,000 patients per group; income missing 55% (Medicare), 10% (Medicaid), 25% (private). Complete-case analysis keeps $4{,}500$, $9{,}000$ and $7{,}500$ → Medicaid dominates what the model learns about income. ==Effective sample sizes become unequal==.
:::

## 7. Scaling and transformations

| method | formula (parameters from the **training** set) |
|---|---|
| standardization | $z=(x-\mu_{\text{train}})/\sigma_{\text{train}}$ |
| min–max | $(x-x_{\min})/(x_{\max}-x_{\min})$ |
| robust | $(x-\text{median})/\text{IQR}$ |
| unit vector | $x/\|x\|_2$ |
| log | $\log(1+x)$ |

:::example Fit on training, apply to test
Training ages $20,30,40,50,60$: $\mu=40$, $s=\sqrt{1000/4}\approx15.81$.
- Training $z$-scores: $-1.26,-0.63,0,0.63,1.26$.
- A **test** patient aged 70: $z=(70-40)/15.81\approx1.90$ — computed with the **training** $\mu$ and $s$. !!Recomputing $\mu$ and $s$ with the test data included is leakage!! (notes §3.5.2).
- Min–max of 45: $(45-20)/(60-20)=0.625$. Robust of 45: median 40, IQR $50-30=20$ → $(45-40)/20=0.25$.
:::

:::example Why min–max fails with an outlier
Incomes $30\text{k},45\text{k},60\text{k},80\text{k},2{,}000\text{k}$ → min–max values $0,\ 0.008,\ 0.015,\ 0.025,\ 1$. The four ordinary incomes are squashed into $[0,0.03]$ because ==one extreme value sets the range==. Robust scaling or $\log(1+x)$ is better here.
:::

:::example Log and unit-vector
$\log(1+x)$ for $x=0,9,99,999,9999$ gives $0,\ 2.30,\ 4.61,\ 6.91,\ 9.21$: each tenfold increase adds about $2.3$ — large values are compressed, and the model now reads **relative** changes. Unit vector: $(3,4)/\sqrt{9+16}=(0.6,0.8)$, length 1 — only the direction is kept.
:::

## 8. Encoding categorical variables

:::example One-hot with a reference category (notes Example 100)
Gender $\in\{\text{Male},\text{Female},\text{Other}\}$; drop **Other**: $\hat y=\beta_0+\beta_1\text{Male}+\beta_2\text{Female}$. Other → $\beta_0$; Male → $\beta_0+\beta_1$; Female → $\beta_0+\beta_2$. With $\beta_0=50$, $\beta_1=4$, $\beta_2=-2$: Other 50, Male 54, Female 48. $\beta_1$ is the Male–Other difference. Keeping all three dummies **and** an intercept makes the columns perfectly dependent (they sum to 1).

Columns needed: $K$ categories → $K-1$ dummies with an intercept. 40,000 ZIP codes → 39,999 sparse columns, which is why one-hot fails at **high cardinality**.
:::

:::example Frequency encoding (notes Example 101)
Cities LHR ×4, KHI ×3, ISL ×2, PEW ×1 among 10 customers → LHR 0.4, KHI 0.3, ISL 0.2, PEW 0.1. One column instead of four. !!Two cities with equal frequencies get the same value even if they behave very differently!! (notes Table 33).
:::

:::example Target encoding, smoothing, and the notes' slip (Examples 102–103)
Occupations with default outcomes: Teacher $0,0,1$ → $1/3\approx0.33$; Driver $1,1,0$ → $2/3\approx0.67$; a lone Engineer who defaulted → $1/1=1.00$, i.e. ==the feature *is* the label== (target leakage). Global default rate $3/6=0.5$.

**Smoothing** with $\lambda=10$:
$$
\text{TE}(\text{Engineer})=\frac{n_c\bar y_c+\lambda\bar y}{n_c+\lambda}=\frac{1(1)+10(0.5)}{1+10}=\frac{6}{11}\approx0.545 .
$$
!!The notes print 0.455 — that is an arithmetic slip; $6/11=0.545$.!! The point is unchanged: the value moves from 1.00 towards the global 0.5. Teacher, smoothed: $\frac{3(1/3)+10(0.5)}{13}=\frac{6}{13}\approx0.46$. Larger $n_c$ → less pull towards the global mean.

**Out-of-fold:** each row's encoding uses only the other fold(s). If a category is absent from the other fold, fall back to the global training mean. **Unseen category at deployment:** global training mean or an "unknown" value.
:::

## 9. Interactions and polynomial features

:::example Interaction (notes §3.5.7)
$\hat y=\beta_0+\beta_1x_1+\beta_2x_2+\beta_3x_1x_2$, so $\dfrac{\partial\hat y}{\partial x_1}=\beta_1+\beta_3x_2$. With expenditure $=5+0.3\,\text{income}+2\,\text{size}+0.1\,\text{income}\times\text{size}$: the effect of one more unit of income is $0.3+0.1(2)=0.5$ for a household of 2 and $0.3+0.1(5)=0.8$ for a household of 5. ==The effect of $x_1$ depends on $x_2$== whenever $\beta_3\neq0$.
:::

**Polynomial feature count:** degree 2 on $p$ variables gives $p$ linear terms + $p$ squares + $\binom p2$ products $=p+\frac{p(p+1)}{2}$. For $p=2$: $x_1,x_2,x_1^2,x_2^2,x_1x_2$ (5). For $p=10$: $10+55=65$. That rapid growth is the notes' "excessive dimensionality" risk.

## 10. Time-window features

:::example Daily spend $x_1,\dots,x_6=100,120,90,150,130,400$; predicting at day 6
Use only days 1–5 (information available **before** the prediction):
- lag-1: $x_5=130$; difference $\Delta x_5=130-150=-20$; percentage change $-20/150=-13.3\%$.
- rolling mean, $w=3$: $(90+150+130)/3=123.3$; rolling SD $=\sqrt{\frac{(90-123.3)^2+(150-123.3)^2+(130-123.3)^2}{2}}\approx30.6$.

Day 6's 400 is **not** allowed in day 6's features. !!A centred window (days 5–7) would include the future — temporal leakage.!! After day 6 is observed, $\Delta x_6=270$ and $\%\Delta=270/130\approx208\%$ — a flag-worthy jump for fraud detection.
:::

## 11. Cyclical encoding

$$
x_{\sin}=\sin\frac{2\pi x}{P},\qquad x_{\cos}=\cos\frac{2\pi x}{P}.
$$

:::example Hours ($P=24$)
| hour | $\sin$ | $\cos$ |
|---|---|---|
| 0 | 0 | 1 |
| 6 | 1 | 0 |
| 12 | 0 | −1 |
| 18 | −1 | 0 |
| 23 | −0.259 | 0.966 |

As integers, hours 23 and 0 are 23 apart; on the circle their distance is $\sqrt{(-0.259-0)^2+(0.966-1)^2}\approx0.26$ — ==neighbours again==. Hours 0 and 12 are opposite ($2$, the maximum). Days ($P=7$, Monday $=0$, Sunday $=6$): Sunday–Monday distance $\approx0.87$, Monday–Thursday $\approx1.95$.
:::

## 12. Plot sizes and screening counts

- **Correlation heatmap:** $p$ variables → $\binom p2=p(p-1)/2$ distinct pairs. $p=100$ → **4,950** (notes). Expect some large values by chance.
- **Pair plot:** $p^2$ panels ($p$ diagonal + $p(p-1)$ off-diagonal); $p=6$ → 36 panels showing 15 distinct pairs.
- **Histogram bins:** equal width $=(x_{\max}-x_{\min})/k$. Data $1,2,2,3,4,5,6,8,15,40$ with 4 equal-width bins (width $9.75$) give counts $8,1,0,1$ — the outlier squashes almost everything into one bin; 4 equal-frequency bins (edges at quantiles $1,2.25,4.5,7.5,40$) hold about 2–3 values each.

## 13. Big Data paradox (Meng)

$$
\bar X_S-\bar X_U=\rho_{R,X}\sqrt{\frac{N-n}{n}}\;\sigma_X .
$$

:::example A biased million
Population $N=10{,}000{,}000$, dataset $n=1{,}000{,}000$, $\sigma_X=1$, and a small inclusion–outcome correlation $\rho_{R,X}=0.05$:
$$
\text{error}=0.05\sqrt{\frac{9{,}000{,}000}{1{,}000{,}000}}(1)=0.05\times3=0.15 .
$$
A **simple random sample** of the same size has standard error $\sigma/\sqrt n=0.001$ — 150 times smaller. With $n=100{,}000$ instead, the error is $0.05\sqrt{99}\approx0.50$: ten times less data, error only $\sqrt{10}\times$-ish larger, and ==no amount of $n$ removes $\rho_{R,X}$==. If $\rho_{R,X}=0$ (random inclusion), the bias term vanishes.
:::

## 14. Practice (answers hidden)

:::question P1. Data $\{5,7,8,9,10,11,12,40\}$. Find the mean, median, Type 7 $Q_1$ and $Q_3$, IQR and the fences. Is 40 an outlier by the rule? Should it be deleted?
:::solution Answer
Mean $=102/8=12.75$; median $=(9+10)/2=9.5$. Type 7: $Q_1$ at $1+7(0.25)=2.75$ → $7+0.75(1)=7.75$; $Q_3$ at $6.25$ → $11+0.25(1)=11.25$. IQR $=3.5$; fences $7.75-5.25=2.5$ and $11.25+5.25=16.5$. 40 lies beyond the upper fence, so it is **flagged**, but it should be **investigated, not deleted automatically** — it may be a genuine extreme or an error.
:::
:::

:::question P2. Compute the sample variance and SD of $\{2,4,4,4,5,5,7,9\}$.
:::solution Answer
Mean $=40/8=5$. Squared deviations: $9,1,1,1,0,0,4,16$, sum $32$. $s^2=32/7\approx4.57$, $s\approx2.14$. (Dividing by $n$ would give $4$ and SD $2$.)
:::
:::

:::question P3. $x=(1,2,3,4)$, $y=(10,20,40,80)$. Compute Pearson $r$ and Spearman $\rho_S$. Why do they differ?
:::solution Answer
$\bar x=2.5$, $\bar y=37.5$. Deviations $x$: $-1.5,-0.5,0.5,1.5$; $y$: $-27.5,-17.5,2.5,42.5$. $\sum$ products $=41.25+8.75+1.25+63.75=115$; $\sum dx^2=5$; $\sum dy^2=756.25+306.25+6.25+1806.25=2875$. $r=115/\sqrt{5\cdot2875}=115/119.9\approx0.96$. Ranks agree perfectly, so $\rho_S=1$. The relationship is perfectly **monotonic** but **not linear** (doubling), so Spearman is 1 while Pearson is below 1.
:::
:::

:::question P4. Training values $10,20,30,40,50$. Standardize the test value 65, and give its min–max value. What is unusual about the min–max result?
:::solution Answer
$\mu=30$, $s=\sqrt{1000/4}=15.81$ → $z=(65-30)/15.81\approx2.21$. Min–max $=(65-10)/(50-10)=1.375$ — **outside $[0,1]$**, because the test value exceeds the training maximum. That is expected and correct: you must not refit min/max on test data.
:::
:::

:::question P5. A category has 4 rows with outcomes $1,1,1,0$; the global rate is 0.2. Give its plain and smoothed ($\lambda=6$) target encodings.
:::solution Answer
Plain: $3/4=0.75$. Smoothed: $\dfrac{4(0.75)+6(0.2)}{4+6}=\dfrac{3+1.2}{10}=0.42$. Smoothing pulls a small category towards the global rate; out-of-fold computation is still needed to keep each row's own outcome out of its feature.
:::
:::

:::question P6. Encode 3 AM and 9 PM cyclically ($P=24$). Which of 9 PM and 3 AM is closer to midnight?
:::solution Answer
3 AM: $(\sin\frac{\pi}{4},\cos\frac{\pi}{4})=(0.707,0.707)$. 9 PM $=21$: $(\sin\frac{7\pi}{4},\cos\frac{7\pi}{4})=(-0.707,0.707)$. Midnight $=(0,1)$. Both are $\sqrt{0.707^2+0.293^2}\approx0.77$ from midnight — equally close (3 hours each way), which integer encoding (3 vs 21) would hide.
:::
:::

:::question P7. A dataset has 1,200 rows; blood pressure is missing in 96 rows, heart rate in 90, and 85 rows are missing both. Compute $r_j$ for each and comment on the pattern.
:::solution Answer
$r_{\text{BP}}=96/1200=0.08$, $r_{\text{HR}}=90/1200=0.075$. 85 of the ~90 missing heart-rate rows also miss BP: a strong **pattern-level** co-missingness, suggesting one cause (e.g. a failed monitoring device), not random gaps. Investigate the cause, and check whether it is concentrated in particular wards or times (subgroup-level).
:::
:::

:::question P8. Model: $\hat y=2+0.5x_1+1.2x_2-0.3x_1x_2$. What is the effect of a one-unit increase in $x_1$ when $x_2=0$ and when $x_2=4$?
:::solution Answer
$\partial\hat y/\partial x_1=0.5-0.3x_2$: $0.5$ at $x_2=0$; $0.5-1.2=-0.7$ at $x_2=4$. The effect of $x_1$ **changes sign** depending on $x_2$ — a genuine interaction.
:::
:::
