# M2 · Scenario answers S1–S5

The five scenario-based questions at the end of Module 2 (PDF pages 135–138). **Quiz 1's 21-mark scenario (water pipes) had exactly this shape** — a case, then 4–6 parts, each marked for *naming the concept* and *explaining it in the scenario*. Expect one of these (or a close cousin) in Quiz 2.

<div class="pdf-links">
<a href="m2-answers-1.html">Answers Q1–50</a>
<a href="m2-answers-2.html">Answers Q51–100</a>
<a href="m2-reflections.html">Reflections R1–R5</a>
<a href="pdfs/notes/Module-2-Notes.pdf#page=135">Scenarios in the PDF (p.135)</a>
</div>

:::exam Answer template for every scenario part
**Name it** (the module's term) → **point to the evidence** in the case → **say the consequence** for the model or decision → **give the fix**. Four short sentences beat one long paragraph.
:::

## S1 — University student risk prediction

:::orig Scenario S1
Model uses GPA, attendance, library usage, tuition payment history and online activity. **Dropout = failure to register next semester**, which also labels transfers, approved leave, temporary financial difficulty and administrative delays. Attendance from scanners, manual sheets or not at all; **missing attendance stored as zero**. Training data: **main-campus undergraduates only**, but deployment planned for **online, graduate and satellite-campus** students. **87% accuracy.** Administrators propose **automatically restricting scholarships** for high-risk students.
:::

:::question (a) How has the target variable *dropout* been constructed in this case?
:::solution Answer
It is an **operational, administrative definition** — "did not register next semester" — not a measure of actually leaving education. The rule lumps together very different realities: **transfer** to another university, **approved leave**, **temporary financial difficulty**, **administrative registration delay**, and true withdrawal. So the label reflects **registration-office events and university policy** (constructed, not discovered — Example 38). The model will learn to predict *non-registration*, including administrative noise, and many "positives" are students who never left — inflating risk for financially stressed students and those with paperwork problems.
:::
:::

:::question (b) What problems arise from storing missing attendance as zero?
:::solution Answer
Zero is a **real value** ("attended nothing"), so **missing is disguised as an extreme observation** — a **completeness** problem hidden as an **accuracy** error (the notes' question: "Does a zero mean zero or missing?"). As in Example 38, one code now stands for several realities: the student skipped, the instructor didn't upload, or attendance was never taken. Missingness here comes from **instructor and department practice** (no scanner, manual sheet, no policy) — it is **not at random** and differs by course and department. Consequences: (i) students in classes without scanning look like chronic non-attenders → **false high-risk flags**; (ii) the model learns **department/instructor habits** as a risk signal; (iii) mean attendance and its relationship with dropout are **distorted**. Fix: encode as **missing (NA)** with a `attendance_missing` indicator and its source (scanner/manual/none); impute (if at all) using training data only, or exclude attendance where not recorded.
:::
:::

:::question (c) Is the dataset representative of the intended deployment population? Explain.
:::solution Answer
**No.** Training covers only **main-campus undergraduates**; deployment includes **online, graduate and satellite-campus** students. $P_{\text{data}}(X,Y)\ne P_{\text{target}}(X,Y)$: online students have no classroom attendance or physical library use (**missing deployment scenarios / covariate shift**); graduate students may have different dropout rates (**label distribution shift**) and a different relationship between GPA and leaving (**concept shift**); satellite campuses may record attendance differently. None of this can be checked, because these groups are absent from the training data. The 87% accuracy says nothing about these groups. Collect data from each group, or restrict deployment to main-campus undergraduates and report subgroup performance.
:::
:::

:::question (d) Evaluate the dataset using $Q(D,T,C)$.
:::solution Answer
- **$D$** = main-campus undergraduate records: GPA, scanner/manual attendance (missing = 0), library, tuition history, online activity; label = "not registered next semester".
- **$T$** = identify students likely to leave so as to (as proposed) **restrict scholarships** — an individual, high-stakes allocation decision.
- **$C$** = deployment across online, graduate and satellite campuses, with varying attendance recording, at a university that must treat students fairly.

**Judgement: $Q(D,T,C)$ is low.** The label doesn't measure dropout; attendance is mis-encoded; the sample doesn't cover the deployment population; and the task is punitive, demanding high validity and fairness. The **same $D$** might be adequate for a lower-stakes task — e.g. **annual reporting** of non-registration counts on the main campus — but not for this $T$ in this $C$. Accuracy of 87% is also uninformative without class balance, recall, calibration and subgroup results.
:::
:::

:::question (e) What ethical problem arises from using the prediction to restrict scholarships?
:::solution Answer
The prediction is being turned into a **punitive automated decision** that **harms the students it was meant to help**. Students flagged for *financial difficulty* lose funding → more likely to drop out (**self-fulfilling feedback loop / performative effect**). Errors are not neutral: transfers, approved leave and admin delays are mislabeled, and scanner-less classes look like absence, so **false positives** fall on specific groups (low-income, certain departments, non-represented campuses) — **historical/measurement/representation bias**. There is **no human review, contestability or appeal**, and using it for punishment is a **secondary use** beyond the system's purpose (deployment bias). Ethically the score should trigger **support** (advising, financial aid), with human review and appeal.
:::
:::

:::question (f) What documentation should be included in a Datasheet for Datasets before deployment?
:::solution Answer
- **Motivation:** purpose (early support, not sanctions), funder, intended users (advisors).
- **Composition:** unit (student-semester), counts, **population covered (main-campus undergraduates only)**, variables and **exact label definition** with its known inclusions (transfer, leave, admin delay), class balance, sensitive fields.
- **Collection process:** attendance mechanism per course (scanner/manual/none), time periods, consent/notice to students.
- **Preprocessing:** **how missing attendance was encoded**, imputation, exclusions, linkage.
- **Intended & discouraged uses:** support/outreach; **not** scholarship restriction or disciplinary use; not valid for online/graduate/satellite students without revalidation.
- **Distribution/licensing & access:** who may access, privacy restrictions.
- **Maintenance:** owner, error reporting, update schedule, versioning; subgroup performance and limitations.
:::
:::

## S2 — Public opinion analysis from social media

:::orig Scenario S2
Four million keyword-matched posts → sentiment classifier (supportive/neutral/opposed) for a **transportation policy**. Many **reposts**; **automated accounts** post the same statements thousands of times; the algorithm **promotes emotionally charged content**; users mostly **young urban**; agency calls it **national opinion**. Mid-collection, the platform switches to **promoting short video** → text posts fall sharply; team concludes **public interest declined**.
:::

:::question (a) Why should the platform be treated as part of the measurement instrument?
:::solution Answer
Because the posts are produced **within an engineered environment**: the **recommendation algorithm** decides what users see and therefore react to; **moderation** decides what survives; **trending topics, interface design and incentives** (likes, shares) shape what is written. Unlike a survey whose questions researchers design, here the **platform designs the "questions"**. A post is a response to the platform, not a direct readout of stable opinion — so changes in the platform change the measurement (as the video switch shows).
:::
:::

:::question (b) Identify the representativeness problems in the dataset.
:::solution Answer
- **Coverage:** only platform users; mostly **young and urban**; older, rural and offline citizens nearly absent — yet results are labelled "national".
- **Selection by activity:** a few very active users produce most posts; silent users are invisible.
- **Keyword sampling:** only posts using selected keywords — misses people who discuss the policy in other words or languages.
- **Algorithmic amplification:** polarized content over-collected, moderate views under-represented.
- **Format bias:** text-only collection excludes video/image discussion, increasingly so after the redesign.
$P_{\text{data}}\ne P_{\text{target}}$ (national adult population).
:::
:::

:::question (c) How can reposts and automated accounts distort the estimated level of public support?
:::solution Answer
The estimate counts **posts**, not **people**. A popular message reposted thousands of times counts one opinion thousands of times (100,000 shares → 100,001 copies), and **bots** posting identical statements thousands of times make **coordinated automation look like genuine sentiment**. Both inflate the share of whichever side is amplified, also distort training data (duplicates leak across train/test), and bias the classifier towards repeated phrasings. Fix: deduplicate/near-deduplicate, count unique accounts, detect and remove bots, weight by person.
:::
:::

:::question (d) Does the decline in text posts necessarily represent a real change in public opinion?
:::solution Answer
**No.** The decline coincides with the **platform's interface change** to promote short video — users were **encouraged to create a different format**, so text volume fell regardless of interest. This is a **measurement-instrument change** (like a sensor firmware update), a structural break/distribution shift, not a change in the phenomenon. To claim declining interest you would need format-independent measures (video posts too, a consistent panel, search data, or a survey) and to model the break.
:::
:::

:::question (e) What legal and ethical issues should be examined before collecting and retaining the posts?
:::solution Answer
Platform **Terms of Service** (official API vs prohibited scraping); **copyright** in posted content; **privacy** and expectations of users — public ≠ consent to political profiling; **deleted posts** persisting in the archive (right to withdraw); **identity/demographic inference** and profiling of political views (a sensitive attribute); **data minimization and retention limits** (store aggregates, not identities); **secondary use** by a government agency and potential surveillance chilling effects; security and access controls; ethics/legal review before collection.
:::
:::

:::question (f) What additional data source could provide a more defensible estimate of national opinion?
:::solution Answer
A **nationally representative probability survey** (stratified by region, age, urban/rural, with weighting to census margins, multiple languages and modes such as phone + face-to-face for offline people). Documented sampling frame, response rate and exact wording make it defensible. Social media can remain a **complementary, timely signal**, not the national estimate.
:::
:::

## S3 — Hospital readmission model with missing data

:::orig Scenario S3
Predict 30-day readmission from age, diagnoses, previous admissions, BP, labs, length of stay, discharge info. **BP missing 8%**; **lactate missing 75%** because it's ordered mainly when severe illness is suspected. Team replaces **every missing value with the overall mean from the full dataset before splitting**. Profiling finds BP > 300 mmHg; team **deletes every extreme value automatically** — some were entry errors, others real emergencies.
:::

:::question (a) Why might missing lactate values contain clinically meaningful information?
:::solution Answer
Lactate is ordered **mainly when clinicians suspect severe illness** (sepsis, shock). So *whether* it was measured reflects **clinical judgement of severity**: absent lactate usually signals the patient looked **less ill**. The indicator "lactate not ordered" is itself predictive (informative missingness, $R_{ij}$ carries signal). Imputing the mean makes those patients look like they had an average measured value and **erases the signal**.
:::
:::

:::question (b) Which missingness mechanisms could plausibly explain absent BP and lactate?
:::solution Answer
- **BP (8%):** plausibly **MCAR** (device glitch, transcription loss) or **MAR** (missing more for certain wards, admission types or short stays — observed variables). Possibly MNAR if very sick patients rushed through without routine BP.
- **Lactate (75%):** **not MCAR**. It is at least **MAR** (ordering depends on observed signs — vitals, diagnoses) and likely **MNAR**: it is missing *because* the unmeasured lactate would likely have been normal (clinicians' unrecorded impression of severity).
These are assumptions about the data-generating process, to be justified with clinicians, not proven from data.
:::
:::

:::question (c) What statistical problems can result from mean imputation?
:::solution Answer
It **reduces variance** (many identical values; spread understated), creates an **artificial spike/cluster** at the mean, **distorts relationships** (correlations with readmission weakened), obscures **subgroup differences**, and — for lactate — **removes informative missingness**; 75% of patients would share one fabricated value, so the lactate feature becomes mostly "has the mean". Downstream estimates and uncertainty are wrong.
:::
:::

:::question (d) How has the team introduced train–test contamination?
:::solution Answer
The means were computed on the **full dataset before the train–test split**, so test-set values helped set the imputation parameters applied to the training data (and vice versa). Preprocessing must use $\mu_{\text{train}}$ only and apply it unchanged to the test set. This is **preprocessing contamination**; it slightly inflates performance and violates the rule that the test set is untouched.
:::
:::

:::question (e) Why should the extreme BP observations be investigated rather than automatically deleted?
:::solution Answer
Because they mix **two different realities**: **data-entry errors** (should be corrected or set missing) and **genuine medical emergencies** (critically important, likely readmission-related). Auto-deletion removes the **sickest patients** — the **tail** the model most needs — biasing the model towards stable patients and underestimating risk. Investigate against the source record, correct documented errors (e.g. 1400 → 140), keep plausible extremes, use robust methods or clipping with justification, and exclude only by predefined, documented criteria with an audit trail.
:::
:::

:::question (f) Propose a more principled workflow for handling missing values and outliers.
:::solution Answer
1. **Inventory & profile:** missingness by variable, ward, time; extreme values; consult clinicians on why values are absent.
2. **Split first** (patient-level, ideally chronological) and keep the test set untouched.
3. **Lactate:** add `lactate_measured` indicator; keep missing (for models that allow it) or impute with an indicator — never plain mean; consider groupwise/model-based only with the indicator.
4. **BP (8%):** median or groupwise/model-based (k-NN/regression) imputation **fitted on training data**, plus indicator; or multiple imputation.
5. **Outliers:** validation rules (physiological ranges); flag BP > 300 for **source verification**; correct errors, set unverifiable impossible values to missing, **retain verified emergencies**; use robust loss or winsorization if justified.
6. **Log every change** in an immutable audit trail; all fitting inside CV training folds (pipeline).
7. Evaluate on the untouched test set with calibration and subgroup metrics; document in datasheet and data dictionary (missing-value codes).
:::
:::

## S4 — Cancer detection with imbalanced medical images

:::orig Scenario S4
1,000 patients: **950 no cancer, 50 cancer**. **SMOTE + augmentation applied to the complete dataset before splitting.** Several images per patient, **split at image level**. Images **standardized with full-dataset statistics**. **99% accuracy**; performance falls at a **non-contributing hospital**; **very high cancer probabilities** although deployment prevalence is **5%**.
:::

:::question (a) Why is accuracy alone inadequate for evaluating this model?
:::solution Answer
With 95% negatives, a model predicting "no cancer" for everyone already gets **95% accuracy** and detects nothing. Accuracy hides **false negatives** (missed cancers — the costliest error), says nothing about **precision/recall/specificity**, **calibration** of probabilities, **subgroup** performance or **external validity**, and here it is inflated by leakage. Report sensitivity, specificity, PPV, F1, PR-AUC/ROC-AUC with CIs, calibration, by site and subgroup.
:::
:::

:::question (b) Identify three forms of data leakage or contamination.
:::solution Answer
1. **Resampling before splitting:** SMOTE/augmented images derived from the same originals appear in **both** train and test → train–test contamination.
2. **Group (patient) leakage:** image-level split puts **images from the same patient/examination** in both sets → the model recognizes patients.
3. **Preprocessing contamination:** standardization with **full-dataset** mean/SD → test statistics used in training.
(Also **site leakage**: evaluation only on contributing hospitals, so no test of a new site.) Together these explain 99% internally and the collapse externally.
:::
:::

:::question (c) Why must all images from the same patient remain in one partition?
:::solution Answer
Images from one examination are **highly correlated** (same anatomy, scanner, lesion, artefacts). If split across partitions, the model can match the **patient** rather than learn general cancer patterns, so test accuracy measures memorization. Deployment is always on **new patients**: require $G_{\text{train}}\cap G_{\text{test}}=\varnothing$ (GroupKFold / patient-level split).
:::
:::

:::question (d) When should SMOTE or augmentation be applied?
:::solution Answer
**Only after splitting, and only to the training data** — inside each **training fold** during cross-validation. Validation and test sets stay untouched at their natural distribution and prevalence. (SMOTE is for continuous tabular features; for images, augmentation of training images is the analogue; SMOTENC for mixed data.)
:::
:::

:::question (e) Why might the predicted probabilities require recalibration?
:::solution Answer
Training on an **artificially balanced** set (≈50% cancer after SMOTE) teaches the model a base rate far above the real **5%**, so its probabilities are **systematically too high** (Example 53: 70% → ~22%). Leakage also makes it over-confident. Recalibrate on a **representative, untouched validation set** at deployment prevalence with **Platt scaling** or **isotonic regression**, and check calibration curves per site.
:::
:::

:::question (f) What evaluation design would provide evidence of generalization to a new hospital?
:::solution Answer
- **Patient-level** split; preprocessing, augmentation and SMOTE fitted **inside training folds** only.
- **Site-level hold-out:** leave-one-hospital-out CV and a **final external test set** from a hospital that contributed **no** training data, at its real prevalence.
- Metrics: sensitivity, specificity, PPV, PR-AUC with **confidence intervals**, **calibration** at 5% prevalence, subgroup and scanner-type analysis.
- Ideally a **prospective/silent** deployment at the new site with monitoring before clinical use.
:::
:::

## S5 — Commercial use of a public medical dataset

:::orig Scenario S5
Public imaging dataset; page says **access available for academic research**; original consent permits image analysis but **prohibits commercial use and international transfer**. A company offers to **buy the model and deploy in several countries**; researchers argue images are **de-identified** and only the **model** is transferred. They also **combine** it with an openly licensed dataset and plan to **publish the combined collection**. Documentation: only **"Consent obtained: Yes"** and **"Data publicly available"** — no versions, preprocessing, exclusions, consent conditions, licence restrictions or lineage.
:::

:::question (a) Why is "Consent obtained: Yes" inadequate documentation?
:::solution Answer
It records **that** consent exists but not **what** was agreed: permitted purposes, commercial use, international transfer, linkage, AI development, withdrawal rights and their effect on derived models, vulnerable groups, broad vs specific. Here the actual form **prohibits commercial use and international transfer**, so "Yes" is actively misleading — a reviewer would wrongly approve the deal. Consent must be documented as **conditions**, not a binary flag.
:::
:::

:::question (b) Distinguish among consent, licensing, copyright and privacy in this case.
:::solution Answer
- **Consent:** participants agreed to image analysis, **not commercial use or international transfer** → the sale and global deployment conflict with consent.
- **Licensing:** the dataset is offered for **academic research** → commercial deployment and **redistribution** of the combined collection are likely outside the licence.
- **Copyright:** rights in the images/compilation held by the dataset creators — publishing the combined collection may infringe them; the open dataset's licence terms also apply.
- **Privacy:** images are personal health data; de-identification reduces but doesn't remove re-identification risk; obligations persist.
Each is a **separate constraint** — satisfying one (e.g. public access) does not satisfy the others.
:::
:::

:::question (c) Does de-identification automatically permit commercial or international use?
:::solution Answer
**No.** De-identification is **risk reduction, not anonymity** — quasi-identifiers and medical images can be re-identified, and **models can memorize** training data (membership inference, model inversion). More fundamentally, **consent and licence restrictions still apply**: participants refused commercial use and transfer, and the licence is academic-only. Transferring the **model** (a derived product) does not escape those terms. Commercial/international use would need renewed consent or a lawful basis, licence permission, and ethics/legal approval.
:::
:::

:::question (d) What licence-compatibility problem may arise when the two datasets are combined?
:::solution Answer
The **academic-only / no-redistribution** terms of the medical dataset are **incompatible** with publishing the combination openly: the combined collection **inherits the most restrictive terms**, so it cannot be redistributed or used commercially, whatever the open dataset's licence says. The open licence may also impose its own conditions (attribution, share-alike) that conflict. Downstream users can't assume all components are compatible. A licence-compatibility review is needed before publication.
:::
:::

:::question (e) What information should be added to the dataset documentation and lineage record?
:::solution Answer
**Documentation:** source and **dataset versions** of both datasets; **consent conditions** (purposes, no commercial use, no international transfer, withdrawal); **licence terms** for each source and of the combination; access procedure; de-identification method and residual risk; composition; **excluded cases** and reasons; label definitions; intended and **prohibited uses**; maintainer.
**Lineage:** $D_0^{(A)}, D_0^{(B)}\to$ each transformation (de-identification, preprocessing, merging, exclusions) with input version, code version, parameters, output version, timestamp, responsible person, validation results — linking the trained model to exact data and code.
:::
:::

:::question (f) Which organizational roles should approve or reject the commercial deployment?
:::solution Answer
The **data owner/custodian** of the original dataset (licence holder); the **institutional review board/research ethics committee** (consent scope); the **data-protection/privacy office** (re-identification, international transfer); **legal counsel** (licences, copyright, contracts, cross-border law); the university's **technology-transfer/leadership**; **clinical governance** (safety of the diagnostic); ideally **participant/community representatives**; and **regulators** in deployment countries. Given the explicit prohibitions, the likely outcome is **reject**, or proceed only with **renewed consent**, licence permission and a lawful transfer basis.
:::
:::
