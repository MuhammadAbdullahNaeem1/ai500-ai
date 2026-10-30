# Real Quiz 2 (solved) — 24 October 2026

**20 points · 30 minutes · Module 2.** The instructor's solution scheme, condensed. The best guide available to how the mid may be marked.

<div class="pdf-links">
<a href="pdfs/quizzes/Quiz-2-Solution.pdf">Quiz 2 solution scheme (PDF)</a>
<a href="mid-guide.html">Mid guide</a>
<a href="m2b-notes.html">Module 2 Part B</a>
</div>

:::orig Predicting Customer Complaints for an Online Store [CLO 1, CLO 2]
An online retailer wants an AI system to predict whether a newly placed order is likely to result in a **customer complaint within 14 days**, to identify orders needing attention before shipment. Fields: product category, order value, delivery method, customer region, previous orders, previous complaints, customer age, website activity, payment method, final delivery time, whether the customer contacted support, whether a complaint was filed.

- age is missing for 30% of customers because entering it is optional;
- some customers place several orders, so one customer appears many times;
- several orders appear twice because payments are occasionally resubmitted;
- only 6% of orders result in complaints;
- missing ages are replaced by the mean of the entire dataset before splitting;
- orders are randomly split, so a customer's orders may occur in both sets;
- `final_delivery_time` and `whether_the_customer_contacted_support` are predictors though both may become known only after the order is placed;
- the model achieves 94% accuracy.

Management concludes the data is clean and the model is ready.
:::

:::question (a)(i) [2 points] Is a missing value for customer age necessarily a data-quality error?
:::solution Official answer
**No.** Age is optional, so a missing value may simply mean the customer chose not to give it. What matters is **why** it is missing and whether that affects the task; the absence may itself carry information.
*Rubric:* not automatically an error 1 · optional entry or reason for missingness 1.
:::
:::

:::question (a)(ii) [2 points] Why might replacing every missing age with the overall mean be problematic? Give two reasons.
:::solution Official answer
Any two: **distorts the distribution** (artificial spike, lower variance); **distorts relationships** between variables; **removes informative missingness**; computed on the entire dataset, so it causes **train–test contamination**.
*Rubric:* 1 per reason.
:::
:::

:::question (b)(i) [2 points] Why can duplicate records be harmful?
:::solution Official answer
They inflate the number of orders, distort frequencies and the complaint rate, give duplicates too much influence, place one transaction in training and test, and produce overly optimistic estimates.
*Rubric:* 1 per consequence.
:::
:::

:::question (b)(ii) [1 point] What should the data team do before simply deleting them?
:::solution Official answer
Establish whether they are **true duplicates** by checking order IDs, timestamps, payment identifiers, customer IDs, product details and source-system logs. Resolve confirmed cases with a **documented, reproducible rule**.
*Rubric:* investigates/verifies before deletion 1 · "check the duplicates" without saying what is checked 0.5.
:::
:::

:::question (c) [5 points] Identify and explain three distinct leakage or contamination problems, and state how each should be corrected.
:::solution Official answer
| Problem | What is wrong | Correction |
|---|---|---|
| **Preprocessing contamination** | Mean age uses the entire dataset | Split first; compute the mean on training data; apply that value to both |
| **Group leakage** | One customer's orders in both sets | Partition by customer so $G_{\text{train}}\cap G_{\text{test}}=\emptyset$ |
| **Temporal/target leakage** | `final_delivery_time` and support contact are unknown at prediction time | Define the index time; retain only variables available by then |

*Rubric:* 1.5 per problem with correction · 0.5 for connecting leakage to unrealistically optimistic evaluation.
:::
:::

:::question (d)(i) [2 points] Explain why 94% accuracy may provide very little evidence that the model is useful.
:::solution Official answer
94% of orders have no complaint, so predicting **no complaint for every order** gives 94% accuracy while detecting **zero** complaints.
*Rubric:* class imbalance 1 · the always-"no complaint" argument 1.
:::
:::

:::question (d)(ii) [2 points] Give two better ways of evaluating the model and briefly explain what each would reveal.
:::solution Official answer
Any two: **recall** (share of real complaints caught), **precision** (share of flags that are real), **F1**, **AUPRC**, **confusion matrix**, **calibration**, **subgroup analysis**.
*Rubric:* 1 each with explanation · 0.5 without.
:::
:::

:::question (e) [4 points] Recommend four improvements before deployment.
:::solution Official answer
Any four, with a reason: handle missing age carefully · fit preprocessing on training data · deduplicate verified duplicates · split by customer · remove future information · address imbalance · use suitable metrics · assess representativeness · improve documentation · record provenance and lineage · apply minimization and privacy controls · monitor the deployed pipeline.
*Rubric:* 0.5 for the action, 0.5 for why, four times.
:::
:::
