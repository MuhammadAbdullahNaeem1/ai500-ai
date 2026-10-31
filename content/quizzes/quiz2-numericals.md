# Quiz 2 numericals — confusion matrix, F1 and ROC

**Module 2 · worked on the board in class, 17 October 2026.** The instructor's example, step by step, with the board photos and extra practice. The method applies to any confusion-matrix question on the mid.

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

## 7. Practice

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
