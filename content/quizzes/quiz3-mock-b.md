# Mock Quiz 3B — Online retail and pathological plots

Module 3, §3.1–3.5 · in the style announced for Quiz 3 · try each question before opening the model answer.

<div class="pdf-links">
<a href="quiz3-guide.html">Quiz 3 guide</a>
<a href="m3a-notes.html">M3 Notes A</a>
<a href="m3b-notes.html">M3 Notes B</a>
</div>

**Scenario.** An online store has 2 million transaction rows from 150,000 customers over two years: transaction amount (PKR), product category (38 categories), customer city (1,400 cities), device (Android/iOS/Web), timestamp, discount applied (yes/no), and whether the order was returned. The team wants to understand spending and later predict returns.

:::question Q1 (4 marks) — Pathological histogram
A histogram of transaction amount with 10 equal-width bins from 0 to 2,000,000 PKR shows almost all transactions in the **first bar** and nothing visible elsewhere. Explain what is going on and how you would explore the variable properly.

:::solution
- **Diagnosis:** "outliers dominating the scale". A few very large transactions stretch the x-axis to 2 million, so each bin is 200,000 PKR wide and the whole typical range falls into one bar — the central structure is hidden (1).
- **Genuine or artefact?** The large values may be real (bulk/business orders — a heavy right tail is expected for spending) or errors (extra zeros, test orders, a currency mix-up). Inspect the top transactions before deciding (1).
- **Better views:** zoom to the bulk (e.g. 0–20,000) with finer bins, try several bin widths, use a **log** scale or $\log(1+x)$, and add an ECDF or boxplot (1).
- **Numbers:** report the median, IQR and upper quantiles (95th/99th) rather than only the mean and SD, which the tail inflates (1).
:::
:::

:::question Q2 (4 marks) — Heaping
After zooming, the histogram shows sharp spikes at 999, 1,999, 2,499 and 4,999 PKR, with low bars in between. A colleague suspects a data error. Analyse.

:::solution
- **Pattern:** heaping/spikes at particular values (1).
- **Genuine explanation:** retail price points — products are priced at 999, 1,999 and so on, so many single-item orders have exactly these amounts. This is real structure, not an error (1).
- **Interpretation caution:** the spikes reflect pricing, so the "shape" between spikes is partly an artefact of bin boundaries; don't read the dips as meaningful gaps (1).
- **Next step:** check how many items each order has (single-item orders create the spikes), and look at an ECDF, where heaping appears as vertical steps without any binning choice (1).
:::
:::

:::question Q3 (4 marks) — Correlation heatmap
A heatmap of 25 numerical customer features (total spend, number of orders, average basket, days since last order, …) uses a colour scale from 0.0 to 0.2. The team picks the 5 "darkest" pairs as key relationships. Discuss the advantages of a heatmap here and its limitations.

:::solution
- **Advantages:** screens all $25\cdot24/2=300$ pairs at once; reveals blocks of related or redundant features (e.g. total spend vs number of orders), and possible multicollinearity before modelling (1).
- **Limitation — colour scale:** a 0–0.2 scale makes tiny differences look dramatic; correlations should be shown on a symmetric $-1$ to $1$ scale, so the "darkest" pairs may all be weak (1).
- **Limitation — many comparisons and form:** with 300 pairs some moderate values arise by chance; Pearson $r$ misses non-linear relations and can be driven by a few big spenders (heavy tails) (1).
- **What to do:** scatterplots (with transparency/log scales) for the selected pairs, Spearman correlations for skewed variables, check $n$ per pair if values are missing, and confirm on a held-out period (1).
:::
:::

:::question Q4 (4 marks) — Unit of analysis and encoding
The team plans a random 80/20 split of the 2 million transaction rows to predict returns, with target encoding of **city** computed on the full dataset. Identify the problems and fix them.

:::solution
- **Unit of analysis:** the unit of observation is a transaction, but customers appear many times. A random row split puts the same customer in train and test — **identity leakage** — so test performance is optimistic. Split by **customer** (and by time if predicting future returns) (1).
- **Target encoding on the full data:** the encoded value for each city uses the return outcomes of the test rows and of the row itself — **target leakage** (1).
- **Fix:** fit target encoding **on the training data only**, with **out-of-fold** (cross-fitted) estimates for training rows and **smoothing** towards the global return rate for small cities: $\dfrac{n_c\bar y_c+\lambda\bar y}{n_c+\lambda}$ (1).
- **Rare and unseen cities:** 1,400 cities include many with very few customers; group rare cities into "Other" or use a region hierarchy, and define a fallback (global mean / "unknown") for cities first seen at deployment (1).
:::
:::

:::question Q5 (4 marks) — Is a mean enough?
A report says: "Customers using iOS spend on average 2,900 PKR per order versus 2,100 on Android, so iOS users are more valuable." Is this enough? What else would you check?

:::solution
**No.**

- **Skew:** order amounts are right-skewed; a few large orders can drive the mean. Compare medians and IQRs, and side-by-side boxplots/ECDFs (1).
- **Unit and weighting:** the means are per **order**; heavy buyers contribute many rows. Compare per-customer averages too (1).
- **Subgroups/confounding:** device mix may differ by city, product category or income; compare within categories and cities — the gap could shrink or reverse (1).
- **Causation and returns:** a higher basket says nothing about *value* if return rates differ, and device does not *cause* spending. Treat it as an exploratory hypothesis to confirm on new data (1).
:::
:::
