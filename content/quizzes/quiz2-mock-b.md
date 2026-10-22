# Mock Quiz 2B — Module 2

**50 points · 60 minutes · closed book.** Emphasis: data sources, documentation, consent and licensing.

<div class="pdf-links">
<a href="quiz2-guide.html">Quiz 2 guide</a>
<a href="quiz2-mock-a.html">Mock 2A</a>
<a href="quiz2-mock-c.html">Mock 2C</a>
</div>

## Basic Definitions [CLO 4] — 9 points

:::question 1(a) [3 points] Define construct validity. Give one proxy from the notes that fails it and explain why.
:::solution Solution & marking
> **Notes wording** — “The most dangerous measurement error occurs before the instrument is even used: the chosen variable simply does not measure the intended concept.” (§2.3.6)

**Construct validity** is the degree to which a measured variable or label faithfully represents the **concept we actually intend** to measure. Example: **healthcare cost as a proxy for health need** — cost also depends on access, insurance, provider behaviour and historical inequality, so patients with equal need but less access appear "low need" (Obermeyer et al.). (Also: arrests for crime, clicks for satisfaction, exam scores for intelligence, absence for disengagement.)

| Rubric | |
|---|---|
| Correct definition | 1.5 |
| Valid proxy example | 0.5 |
| Explains how the proxy diverges from the construct | 1 |
:::
:::

:::question 1(b) [3 points] Define the four timestamps of a logged event. Why does confusing them matter?
:::solution Solution & marking
> **Notes wording** — “When the real-world action actually occurred.” (§2.2.4) “When the local system logged it.” (§2.2.4) “When it reached the central data pipeline.” (§2.2.4) “When the pipeline actually handled it.” (§2.2.4)

**Event time** (real action), **recording time** (logged locally), **arrival time** (reached central pipeline), **processing time** (handled by pipeline). Confusing them causes **temporal leakage** and **wrong feature windows**: a feature may be assigned to before the prediction time although it was only available later.

| Rubric | |
|---|---|
| All four correct (½ each) | 2 |
| Consequence: temporal leakage/incorrect windows | 1 |
:::
:::

:::question 1(c) [3 points] Define data minimization and state the decision rule given in the notes.
:::solution Solution & marking
> **Notes wording** — “Data minimization is the principle that organizations should collect, retain, and process only the information reasonably necessary to achieve a clearly defined and legitimate purpose.” (§2.8.5)

**Data minimization:** organizations should collect, retain and process only the information **reasonably necessary** for a clearly defined, legitimate purpose. Rule: **collect $X_j$ only if Benefit$(X_j)$ > Risk$(X_j)$**, considering the intended use and available safeguards (e.g. keep postal code, drop full address and national ID; keep ethnicity only for restricted fairness auditing).

| Rubric | |
|---|---|
| Definition (necessary for defined purpose) | 1.5 |
| Benefit > Risk rule | 1 |
| Example or mention of safeguards/retention | 0.5 |
:::
:::

## Short, Conceptual Questions [CLO 4] — 12 points

:::question 2(a) [4 points] Explain why a social-media platform should be treated as part of the measurement instrument. Give two consequences for an AI model trained on its posts.
:::solution Solution & marking
> **Notes wording** — “Observed web behavior is not a direct measure of stable human preference. It is a reaction within an engineered environment, defined by a combination of user, interface, ranking algorithm, moderation, and platform incentives.” (§2.2.3)

Observed behaviour is a **reaction within an engineered environment** — recommendation algorithm, interface, moderation, trending topics and engagement incentives decide what users see, create and what remains. So posts are not direct measures of stable opinion. Consequences: (1) the model learns **platform-specific language, amplified polarized topics and bot activity**, and its accuracy **drops on representative survey data**; (2) **platform changes** (e.g. favouring short video) create shifts the model misreads as changes in opinion; also non-representative users, duplicates.

| Rubric | |
|---|---|
| Engineered environment explanation | 2 |
| Consequence 1 | 1 |
| Consequence 2 | 1 |
:::
:::

:::question 2(b) [4 points] Distinguish consent, licensing, copyright and privacy. Why does satisfying one not satisfy the others?
:::solution Solution & marking
> **Notes wording** — “Consent explains what participants agreed to, while licensing defines what users are legally permitted to do with the data.” (§2.7 Ex. 57) “Legal permission to access a dataset does not automatically mean that every possible use is acceptable.” (§2.7.6)

**Consent** — what participants agreed to (purposes, commercial use, transfer, withdrawal). **Licence** — what users are legally permitted to do with the dataset. **Copyright** — intellectual-property rights in the content. **Privacy** — obligations protecting personal information. They come from different sources (participants, data provider, creators, law) and constrain different things: an **openly licensed** dataset may still contain personal data; **de-identified** data may still be under copyright or contract; "Consent: Yes" doesn't permit uses the licence forbids (Example 57).

| Rubric | |
|---|---|
| Four correct definitions (½ each) | 2 |
| Independence explained | 1 |
| Example | 1 |
:::
:::

:::question 2(c) [4 points] Why should a sepsis model's evaluation include a hold-out of entire hospitals? What does a random patient-level split fail to test?
:::solution Solution & marking
If the model will be deployed at **previously unseen hospitals**, evaluation must mimic that. Patients from the same hospital share **equipment, units, EHR systems, coding and ordering practices and populations**; a random patient split puts the same hospitals in train and test, so the model can exploit **site-specific shortcuts** and evaluation overestimates transfer (**site leakage**). Holding out whole sites tests **generalization to new clinical environments** (covariate/concept shift).

| Rubric | |
|---|---|
| Deployment to new sites → evaluation must mirror it | 1 |
| Site-specific characteristics shared within hospital | 1 |
| Random split overestimates/shortcuts (site leakage) | 1 |
| Whole-site hold-out tests real generalization | 1 |
:::
:::

## Scenario-based Question [CLO 4] — 21 points

:::orig Voice-assistant dataset for a national helpline
A telecom regulator funds a **speech-recognition model** for an emergency helpline. A university releases a public dataset of **200,000 voice clips** collected through a smartphone app: volunteers read prompts aloud. Its page says *"Free for research"*. Most volunteers are **urban university students**; about **4%** of clips are in regional languages. Transcripts were produced by a **single annotator per clip**; disputed clips were resolved by majority vote among three crowd workers. The developer merges this dataset with a **commercial call-centre dataset** licensed for internal use only, re-encodes all audio, removes clips longer than 20 seconds, and keeps no record of these steps. The documentation reads only *"Consent obtained: Yes"*. The finished model will be sold to helplines in **three countries**.
:::

:::question 3(a) [4 points] Evaluate the dataset using $Q(D,T,C)$. Define D, T and C explicitly.
:::solution Solution & marking
- **D:** 200k read-aloud smartphone clips, mostly urban students, 4% regional languages, single-annotator transcripts, merged with call-centre audio, undocumented preprocessing.
- **T:** transcribe **spontaneous emergency calls** accurately in real time.
- **C:** national helplines in three countries — distressed, noisy, phone-line audio; many languages and accents; older and rural callers; high stakes.
- **Judgement: low fitness** — read speech ≠ distressed spontaneous speech; smartphone ≠ phone-line audio; demographic and language coverage inadequate; label quality uncertain; legal status unclear. Possibly fit for **research benchmarking** of urban read speech, not for this deployment.

| Rubric | |
|---|---|
| D, T, C each explicit (1 each) | 3 |
| Reasoned verdict | 1 |
:::
:::

:::question 3(b) [5 points] Identify the representativeness problems and explain why collecting 200,000 more clips from the same app would not solve them.
:::solution Solution & marking
- **Demographic:** urban students; missing older, rural, less-educated callers, children.
- **Linguistic:** 4% regional languages; accents under-represented.
- **Situational (missing deployment scenarios):** read prompts vs spontaneous, emotional, panicked speech; background noise; phone codecs vs smartphone microphone (covariate shift).
- **Geographic:** one country vs three.
- More clips from the same app sample the **same population and setting**; size reduces variance but **not systematic absence** — under-represented groups stay under-represented (Table 15 logic). Need targeted collection with subgroup minimums.

| Rubric | |
|---|---|
| Three distinct representativeness gaps (1 each) | 3 |
| Why more data doesn't fix it | 2 |
:::
:::

:::question 3(c) [4 points] Assess the transcript labelling process. What should the annotation record preserve?
:::solution Solution & marking
Single annotators give **no agreement estimate** (no κ), so error rates are unknown; regional languages may be transcribed by non-speakers. **Majority voting** among crowd workers may suppress legitimate alternative transcriptions and hide genuinely ambiguous audio — *consensus ≠ truth*. Test-set label errors would distort evaluation. Preserve: **original transcripts, annotator identity/expertise (language proficiency), consensus label, adjudication decisions, uncertainty flags, acceptable alternative transcripts**; measure inter-annotator agreement on a double-annotated sample.

| Rubric | |
|---|---|
| Problem with single annotator | 1 |
| Problem with majority vote | 1 |
| Items to preserve (≥4) | 2 |
:::
:::

:::question 3(d) [4 points] Identify the consent and licensing problems with selling the merged model in three countries.
:::solution Solution & marking
- "Free for research" signals a **research-only licence** → commercial sale likely not permitted.
- Call-centre data **licensed for internal use only** → can't be used in a product sold externally; combined data **inherit the most restrictive terms** (licence compatibility).
- **"Consent obtained: Yes"** doesn't record whether volunteers agreed to **commercial use, international transfer**, or how withdrawal applies to the model.
- **Privacy:** voices are biometric/personal data; de-identification of voice is weak; cross-border transfer rules apply. Model weights don't escape these constraints (memorization).

| Rubric | |
|---|---|
| Research-only licence vs commercial sale | 1 |
| Internal-use licence / incompatibility | 1 |
| Consent inadequacy | 1 |
| Privacy/transfer issue | 1 |
:::
:::

:::question 3(e) [4 points] The developer kept no record of re-encoding and removing long clips. Explain why this matters and list what should have been recorded.
:::solution Solution & marking
Without **lineage**, results are **not reproducible**, errors can't be debugged or rolled back, and users can't judge suitability — e.g. dropping clips > 20 s may disproportionately remove long, distressed emergency calls or certain languages (undocumented **exclusion** → representation bias). For each transformation record: **input dataset version, code/software version, parameters (codec, bitrate, 20 s threshold), output version, timestamp, responsible person, validation results** — plus counts of excluded clips by language/group.

| Rubric | |
|---|---|
| Reproducibility/audit/rollback consequence | 1 |
| Hidden bias from undocumented exclusion | 1 |
| Lineage fields (≥5 → 2, 3–4 → 1) | 2 |
:::
:::

## Identifying Failures [CLO 4] — 8 points

:::question 4 [8 points] For each of the following, name the bias type from Table 27 and justify it in one sentence (2 points each): (i) a fall-detection wearable validated on young volunteers is deployed in care homes; (ii) one model predicts diabetes complications for all ethnic groups although risk factors differ between them; (iii) a loan model is trained on approvals made under a past discriminatory policy; (iv) a triage assistant validated for nurse support is used by a call centre to refuse ambulances automatically.
:::solution Solution & marking
(i) **Evaluation bias** (or representation bias) — validation population didn't reflect deployment (elderly care-home residents). (ii) **Aggregation bias** — one model for populations with different predictor–outcome relationships. (iii) **Historical bias** — past inequities embedded in labels. (iv) **Deployment bias** — used outside its validated purpose and without human review. 1 point for the name, 1 for the justification.
:::
:::
