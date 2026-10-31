# Quiz 2 numericals — confusion matrix, ROC, IQR and kappa

**Module 2 · worked on the board in class, 17 October 2026.** The instructor's example step by step with the board photos, plus IQR from the basics, Cohen's and Fleiss' kappa, two corrections to the notes, and practice.

<div class="pdf-links">
<a href="pdfs/quizzes/Board-Numericals-17-Oct.pdf">Board photos (PDF)</a>
<a href="quiz2-solved.html">Real Quiz 2 (solved)</a>
<a href="m2b-notes.html">Module 2 Part B</a>
<a href="mid-guide.html">Mid guide</a>
</div>

<div class="hl-legend">
<span><mark class="hl">Yellow</mark> the one line to remember</span>
<span><span class="key">Blue</span> keywords a rubric looks for</span>
<span><mark class="trap">Coral</mark> a common trap</span>
</div>

## 1. Setup: from probability to class

A **model** $M$ outputs a probability $p\in[0,1]$. Close to 0 means no disease, close to 1 means disease, and close to 0.5 is ambiguous. With **threshold** $\tau=0.5$:

$$p\ge\tau\ \to\ \text{disease}\qquad\qquad p<\tau\ \to\ \text{non-disease}$$

Class example: $N=100$ subjects, of whom $D=40$ have the disease and $ND=60$ do not.

## 2. Confusion matrix

| Actual ↓ / Predicted → | Predicted +ve | Predicted −ve | Row total |
|---|---|---|---|
| **Disease (+ve)** | TP = 35 | FN = 5 | 40 |
| **No disease (−ve)** | FP = 10 | TN = 50 | 60 |

==Rows are the truth and columns are the prediction.== The first letter says whether the prediction was right (T/F); the second says what was predicted (P/N).

## 3. The class example, worked

:::question Sensitivity (TPR)
$$\text{Sens}=\frac{TP}{TP+FN}=\frac{35}{35+5}=\frac{35}{40}=\frac78=0.875$$
Of all diseased patients, how many did we catch? ==Sensitivity, recall and TPR are the same quantity.==
:::

:::question Specificity (TNR)
$$\text{Spec}=\frac{TN}{TN+FP}=\frac{50}{50+10}=\frac56=0.833$$
Of all healthy patients, how many did we correctly clear?
:::

:::question Precision
$$\text{Prec}=\frac{TP}{TP+FP}=\frac{35}{35+10}=\frac{35}{45}=\frac79=0.778$$
Of everyone we flagged, how many really have the disease?

:::warn Slip on the board
The board shows $7/8$ here, but $35/45=7/9$. The decimal on the board, 0.778, is correct. Use $7/9$.
:::
:::

:::question Recall
$$\text{Recall}=\frac{TP}{TP+FN}=\text{Sens}=0.875$$
:::

:::question F1 score
The harmonic mean of precision and recall, where $H(a,b)=\dfrac{2ab}{a+b}$:
$$F_1=\frac{2PR}{P+R}=\frac{2(0.778)(0.875)}{0.778+0.875}=0.8235$$
Check with counts: $F_1=\dfrac{2TP}{2TP+FP+FN}=\dfrac{70}{85}=0.8235$. Always $F_1\in[0,1]$.
:::

:::question False positive rate (FPR)
$$\text{FPR}=1-\text{TNR}=1-\text{Specificity}=\frac{FP}{FP+TN}=\frac{10}{10+50}=\frac16=0.1667$$
:::

:::question Accuracy
$$\text{Acc}=\frac{TP+TN}{TP+FP+TN+FN}=\frac{35+50}{100}=0.85$$
:::

| Metric | Value |
|---|---|
| Sensitivity = Recall = TPR | 0.875 |
| Specificity = TNR | 0.833 |
| Precision | 0.778 |
| $F_1$ | 0.8235 |
| FPR | 0.1667 |
| Accuracy | 0.85 |

## 4. The imbalance trap

Now only **5** of 100 subjects have the disease, and the model catches none of them.

| Actual ↓ / Predicted → | Predicted +ve | Predicted −ve | Row total |
|---|---|---|---|
| **+ve** | TP = 0 | FN = 5 | 5 |
| **−ve** | FP = 5 | TN = 90 | 95 |

$$\text{Acc}=\frac{0+90}{100}=0.90\qquad P=\frac{0}{0+5}=0\qquad R=\frac{0}{0+5}=0\qquad F_1=0$$

!!90% accuracy, yet the model finds no disease at all.!! $F_1$ exposes what accuracy hides. Predicting "no disease" for everyone would score even higher, at 95%.

> **Notes wording** — “Overall accuracy may provide an overly optimistic assessment of performance when classes are highly imbalanced.” (M2 p.64)

$F_1$ as a formula is $\frac{2\cdot0\cdot0}{0+0}$, which is strictly $0/0$. The board writes 0, the usual convention when $TP=0$.

## 5. ROC curve and AUC

==For every threshold $\tau$ we get one point (FPR, TPR).== Sweeping $\tau$ traces the **ROC curve**. In the class example, $\tau=0.5$ gives the point $(0.1667,\ 0.875)$.

<figure class="board"><a href="assets/board/roc.jpg" class="zoom"><img src="assets/board/roc.jpg" alt="Board: precision, recall and F1 all zero on the left; ROC curves with TPR against FPR on the right" loading="lazy"></a><figcaption>Board, 17 October. ROC curves bending towards the top-left, with the diagonal at AUC 0.5.</figcaption></figure>

- **AUC / AUROC** is the area under this curve.
- The **perfect** curve hugs the top-left corner: maximum AUC $=1$.
- The **diagonal** is a model with no skill: AUC $=0.5$.
- A curve closer to the top-left is better.
- Moving along one curve is a **trade-off**: a lower $\tau$ raises TPR but also raises FPR.

AUROC measures ranking, so a high AUC does not show that the probabilities are calibrated.

> **Notes wording** — “The team only measures discrimination (ranking ability)” (M1 p.67)

## 6. Sketch: is missingness related to age?

The last board photo is a diagram, not a calculation, and it is only partly legible. It shows a table with **age** and **wealth/salary** columns, then a curve of **missingness** rising across age bins that look like deciles.

<figure class="board"><a href="assets/board/missingness.jpg" class="zoom"><img src="assets/board/missingness.jpg" alt="Board sketch: a data table with age and salary, and a curve of missingness rising across age bins" loading="lazy"></a><figcaption>Board, 17 October. The labels are hard to read, so check this against your own class notes.</figcaption></figure>

My reading: bin one variable and plot the missing rate of another in each bin. If the rate changes with age, missingness depends on an observed variable, which points to MAR rather than MCAR. This is my interpretation, not the instructor's written statement.

> **Notes wording** — “Here, missingness may depend on observed variables but not on the missing values themselves after conditioning on the observed data.” (§2.5.1)

## 7. IQR and outliers, from the very beginning

:::note What this answers
How do I spot an unusually large or small value? The IQR gives a rule for it using only sorting and the middle of a list.
:::

### Step 0: What is a median?

Sort the numbers. The **median** is the middle one, so half the values lie below it.

- **Odd count:** take the middle value. For 3, 5, 9 the median is 5.
- **Even count:** average the two middle values. For 3, 5, 9, 11 the median is $(5+9)/2=7$.

### Step 1: What are quartiles?

Quartiles cut sorted data into **four equal parts**.

| Symbol | Name | Meaning |
|---|---|---|
| $Q_1$ | First quartile | About 25% of values lie below it |
| $Q_2$ | Median | About 50% lie below it |
| $Q_3$ | Third quartile | About 75% lie below it |

> **Notes wording** — “A quartile is a specific type of quantile that divides an ordered dataset into four parts of approximately equal size.” (M3 §3.4.6)

### Step 2: What is the IQR?

$$\text{IQR}=Q_3-Q_1$$

It is the width of the middle 50% of the data. ==Extreme values barely move it, because it ignores the top and bottom quarters.==

> **Notes wording** — “A measure of statistical dispersion defined as the difference between the third quartile” (§2.5.2, footnote 213)

### Step 3: The screening fences

$$\text{Lower fence}=Q_1-1.5\times\text{IQR}\qquad\text{Upper fence}=Q_3+1.5\times\text{IQR}$$

Any value outside the fences is **flagged**, meaning it needs checking. It does not mean delete it.

> **Notes wording** — “These methods identify observations for further investigation rather than providing automatic criteria for deletion.” (§2.5.2)

### Worked example: odd count

Resting heart rates for 11 patients: 72, 68, 75, 70, 74, 69, 71, 73, 180, 67, 76.

| Step | Working |
|---|---|
| 1. Sort | 67, 68, 69, 70, 71, **72**, 73, 74, 75, 76, 180 |
| 2. Median | 11 values, so the 6th: $Q_2=72$ |
| 3. Lower half | 67, 68, **69**, 70, 71, so $Q_1=69$ |
| 4. Upper half | 73, 74, **75**, 76, 180, so $Q_3=75$ |
| 5. IQR | $75-69=6$ |
| 6. 1.5 × IQR | $1.5\times6=9$ |
| 7. Fences | $[69-9,\ 75+9]=[60,\ 84]$ |
| 8. Check | 180 is above 84, so it is **flagged** |

With an odd count, leave the median out of both halves.

**Next step:** ask why it is 180. A typing error for 80? A sensor fault? A real emergency? Only the source can tell you.

### Worked example: even count

Waiting times in minutes: 12, 7, 9, 15, 8, 10, 11, 40.

| Step | Working |
|---|---|
| 1. Sort | 7, 8, 9, 10, 11, 12, 15, 40 |
| 2. Split in half | 7, 8, 9, 10 and 11, 12, 15, 40 |
| 3. $Q_1$ | Median of the lower half: $(8+9)/2=8.5$ |
| 4. $Q_3$ | Median of the upper half: $(12+15)/2=13.5$ |
| 5. IQR | $13.5-8.5=5$ |
| 6. Fences | $[8.5-7.5,\ 13.5+7.5]=[1,\ 21]$ |
| 7. Check | 40 is above 21, so it is **flagged** |

### The z-score, and why the IQR is more robust

$$z_i=\frac{x_i-\bar x}{s}$$

This says how many standard deviations a value sits from the mean. In the heart-rate data, $\bar x=81.4$ and $s=32.8$, so:

$$z_{180}=\frac{180-81.4}{32.8}\approx3.0$$

!!The outlier inflates the very mean and $s$ used to judge it.!! Without 180, the mean is 71.5 and $s$ is 3.0. With it, the mean jumps to 81.4 and $s$ to 32.8. The quartiles barely change, which is why the notes call the IQR “a more robust alternative”.

:::warn Quartiles can differ slightly by method
Software such as NumPy interpolates and gives $Q_1=69.5$, $Q_3=74.5$ for the heart-rate data. The fences become $[62,\ 82]$ and 180 is still flagged. In an exam, show your working so your method is clear. The notes do not fix one hand method.

> **Notes wording** — “Different statistical software packages can therefore produce slightly different sample quantiles because they use different interpolation or estimation conventions.” (M3 §3.4.6)
:::

## 8. Cohen's κ — two raters

Sir has confirmed that Cohen's and Fleiss' kappa are discussed in Module 2. They are listed in §2.5.3 as inter-annotator agreement measures (printed p. 229). The notes' worked examples are in §3.11, and these are used below.

> **Notes wording** — “Cohen's κ is a statistical measure used to assess the level of agreement between two raters who classify the same items into categories. It accounts for the agreement that could occur by chance.” (§3.11.1)

Two people can agree often just by luck. ==κ asks how much better the agreement is than chance.==

**Notes' example:** two teachers grade the same 50 students as Pass or Fail.

| A ↓ / B → | B: Pass | B: Fail | Total |
|---|---|---|---|
| **A: Pass** | 30 | 5 | 35 |
| **A: Fail** | 3 | 12 | 15 |
| **Total** | 33 | 17 | 50 |

**Step 1: Observed agreement.** Add the diagonal, where both agree.
$$P_o=\frac{30+12}{50}=0.84$$

**Step 2: Agreement expected by chance.** Use the totals.

| | Teacher A | Teacher B |
|---|---|---|
| Pass | $35/50=0.70$ | $33/50=0.66$ |
| Fail | $15/50=0.30$ | $17/50=0.34$ |

$$P_e=\sum_{i=1}^{k}P_{Ai}\times P_{Bi}=(0.70\times0.66)+(0.30\times0.34)=0.462+0.102=0.564$$

**Step 3: Compute κ.**
$$\kappa=\frac{P_o-P_e}{1-P_e}=\frac{0.84-0.564}{1-0.564}\approx0.633$$

**Step 4: Interpret** with the Landis and Koch scale.

| κ | Interpretation |
|---|---|
| $\le0$ | Poor agreement |
| 0.01–0.20 | Slight agreement |
| 0.21–0.40 | Fair agreement |
| 0.41–0.60 | Moderate agreement |
| 0.61–0.80 | Substantial agreement |
| 0.81–1.00 | Almost perfect agreement |

So 0.633 is **substantial agreement**. The teachers agree on 84% of students, but after removing chance the figure is about 0.633.

> **Notes wording** — “Note that these ranges are guidelines, not universal thresholds.” (§3.11.1)

## 9. Fleiss' κ — three or more raters

> **Notes wording** — “Fleiss' κ extends this approach to assess agreement among multiple raters.” (§3.11)

**Notes' example:** three experts ($n=3$) classify 5 abstracts ($N=5$) as Relevant or Not Relevant ($k=2$).

| Abstract | Relevant | Not Relevant | Working for $P_i$ | $P_i$ |
|---|---|---|---|---|
| 1 | 3 | 0 | $\frac16(3^2+0^2-3)$ | 1 |
| 2 | 2 | 1 | $\frac16(2^2+1^2-3)$ | 1/3 |
| 3 | 2 | 1 | $\frac16(2^2+1^2-3)$ | 1/3 |
| 4 | 1 | 2 | $\frac16(1^2+2^2-3)$ | 1/3 |
| 5 | 0 | 3 | $\frac16(0^2+3^2-3)$ | 1 |
| **Total** | **8** | **7** | | **3** |

**Step 1: Agreement on each item, then the average.**
$$P_i=\frac{1}{n(n-1)}\left(\sum_{j=1}^{k}n_{ij}^2-n\right)\qquad n(n-1)=3\times2=6$$
Square each count, add them, subtract $n$, then divide by 6.
$$\bar P=\frac1N\sum_{i=1}^{N}P_i=\frac{1+\frac13+\frac13+\frac13+1}{5}=\frac35=0.60$$

**Step 2: Chance agreement.** There are 15 ratings in all, so $p_1=\frac{8}{15}$ and $p_2=\frac{7}{15}$.
$$\bar P_e=\sum_{j=1}^{k}p_j^2=\left(\frac{8}{15}\right)^2+\left(\frac{7}{15}\right)^2=0.5022$$

**Step 3: Compute κ.**
$$\kappa=\frac{\bar P-\bar P_e}{1-\bar P_e}=\frac{0.600-0.5022}{1-0.5022}\approx0.196$$

**Step 4: Interpret.** κ ≈ 0.20 is **slight agreement**. !!60% agreement sounds fine, but chance alone already gives about 50%.!!

| | Cohen's κ | Fleiss' κ |
|---|---|---|
| Raters | Exactly 2 | 3 or more |
| Chance term | $\sum P_{Ai}P_{Bi}$ (each rater's own totals) | $\sum p_j^2$ (pooled totals) |
| Formula | $\dfrac{P_o-P_e}{1-P_e}$ | $\dfrac{\bar P-\bar P_e}{1-\bar P_e}$ |

## 10. Corrections to the Module 2 notes

:::warn Learn the corrected versions
**1. IQR rule, §2.5.2, printed p. 223.** The main text prints the rule as $[Q_1-1.5\,\text{IQR},\ Q_3-1.5\,\text{IQR}]$. The upper bound should be $Q_3+1.5\,\text{IQR}$. Footnote 213 on the same page has it right.

**2. Example 52, §2.5.4, printed pp. 233–234.** Both approaches are headed "Incorrect approach". The second, "partition first, then oversample", describes the right method: split first, oversample only the training set, and leave the test set unchanged. Its heading should presumably read "Correct approach".
:::

## 11. Practice

These are new sets for practice, not from the board. Compute everything, then open the answer.

:::question Set 1 [balanced case] TP = 48, FN = 12, FP = 8, TN = 132. Find accuracy, sensitivity, specificity, precision, FPR and $F_1$.
:::solution Answer
$N=200$. Accuracy $=\frac{180}{200}=0.90$. Sensitivity $=\frac{48}{60}=0.80$. Specificity $=\frac{132}{140}=0.943$. Precision $=\frac{48}{56}=0.857$. FPR $=\frac{8}{140}=0.057$. $F_1=\frac{96}{96+8+12}=\frac{96}{116}=0.828$.
:::
:::

:::question Set 2 [rare disease] TP = 9, FN = 21, FP = 30, TN = 940. Find accuracy, recall, precision and $F_1$. Compare the accuracy with always predicting negative. Is this model good?
:::solution Answer
$N=1000$, with 30 positives. Accuracy $=\frac{949}{1000}=0.949$. Recall $=\frac{9}{30}=0.30$. Precision $=\frac{9}{39}=0.231$. $F_1=\frac{18}{18+30+21}=\frac{18}{69}=0.261$.
Always negative gives $\frac{970}{1000}=0.97$, which beats the model. So no: it looks accurate but misses 70% of cases, and most of its flags are false alarms.
:::
:::

:::question Set 3 [screening] TP = 18, FN = 2, FP = 40, TN = 140. Find recall, FPR and precision. Why is precision low when recall is high? Give the ROC point for this threshold.
:::solution Answer
Recall $=\frac{18}{20}=0.90$. FPR $=\frac{40}{180}=0.222$. Precision $=\frac{18}{58}=0.310$.
Negatives outnumber positives 9 to 1, so even a modest FPR produces more false alarms (40) than true cases (18). The ROC point is $(0.222,\ 0.90)$.
:::
:::

:::question Set 4 [IQR, even count] Scores: 22, 25, 28, 30, 24, 26, 29, 27, 23, 31, 5, 60. Find $Q_1$, $Q_3$, the IQR and the fences. Which values are flagged?
:::solution Answer
Sorted: 5, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 60. Lower half: 5, 22, 23, 24, 25, 26, so $Q_1=23.5$. Upper half: 27, 28, 29, 30, 31, 60, so $Q_3=29.5$. IQR $=6$. Fences $=[23.5-9,\ 29.5+9]=[14.5,\ 38.5]$. Flagged: **5 and 60**, which should be investigated, not deleted.
:::
:::

:::question Set 5 [IQR, odd count] Values: 40, 45, 48, 50, 52, 55, 58, 60, 120. Find the median, $Q_1$, $Q_3$, the IQR and the fences. Is 120 flagged?
:::solution Answer
Median $=52$. Lower half: 40, 45, 48, 50, so $Q_1=46.5$. Upper half: 55, 58, 60, 120, so $Q_3=59$. IQR $=12.5$. $1.5\times12.5=18.75$. Fences $=[27.75,\ 77.75]$. Yes, 120 is flagged.
:::
:::

:::question Set 6 [Cohen's κ, 3 categories] Two doctors label 100 scans. Rows are Doctor A and columns are Doctor B, in the order Mild, Moderate, Severe. Row 1: 20, 5, 0. Row 2: 10, 25, 5. Row 3: 0, 5, 30. Find $P_o$, $P_e$ and κ, then interpret it.
:::solution Answer
$P_o=\frac{20+25+30}{100}=0.75$. A's totals: 0.25, 0.40, 0.35. B's totals: 0.30, 0.35, 0.35.
$P_e=(0.25)(0.30)+(0.40)(0.35)+(0.35)(0.35)=0.075+0.14+0.1225=0.3375$.
$\kappa=\frac{0.75-0.3375}{1-0.3375}\approx0.623$, which is **substantial agreement**.
:::
:::

:::question Set 7 [Fleiss' κ] Four raters ($n=4$) label 6 images as Yes/No. Counts (Yes, No): (4,0), (3,1), (2,2), (4,0), (0,4), (1,3). Find $\bar P$, $\bar P_e$ and κ.
:::solution Answer
$n(n-1)=12$. $P_i$: 1, 1/2, 1/3, 1, 1, 1/2. Sum $=4.333$, so $\bar P=\frac{4.333}{6}=0.722$.
24 ratings: Yes $=14$, No $=10$, so $p_1=\frac{7}{12}$, $p_2=\frac{5}{12}$. $\bar P_e=0.3403+0.1736=0.5139$.
$\kappa=\frac{0.7222-0.5139}{1-0.5139}\approx0.429$, which is **moderate agreement**.
:::
:::
