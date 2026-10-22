# M2 · Reflection answers R1–R5

Take-home reflection questions (Module 2 notes, PDF pages 138–145). The notes say there is **no single correct answer** — these are model answers that apply every Module 2 tool to one system. They are the best preparation for a **long scenario question** in Quiz 2 or the mid: each bullet below is a ready-made 3–5 mark paragraph.

<div class="pdf-links">
<a href="m2-scenarios.html">Scenario answers S1–S5</a>
<a href="m2c-notes.html">Part C notes (governance, case studies)</a>
<a href="pdfs/notes/Module-2-Notes.pdf#page=138">Reflections in the PDF (p.138)</a>
</div>

## R1 — National student success and intervention system

:::orig R1: A National Student Success and Intervention System — Module 2 notes, PDF p.138
The national higher education authority plans to build an AI system that identifies university students at risk of leaving their programs. The purpose is to provide early academic, financial, and psychological support.

The participating universities submit the following data:

- GPA and course grades
- attendance records
- tuition payment history
- library and online learning activity
- disciplinary records
- scholarship status
- accommodation location
- counseling service usage
- family income
- disability status

However, the universities define dropout differently. Some label a student as a dropout after one missed semester. Others wait for two years. Some include students who transfer to another institution, while others do not. Attendance is recorded through scanners at certain universities, manual registers at others, and not recorded at all in some departments.

The training dataset contains mostly students from large urban universities. Students from rural campuses, online programs, small private institutions, and vocational colleges are poorly represented. The project team proposes replacing all missing values with the overall mean and removing students with unusual academic histories.

The final model assigns each student a risk score. Some universities intend to use the score to offer additional support. Others intend to reduce scholarships for students classified as highly likely to leave.

**Questions**

1. Develop a precise operational definition of student dropout. Explain how your definition treats temporary leave, delayed registration, transfer, expulsion, late graduation, and administrative registration errors.
2. Apply the fitness-for-purpose formulation $Q(D,T,C)$ to determine whether the available dataset is suitable for national deployment. Define the dataset, task, and context explicitly.
3. Explain how the dataset represents a constructed institutional record rather than an objective description of student motivation or ability. Identify the human, technical, administrative, and policy decisions embedded in the data.
4. Design a representativeness audit covering institution type, geographic region, mode of study, socioeconomic status, disability, gender, program level, and intersectional groups. Explain what evidence would justify national deployment.
5. Propose a missing-data strategy for attendance, income, counseling usage, and online activity. For each variable, discuss whether missingness may be MCAR, MAR, or MNAR and whether the absence itself could be informative.
6. Evaluate whether counseling usage and disability status should be included as predictive features, retained only for fairness auditing, or excluded entirely. Consider privacy, data minimization, potential benefit, and possible harm.
7. Design a governance structure for the system. Specify the responsibilities of data owners, data stewards, university administrators, ethics committees, technical teams, student representatives, and national regulators.
8. Compare the ethical consequences of using the risk score to provide assistance with using it to restrict scholarships. Explain how the same model can produce beneficial or harmful outcomes depending on the decision policy surrounding it.
9. Prepare a plan for contestability and human review. Explain how students could inspect, challenge, and correct the data and decisions associated with their risk scores.
10. Identify the conditions under which the project should be delayed, redesigned, limited to selected institutions, or rejected entirely.
:::

:::question 1. Develop a precise operational definition of student dropout. Explain how your definition treats temporary leave, delayed registration, transfer, expulsion, late graduation, and administrative registration errors.
:::solution Model answer
**Dropout (at index time $t$ = start of semester $s$):** a student enrolled in a degree programme in semester $s-1$ who, by the **census date of semester $s+2$** (one academic year later), is **not enrolled in any degree programme at any institution in the national registry**, has **not graduated**, and has **no approved leave** in force.
- **Temporary approved leave:** *not* dropout while the leave is valid; becomes dropout only if the student does not return by the end of approved leave + one semester.
- **Delayed registration:** not dropout if registered by the census date (late fee cases).
- **Transfer:** *not* dropout (student continues education) — tracked as a separate outcome "institutional transfer" via the national registry.
- **Expulsion:** a **separate category** ("institution-initiated exit"), not voluntary dropout — mixing them confuses disciplinary policy with student risk.
- **Late graduation:** not dropout (still enrolled / eventually graduates).
- **Administrative registration errors:** corrected through a verification step before labelling; never counted as dropout.
The same definition must be applied by **all** universities (harmonized data dictionary), with the raw institutional codes preserved for audit.
:::
:::

:::question 2. Apply the fitness-for-purpose formulation $Q(D,T,C)$ to determine whether the available dataset is suitable for national deployment. Define the dataset, task, and context explicitly.
:::solution Model answer
- **$D$:** pooled records from participating universities with heterogeneous dropout labels, three attendance regimes, sensitive attributes, over-representation of large urban universities.
- **$T$:** estimate each student's probability of leaving within one year, at the start of each semester, to **target support** (advising, financial, psychological).
- **$C$:** national deployment across urban, rural, online, private and vocational institutions; decisions affect funding and wellbeing; legal duties of fairness and privacy.
**Verdict:** currently **not fit**. Labels are inconsistent (construct problem), attendance is incomparable, key populations are under-represented, imputation plan erases information, and some intended uses are punitive. It may be fit for **descriptive national reporting** after harmonization, and for a **pilot support tool** in well-represented institutions — not national deployment until the gaps below are fixed.
:::
:::

:::question 3. Explain how the dataset represents a constructed institutional record rather than an objective description of student motivation or ability. Identify the human, technical, administrative, and policy decisions embedded in the data.
:::solution Model answer
The data do not measure motivation or ability; they record **institutional processes**:
- **Human decisions:** what counts as dropout, what to measure (no mental health, no part-time work), who is included.
- **Technical:** scanners vs registers vs nothing; online-platform logging (clicks ≠ learning); missing values encoded differently.
- **Administrative:** grading standards differ by university; disciplinary records reflect local enforcement; scholarship status reflects funding rules; counselling usage reflects **service availability and stigma**, not need.
- **Policy:** fee deadlines, leave rules, transfer recognition, and which universities chose to participate.
So a "risk score" partly reflects **which university and department a student is in**, not just the student.
:::
:::

:::question 4. Design a representativeness audit covering institution type, geographic region, mode of study, socioeconomic status, disability, gender, program level, and intersectional groups. Explain what evidence would justify national deployment.
:::solution Model answer
For each axis — **institution type** (public/private/vocational), **region** (urban/rural, province), **mode** (on-campus/online), **socioeconomic status** (income band, scholarship), **disability**, **gender**, **programme level** (UG/PG), and **intersections** (e.g. rural × female × low-income; online × disability) — compare **dataset share vs national enrolment share**, outcome prevalence, and data completeness. Then evaluate model **sensitivity, false-negative rate, calibration and CIs per group**, requiring minimum sample sizes $n_g\ge n_{\min}$ for precise estimates.
**Evidence for national deployment:** adequate coverage of every major group; subgroup performance and calibration within agreed tolerances; external validation on held-out **institutions** (site-level hold-out); and a pilot in under-represented institutions. Otherwise restrict deployment to validated institution types.
:::
:::

:::question 5. Propose a missing-data strategy for attendance, income, counseling usage, and online activity. For each variable, discuss whether missingness may be MCAR, MAR, or MNAR and whether the absence itself could be informative.
:::solution Model answer
- **Attendance:** missing mainly where no recording system exists. That depends on the department/university — an **observed** variable — not on how often the student actually attended, so it is best treated as **MAR (given institution/department)**, not MNAR. It would only be MNAR if, within the same course, students who skip were less likely to be recorded. Absence is informative about the *institution*, not the student. Don't impute a mean; record `attendance_system` and `attendance_missing`; use attendance only where measured, or build models that don't depend on it.
- **Income:** likely **MNAR** (high or very low earners withhold; non-applicants for aid have no form) or MAR by scholarship status. Use an indicator + groupwise or multiple imputation fitted on training data; consider income bands.
- **Counselling usage:** missing = didn't use **or** service unavailable/not shared → absence is **informative and ambiguous**; also highly sensitive. Better excluded (see 6).
- **Online activity:** missing for on-campus courses without LMS use → **MAR given mode/course**; encode "not applicable" separately from "zero activity".
All imputation **inside training folds**; never mean-impute the whole dataset; never delete students with unusual histories — they may be exactly those needing support.
:::
:::

:::question 6. Evaluate whether counseling usage and disability status should be included as predictive features, retained only for fairness auditing, or excluded entirely. Consider privacy, data minimization, potential benefit, and possible harm.
:::solution Model answer
**Counselling usage:** **exclude from prediction**. It's highly sensitive health information; using it would penalize help-seeking (students may avoid counselling), it reflects availability more than need, and benefit < risk (data minimization). Possibly retain aggregated, restricted data for evaluating whether the system serves students in distress.
**Disability status:** **exclude from prediction, retain under restricted access for fairness auditing** — without it you cannot detect whether disabled students receive lower-quality scores; access limited to the audit team, with retention limits and consent/lawful basis. Using it as a predictor risks discriminatory treatment, especially where scores restrict scholarships.
:::
:::

:::question 7. Design a governance structure for the system. Specify the responsibilities of data owners, data stewards, university administrators, ethics committees, technical teams, student representatives, and national regulators.
:::solution Model answer
- **National regulator / higher-education authority (data owner):** ultimate accountability, approves purpose and uses, bans punitive uses.
- **Data stewards** (national + each university): harmonized dictionary, label definition, quality reports, access policy.
- **Data custodians / technical team:** secure platform, lineage, leakage-safe pipelines, monitoring dashboards.
- **University administrators:** act on scores only through approved support policies; ensure human review.
- **Ethics committee / IRB and data-protection office:** consent/lawful basis, sensitive data, secondary use, retention.
- **Student representatives:** co-design, review of uses, appeals oversight.
- **Independent auditor:** periodic fairness and performance audits, published summaries.
Clear assignment avoids "everyone uses it, no one owns it".
:::
:::

:::question 8. Compare the ethical consequences of using the risk score to provide assistance with using it to restrict scholarships. Explain how the same model can produce beneficial or harmful outcomes depending on the decision policy surrounding it.
:::solution Model answer
The **model is identical; the decision policy changes the ethics**. As **assistance**, a false positive costs an unnecessary advising email; a true positive gets help → errors are cheap and the intervention reduces dropout. As **restriction**, a false positive removes funding from a student who wasn't leaving and a true positive is pushed out faster → **self-fulfilling prophecy**, feedback loop, and disproportionate harm to low-income and under-represented groups whose scores are least reliable. Restriction also changes behaviour (students hide difficulties). Hence approve the system **only for supportive interventions**, with thresholds set by support capacity.
:::
:::

:::question 9. Prepare a plan for contestability and human review. Explain how students could inspect, challenge, and correct the data and decisions associated with their risk scores.
:::solution Model answer
Students are **notified** that a score exists and what it is used for; can **view the data** behind it (grades, attendance, flags) and the main contributing factors; can **correct errors** (e.g. attendance recorded as missing, wrong registration status) through a registrar process with deadlines; can **appeal** any adverse decision to a human panel that may override the score; overrides and appeals are **logged** and fed back to data stewards; no decision is made on the score alone. Periodic reports on appeal rates by subgroup act as an early-warning signal for bias.
:::
:::

:::question 10. Identify the conditions under which the project should be delayed, redesigned, limited to selected institutions, or rejected entirely.
:::solution Model answer
- **Delay:** until a harmonized dropout definition and dictionary are adopted and data corrected.
- **Redesign:** if labels remain inconsistent, if attendance can't be standardized, or if subgroup calibration fails.
- **Limit to selected institutions:** where data coverage and validation are adequate (e.g. large urban universities) while collecting data elsewhere.
- **Reject:** if universities insist on **punitive uses** (scholarship cuts), if sensitive data can't be lawfully used or protected, if severe subgroup disparities can't be fixed, or if no contestability/human review can be guaranteed.
:::
:::

## R2 — Smart-city predictive policing platform

:::orig R2: A Smart City Predictive Policing Platform — Module 2 notes, PDF p.140
A city government plans to predict where serious crime is likely to occur during the next week. The proposed system combines:

- historical arrest records
- emergency telephone calls
- police patrol logs
- reported crimes
- CCTV detections
- social media posts
- geographic and demographic information
- records from courts and correctional institutions

The developers treat arrest counts as a measure of crime prevalence. Neighborhoods with more recorded arrests receive higher predicted risk scores and consequently receive more patrol officers. Increased policing produces more stops, searches, and arrests, which are then added to the training dataset.

Residents argue that certain neighborhoods have historically received more police attention and therefore generate more records, even when underlying offending rates are similar. They also claim that the system may treat poverty, housing density, and ethnicity as indirect proxies for criminality.

The police department proposes retaining detailed location and identity information indefinitely because it may be useful for future investigations.

**Questions**

1. Evaluate the construct validity of using arrests as a proxy for crime commission. Propose alternative outcome definitions and discuss the limitations of each.
2. Map the complete data-generating process from underlying events to reported incidents, police responses, arrests, administrative records, and model predictions. Identify where institutional behavior shapes the observed data.
3. Explain how a feedback loop could arise between historical policing, recorded arrests, predicted risk, and future police deployment. Discuss how this loop may reinforce historical inequalities.
4. Determine which variables may act as proxies for sensitive attributes even if race or ethnicity is removed. Explain why removing explicit sensitive attributes does not necessarily eliminate discrimination.
5. Design a fairness evaluation that considers geographic, demographic, socioeconomic, and intersectional disparities. Specify what outcomes should be compared and how unequal measurement rates should be handled.
6. Propose a data-minimization policy for identity, location, social media, and CCTV data. Explain which information is necessary, which can be aggregated, and how long different data elements should be retained.
7. Develop an oversight and accountability framework involving police leadership, courts, elected officials, community representatives, civil-rights experts, data stewards, and independent auditors.
8. Discuss whether individuals should be informed that their neighborhoods or activities contributed to model training. Consider transparency, public safety, privacy, and procedural justice.
9. Propose safeguards that prevent a model-generated risk score from becoming automatic justification for stops, searches, surveillance, or arrests.
10. Decide whether predictive policing can be made ethically acceptable through technical and governance controls, or whether its underlying measurement and power structures create limitations that cannot be solved through model improvement alone.
:::

:::question 1. Evaluate the construct validity of using arrests as a proxy for crime commission. Propose alternative outcome definitions and discuss the limitations of each.
:::solution Model answer
Arrests measure **enforcement**, not offending: they depend on patrol intensity, discretion, reporting and surveillance (Table 29). Similar true offending yields more arrests where police are present. **Alternatives:** (i) **victim-reported serious crimes** — closer to harm, but reporting rates vary with trust in police; (ii) **emergency calls for service** — citizen-initiated, but include non-crime and duplicate calls, vary by community; (iii) **victimization surveys** — capture unreported crime, but small samples, recall/social-desirability bias, coarse geography; (iv) **injury/hospital data for violent crime** — objective harm measure, but only for some crimes and has privacy issues. A composite of victim reports + surveys for serious violent crime, validated against each other, is more defensible than arrests.
:::
:::

:::question 2. Map the complete data-generating process from underlying events to reported incidents, police responses, arrests, administrative records, and model predictions. Identify where institutional behavior shapes the observed data.
:::solution Model answer
**Underlying events** (offences) → **detection/reporting** (victims call or not; CCTV coverage; social media visibility) → **police response** (where patrols are, what's prioritized) → **stops/searches/arrests** (officer discretion) → **charging/courts/convictions** (prosecutorial and judicial decisions, legal aid) → **administrative records** (coding rules) → **model training** → **predictions** → **patrol allocation** → back to detection. Institutional behaviour shapes the data at **detection, response, arrest, charging and recording** — every arrow except the first.
:::
:::

:::question 3. Explain how a feedback loop could arise between historical policing, recorded arrests, predicted risk, and future police deployment. Discuss how this loop may reinforce historical inequalities.
:::solution Model answer
Historical over-policing → more recorded arrests in area A → model predicts higher risk in A → **more patrols** in A → more stops/searches → more **minor** incidents recorded → arrests rise → model "confirmed" and even more confident (**feedback bias**, selective labels, performative prediction — Example 5). Areas with less policing look safer because offences go unrecorded. The loop **amplifies historical inequality** independent of true crime rates. Breaking it needs outcomes not generated by patrol presence, randomized/held-out allocation, and monitoring of how much new data comes from model-directed patrols.
:::
:::

:::question 4. Determine which variables may act as proxies for sensitive attributes even if race or ethnicity is removed. Explain why removing explicit sensitive attributes does not necessarily eliminate discrimination.
:::solution Model answer
Neighbourhood/geography (segregation), **housing density**, poverty indicators, demographic composition, school and income data, prior arrests/convictions (shaped by historical policing), social-media language/dialect, CCTV density, call volumes. Removing race/ethnicity does not remove discrimination because these variables are **correlated with it** ($X_{\text{proxy}}\leftrightarrow A$) and because the **label itself** (arrests) carries historical bias — the model reproduces disparities through location and history (Example 59 logic).
:::
:::

:::question 5. Design a fairness evaluation that considers geographic, demographic, socioeconomic, and intersectional disparities. Specify what outcomes should be compared and how unequal measurement rates should be handled.
:::solution Model answer
Compare across **areas grouped by demographic composition, income and geography**, and their **intersections**: predicted-risk distributions; patrol allocation; stops, searches and arrests **per resident** and per **victim-reported crime**; **hit rates** (share of stops finding wrongdoing — lower hit rates suggest over-stopping); false-positive rates against victim-reported serious crime; changes in community outcomes. **Handle unequal measurement** by using outcomes less dependent on policing (victimization surveys, hospital data), estimating reporting rates by area, and reporting uncertainty. Track trends over time to detect feedback amplification.
:::
:::

:::question 6. Propose a data-minimization policy for identity, location, social media, and CCTV data. Explain which information is necessary, which can be aggregated, and how long different data elements should be retained.
:::solution Model answer
- **Identity data:** not needed for **place-based** weekly forecasting → do not ingest names/IDs into the model; keep only in the source police systems under existing law.
- **Location:** aggregate to grid cells/weeks; delete precise coordinates after aggregation.
- **Social media:** exclude (low validity, chilling effects, consent issues) or use only aggregated public-safety signals with legal review.
- **CCTV:** use only counts of verified detections, not footage or face data; footage retained ≤ statutory short period (e.g. 30 days) unless evidence.
- **Retention:** model features kept for a fixed period (e.g. 1–2 years) for auditing, then deleted; **no indefinite retention** "for future investigations" — that's a secondary use requiring separate legal authority.
Benefit > Risk test for every variable, documented.
:::
:::

:::question 7. Develop an oversight and accountability framework involving police leadership, courts, elected officials, community representatives, civil-rights experts, data stewards, and independent auditors.
:::solution Model answer
**Elected officials/city council** approve the purpose and publish policy; **police leadership** owns operational use (model owner) and is accountable; **courts** set legal limits on stops/searches and admissibility; **community representatives** sit on an oversight board with review rights; **civil-rights experts** assess discrimination; **data stewards** manage definitions, quality, lineage; **independent auditors** run annual fairness and effectiveness audits with public reports; an **ethics/privacy office** reviews data uses. Include sunset clauses, public registers of model versions, and the power to suspend the system.
:::
:::

:::question 8. Discuss whether individuals should be informed that their neighborhoods or activities contributed to model training. Consider transparency, public safety, privacy, and procedural justice.
:::solution Model answer
At least **collective transparency**: publish that the system exists, what data sources are used, how neighbourhoods are scored, accuracy and fairness audits — required for **procedural justice** and public trust. **Individual notification** is warranted where personal data (arrest/court records, social media) are used for training, unless it would compromise specific active investigations; a place-based model that uses only aggregated data reduces the need. Balance: public safety interest in not revealing tactics vs privacy rights and the legitimacy of policing; default to openness about **methods and impacts**.
:::
:::

:::question 9. Propose safeguards that prevent a model-generated risk score from becoming automatic justification for stops, searches, surveillance, or arrests.
:::solution Model answer
Policy that a risk score is **never** grounds for reasonable suspicion, stops, searches, surveillance or arrests; scores inform **resource planning only** (e.g. non-enforcement services, lighting, community programmes); officer training on **automation bias**; documentation of the independent basis for every stop; audit of stops in high-score areas; prohibition on individual-level scores; interface design that shows uncertainty; and an appeal/complaint channel for residents.
:::
:::

:::question 10. Decide whether predictive policing can be made ethically acceptable through technical and governance controls, or whether its underlying measurement and power structures create limitations that cannot be solved through model improvement alone.
:::solution Model answer
Technical controls (better targets, debiasing, audits) can reduce harm but **cannot fix the core problems**: the outcome data are generated by the very institution being optimized, crime is under-observed unevenly, and deploying police changes the data (feedback). These are **measurement and power-structure** limits, not modelling errors. A defensible position: predictive **policing** for enforcement allocation is **not acceptable** in its proposed form; a narrowly scoped, transparent, community-governed tool using **victimization-based** outcomes for **non-punitive** prevention resources might be, subject to independent audit and sunset.
:::
:::

## R3 — Multihospital sepsis early-warning system

:::orig R3: A Multihospital Sepsis Early-Warning System — Module 2 notes, PDF p.141
A healthcare network wants to build an AI system that predicts sepsis six hours before clinical recognition. Data are collected from twelve hospitals and include:

- vital signs
- laboratory results
- medication orders
- diagnosis codes
- clinical notes
- device measurements
- intensive care transfers
- mortality and discharge records

The system achieves an AUC of 0.98 during internal evaluation. Investigation shows that broad-spectrum antibiotic orders and intensive care transfer requests are among the strongest predictors. These variables often become available only after clinicians suspect sepsis.

Some hospitals use different laboratory equipment, measurement units, and electronic record systems. A device firmware update changes the distribution of heart-rate readings halfway through the collection period. Several patients appear in the dataset multiple times, and images or records from the same patient may enter different partitions.

Lactate values are missing for most patients because clinicians order the test mainly for those who appear seriously ill. The team proposes imputing all missing lactate values with the population mean. The training data contain few patients from rural hospitals and limited representation of some age and ethnic groups.

**Questions**

1. Define the prediction time and outcome window precisely. Construct a timeline showing which variables are legitimately available six hours before clinical recognition.
2. Identify possible target leakage, temporal leakage, group leakage, site leakage, and preprocessing contamination. Explain how each could inflate reported performance.
3. Evaluate whether antibiotic orders and intensive care transfer requests should be included as predictors. Distinguish early physiological risk factors from variables that encode clinician recognition or response.
4. Develop an appropriate partitioning and validation strategy. Consider patient-level grouping, chronological evaluation, hospital-level holdout, cross-validation, and a final untouched test set.
5. Analyze the missing lactate values. Explain why missingness may be informative and how mean imputation could erase clinically meaningful information.
6. Design a harmonization plan for different laboratory units, devices, firmware versions, sampling frequencies, clocks, and electronic health record systems.
7. Propose a subgroup and intersectional evaluation plan. Include performance, calibration, false-negative rates, false-positive rates, and measurement quality across hospitals and populations.
8. Create a data-lineage plan that connects every trained model to the exact source data, dataset versions, preprocessing code, parameters, validation results, and responsible personnel.
9. Design a deployment policy explaining how the model output should interact with clinical judgment. Include alert thresholds, escalation procedures, override mechanisms, audit logs, and monitoring for alert fatigue.
10. State the evidence that would be required before the model could be deployed at a hospital that did not contribute data to development.
:::

:::question 1. Define the prediction time and outcome window precisely. Construct a timeline showing which variables are legitimately available six hours before clinical recognition.
:::solution Model answer
**Unit:** an inpatient encounter, evaluated **every hour** (index time $t$). **Outcome:** at index time $t$ the model predicts whether **clinical recognition of sepsis** (adjudicated onset, e.g. Sepsis-3 criteria, timed at the first sepsis-suspicion order or diagnosis) will occur in the window $(t,\ t+6\text{h}]$. Patients are no longer scored once sepsis has been recognized.
**Timeline:** admission → vitals and device data (available within minutes, by **availability** time) → labs (available at **result-finalized** time, not draw time) → **clinician suspicion** (blood cultures, antibiotic orders, ICU request) → recognition/diagnosis code → ICU transfer → discharge/mortality. **Legitimate at $t$:** demographics, comorbidities from prior encounters, vitals and device data up to $t$, labs **finalized** before $t$, lab-ordering patterns before $t$ (with care). **Not legitimate:** antibiotic orders, ICU requests, diagnosis codes, notes and anything time-stamped after $t$ or recorded at discharge.
:::
:::

:::question 2. Identify possible target leakage, temporal leakage, group leakage, site leakage, and preprocessing contamination. Explain how each could inflate reported performance.
:::solution Model answer
- **Target leakage:** antibiotic orders, ICU transfer requests, sepsis diagnosis codes, notes mentioning sepsis encode clinician recognition → the model "predicts" recognition by seeing it.
- **Temporal leakage:** labs/notes stamped by event time but available later; discharge and mortality records used as features.
- **Group leakage:** repeated encounters of the same patient across train/test → patient memorization.
- **Site leakage:** random splits across 12 hospitals don't test a new hospital; site-specific practices (ordering habits) become shortcuts.
- **Preprocessing contamination:** lactate mean and any scaling computed on the full dataset.
Each lets the model use information unavailable 6 hours before recognition → AUC 0.98 that collapses prospectively (cf. external validation of the Epic Sepsis Model).
:::
:::

:::question 3. Evaluate whether antibiotic orders and intensive care transfer requests should be included as predictors. Distinguish early physiological risk factors from variables that encode clinician recognition or response.
:::solution Model answer
**Exclude them.** They are **clinician responses** — they occur *because* sepsis is suspected, so they encode recognition rather than **early physiological risk**. The model would fire only after clinicians already know, adding nothing (and the 6-hour lead would vanish). Keep **early physiological risk factors**: rising heart and respiratory rate, temperature, falling BP, mental-status change, lab trends (WBC, creatinine, lactate when available), comorbidities. Borderline features (e.g. "blood culture ordered") must be time-gated and usually excluded too.
:::
:::

:::question 4. Develop an appropriate partitioning and validation strategy. Consider patient-level grouping, chronological evaluation, hospital-level holdout, cross-validation, and a final untouched test set.
:::solution Model answer
1. Hold out **2 whole hospitals** (incl. a rural one) as an **external test set**, untouched.
2. From the remaining 10, hold out the **most recent period** as a temporal test set.
3. On the training portion use **GroupKFold by patient** (stratified where possible) with **leave-one-hospital-out** folds for model selection; all preprocessing (unit harmonization fits, imputation, scaling) inside training folds.
4. Final evaluation once on temporal + external sets: AUROC, **PPV at the alert threshold**, sensitivity, lead time, calibration, alerts per bed-day.
5. Silent prospective deployment before go-live.
:::
:::

:::question 5. Analyze the missing lactate values. Explain why missingness may be informative and how mean imputation could erase clinically meaningful information.
:::solution Model answer
Lactate is ordered when clinicians **suspect serious illness**, so its presence is a marker of clinician concern (possibly itself near-leakage if ordered close to recognition) and its absence signals lower suspected severity — **informative, MNAR-like missingness**. Population-mean imputation gives the 70%+ unmeasured patients a fabricated "moderately abnormal" value, **erasing** the difference between "not ordered" and "measured normal", shrinking variance and blurring the real lactate signal. Instead: a `lactate_measured_before_t` indicator, last value carried forward only within a validity window, time since last measurement; and check that ordering itself isn't a recognition proxy.
:::
:::

:::question 6. Design a harmonization plan for different laboratory units, devices, firmware versions, sampling frequencies, clocks, and electronic health record systems.
:::solution Model answer
- **Lab units:** unit-aware schema; map every lab to a standard code (e.g. LOINC) and unit with explicit conversions (lactate mg/dL ↔ mmol/L); range validation.
- **Lab equipment:** compare reference ranges across analyzers; site-level calibration offsets if needed.
- **Devices/firmware:** record device model and **firmware version** as metadata; detect the change point; re-calibrate or model pre/post separately; test performance on both periods.
- **Sampling frequency:** resample vitals to a common grid (e.g. hourly summaries) with measurement-count features.
- **Clocks:** synchronize to a single time standard; use **availability timestamps**; check device vs server time.
- **EHR systems:** common data model mapping, data dictionary per field, validation of cross-site consistency; document all mappings in lineage.
:::
:::

:::question 7. Propose a subgroup and intersectional evaluation plan. Include performance, calibration, false-negative rates, false-positive rates, and measurement quality across hospitals and populations.
:::solution Model answer
Report for each **hospital** (rural vs urban), **age band**, **sex**, **ethnicity**, and intersections (e.g. elderly × rural × ethnic minority): sensitivity/**false-negative rate** (missed sepsis), **false-positive rate** and alerts per patient (alert fatigue), PPV, AUROC with CIs, **calibration curves**, median **lead time**, and **measurement quality** (missingness of vitals/labs, device accuracy across skin tones for SpO₂). Set minimum sample sizes; where groups are too small, collect more data before claiming validity. Choose **equal opportunity** (equal TPR) as the main fairness target because missed cases are most harmful (Example 62).
:::
:::

:::question 8. Create a data-lineage plan that connects every trained model to the exact source data, dataset versions, preprocessing code, parameters, validation results, and responsible personnel.
:::solution Model answer
Every model version links to: **source extracts** per hospital (system, extraction query, date range, version hash); each transformation step $T_i$ (harmonization, cohort selection, labelling algorithm, feature generation, imputation, splitting) with **code commit, parameters, input/output dataset versions, timestamp, responsible engineer, validation results**; the **split specification** (patients/hospitals per partition); training configuration and random seeds; evaluation reports; **approval sign-off**. Stored in a versioned registry (e.g. dataset and model versioning tools) so any prediction can be traced and the model rebuilt or rolled back.
:::
:::

:::question 9. Design a deployment policy explaining how the model output should interact with clinical judgment. Include alert thresholds, escalation procedures, override mechanisms, audit logs, and monitoring for alert fatigue.
:::solution Model answer
The model **supports**, never replaces, clinical judgement. **Alert threshold** chosen by expected alerts per nurse-shift and target sensitivity (capacity-aware, like Quiz 1's 20 inspections/day); tiered alerts (watch vs urgent). **Escalation:** urgent alert → bedside nurse assessment within 30 min → rapid-response team if criteria met. **Override:** clinicians can dismiss with a reason code; overrides logged. **Audit logs** of every score, alert, action and outcome. **Monitoring:** alert rate, PPV, sensitivity, lead time, override rates, alert fatigue surveys, calibration drift, data drift (firmware, units), subgroup performance; **fallback** to standard screening (qSOFA/NEWS) when inputs are missing or the system fails.
:::
:::

:::question 10. State the evidence that would be required before the model could be deployed at a hospital that did not contribute data to development.
:::solution Model answer
**External validation** on that hospital's own retrospective data (or a held-out site similar to it) after **harmonization checks** (units, devices, EHR mapping); acceptable sensitivity, PPV, lead time and **calibration** (recalibrate locally if needed); subgroup performance for its population; a **silent (shadow) deployment** period comparing alerts with real outcomes; workflow integration and staff training plan; governance approval (clinical governance, IRB if research) and a monitoring plan with stop criteria.
:::
:::

## R4 — Synthetic financial data for credit approval

:::orig R4: Synthetic Financial Data for Credit Approval — Module 2 notes, PDF p.142
A financial technology company wants to develop a credit approval model but faces restrictions on sharing customer records with external developers. It trains a generative model on historical loan applications and produces a synthetic dataset containing:

- income
- occupation
- age
- geographic region
- repayment history
- property ownership
- previous defaults
- loan amount
- approval decisions

The synthetic data closely match the overall distributions of the source dataset. External developers train a classifier that performs well when evaluated on a synthetic test set.

However, the original data contain few applicants from rural regions, informal employment sectors, and low-income households. Historical approval decisions may also reflect discriminatory lending practices. Rare default patterns are poorly represented. Several synthetic records are unusually similar to real customers, raising possible membership inference and reconstruction risks.

Management argues that because the dataset is synthetic, consent, privacy, fairness, and licensing concerns no longer apply.

**Questions**

1. Challenge or defend the claim that synthetic data are automatically anonymous, fair, representative, and ethically unrestricted.
2. Design a validation framework covering fidelity, utility, privacy, fairness, coverage, and realism. For each dimension, specify suitable tests and acceptable evidence.
3. Explain why matching overall distributions is insufficient. Identify subgroup, intersectional, tail, and dependency structures that should also be examined.
4. Analyze how historical discrimination in approval decisions could be reproduced or amplified by the synthetic generator and the downstream credit model.
5. Propose methods for evaluating membership inference, reconstruction, memorization, and record similarity risks.
6. Determine whether protected attributes should be included in the synthetic dataset, excluded from model training, or preserved under restricted access for fairness auditing.
7. Explain why evaluation only on synthetic test data cannot establish real-world utility. Propose a secure method for evaluating models on representative real data.
8. Develop a documentation package for the synthetic dataset, including motivation, source data, generation method, model version, privacy safeguards, known limitations, intended uses, discouraged uses, and maintenance procedures.
9. Consider a case where the synthetic dataset improves privacy but reduces representation of already marginalized applicants. Explain how the organization should balance privacy, fairness, and utility.
10. Recommend whether the synthetic dataset should be approved for internal experimentation, external research, operational credit decisions, or none of these uses. Justify different approval levels.
:::

:::question 1. Challenge or defend the claim that synthetic data are automatically anonymous, fair, representative, and ethically unrestricted.
:::solution Model answer
**Not anonymous:** generators can memorize; records "unusually similar to real customers" enable **membership inference and reconstruction** — residual disclosure risk. **Not fair:** the generator copies **historically discriminatory approvals**. **Not representative:** it reproduces the source's **under-representation** of rural, informal and low-income applicants and misses rare defaults. **Not unrestricted:** it is a **derived product** of personal data — the original **consent, privacy law, contracts and licences** still constrain its use and sharing. Synthetic changes the risk profile; it doesn't remove obligations.
:::
:::

:::question 2. Design a validation framework covering fidelity, utility, privacy, fairness, coverage, and realism. For each dimension, specify suitable tests and acceptable evidence.
:::solution Model answer
| Dimension | Tests | Acceptable evidence |
|---|---|---|
| **Fidelity** | Marginals, pairwise correlations, conditional distributions, tails; distance metrics | Close agreement overall **and by subgroup** |
| **Utility** | Train on synthetic, **test on real** (TSTR) vs train-on-real | Small performance gap on real held-out data |
| **Privacy** | Membership-inference attack, nearest-neighbour distance to real records, attribute inference | Attack success ≈ chance; no near-copies beyond threshold |
| **Fairness** | Approval rates, error rates by group in synthetic vs real; downstream model disparity | No amplification; disparities documented |
| **Coverage** | Counts of rare defaults, rural/informal/low-income cells | Minimum counts per critical cell |
| **Realism** | Domain-rule checks (age vs employment length, loan vs income limits) | Near-zero impossible records |
:::
:::

:::question 3. Explain why matching overall distributions is insufficient. Identify subgroup, intersectional, tail, and dependency structures that should also be examined.
:::solution Model answer
Overall marginals can match while **subgroups, intersections, tails and dependencies** are wrong. Examine: rural × low-income × informal applicants; age × occupation; **joint** income–loan–default relationships; **tail** behaviour (rare defaults, very large loans); temporal structure of repayment histories; and the **conditional relationship $P(\text{approval}\mid X)$** within groups. A model can look good overall yet fail on exactly the applicants who need fair treatment (Gender Shades logic: $E_{\text{overall}}=\sum P(g)E_g$).
:::
:::

:::question 4. Analyze how historical discrimination in approval decisions could be reproduced or amplified by the synthetic generator and the downstream credit model.
:::solution Model answer
The generator learns $P(X,\text{approval})$ from **biased past decisions**; synthetic data encode the same rejections for disadvantaged groups. The downstream model trained on "approval" as a label then learns to **imitate discrimination** (historical bias, label = past decision, not creditworthiness). Amplification arises because generators under-sample sparse groups (fewer, more stereotyped examples), smooth away counter-examples, and the classifier optimizes accuracy on majority patterns. A better target is **actual repayment**, with selective-labels caveats (we only see repayment for approved applicants).
:::
:::

:::question 5. Propose methods for evaluating membership inference, reconstruction, memorization, and record similarity risks.
:::solution Model answer
Run **membership-inference attacks** (shadow models, distance-to-closest-record tests: are training records closer to synthetic records than held-out real records are?); **attribute-inference/reconstruction** tests (can an attacker with partial info recover income/defaults?); **memorization checks** (exact/near-duplicate search, rare-combination uniqueness); and consider training the generator with **differential privacy** and reporting the privacy budget. Remove or regenerate records too close to real customers.
:::
:::

:::question 6. Determine whether protected attributes should be included in the synthetic dataset, excluded from model training, or preserved under restricted access for fairness auditing.
:::solution Model answer
**Preserve them in the synthetic dataset under restricted access** so fairness can be audited (Example 60 logic); **exclude them from the credit model's inputs**, while checking proxies (region, occupation). Governance distinguishes prediction use from fairness evaluation; external developers get versions without protected attributes unless they are performing an approved audit.
:::
:::

:::question 7. Explain why evaluation only on synthetic test data cannot establish real-world utility. Propose a secure method for evaluating models on representative real data.
:::solution Model answer
A synthetic test set comes from the **same generator** — it shares its biases, gaps and simplifications, so high scores measure agreement with the generator, not real applicants (no utility evidence, no coverage of real tails). Propose: the company keeps a **real, representative held-out set** in a **secure enclave**; developers submit models that are evaluated there (**remote/"code-to-data" evaluation**), returning only aggregate metrics (performance, calibration, subgroup gaps), optionally with differential-privacy noise; or federated evaluation.
:::
:::

:::question 8. Develop a documentation package for the synthetic dataset, including motivation, source data, generation method, model version, privacy safeguards, known limitations, intended uses, discouraged uses, and maintenance procedures.
:::solution Model answer
**Motivation** (enable external development without sharing records); **source data** (period, population, known gaps — rural/informal/low-income, discriminatory approvals); **generation method** (model type, training data version, hyperparameters, **model version**, random seeds); **privacy safeguards** (DP budget, membership-inference results, record-distance threshold); **validation results** across all six dimensions; **known limitations** (rare defaults, under-represented groups); **intended uses** (prototyping, pipeline testing) and **discouraged uses** (operational credit decisions, fairness claims); licence and access terms; **maintenance** (owner, versioning, regeneration schedule, issue reporting).
:::
:::

:::question 9. Consider a case where the synthetic dataset improves privacy but reduces representation of already marginalized applicants. Explain how the organization should balance privacy, fairness, and utility.
:::solution Model answer
Stronger privacy (more DP noise, suppressing rare records) disproportionately **erases small groups** — marginalized applicants become even rarer. The organization should: set **minimum coverage targets** for those groups as a hard constraint; use privacy methods that preserve subgroup structure (stratified generation, targeted oversampling of under-represented cells with privacy accounting); accept slightly lower overall fidelity/utility to protect both privacy and representation; **document** the trade-off; and, where synthetic data can't serve those groups, evaluate on real data in a secure environment instead. Decisions should be approved by governance, not left to engineers.
:::
:::

:::question 10. Recommend whether the synthetic dataset should be approved for internal experimentation, external research, operational credit decisions, or none of these uses. Justify different approval levels.
:::solution Model answer
- **Internal experimentation / pipeline testing:** **approve**, with documentation and access control.
- **External research/development:** **conditional approval** — after privacy validation (no near-copies, attack ≈ chance), data-use agreement, no re-identification, limited access, and evaluation on real data via enclave.
- **Operational credit decisions:** **do not approve** a model validated only on synthetic data; requires real-data validation, fairness audit, regulatory compliance, monitoring.
- **None** if privacy tests fail — regenerate first.
:::
:::

## R5 — Commercial reuse of an international medical imaging repository

:::orig R5: Commercial Reuse of an International Medical Imaging Repository — Module 2 notes, PDF p.144
A consortium of universities creates a medical imaging repository using scans collected from several countries. The original consent forms vary considerably:

- some permit academic research only
- some permit commercial research
- some prohibit international transfer
- some permit future unspecified health research
- some allow withdrawal at any time
- some do not mention AI development

The dataset is released under a research-only license. Images are de-identified by removing names and identification numbers, but retain exact examination dates, rare diagnoses, age, sex, and hospital location.

A technology company proposes combining the repository with two open datasets and training a commercial diagnostic model. The company plans to distribute the model globally but not distribute the original images. It argues that model weights are not personal data and that open access to some of the source datasets makes the combined project permissible.

During development, the team discovers inconsistent diagnosis labels, undocumented exclusions, duplicated scans, incompatible licenses, and missing records of the preprocessing applied to earlier dataset versions.

**Questions**

1. Distinguish consent, privacy, licensing, copyright, institutional approval, and ethical acceptability. Explain why satisfying one of these does not automatically satisfy the others.
2. Develop a consent matrix that maps each data source to permitted purposes, commercial use, international transfer, withdrawal rights, redistribution, and AI model development.
3. Analyze whether transferring model weights rather than images resolves the ethical and legal concerns. Consider memorization, membership inference, model inversion, and restrictions on derived products.
4. Evaluate the re-identification risk created by exact dates, rare diagnoses, age, sex, and hospital location. Propose a risk-reduction strategy that preserves useful information where possible.
5. Design a license-compatibility review for combining the three datasets. Explain how the most restrictive terms may affect redistribution and commercial deployment.
6. Develop a plan for handling participant withdrawal after a model has already been trained. Consider deletion of source records, retraining, model updates, documentation, and communication with downstream users.
7. Propose a quality-control workflow addressing duplicate scans, inconsistent labels, undocumented exclusions, missing provenance, and historical preprocessing.
8. Prepare a minimum Datasheet for Datasets and data dictionary for the combined repository. Identify the information required before any external user could assess fitness for purpose.
9. Design an approval process involving data custodians, ethics committees, legal experts, privacy officers, clinical specialists, technical teams, participant representatives, and organizational leadership.
10. Make a final recommendation on whether the commercial project should proceed, proceed under restrictions, require renewed consent, use only selected data sources, or be rejected. State the assumptions, evidence, and unresolved uncertainties underlying your decision.
:::

:::question 1. Distinguish consent, privacy, licensing, copyright, institutional approval, and ethical acceptability. Explain why satisfying one of these does not automatically satisfy the others.
:::solution Model answer
**Consent** — what each participant agreed to (varies by source). **Privacy** — legal duty to protect personal data and prevent re-identification. **Licensing** — the repository's research-only terms and the open datasets' terms. **Copyright** — rights in images/compilations. **Institutional approval** — ethics/IRB and data-protection sign-off for the specific project. **Ethical acceptability** — whether the use respects participants and communities and balances benefit and harm. They are **independent**: open access (licence) doesn't give consent; de-identification (privacy) doesn't grant licence; IRB approval doesn't make an unfair use ethical.
:::
:::

:::question 2. Develop a consent matrix that maps each data source to permitted purposes, commercial use, international transfer, withdrawal rights, redistribution, and AI model development.
:::solution Model answer
| Source / consent type | Permitted purposes | Commercial | Intl transfer | Withdrawal | Redistribution | AI development |
|---|---|---|---|---|---|---|
| Academic-only | Academic research | ✗ | ? (per form) | per form | ✗ | Unclear → ✗ without renewal |
| Commercial research | Research incl. commercial | ✓ | per form | per form | ✗ (licence) | Likely ✓ if research-framed |
| No international transfer | Research | per form | **✗** | per form | ✗ | Only in-country |
| Future unspecified health research | Broad health research | Unclear | Unclear | per form | ✗ | Possibly ✓ (needs ethics review) |
| Withdrawal at any time | per form | per form | per form | **✓ — must honour** | ✗ | ✓ but with deletion/retraining duties |
| Silent on AI | per form | per form | per form | per form | ✗ | **Unclear → renewed consent or ethics waiver** |
Each record is tagged with its consent profile; the training set for a commercial global model is the **intersection** of permissions.
:::
:::

:::question 3. Analyze whether transferring model weights rather than images resolves the ethical and legal concerns. Consider memorization, membership inference, model inversion, and restrictions on derived products.
:::solution Model answer
**No.** Models can **memorize** training data (especially rare cases), enabling **membership inference** (was this patient in training?) and **model inversion** (reconstruct images/attributes). A model is a **derived product**: research-only licences and consent forbidding commercial use or international transfer restrict derived products too. Distributing weights globally is effectively **commercial use and international transfer** of what was learned from the data. Mitigations (DP training, memorization audits) reduce risk but don't override consent and licence terms.
:::
:::

:::question 4. Evaluate the re-identification risk created by exact dates, rare diagnoses, age, sex, and hospital location. Propose a risk-reduction strategy that preserves useful information where possible.
:::solution Model answer
**Exact exam dates + rare diagnosis + age + sex + hospital location** is a highly unique combination — linkable to hospital records, news or social media (**linkage attacks**). Reduce: shift dates by a random per-patient offset (preserving intervals); generalize age to bands (top-code 90+); coarsen location to region; suppress or group rare diagnoses where counts < k (k-anonymity); strip DICOM header metadata and burned-in text; restrict access for rare-disease subsets; assess residual risk with a formal re-identification test.
:::
:::

:::question 5. Design a license-compatibility review for combining the three datasets. Explain how the most restrictive terms may affect redistribution and commercial deployment.
:::solution Model answer
List each dataset's licence and version: research-only repository; open dataset A; open dataset B (check: commercial allowed? share-alike? attribution? no-derivatives?). Determine for the **combined** use: redistribution — blocked by research-only terms; **commercial deployment** — blocked by research-only terms unless a commercial licence is negotiated; share-alike terms may force release of derived works. **The most restrictive terms govern**: the commercial global model can be trained only on components whose licences allow commercial derivatives, or after obtaining new permissions. Record outcomes alongside the dataset artifact.
:::
:::

:::question 6. Develop a plan for handling participant withdrawal after a model has already been trained. Consider deletion of source records, retraining, model updates, documentation, and communication with downstream users.
:::solution Model answer
Delete the participant's **source records** and derived features from all dataset versions; mark them in the lineage register; determine whether the model must be **retrained** (or machine-unlearning applied) — set a policy (e.g. retrain at the next scheduled release, immediately for high-risk cases); update model version and documentation; **notify downstream users** to replace older versions; keep an auditable log of withdrawal handling. Consent forms should state this policy in advance.
:::
:::

:::question 7. Propose a quality-control workflow addressing duplicate scans, inconsistent labels, undocumented exclusions, missing provenance, and historical preprocessing.
:::solution Model answer
Inventory and profile all sources → **duplicate detection** (image hashing/near-duplicate search; patient-level linkage) and group-aware splits → **label harmonization** (common taxonomy, re-adjudication of inconsistent labels by experts, record uncertainty and acceptable alternatives) → document **exclusions** with reasons → reconstruct **historical preprocessing** where possible, otherwise flag versions as non-reproducible and regenerate from raw → validate → version ($D(1.0)$…) → approve. All changes in an immutable audit trail.
:::
:::

:::question 8. Prepare a minimum Datasheet for Datasets and data dictionary for the combined repository. Identify the information required before any external user could assess fitness for purpose.
:::solution Model answer
**Datasheet:** motivation; sources/countries/hospitals and periods; instances (scan, patient, study); counts by modality and diagnosis; **consent profiles and licence per source**; collection and de-identification methods with residual risk; preprocessing and exclusions; label process and inter-rater agreement; known biases (sites, devices, demographics); intended and prohibited uses (no commercial use for research-only subsets); access procedure; maintenance and withdrawal process; versions.
**Data dictionary (per field):** patient/study IDs (pseudonymous), exam date (shifted), age band, sex, site region, modality, device/vendor, diagnosis label (taxonomy, allowed values, uncertainty), consent profile code, licence code, missing-value codes, time semantics, transformations, sensitivity, quality notes.
:::
:::

:::question 9. Design an approval process involving data custodians, ethics committees, legal experts, privacy officers, clinical specialists, technical teams, participant representatives, and organizational leadership.
:::solution Model answer
1. **Data custodians** of each source confirm licence and consent constraints. 2. **Privacy officers** assess re-identification and cross-border transfer (DPIA). 3. **Legal experts** review licences, copyright, contracts, applicable laws per country. 4. **Ethics committees** (each consortium institution) review purpose, consent scope, need for renewed consent. 5. **Clinical specialists** validate labels and clinical safety. 6. **Technical team** presents lineage, QC, memorization/privacy tests. 7. **Participant representatives** review acceptability. 8. **Organizational leadership** makes the final decision with conditions, monitoring and sunset/renewal dates. Each step documented; any veto stops the project.
:::
:::

:::question 10. Make a final recommendation on whether the commercial project should proceed, proceed under restrictions, require renewed consent, use only selected data sources, or be rejected. State the assumptions, evidence, and unresolved uncertainties underlying your decision.
:::solution Model answer
**Do not proceed as proposed.** The whole repository is released under a **research-only licence**, so no part of it can be used commercially until the consortium agrees a **commercial licence**. Only then could the project **proceed under restrictions**, using **only records whose consent permits commercial research and international transfer**, combined only with open datasets whose licences allow commercial derivatives, after QC fixes and privacy-preserving training, with formal approval from all bodies. For academic-only, no-transfer or AI-silent sources: **seek renewed consent** (or exclude). **Assumptions:** consent forms can be mapped to records; licences can be renegotiated. **Evidence needed:** consent matrix, licence review, re-identification and memorization tests, external validation. **Unresolved uncertainties:** legal status of model weights across jurisdictions; whether enough permitted data remain for a clinically valid model — if not, the commercial project should be **rejected**.
:::
:::
