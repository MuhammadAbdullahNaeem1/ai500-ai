# M2 · Practice answers Q1–50

Answers to the end-of-module practice questions (Module 2 notes, PDF pages 130–132), written from the notes' own definitions, lists and examples so the wording matches what is marked. Each answer is sized for a **3–4 mark** quiz part: definition → mechanism → example from the notes.

<div class="pdf-links">
<a href="m2a-notes.html">Part A notes (2.1–2.3)</a>
<a href="m2-answers-2.html">Answers Q51–100</a>
<a href="pdfs/notes/Module-2-Notes.pdf#page=130">Questions in the PDF (p.130)</a>
</div>

:::note How to use
Read the question, say your answer out loud, then open the box. The **bold** words are the ones a rubric looks for (Quiz 1's rubric gave a mark per named concept and a mark per correct explanation).
:::

## Data as a Constructed Record of Reality

:::question Q1. Why is the phrase *raw data* considered misleading in data science and AI?
:::solution Answer
Because data are **never raw — they are always "cooked"**. Before any row is recorded, people have already decided what phenomenon matters and how to define it (**conceptualization**), what unit, population, instrument and frequency to use (**observation**), and what to record, how to encode missing values and how to store/link/transform it (**engineering**). "Raw" suggests an objective, pre-existing truth waiting to be harvested; in reality the dataset is an **engineered artifact** shaped by human assumptions, technical constraints and institutional priorities. Treating it as raw hides those choices and leads to models that inherit them unnoticed.
:::
:::

:::question Q2. Explain why a dataset should be understood as an engineered artifact rather than a passive reflection of reality.
:::solution Answer
A dataset is produced by a chain of choices: **Dataset = Phenomenon + Measurement process + Sampling process + Institutional context + Data representation** (Figure 14). Each component filters reality — the definition chooses what counts, the instrument decides what is observable, sampling decides who is seen, institutions decide the rules behind labels, and representation decides encoding and format. The values may look precise, but the concepts they stand for remain ambiguous. *Example 38:* a "dropout" dataset reflects university policy (one semester vs two years), scanner use, and main-campus-only sampling — not just student behaviour. So we must interrogate *how* the data were made before trusting what a model learns from them.
:::
:::

:::question Q3. How do conceptualization, observation, sampling, institutional context and data representation jointly produce a dataset?
:::solution Answer
- **Conceptualization** defines the phenomenon and the label (what "dropout" means).
- **Observation/measurement** chooses unit of analysis, instruments and frequency (scanners vs manual registers).
- **Sampling** decides who/what enters (main campus only; online, exchange, graduate and satellite students excluded).
- **Institutional context** supplies the rules and incentives that generate records (dropout after one semester vs two years; billing rules in hospitals).
- **Data representation** sets encoding and storage (NA vs 0, formats, linkage).
Each step removes or reshapes part of reality, and the final spreadsheet is their **combined product** — it records the institution's procedures and systems as much as the people in it.
:::
:::

:::question Q4. Why are labels such as disease, fraud, dropout, risk and success not self-defining?
:::solution Answer
Their meaning is fixed by **operational rules, human judgement and institutional practice**, not by the word. "Dropout" could be permanent exit, failure to enrol next semester, transfer, approved leave or late graduation — each gives **different students different labels** (Example 38). "Disease" may follow a billing code rather than clinical severity; "fraud" depends on what investigators confirm; "risk" on the chosen horizon and threshold. Hence **the target is constructed, not discovered**, and must be explicitly defined and documented.
:::
:::

:::question Q5. How can two institutions use the same variable name while assigning fundamentally different meanings to it?
:::solution Answer
Each institution generates the field under its **own rules**. In Example 38, University A labels a student *dropout* after **one** missed semester, University B only after **two years**. Both columns are called `dropout`, but they encode different policies. Similarly Hospital X codes every complication for reimbursement while Hospital Y codes only the primary diagnosis. **Merging such data without understanding their origins** produces misleading training data — the model learns institutional differences as if they were differences in people. Fix: data dictionaries with precise definitions, provenance, and harmonization before pooling.
:::
:::

:::question Q6. Explain how operational definitions influence the target labels used in supervised learning.
:::solution Answer
A supervised model learns $P(Y\mid X)$ for the **$Y$ that was operationalized**. Change the definition and you change which cases are positive: defining dropout as "fails to register next semester" also labels transfers, approved leave, temporary financial problems and administrative delays as dropouts (Scenario S1). The model then learns to predict *that* rule — including its errors and institutional artefacts — and its accuracy is measured against it. So the operational definition determines **what the model actually predicts**, its class balance, its fairness, and whether it supports the intended decision.
:::
:::

:::question Q7. What does the formulation $Q(D,T,C)$ communicate about dataset quality?
:::solution Answer
$Q(D,T,C)$ = **the fitness of dataset $D$ for task $T$ under context $C$**. It says quality is **not an intrinsic, universal property** of a dataset but a **relation** between the data, the purpose and the setting — aligned with NIST, which judges quality and representativeness relative to intended use (accuracy, completeness, consistency, relevance, timeliness). The same student dataset scores high for annual reporting but low for a 6-month early-warning system, a national model, or a causal question.
:::
:::

:::question Q8. Why can a dataset be suitable for descriptive reporting but unsuitable for causal inference?
:::solution Answer
Descriptive reporting only needs **approximate counts/associations** of what happened ("what % of first-years left?"). Causal inference needs to separate the effect of an intervention from **confounders**. Observational data show that library users drop out less, but library users may also be **more motivated, better prepared, wealthier, better supported** (Example 38, Task 4). Without measuring/controlling these, the data reveal **association, not causation**. The data are adequate for $T_1$ and inadequate for $T_4$ — exactly the $Q(D,T,C)$ point.
:::
:::

:::question Q9. How can an exclusion decision during sampling affect the population to which a model can validly be applied?
:::solution Answer
A model is only validated for the population its data represent. Collecting only **main-campus undergraduates** (excluding online, exchange, graduate, satellite-campus students) means the model is representative of **one population**; applying it to the excluded groups — or nationwide — gives unreliable predictions, because $P_{\text{data}}(X,Y)\ne P_{\text{target}}(X,Y)$ (covariate/label/concept shift). Exclusions must be **documented** and the model's **intended use restricted** to the covered population, or new data collected.
:::
:::

:::question Q10. Explain why the correct question is not "Is this data good?" but "Is this data fit for the intended task and context?"
:::solution Answer
Because **no dataset is good in a vacuum** — quality is contextual. A dataset may be fine for descriptive statistics but fatally flawed for causal inference; useful retrospectively but too late for real-time prediction; representative of an urban hospital but useless for a rural clinic; valid for adults but not children; good for classification but poorly calibrated for absolute risk. Data are a **constructed map**: we must know how it was drawn and whether it is scaled for *our* journey. Asking "fit for $T$ in $C$?" forces us to check timeliness, representativeness, definitions and governance for the actual decision.
:::
:::

## Data Sources and Their Inherent Realities

:::question Q11. What are the principal advantages of surveys as a source of data for AI systems?
:::solution Answer
Surveys can capture **latent constructs** that rarely appear in routine databases: **beliefs, preferences, intentions, self-reported behaviours, social circumstances and perceived quality of life**. They are **designed by the researcher** — target population, questions, wording and sampling are controlled — and can be weighted to match a population (e.g. national age/sex distributions). They are often the only defensible route to measure *opinion* (e.g. a nationally representative survey vs social media in S2).
:::
:::

:::question Q12. Distinguish among coverage error, sampling error, nonresponse bias, recall bias, social-desirability bias and instrument effects.
:::solution Answer
| Error | Definition | Example 39 |
|---|---|---|
| **Coverage** | Sampling frame misses part of the target population | Online-only survey misses older/remote adults |
| **Sampling** | Sample differs from population **by chance** | Random draw over-includes urban gym users |
| **Nonresponse** | Respondents differ **systematically** from non-respondents | Inactive people don't reply → activity overestimated |
| **Recall** | Inaccurate **memory** of past events | Exercised twice, remembers four times |
| **Social desirability** | Answers that look good rather than true | Reports five sessions instead of one |
| **Instrument effects** | **Wording, order, translation** shift answers | "exercise" vs "moderate/vigorous activity" → 0 vs 5 for a daily walker |
:::
:::

:::question Q13. How can a model trained on survey data learn reporting behaviour rather than the intended real-world construct?
:::solution Answer
The label is **self-reported**, so it equals *actual behaviour × willingness/ability to report it*. Systematic differences in reporting become signal: if more-educated respondents report accurately while others overstate, the model may **associate education with activity** purely through reporting accuracy (Example 39). It learns *how people answer questions*. When applied to objective data (wearable trackers measuring movement), performance degrades because the target has changed from reported to actual behaviour.
:::
:::

:::question Q14. Explain the roles of systematic bias, random noise, environmental conditions and device characteristics in sensor measurements.
:::solution Answer
Basic model: $X_{\text{obs}}=X_{\text{true}}+b+\epsilon$ — **$b$ systematic bias** (persistent offset, e.g. a miscalibrated monitor reading +20 mmHg) and **$\epsilon$ random noise** (zero-mean fluctuation). Realistic model: $X_{\text{obs}}=g(X_{\text{true}},Z,\theta_{\text{device}})+\epsilon$, where **$Z$ = environmental conditions** (temperature, lighting, interference) and **$\theta_{\text{device}}$ = device-specific behaviour** (model, firmware, calibration). So the reading depends on the instrument and setting, not only the true quantity — "objective" sensor data are shaped by acquisition.
:::
:::

:::question Q15. What data-quality problems can result from calibration drift, clock misalignment, packet loss, firmware changes and signal saturation?
:::solution Answer
- **Calibration drift** → growing **systematic error** (accuracy), readings not comparable over time.
- **Clock misalignment** (device vs server time) → wrong event order, **temporal leakage** and wrong feature windows (timeliness/consistency).
- **Packet loss** → **missing** values/intervals, often not at random (completeness).
- **Firmware changes** → sudden **distribution shift** halfway through collection (consistency; R3's heart-rate example).
- **Saturation/clipping** → true extremes recorded as the maximum, hiding the **tails** that matter most (accuracy).
Plus: does zero mean zero or missing? Were sites comparable?
:::
:::

:::question Q16. Why should a social media platform be treated as part of the measurement instrument when web data are collected?
:::solution Answer
Because the observed behaviour is **produced inside an engineered environment**: what users see depends on the **recommendation algorithm**, what remains depends on **moderation**, what they post depends on **trending topics, interface design** and **social incentives** (likes, shares). A post is a **response to the platform**, not a direct expression of stable belief. Unlike a survey, where researchers design the questionnaire, here the *platform* is the questionnaire. Example 40: a change to favour short video cut text posts — a platform change, not an opinion change.
:::
:::

:::question Q17. How can recommendation algorithms, moderation policies, bots and duplicate posts distort conclusions drawn from web data?
:::solution Answer
- **Recommendation algorithms** amplify emotionally charged, polarized content → moderate views under-collected.
- **Moderation** removes some posts → what's left is filtered.
- **Bots/coordinated campaigns** post identical messages thousands of times → automation mistaken for public sentiment.
- **Duplicates/reposts:** one post shared 100,000 times counts one person's opinion 100,001 times → frequencies inflated.
Net effect: estimated support reflects **amplification and automation**, not the number of unique people who hold a view; models learn platform-specific patterns.
:::
:::

:::question Q18. Distinguish among event time, recording time, arrival time and processing time in system logs.
:::solution Answer
**Event time** — when the real-world action occurred. **Recording time** — when the local system logged it. **Arrival time** — when it reached the central data pipeline. **Processing time** — when the pipeline handled it. They can differ by seconds to weeks (retries, offline devices, batch jobs). Building features or splits on the wrong one is a **primary cause of temporal leakage** and incorrect feature windows: for prediction, a feature counts only if it was **available** by the prediction time.
:::
:::

:::question Q19. Why do administrative records often represent institutional behaviour and access patterns rather than objective ground truth?
:::solution Answer
They are created to **run organizations** (billing, reimbursement, enforcement), not to measure reality: **Observed outcome = f(Underlying condition, Access, Policy, Institutional practice)**. A diagnosis code may reflect **billing optimization**; an arrest reflects **policing patterns**; spending reflects **access to care**; absences may reflect **transport/caregiving**; unemployment records omit informal workers. Example 41: a remote patient who never returns has *no readmission record* — not because they recovered; Hospital A's overnight-observation policy creates admissions Hospital B never records. Records capture **utilization**, not burden of disease.
:::
:::

:::question Q20. Compare the strengths and limitations of controlled experiments, public datasets and synthetic datasets.
:::solution Answer
| | Strengths | Limitations |
|---|---|---|
| **Controlled experiments** | Randomization $T_i\sim\text{Bernoulli}(p)$ → comparable groups; clear intervention; temporal order; reduced confounding; prespecified outcomes | Ethical/practical limits; noncompliance; **attrition**; contamination; **limited external validity**; selective recruitment; site differences |
| **Public datasets** | Accessible; reproducible; shared benchmarks; low barriers; standardized comparison; education | Outdated versions; unclear provenance; hidden preprocessing; **label errors**; undocumented exclusions; **benchmark saturation**; privacy; licences |
| **Synthetic data** | Controlled labels; configurable scenarios; rare-event simulation; privacy-preserving access; pipeline testing | Reproduces bias; omits rare subgroups; unrealistic correlations; **leaks training records**; too-clean labels; sim-to-real overconfidence |
None is automatically unbiased — each needs scrutiny.
:::
:::

## Public and Synthetic Data

:::question Q21. Why does public availability not guarantee that a dataset is accurate, representative, ethically usable or free of legal restrictions?
:::solution Answer
"Public" describes **access**, not quality or permission. A public dataset may be **outdated**, have **unclear provenance**, **hidden preprocessing**, **undocumented exclusions** and **label errors** (Northcutt et al. found ≥3.3% average test-label error); it may not represent a **real deployment** population; it may carry **privacy risks**; its **licence** may forbid commercial use or redistribution; and the **original consent** may not cover new uses (Example 57). So every public dataset still needs provenance, quality, licence and consent checks.
:::
:::

:::question Q22. What is benchmark saturation, and how can repeated use of a public test set weaken the credibility of model comparisons?
:::solution Answer
**Benchmark saturation:** models become **overfitted to a public test set** after years of reuse, so scores stop reflecting real generalization. Even without training on test labels, researchers inspect errors and redesign models: *test results → research decisions → new models → same test set*. The test set becomes part of development (a form of **leakage**), so small improvements may be noise or label-error artefacts. Remedies: hidden or rotating test sets, fresh data, external validation, limited submissions, post-deployment evaluation.
:::
:::

:::question Q23. How can label errors in a benchmark test set alter the ranking of competing ML models?
:::solution Answer
Reported accuracy is computed against **observed** labels $\tilde Y$, not true labels $Y$: when $\tilde Y_i\ne Y_i$, a **correct prediction is scored wrong** and a wrong one may be scored right. When top models differ by less than the number of mislabeled test cases, rankings are determined by noise. High-capacity models that learn fine distinctions may **disagree with wrong labels** and look worse, while simpler models that reproduce annotation patterns look better. Northcutt et al. showed rankings **changed after correction** — agreement with benchmark labels ≠ agreement with reality.
:::
:::

:::question Q24. Why should public datasets undergo continuous auditing, correction, versioning and maintenance?
:::solution Answer
Because a dataset is **never finished**: label errors, ambiguity, outdated categories and new uses surface over time. **Auditing** (e.g. Confident Learning + human review) finds errors; **correction** restores trustworthy evaluation; **versioning** ($D(1.0),D(1.1),D(2.0)$, reported in every paper) keeps old and new results comparable and reproducible; **maintenance** provides an error-reporting pathway, owners and an update schedule. Treating benchmarks as immutable truth let errors persist (case 2.11.3) — "the inevitability of maintenance".
:::
:::

:::question Q25. What are the main methods used to generate synthetic data?
:::solution Answer
**Rule-based simulators** (traffic simulator with fixed rules), **mechanistic models** (climate physics equations), **agent-based models** (epidemic with interacting agents), **GANs** (generator vs discriminator; synthetic faces), **VAEs** (decode from a latent space; MNIST-like digits), **diffusion models** (learn to reverse noising; text-to-image), **LLMs** (synthetic conversations/text/code), and **statistical sampling from fitted distributions** (fit a normal to blood pressure and sample).
:::
:::

:::question Q26. Identify six useful applications of synthetic data in ML and data engineering.
:::solution Answer
1. **Simulating rare events** (rare complications, failures). 2. **Privacy-preserving data access** (develop models without identifiable records). 3. **Augmenting under-represented classes** / **balancing** datasets. 4. **Testing data pipelines and software** before deployment. 5. **Training in unsafe or expensive environments** (robots, vehicles). 6. **Counterfactual scenarios** ("what if average stay were two days shorter?"). (Example 43 uses privacy, balancing, testing and counterfactuals.)
:::
:::

:::question Q27. Why does synthetic data not automatically guarantee privacy or anonymity?
:::solution Answer
The generator is **trained on real records** and can **memorize** them: some synthetic records may be near-copies of real people, enabling **membership inference** (was this person in the training data?) and **reconstruction** of sensitive attributes. Rare combinations are especially identifying. Generated health data often retains **residual disclosure risk**. Hence privacy must be **tested** (membership-inference attacks, record-similarity/nearest-neighbour distance checks) — *synthetic does not mean anonymous or risk-free*.
:::
:::

:::question Q28. Define fidelity, utility, privacy, fairness, coverage and realism as validation dimensions for synthetic data.
:::solution Answer
- **Fidelity** — preserves relevant distributions and relationships (age distribution, disease frequencies, correlations).
- **Utility** — supports the intended analysis (model trained on synthetic performs similarly **on real data**).
- **Privacy** — original individuals cannot be inferred or reconstructed.
- **Fairness** — subgroup properties preserved without amplifying bias.
- **Coverage** — rare but critical edge cases represented (severe sepsis, uncommon drug reactions).
- **Realism** — combinations obey domain constraints (no male patient marked pregnant).
:::
:::

:::question Q29. How can synthetic data reproduce or amplify biases contained in the original source data?
:::solution Answer
The generator learns the source distribution — **including its gaps and historical patterns**. If young chronically ill patients were under-represented, it produces **too few** of them (Example 43), so a downstream model works for the elderly and poorly for the young. Generators tend to reproduce the **dense, common** regions and smooth away **rare subgroups and tails**, and they faithfully copy biased labels (e.g. discriminatory historical loan approvals, R4). Matching *overall* distributions can therefore hide subgroup erasure and **amplify** disparity.
:::
:::

:::question Q30. What evidence would be required before a model trained on synthetic clinical data could be trusted on real patients?
:::solution Answer
- **Validation on real, representative, held-out patient data** (not a synthetic test set) — discrimination and **calibration**.
- **Subgroup and intersectional** performance (age, sex, ethnicity, sites), including rare conditions (coverage).
- Synthetic-data **fidelity** checks (distributions, correlations, tails) and **realism** constraints.
- **Privacy** audit of the generator (membership inference, memorization).
- **External validation** at other hospitals and, ideally, prospective/silent deployment with monitoring.
- Documentation (datasheet for the synthetic data) and governance approval.
:::
:::

## Data Quality Dimensions

:::question Q31. Define cell-level completeness and record-level completeness.
:::solution Answer
**Cell-level** (per variable $j$): $\text{Completeness}_j=1-\dfrac{m_j}{n}$, the share of non-missing cells among $n$ records. **Record-level:** $\dfrac{\text{records containing all required fields}}{\text{total records}}$. Example: 2 of 5 BP values missing → 0.60; 3 of 5 records complete → 60%.
:::
:::

:::question Q32. A variable contains 80 missing values among 1,000 records. Compute its cell-level completeness.
:::solution Answer
$\text{Completeness}=1-\dfrac{80}{1000}=1-0.08=\mathbf{0.92}$, i.e. **92% complete**. (Whether 92% is adequate depends on *why* the 8% is missing and on the task.)
:::
:::

:::question Q33. Why can a dataset with 99 percent populated cells still be incomplete for a particular application?
:::solution Answer
Cell counts measure **missing cells**, not **missing records, time intervals, subgroups, modalities, labels, metadata or provenance**. A dataset can be 99% populated while **entirely excluding an important or vulnerable population** (e.g. rural or online students), lacking a key modality (mental-health indicators), or missing the timestamps needed for prediction. For a task that needs those, it is incomplete. Completeness is judged by: *does the missing information prevent reliable use for the intended purpose?*
:::
:::

:::question Q34. How should accuracy be assessed for numerical measurements and categorical labels?
:::solution Answer
Against an **independent, trusted reference**. **Numerical:** error $e_i=x_i-x_i^*$, summarized by $\text{MAE}=\frac1n\sum|x_i-x_i^*|$ (Table 11: errors 7,2,3,5,2 → 3.8 mmHg). **Categorical:** $\text{label accuracy}=\dfrac{\text{correctly labeled cases}}{\text{reviewed cases}}$ (95 of 100 → 95%), usually from expert re-review/adjudication of a sample.
:::
:::

:::question Q35. Why does agreement among values within a database not establish that the values are correct?
:::solution Answer
Internal agreement only shows **consistency**. Values can agree and all be wrong: a miscalibrated monitor reads every patient +20 mmHg (consistent, inaccurate); copied or duplicated errors repeat; a wrong record linkage propagates; annotators trained with the same flawed guideline agree with each other. **Accuracy requires comparison with an independent, trustworthy reference** outside the database.
:::
:::

:::question Q36. Distinguish among formatting, logical, structural and cross-system consistency.
:::solution Answer
- **Formatting:** same meaning, different encodings — "Male/M/1/man"; DD/MM vs MM/DD dates; "Yes/Y/1/True/Diabetic".
- **Logical:** violates real-world rules — discharge (Jan 10) before admission (Jan 15); death before a later visit; child older than parent; $p\notin[0,1]$.
- **Structural:** mixed units in one column (70 kg vs 155 lb), duplicate IDs for different people, conflicting labels for one entity across files.
- **Cross-system:** the same entity/value recorded differently in different systems (e.g. two hospitals' EHRs) — needs reconciliation.
:::
:::

:::question Q37. Explain the differences among freshness, latency, update frequency and validity period.
:::solution Answer
**Freshness** — how old the information is. **Latency** — delay between the event and its availability (diabetes in January, recorded in April → 3 months). **Update frequency** — how often values are refreshed (finances once per semester). **Validity period** — how long a value stays operationally relevant (a cholesterol value valid ~6 months). A fraud system needs millisecond latency; annual planning tolerates months.
:::
:::

:::question Q38. What is feature staleness, and how can it reduce the reliability of real-time predictions?
:::solution Answer
**Staleness:** at prediction time $t$, feature age $\Delta t=t-t_{\text{last update}}$; if $\Delta t$ exceeds a task-specific threshold, the feature is **stale**. (Cholesterol from January used in October: $\Delta t=9$ months > 6-month guideline.) Stale features describe a past state — the model predicts on outdated information (e.g. assumes a patient is non-diabetic), reducing accuracy and calibration, and creating a **train–serving mismatch** if training used fresher values.
:::
:::

:::question Q39. Explain the difference between covariate shift, label distribution shift and concept shift.
:::solution Answer
- **Covariate shift:** $P(X)$ changes, $P(Y\mid X)$ stable — model moved to a hospital with different demographics or practices.
- **Label distribution shift:** $P(Y)$ (class proportions) changes — fraud 1% in training, 10% at deployment → poorly **calibrated**.
- **Concept shift:** $P(Y\mid X)$ — the mapping itself — changes — purchasing behaviour after a recession.
:::
:::

:::question Q40. Why does a very large sample size not compensate for systematic underrepresentation of important populations?
:::solution Answer
More data from an **already well-represented** group shrinks variance for that group but adds **no information about the missing ones**. Table 15: 80% of a million patients are 65+ while the population is 25% 65+; adding another million elderly does nothing for the 18–40 group. Systematic gaps are **bias**, not noise — size cannot average them away. Intersectional gaps (500 young women, 500 elderly men) also persist. Fix: targeted collection with subgroup minimums $n_g\ge n_{\min}$.
:::
:::

## Measurement Error and Construct Validity

:::question Q41. Distinguish between random and systematic measurement error.
:::solution Answer
**Random:** $X^*=X+\epsilon$, $\mathbb E[\epsilon]=0$ — scattered around the truth (140 recorded as 138, 141, 142, 139); increases variance, weakens associations, **no bias** in the centre. **Systematic:** $X^*=X+b+\epsilon$, $b\ne0$ — persistent directional shift (140,130,120 recorded as 150,140,130); produces **biased** estimates and flawed conclusions.
:::
:::

:::question Q42. Why can averaging reduce the effect of random error but fail to remove systematic error?
:::solution Answer
Averaging $n$ readings gives $\bar X^*=\bar X+b+\bar\epsilon$. Because $\mathbb E[\epsilon]=0$, $\bar\epsilon\to0$ as $n$ grows (errors −2,+1,+2,−1 cancel), so **random** error shrinks. But $b$ is the **same in every reading**, so it survives averaging unchanged: an uncalibrated monitor is still +10 mmHg on average. Only **calibration against a reference** removes $b$.
:::
:::

:::question Q43. What is differential measurement error, and why is it important for fairness analysis?
:::solution Answer
Error rates that **differ across subgroups**: $P(X^*\neq X\mid A=a)$ varies with a sensitive attribute $A$. If one group is measured much less accurately, the model's inputs (or labels) are noisier or biased for that group → **lower and unequal performance**, which the model **cannot mathematically correct** from the data alone. It produces **measurement bias** and must be checked by subgroup when auditing fairness.
:::
:::

:::question Q44. How can a medical sensor that performs differently across skin tones create unequal model performance?
:::solution Answer
A wearable heart-rate sensor with **±2 bpm** error on light skin and **±10 bpm** on dark skin (notes' example) gives the model **much noisier inputs** for darker-skinned patients. Thresholds and patterns learned mostly from accurate readings misfire on noisy ones → more false alarms/missed deteriorations for that group. If such readings also define labels, errors enter the target. Result: **differential measurement error → measurement bias → unequal accuracy**, invisible unless performance is reported by skin tone.
:::
:::

:::question Q45. Define construct validity in the context of data collection and AI development.
:::solution Answer
**Construct validity** is the degree to which a measured variable or label **faithfully represents the concept we actually care about**. Its failure — "the ultimate error" — happens before any instrument is used: the chosen variable measures something else (cost for need, arrests for crime, clicks for satisfaction, exam scores for intelligence, absence for disengagement). Then the model becomes a highly optimized system for measuring the wrong thing.
:::
:::

:::question Q46. Why can healthcare spending be a poor proxy for health need?
:::solution Answer
Spending $=f(\text{need},\text{access},\text{insurance},\text{provider behaviour},\text{historical inequality})$. Two patients with identical need incur different costs when one faces access barriers (Table 17: both high need, \$30,000 vs \$4,000). A model trained on cost concludes the low-spending patient has lower need. Obermeyer et al.: at the same score, **Black patients were sicker** than White patients because less had historically been spent on them. Accurate cost prediction ≠ accurate need prediction.
:::
:::

:::question Q47. Why can arrest records be a poor proxy for actual crime commission?
:::solution Answer
An arrest requires detection, investigation and enforcement — shaped by **policing intensity, patrol allocation, surveillance, reporting behaviour and institutional practice**. Two people with the same likelihood of offending differ in arrest probability if one lives in a heavily patrolled area (Example 64). Many offences are never detected; some arrests don't involve offending. Arrests measure **enforcement**, and feed **feedback loops** (more patrols → more arrests → more patrols).
:::
:::

:::question Q48. Why can user clicks be a poor proxy for genuine user satisfaction?
:::solution Answer
Clicks reflect **what the interface showed and how** (ranking position, thumbnails, clickbait, autoplay), curiosity, accidental taps and engagement-maximizing design — not whether the user was satisfied afterwards. Platform algorithms amplify emotionally charged content that is clicked but disliked. Optimizing clicks can therefore **reduce** satisfaction while metrics rise — a construct-validity failure in which the platform is part of the measurement instrument.
:::
:::

:::question Q49. Explain why model optimization cannot correct a target variable that measures the wrong construct.
:::solution Answer
Optimization minimizes error **with respect to the given target** $Y$. If $Y$ is a biased proxy for the construct $Y^*$, a better optimizer just predicts the proxy **more accurately** — including its distortions ($\hat C\approx C$ does not imply $\hat C\approx H$). "The algorithm works exactly as designed. It is simply optimizing the wrong target." The data contain no signal telling the model it is off-target; only **redefining the target** (or validating the proxy) fixes it.
:::
:::

:::question Q50. How should domain experts evaluate whether a proposed proxy faithfully represents the concept of interest?
:::solution Answer
- State the **true construct** and trace the chain construct → institutional process → recorded proxy → training target.
- List what *else* drives the proxy (access, insurance, policy, policing, interface).
- **Validate against direct measures** on a sample (chronic conditions, physiological indicators, clinician-reviewed need).
- Check **group invariance:** compare $\mathbb E[H\mid C=c,A=a]$ across groups; check subgroup calibration $P(H\ge h_0\mid S=s,A=a)$.
- Involve clinicians, ethicists, affected communities in **approving the target**; document the proxy and its limitations; monitor outcomes after deployment.
:::
:::
