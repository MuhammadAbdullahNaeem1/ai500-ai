# Mock Quiz 3A — Hospital emergency department

Module 3, §3.1–3.5 · in the style announced for Quiz 3 · try each question before opening the model answer. Marks follow the midterm's rubric style: one mark per distinct, justified point.

<div class="pdf-links">
<a href="quiz3-guide.html">Quiz 3 guide</a>
<a href="m3a-notes.html">M3 Notes A</a>
<a href="m3b-notes.html">M3 Notes B</a>
</div>

**Scenario.** A hospital wants to understand emergency-department (ED) waiting times before building a model that flags patients at risk of waiting more than 4 hours. The dataset has one row per **ED visit** for 18 months: arrival time, triage category (1 = most urgent … 5 = least urgent), age, sex, insurance type, whether a lab test was ordered, the lab result (if any), waiting time in minutes, and whether the patient left without being seen. About 40,000 visits come from 22,000 patients.

:::question Q1 (4 marks) — Choose your tools
The manager asks: "How long do patients usually wait, and how bad are the worst waits?" Which exploratory approach would you use — numerical, graphical or hybrid? Name the specific tools and justify the choice.

:::solution
A **hybrid** approach (1).

- **Graphical:** a histogram of waiting time (checked with at least two bin widths) to see the shape — waiting times are expected to be strongly right-skewed with a long upper tail — and/or an ECDF, which shows the proportion of patients waiting at most any given time without binning choices (1).
- **Numerical:** the **median** for the typical wait (the mean would be pulled up by the long tail) and the **90th/95th percentiles** for the worst waits, plus the IQR for spread (1).
- **Why hybrid / caveat:** the plot shows the skew and any heaping or gaps; the quantiles answer the manager's two questions in numbers. State the quantile method used, and report the results **by triage category**, because a pooled figure mixes urgent and non-urgent patients (1).
:::
:::

:::question Q2 (4 marks) — Analyse a plot
The analyst shows a boxplot of waiting time for all visits. The box sits between 35 and 140 minutes, the median is at 70 minutes, the upper whisker reaches 297 minutes, and there are **hundreds** of points plotted above it, some beyond 900 minutes. The analyst proposes deleting every point above the whisker as "outliers". Analyse the plot and respond to the proposal.

:::solution
- **Reading:** IQR $=140-35=105$ min, so the upper fence is $140+1.5(105)=297.5$ min. The median sits nearer the bottom of the box and the upper side is much longer: **strong right skew** (1).
- **Points above the whisker are not automatically errors.** In a right-skewed, heavy-tailed variable like waiting time, many legitimate long waits lie beyond $1.5\times$IQR — and they are exactly the cases the model is meant to flag (> 240 min). Deleting them would remove the target cases and understate the problem (1).
- **Investigate instead:** flag → verify → explain → correct or retain → document. Values beyond 900 min (15 h) may be genuine (boarding patients) or errors (a missing discharge time filled with the next day's timestamp, clock errors) — check them against the visit records (1).
- **Limitations of the plot:** a single pooled boxplot hides multimodality and group differences; plot waiting time **by triage category** (and add the individual points or a violin plot) (1).
:::
:::

:::question Q3 (4 marks) — Is this enough?
A scatterplot of age (x) against waiting time (y) shows a weak positive trend with Pearson $r=0.18$. The analyst concludes: "Age barely matters for waiting time, so we can drop it." Is this analysis enough? What else needs to be done, and why?

:::solution
**No** (the conclusion is not supported).

- **Form of the relationship:** $r$ measures only *linear* association. Waiting time could relate to age non-linearly (e.g. children and the very old triaged faster or slower); look at the scatterplot shape and Spearman's $\rho_S$ or age bands (1).
- **Subgroups / confounding:** triage category affects both age mix and waiting time. Within triage groups the age relationship may be stronger, weaker or reversed; stratify by triage (1).
- **Unit of analysis:** rows are visits, not patients — 22,000 patients contribute 40,000 visits, so frequent attenders are over-represented and rows are not independent (1).
- **Overplotting / heteroscedasticity:** with 40,000 points the scatterplot needs transparency or hexbin; spread may fan out with age. And a weak *marginal* association does not mean the feature is useless in a model (it may interact with triage) (1).
:::
:::

:::question Q4 (4 marks) — Missingness
Lab results are missing for 62% of visits overall. By triage category the missing rate is 15% (cat. 1), 30% (cat. 2), 70% (cat. 4) and 90% (cat. 5). Interpret this pattern and say what it means for the model.

:::solution
- **The missingness is not random:** it depends strongly on triage (a subgroup-specific pattern, $P(\text{lab missing}\mid G=g)$). Labs are ordered mostly for urgent patients, so "missing" largely means "the clinician did not think a test was needed" (1).
- **Consequence 1:** dropping incomplete rows keeps mostly urgent patients — the effective sample size collapses for categories 4–5 and the data no longer represent the ED population (1).
- **Consequence 2:** imputing lab values for category 5 patients would be unreliable and could distort their distribution (differential imputation error) (1).
- **What to do:** keep a **missingness indicator** as a feature (the fact a test was not ordered is informative), report missingness by subgroup, and evaluate the model separately by triage category (1).
:::
:::

:::question Q5 (4 marks) — Feature engineering
Propose features from **arrival time** and **triage category**, and name one leakage risk.

:::solution
- **Arrival time:** hour of day and day of week with **cyclical** encoding, $\sin(2\pi h/24),\cos(2\pi h/24)$, so 23:00 and 00:00 are neighbours; a weekend/holiday indicator (1).
- **Time-window features:** number of arrivals in the previous hour (current crowding), rolling mean waiting time over the previous 3 hours — computed **only from information available at the patient's arrival** (1).
- **Triage category:** it is **ordinal**, so an ordinal code 1–5 is defensible; one-hot encoding is also safe for a linear model (drop one category as the reference) (1).
- **Leakage risk:** using "left without being seen", the lab result, or a centred rolling average that includes later arrivals — none of these is known when the flag must be raised. Also fit any scaling or encoding on the training period only and split by time and by patient (1).
:::
:::
