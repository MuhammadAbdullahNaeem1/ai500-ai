# Mock Quiz 3C — Air-quality sensors and student data

Module 3, §3.1–3.5 · in the style announced for Quiz 3 · try each question before opening the model answer.

<div class="pdf-links">
<a href="quiz3-guide.html">Quiz 3 guide</a>
<a href="m3a-notes.html">M3 Notes A</a>
<a href="m3b-notes.html">M3 Notes B</a>
</div>

**Scenario A.** A city has 30 low-cost PM2.5 sensors reporting every 10 minutes for one year. Some sensors were replaced in June with a newer model. The goal is to explore pollution patterns and later forecast next-day PM2.5.

:::question Q1 (4 marks) — Choose your tools
Which exploratory tools would you use to understand (a) how PM2.5 changes over the year and the day, and (b) whether the 30 sensors agree with each other? Justify.

:::solution
(a) **Time-series plots** of the raw readings with a moving average overlaid, to see trend, seasonality (winter smog) and daily cycles; plot average by hour of day to show the daily pattern. Keep raw data visible because smoothing hides short spikes; mark missing periods (2).

(b) **Side-by-side boxplots** (or violins) of each sensor's readings with $n$ per sensor, plus a **correlation heatmap / scatterplots** between nearby sensors. Strongly correlated neighbours that differ by a constant offset suggest calibration differences; a sensor that disagrees with all neighbours suggests a fault (2).
:::
:::

:::question Q2 (4 marks) — Analyse a time-series plot
One sensor's series shows a sudden **step up of about 20 µg/m³ in mid-June** that persists for the rest of the year; its neighbours show no such step. Analyse.

:::solution
- **Pattern:** an abrupt level shift / regime change in one series only (1).
- **Likely cause:** the sensor replacement in June — a **measurement bias** (the new device reads systematically higher), not a real pollution change, because neighbours do not show it (1).
- **Check:** confirm the replacement date for that sensor, compare its readings with neighbours before and after, and look for drift in other replaced sensors (1).
- **Action:** document it; correct with a calibration offset estimated from co-located/neighbour data, or add a "device version" feature — don't let the model learn a fake trend (1).
:::
:::

:::question Q3 (4 marks) — Pathological density plot
A KDE of hourly PM2.5 shows probability mass **below 0**, and a separate tall narrow spike at exactly 5 µg/m³. Explain both features.

:::solution
- **Mass below zero:** **boundary bias** of the kernel density — PM2.5 cannot be negative, but a smooth kernel near the boundary spills probability past 0. It is an artefact of the estimator, not real data (1). Use a boundary-aware method or show a histogram/ECDF, which cannot go below the smallest value (1).
- **Spike at 5:** a **detection limit** — readings below the sensor's lower limit are recorded as the same value, producing a pile-up (truncation/censoring) (1). Treat these as "≤ 5" (censored) rather than exact values, and say so when reporting means (1).
:::
:::

**Scenario B.** A university studies 3,000 students: weekly study hours, attendance (%), first-year GPA, department, and whether they graduated within 4 years. A dataset of **graduates only** is used to show "high attendance leads to high GPA".

:::question Q4 (4 marks) — Bias and causation
Identify the problems in the claim and explain how each could distort the conclusion.

:::solution
- **Survivorship / selection bias:** using only graduates excludes students who dropped out — often those with low GPA and low attendance — so the observed relationship (and the average GPA) does not represent all students (1).
- **Restricted range:** after selection, attendance and GPA vary less, which can weaken or distort the correlation (1).
- **Causation:** "leads to" is causal; EDA only shows association. Alternatives: motivation or prior ability drives both (confounding), poor grades lower attendance (reverse causation) (1).
- **Subgroups:** department differences in grading and attendance rules may create or mask the pattern; check within departments (1).
:::
:::

:::question Q5 (4 marks) — Feature engineering choices
For predicting graduation, propose (a) a treatment for **weekly study hours**, which is right-skewed with a few students reporting 80+ hours, and (b) a treatment for **attendance** for a logistic regression. Mention one risk of each.

:::solution
(a) **Study hours:** a $\log(1+x)$ or $\sqrt x$ transform reduces skew, or **robust scaling** $(x-\text{median})/\text{IQR}$; first check whether 80+ hours are genuine or entry errors (1). *Risk:* the transformed scale is harder to interpret; the same transform must be applied at deployment (train–serving consistency) (1).

(b) **Attendance:** standardise with the **training** mean and SD, or bin into domain-meaningful bands (e.g. below the 75% attendance requirement) if there is a real policy threshold (1). *Risk:* binning discards information and creates artificial jumps near the cut-points; fitting scaling on the full dataset leaks test information (1).
:::
:::
