# M1 · Scenario, reflection & application answers

Module 1's scenario questions **S1–S5**, reflection questions **R1–R5** and application problems **A1–A7**, each with the original case (tap to show) and a full answer from your Quiz 1 preparation guide. Real Quiz 1's 21-mark water-pipe scenario followed the S-question pattern; the A-problems mirror Assignment 1 (problem-framing worksheet, model card, datasheet, failure analysis).

<div class="pdf-links">
<a href="m1-answers.html">Answers Q1–100</a>
<a href="m1b-notes.html">Part B notes</a>
<a href="quiz1-solved.html">Real Quiz 1 (solved)</a>
<a href="pdfs/notes/Module-1-Notes.pdf#page=151">Questions in the PDF</a>
</div>


## Scenarios S1–S5


These are the most "quiz-like" questions: a short case, then diagnosis questions. Practise answering each bullet in 3 to 6 lines using the named concept.


### S1: University Student Support System

:::origc S1 (Module 1 notes)
S1: University Student Support System A university plans to build an AI system to identify students who may fail a course. The initial proposal states: Build a machine learning model that predicts student failure. The available data include attendance, assignment grades, learning-platform activity, prior academic performance, financial-aid status, and final examination results. The university intends to use the predictions to allocate a limited number of tutoring appointments. However, the proposal does not specify when the prediction will be made, which students will be included, how failure will be defined, or how many tutoring appointments are available. Questions
- Why is the original problem statement inadequately formulated?
- Rewrite the problem statement by specifying the target population, index time, prediction horizon, outcome, decision-maker, and intended action.
- Which variables may create temporal leakage if the prediction is required during the first four weeks of the semester?
- What are the likely consequences of false-positive and false-negative predictions?
- Should the university evaluate only predictive accuracy, or should it also measure calibration, subgroup performance, and decision utility? Explain briefly.
:::

:::question S1(a). Why is the original problem statement ("Build a machine learning model that predicts student failure") inadequately formulated?
:::solution Answer


It is the "poor framing" pattern from the notes. It starts from an algorithm instead of a decision and leaves every key element undefined:

- No index time: we do not know when the prediction is made, so we cannot tell which features are legitimate (leakage risk).
- No target population: which course, which students (all enrolled, first-years, repeaters)? Who is excluded (students who withdrew before the census date)?
- No outcome definition: does "failure" mean a final grade below the pass mark, withdrawal, or both? Over what period?
- No link to the action or capacity: the purpose is to allocate a limited number of tutoring appointments, but the number is not stated, so we cannot design a ranking or threshold.
- No decision-maker, baseline, metrics, error costs or subgroup analysis. This risks "Failure 1: predicting student failure without an effective support intervention."
:::
:::

:::question S1(b). Rewrite the problem statement by specifying the target population, index time, prediction horizon, outcome, decision-maker, and intended action.
:::solution Answer


"At the end of week 4 of the semester, for every student enrolled in [Course X] on the census date (one student-course enrolment is the unit of analysis), using only information recorded by the end of week 4 (prior academic performance, attendance and assignment grades from weeks 1 to 4, learning-platform activity in weeks 1 to 4, and financial-aid status as recorded at enrolment), produce a calibrated probability that the student will fail the course (final grade below the pass mark, or withdraw after the census date) by the end of the semester, together with a ranked list, so that the course coordinator and academic-support office can offer the N available tutoring appointments to the highest-ranked students after human review. The system will be compared with the current process (self-referral and instructor referral) and evaluated using recall@N, precision@N, calibration and subgroup performance, accounting for the cost of missed struggling students, stigma from being flagged, and fairness across financial-aid and demographic groups."

:::
:::

:::question S1(c). Which variables may create temporal leakage if the prediction is required during the first four weeks of the semester?
:::solution Answer

- Final examination results: these happen at the end of the semester and are part of the outcome itself (target leakage).
- Assignment grades after week 4 and cumulative course grades that include later work.
- Attendance and learning-platform activity after week 4 (future behaviour; declining activity late in the term reflects the outcome developing).
- Midterm results if the midterm occurs after week 4.
- Financial-aid status if it was updated later (for example aid suspended because of poor grades); only the value recorded at the index time can be used. Also any withdrawal records or academic-probation flags.

Rule: every feature must be recorded and available by the end of week 4 (t_feature availability ≤ t).

:::
:::

:::question S1(d). What are the likely consequences of false-positive and false-negative predictions?
:::solution Answer

- False positive (flagged but would have passed): a scarce tutoring slot is spent on a student who did not need it, displacing someone who did; possible stigma, anxiety or feeling labelled; wasted tutor time.
- False negative (not flagged but fails): the student misses support when it could have helped, fails or withdraws, loses time, money, scholarship eligibility, and may drop out. This is usually the more costly and less reversible error, so recall on at-risk students is important, bounded by the appointment capacity.
:::
:::

:::question S1(e). Should the university evaluate only predictive accuracy, or also calibration, subgroup performance, and decision utility?
:::solution Answer


It should evaluate all of them. Accuracy is misleading when most students pass (class imbalance) and treats all errors equally. Calibration matters because probabilities are used to rank students and decide who gets scarce appointments. Subgroup performance matters because financial-aid status and platform activity may act as proxies for socioeconomic status, and errors may concentrate in some groups. Decision utility matters because the real goal is fewer failures: the system must be compared with the current referral process and ideally tested (for example a pilot) to see whether tutoring the flagged students actually improves outcomes.

:::
:::


### S2: Hospital Sepsis Prediction

:::origc S2 (Module 1 notes)
S2: Hospital Sepsis Prediction A hospital develops a model to predict sepsis within the next six hours. During training, missing blood-pressure values are replaced with the median value for the relevant hospital ward. In production, the software team replaces missing values with zero. The training data also include the number of broad-spectrum antibiotic doses administered. In many records, this value is updated after a physician has already suspected or diagnosed sepsis. The model achieves 98 percent accuracy during development but produces a large number of false alerts after deployment. Questions
- Identify the train-serving mismatch in this case.
- Explain why the antibiotic-dose feature may introduce temporal leakage.
- Why can high offline accuracy coexist with poor real-world performance?
- Which data validation checks should be placed between data ingestion and model inference?
- What fallback action should occur when critical clinical inputs are missing or invalid?
:::

:::question S2(a). Identify the train-serving mismatch in this case.
:::solution Answer


In training, missing blood-pressure values were imputed with the median for the relevant ward. In production, the software team imputes missing values with zero. A blood pressure of 0 is physiologically impossible and looks like extreme shock to the model, so it produces floods of high-priority false alarms. This is exactly the notes' train-serving mismatch: different preprocessing pipelines in training and live inference, causing "silent and often catastrophic performance degradation" and alert fatigue.

:::
:::

:::question S2(b). Explain why the antibiotic-dose feature may introduce temporal leakage.
:::solution Answer


The number of broad-spectrum antibiotic doses is often updated after a physician has already suspected or diagnosed sepsis. So in historical records the feature carries information about the diagnosis itself. The model learns to "wait for the doctor's order": it detects sepsis by detecting the treatment. At the real index time (six hours before sepsis), those doses have not yet been given, so the feature is unavailable or systematically different. It is future information leaking into the past (and a form of target leakage because the feature is a consequence of the outcome).

:::
:::

:::question S2(c). Why can high offline accuracy coexist with poor real-world performance?
:::solution Answer

- The leaked antibiotic feature inflates offline accuracy but is absent at prediction time.
- The imputation mismatch changes inputs in production.
- Accuracy is dominated by the many non-sepsis patients (low prevalence), so 98% accuracy can hide poor detection of actual sepsis and a low positive predictive value.
- Offline evaluation may have used random splits and not tested temporal, external or workflow claims. The Epic Sepsis Model shows the same pattern: AUROC 0.63 externally, alerts on 18% of hospitalizations, 67% of cases missed.
:::
:::

:::question S2(d). Which data validation checks should be placed between data ingestion and model inference?
:::solution Answer

- Schema checks: required fields present, correct data types and units (mmHg).
- Range checks: physiologically plausible values (reject BP = 0, heart rate > 300).
- Missingness checks: rate of missing values per feature compared with the reference; flag spikes.
- Imputation consistency test: the same versioned transformation code used in training and serving (feature store); automated test comparing training and serving outputs for the same record.
- Timestamp checks: event time, recording time, availability time; reject features whose availability time is after the index time.
- Distribution/drift checks: compare incoming distributions with training statistics (TFX-style statistics + schema + validation).
- Identity checks: patient and encounter IDs resolve correctly (no split identities after transfers).
:::
:::

:::question S2(e). What fallback action should occur when critical clinical inputs are missing or invalid?
:::solution Answer


The model should abstain rather than impute a misleading value: no risk score is produced (or it is clearly marked "insufficient data"), and the case is routed to the standard clinical process, such as the existing early-warning score or nurse assessment, with a prompt to re-measure the vital sign. Missing-input events should be logged and monitored; if the rate spikes, a circuit breaker should suspend alerts and fall back to the legacy protocol while the pipeline is fixed.

:::
:::


### S3: Automated Loan Underwriting

:::origc S3 (Module 1 notes)
S3: Automated Loan Underwriting
A bank compares two models for predicting loan default: (a) A deep neural network with 94% accuracy (b) A logistic regression model with 91% accuracy. The deep neural network uses thousands of behavioral features and requires substantial computing resources. Its explanations vary when different post-hoc methods are applied. The logistic regression model uses 15 established financial variables, runs on standard hardware, and provides directly interpretable coefficients. The bank must provide applicants with clear reasons for rejected applications and has limited machine-learning engineering capacity. Questions
- Which model should the bank consider for deployment, and why?
- Why is the model with the highest predictive accuracy not automatically the best operational choice?
- Which criteria beyond accuracy should guide model selection?
- How do interpretability, latency, maintenance cost, and governance requirements affect the decision?
- What information should be documented in a Model Card before deployment?
:::

:::question S3(a). Which model should the bank consider for deployment, and why?
:::solution Answer


The logistic regression model (91%). This is the notes' Example 25. The bank must give applicants clear reasons for rejection (adverse-action reasons, as under the Equal Credit Opportunity Act); logistic regression gives directly interpretable coefficients, while the DNN's explanations vary across post-hoc methods (unstable SHAP-type explanations). The bank also has limited ML engineering capacity, and logistic regression uses 15 established financial variables on standard hardware, making it easier to maintain, audit, recalibrate and monitor. The 3-point accuracy gain does not outweigh legal, governance and lifecycle costs.

:::
:::

:::question S3(b). Why is the model with the highest predictive accuracy not automatically the best operational choice?
:::solution Answer


Because accuracy is only one criterion. "The most complex model is not automatically the best model." A model must also meet legal explainability requirements, run within compute and latency budgets, be maintainable by the available team, be robust to drift (thousands of behavioural features may shift or act as proxies), and be auditable. A model that cannot be explained or maintained will be unusable or risky, however accurate offline.

:::
:::

:::question S3(c). Which criteria beyond accuracy should guide model selection?
:::solution Answer


Data characteristics (size relative to model complexity; about 50,000 applications a year is small for a large DNN); task requirements (calibrated default probabilities); operational constraints (latency, memory, compute); governance and trust (interpretability, explainability, robustness, fairness across groups, proxy risk in behavioural features); lifecycle costs (maintenance burden, team expertise, retraining frequency); plus calibration, subgroup performance and external/temporal validation.

:::
:::

:::question S3(d). How do interpretability, latency, maintenance cost, and governance requirements affect the decision?
:::solution Answer

- Interpretability: decisive. Regulations require specific reasons; coefficients provide stable, auditable reasons, while variable post-hoc explanations do not.
- Latency: both may respond in milliseconds, but the DNN needs much more computing resources (CPUs/GPUs) to keep that speed at scale; logistic regression runs cheaply on standard CPUs.
- Maintenance cost: when macroeconomic conditions shift (inflation spike), relationships change; a DNN needs specialized ML engineers to monitor, recalibrate and retrain, whereas standard risk analysts can maintain logistic regression.
- Governance: auditors and regulators need to understand and challenge decisions; thousands of behavioural features raise proxy-discrimination and privacy risks that are hard to audit.
:::
:::

:::question S3(e). What information should be documented in a Model Card before deployment?
:::solution Answer


Model overview (name, version, type: logistic regression binary classifier of default within a defined horizon; purpose; intended use as decision support for underwriters); data description (source and period of loan records, the 15 features and definitions, preprocessing and missing-value handling, exclusions); performance (accuracy, precision, recall, AUROC, calibration curve, confidence intervals, temporal validation results); subgroup performance by protected and proxy-sensitive groups (age, sex, region, thin-credit-file applicants); fairness observations; known limitations (limited credit history, economic regime changes); intended and inappropriate uses (not for automated rejection without review, not for other products or countries without validation); the decision threshold and its justification; adverse-action reason generation; monitoring plan and triggers for recalibration or rollback; and the accountable owner.

:::
:::


### S4: AI-Based Recruitment Ranking

:::origc S4 (Module 1 notes)
S4: AI Based Recruitment Ranking A company trains a ranking model using ten years of historical recruitment data. The model gives higher scores to applicants from a small group of universities because candidates from these institutions were hired more frequently in the past. Recruiters receive a dashboard containing a ranked list of applicants. The interface highlights the top ten candidates in green, while all remaining candidates appear in grey. Recruiters are instructed to review all applications, but most interview invitations are sent only to the highlighted candidates. After one year, the company retrains the model using the new hiring data generated under this process. Questions
- Why should this system be understood as a socio-technical system rather than only as a ranking algorithm?
- How may historical hiring data encode institutional bias?
- How can the dashboard design influence human decisions and create automation bias?
- Explain how retraining on the new hiring data may create a self-reinforcing feedback loop.
- Which stakeholders should be responsible for governing, measuring, and managing the risks of this system?
:::

:::question S4(a). Why should this system be understood as a socio-technical system rather than only as a ranking algorithm?
:::solution Answer


Its impact depends on all five layers: the model (ranks applicants), the data infrastructure (ten years of past hiring decisions), the interface (top ten in green, the rest grey), the human workflow (recruiters told to review all, but invitations go mostly to the highlighted ten), and the institutional rules (retraining on new hires, employment law, fairness policy). The outcome, who gets interviewed, is produced by this whole composite, not by the ranking function alone. This is the notes' Example 12.

:::
:::

:::question S4(b). How may historical hiring data encode institutional bias?
:::solution Answer


The label is "who was hired in the past", which records past recruiter decisions, not true candidate quality (status quo bias). If recruiters favoured a small group of universities (because of networks, prestige or familiarity), the model learns university as a strong signal. University then acts as a proxy for socioeconomic status, geography and other protected attributes (proxy encoding). The model reproduces the old preference "faster and at a much larger scale".

:::
:::

:::question S4(c). How can the dashboard design influence human decisions and create automation bias?
:::solution Answer


Colour-highlighting the top ten signals "these are the right ones" and makes accepting the ranking the easiest option; the grey candidates look pre-rejected. Automation bias is "the tendency of humans to place excessive trust in automated systems and accept their outputs without sufficient independent evaluation". Although recruiters are instructed to review everyone, most invitations go to the green candidates, so the formal instruction is overridden by the interface. There is no uncertainty information, so small score differences look meaningful.

:::
:::

:::question S4(d). Explain how retraining on the new hiring data may create a self-reinforcing feedback loop.
:::solution Answer


Candidates from the favoured universities are ranked high → highlighted → interviewed and hired → recorded as successful. Candidates from other universities are rarely interviewed, so their potential success is never observed (selective labels). Retraining on these new hires therefore shows an even stronger link between the favoured universities and hiring. The model's output has become its input: past exposure → observed interaction → training data → future exposure. The bias grows and the model looks increasingly "accurate" because it is judged on people it selected.

:::
:::

:::question S4(e). Which stakeholders should be responsible for governing, measuring, and managing the risks of this system?
:::solution Answer


Apply NIST: Govern: senior HR leadership and the organization's AI governance/ethics committee, with legal/compliance, set policy and name an accountable owner who can suspend the system. Map: HR, legal, diversity and inclusion teams and data scientists identify risks (proxy discrimination, automation bias, feedback loops) and affected groups (applicants from non-favoured universities). Measure: data scientists and independent auditors track selection rates and error rates by subgroup, override rates, drift and feedback effects. Manage: product/interface designers remove the green/grey framing and add uncertainty; recruiters and hiring managers keep decision authority and log overrides; ML engineers use counterfactual logging and stop naive retraining; an appeal channel for applicants. Applicants and regulators are stakeholders who must be informed and consulted.

:::
:::


### S5: Smart Warehouse Robot

:::origc S5 (Module 1 notes)
S5: Smart Warehouse Robot A warehouse deploys a robot that identifies packages using cameras, calculates routes through the facility, and transports items to shipping stations. The robot uses:
- A deep learning model for package and obstacle recognition
- A search algorithm for route selection
- An optimization procedure for reducing travel time
- Explicit rules that prohibit entry into restricted areas
- A safety controller that stops the robot when collision risk becomes high
- Human review when damaged packages are detected During peak season, the layout of the warehouse changes, new packaging materials are introduced, and the number of workers in the facility increases. The robot begins taking longer routes and occasionally fails to recognize reflective packages. Questions
- Why is this system an example of hybrid AI?
- Which components are statistical, symbolic, search-based, optimization-based, and human-controlled?
- What types of data drift or environmental change are present?
- Which operational indicators should be monitored after deployment?
- Under what conditions should the robot abstain, stop, use a fallback procedure, or request human review? These are take-home reflection questions intended to encourage deep thinking and planning. There are no single correct answers. Each question can’t be answered in a couple sentences. It will push you to think deeply about the concepts, principles, and practices in this module.
:::

:::question S5(a). Why is this system an example of hybrid AI?
:::solution Answer


It combines several computational approaches, each used where it fits: deep learning for noisy visual perception, search for routing, optimization for travel time, explicit rules for restricted areas, a safety controller for collisions, and human review for damaged packages. Neither a purely symbolic system (cannot interpret noisy camera images) nor a purely statistical system (might violate safety rules in unfamiliar situations) would be sufficient. This is the notes' Example 9.

:::
:::

:::question S5(b). Which components are statistical, symbolic, search-based, optimization-based, and human-controlled?
:::solution Answer


| Category | Component |
|---|---|
| Statistical (learned) | Deep learning model for package and obstacle recognition |
| Symbolic (rule-based) | Explicit rules prohibiting entry into restricted areas; the safety controller's stop rule (collision-risk threshold) |
| Search-based | Search algorithm for route selection |
| Optimization-based | Procedure that minimizes travel time |
| Human-controlled | Review and final decision on damaged packages |

:::
:::

:::question S5(c). What types of data drift or environmental change are present?
:::solution Answer

- Environment/layout change: the warehouse layout changes, so the map and learned traversable paths are outdated (the search space and costs changed); routes get longer.
- Input distribution drift (new device/appearance): new reflective packaging materials look different from training images, so the perception model fails to recognize them (covariate shift and possibly a new unseen class).
- Population/context change: more workers in the facility (more people and obstacles, more congestion), which changes traffic patterns and the frequency of safety stops.
- Seasonal effect: peak season raises volume and changes the operating regime.
:::
:::

:::question S5(d). Which operational indicators should be monitored after deployment?
:::solution Answer


Recognition confidence and failure rate by package type (especially reflective); abstention/unknown-object rate; route length, travel time and delivery time vs planned; frequency of re-planning and blocked paths; safety-stop and near-miss counts; congestion and throughput (packages per hour); collision-risk events near workers; human-review volume for damaged packages and override rates; map-version/layout-change logs; operational health (latency, battery, uptime); and input drift statistics of camera images (lighting, reflectance).

:::
:::

:::question S5(e). Under what conditions should the robot abstain, stop, use a fallback procedure, or request human review?
:::solution Answer

- Abstain: when recognition confidence for a package is below a threshold (for example a reflective package it cannot classify), do not pick or sort it; flag it.
- Stop: when the safety controller detects high collision risk or a person in its path, or when entering a restricted area is possible; safety rules always override the learned policy.
- Fallback: when the map does not match observed layout (repeated failed routes, blocked paths), switch to a conservative mode (lower speed, pre-approved safe routes, re-mapping) or a manual dispatch procedure; roll back to a previous model if a new version increases failures.
- Request human review: damaged packages, unrecognized or unusual objects, repeated recognition failures, and ambiguous situations near workers.
:::
:::


## Reflections R1–R5


The notes say these have "no single correct answers" and cannot be answered in a couple of sentences. The answers below give a complete, defensible structure. In a quiz, use the headings as your skeleton and add two or three points under each.


### R1: National Early Warning System for Disease Outbreaks

:::origc R1 (Module 1 notes)
R1: National Early Warning System for Disease Outbreaks A national public health agency proposes an AI system to identify emerging infectious disease outbreaks before hospitals become overwhelmed. The proposed system will combine hospital admission records, pharmacy sales, laboratory test orders, school absenteeism, internet search activity, weather conditions, and social media posts. The project team initially defines the objective as follows: Use AI to detect disease outbreaks as early as possible. A machine learning model performs well when tested retrospectively. However, several concerns emerge. Internet search activity changes after media reports about a disease. Laboratory testing is more frequent in wealthy urban areas than in rural regions. Pharmacy sales include purchases made for prevention rather than illness. Social media activity is
concentrated among younger populations. The system may also influence future data because issuing an outbreak warning can increase testing, hospital visits, online searches, and public concern. Questions
- Reformulate the problem comprehensively. Define the target population, unit of analysis, index time, prediction horizon, output, decision-maker, intended intervention, resource constraints, and acceptable delay. Explain whether the primary task should be classification, anomaly detection, forecasting, causal estimation, or a hybrid of several problem types.
- Examine the meaning of the available data. For every major source, discuss what phenomenon it directly measures, what it only approximates, and how the data- generation process may differ across regions and populations. Identify the proxies, missing populations, selective labels, and possible measurement biases.
- Design an evaluation strategy that matches the deployment claims. Explain how temporal validation, geographic validation, calibration assessment, subgroup analysis, detection delay, false-alarm rate, and comparison with existing epidemiological surveillance should be incorporated. Discuss why a random train- test split would be inadequate.
- Analyze the feedback loop created by deployment. Explain how an alert could change testing, reporting, public behavior, and future training data. Propose a logging, monitoring, and retraining strategy that distinguishes changes in actual disease prevalence from changes caused by the warning system itself.
- Develop a governance plan. Allocate responsibility across public health officials, data engineers, epidemiologists, model developers, hospitals, communication teams, and government leaders. Apply the Govern, Map, Measure, and Manage functions to determine when the system should issue a warning, abstain, request expert review, or be suspended.
:::

:::question R1(a). Reformulate the problem comprehensively and choose the problem type.
:::solution Answer


Worksheet statement: "Every Monday (index time), for each district in the country (unit of analysis: district-week), using only data received and validated by Sunday midnight (hospital admissions for respiratory and gastrointestinal syndromes, laboratory test orders and positivity, pharmacy sales, school absenteeism, weather, search and social-media signals, each with its reporting lag), produce (i) a calibrated probability that confirmed cases of a target disease will exceed the district's seasonal epidemic threshold within the next 2 to 4 weeks, (ii) a forecast with prediction intervals of cases and hospital admissions, and (iii) an anomaly flag for unusual syndromic patterns, so that the national public-health agency's epidemiology team can decide whether to issue an alert, dispatch investigation teams, pre-position test kits, or notify hospitals to prepare surge capacity. The system will be compared with the existing surveillance system and seasonal baselines and evaluated with detection delay, false-alarm rate, sensitivity, calibration, and regional and subgroup performance, while accounting for the cost of missed and late outbreaks, alert fatigue and public panic, data inequality between urban and rural areas, investigation-team capacity, and privacy governance."

- Target population: the national population, represented by districts; include rural and urban districts; separate pathogens (for example influenza-like illness, cholera, dengue) because signals differ.
- Unit of analysis: district-week (not individuals), which keeps privacy and matches the response unit.
- Index time: weekly (daily during active alerts), after data arrive and pass validation.
- Prediction horizon: 2 to 4 weeks ahead, the lead time needed to mobilize staff, supplies and hospital beds (a horizon too short is useless, like the six-minute flood warning).
- Output: probabilities, forecast intervals and anomaly flags with uncertainty, plus abstention when data are too incomplete.
- Decision-maker: the national epidemiology/surveillance unit, with regional health officers; not an automatic public announcement.
- Intended intervention: field investigation, confirmatory testing, hospital preparedness, targeted communication, vaccination or supplies.
- Resource constraints: limited investigation teams and test kits; limited ability to respond to many alerts at once.
- Acceptable delay: alerts must arrive before hospitals are overwhelmed (for example at least two weeks earlier than the current surveillance signal).

Problem type: hybrid. Forecasting (future admissions with intervals, temporal ordering), anomaly detection (new or unexpected patterns, where "unusual is not the same as undesirable" and an investigation policy is required), classification (probability of exceeding a threshold), and decision optimization (allocating limited teams). Causal estimation is needed later to judge whether interventions worked. A single classifier would ignore time, uncertainty and capacity.

:::
:::

:::question R1(b). Examine the meaning of the available data (proxies, missing populations, selective labels, measurement bias).
:::solution Answer


| Source | Directly measures | Only approximates | Bias and variation |
|---|---|---|---|
| Hospital admissions | People admitted with certain diagnoses | Community disease activity (severe cases only) | Access to hospitals differs; coding practices vary; lag; late-stage signal |
| Laboratory test orders/results | Tests ordered and positives | Infection prevalence | Testing much more frequent in wealthy urban areas; rural areas look "healthy" because unobserved (selective labels, access bias) |
| Pharmacy sales | Purchases of medicines | Illness in the community | Includes preventive purchases, stockpiling after news, promotions; pharmacy coverage uneven |
| School absenteeism | Children absent from school | Illness among children | Holidays, weather, strikes; covers only school-age children |
| Internet search | Search queries | Symptoms and concern | Changes after media reports; platform changes (Google Flu Trends); requires internet access |
| Social media | Posts by users | Public concern and symptoms | Concentrated among younger, urban users; bots; rumours |
| Weather | Temperature, rainfall, humidity | Conditions favouring transmission | Station coverage; a driver, not a measure of disease |

- Proxies: almost every source is a proxy for disease; their relationship to true prevalence can change (proxy instability).
- Missing populations: rural, poor, elderly, offline populations and people who do not seek care.
- Selective labels: confirmed cases exist only where tests were done; negatives in low-testing areas mean "not observed", not "no disease" (the meaning of "negative").
- Measurement bias: case definitions, lab capacity and reporting lags differ by region and change over time.
:::
:::

:::question R1(c). Design an evaluation strategy that matches the deployment claims.
:::solution Answer

- Temporal validation: train on earlier seasons and test on later ones (rolling-origin validation), because the claim is about predicting future outbreaks. A random train-test split would leak future information (weeks from the same outbreak on both sides, autocorrelated data) and make performance look better than reality.
- Geographic validation: hold out entire regions (especially rural, low-testing regions) to test transportability.
- Calibration: check that a predicted 30% chance of exceeding the threshold matches the observed frequency; check interval coverage for forecasts.
- Subgroup/regional analysis: sensitivity, false-alarm rate and delay by region, urban vs rural, income level and age group.
- Detection delay: how many weeks earlier than the current surveillance system the alert fires (the key utility metric).
- False-alarm rate: alerts per region per season, because false alarms cause alert fatigue, wasted teams and public panic.
- Baseline comparison: compare with existing epidemiological surveillance and seasonal/naive baselines; Google Flu Trends showed that combining new signals with lagged official data beat either alone.
- Stress tests: high-media periods, new pathogens, data outages.
- Prospective silent evaluation before any public use.
:::
:::

:::question R1(d). Analyze the feedback loop created by deployment and propose a logging, monitoring and retraining strategy.
:::solution Answer


An alert changes the data-generating process: more testing is ordered (more positives found), more people go to hospital, searches and social-media posts increase, pharmacies sell more. The next week's data therefore look worse partly because of the alert (a performative effect), and retraining on these data would teach the model that its alert was correct (self-reinforcing bias). Conversely, a successful intervention reduces cases and may make the alert look like a false alarm.


Strategy:

- Log every alert and response (counterfactual logging): which districts were alerted, when, what actions were taken, testing volumes before and after.
- Adjust for testing effort: track test positivity rate and tests per capita, not just case counts; use lab-confirmed cases and hospital admissions as more stable anchors.
- Mark post-alert periods in training data, or model them explicitly, so the model does not learn from its own influence.
- Keep held-out comparison areas or use staggered rollout where ethically acceptable to estimate the alert's effect.
- Monitor input drift, residual error, calibration, alert volume, media events and platform changes; persistent residual growth should trigger recalibration or suspension (Google Flu Trends lesson).
- Retrain on a schedule with human epidemiologist review, not automatically after each alert.
:::
:::

:::question R1(e). Develop a governance plan using Govern, Map, Measure and Manage.
:::solution Answer


Responsibilities: public-health officials (own the decision to warn and the response); epidemiologists (define case definitions and thresholds, review every alert); data engineers (pipelines, validation, lineage, privacy); model developers (models, calibration, documentation, model card); hospitals (timely, consistent reporting, surge planning); communication teams (clear public messages that avoid panic); government leaders (mandate, resources, legal basis, accountability).

- Govern: a surveillance governance board chaired by the national public-health authority; a named accountable owner; privacy rules (aggregate district data, no individual social-media tracking), data-sharing agreements, documentation (datasheets, model card), and escalation rules.
- Map: identify risks: under-detection in rural/low-testing areas, false alarms and panic, stigma of alerted districts, privacy harms, proxy instability, feedback loops.
- Measure: detection delay, false-alarm rate, calibration, regional and subgroup performance, data completeness, feedback indicators.
- Manage: decision rules for action:
- Issue a warning when the calibrated probability exceeds the agreed threshold and an epidemiologist confirms with at least one anchored source (lab or hospital data).
- Abstain when key sources are missing or delayed (for example a district's lab reports absent), and show "insufficient data".
- Request expert review for anomalies driven mainly by search or social-media signals, or for new patterns.
- Suspend the model if residual error or false alarms exceed limits, if a data-source definition changes, or if the system is shown to systematically miss certain regions; fall back to traditional surveillance.
:::
:::


### R2: Adaptive Traffic Management for a Large City

:::origc R2 (Module 1 notes)
R2: Adaptive Traffic Management for a Large City A city plans to replace fixed traffic-light schedules with an AI-based traffic-management system. The system will use road cameras, vehicle sensors, mobile-phone location data, public-transport schedules, emergency-service requests, weather information, and historical traffic records. The stated goal is to minimize average travel time. The optimization system learns to give longer green signals to roads with the largest traffic volumes. After deployment, average travel time decreases by 12 percent, but buses become less reliable, pedestrian waiting times increase, cyclists report more dangerous crossings, and traffic is redirected through low-income residential areas.
The city argues that the system is successful because it achieved the objective that engineers specified. Questions
- Critique the objective function. Explain why minimizing average vehicle travel time may be mathematically clear but socially incomplete. Propose a multi-objective formulation that accounts for public transport, pedestrians, cyclists, emergency vehicles, air pollution, neighborhood disruption, safety, and equity.
- Distinguish prediction, planning, optimization, and control within this system. Identify the role played by each component and explain why the complete system cannot be described merely as a traffic-prediction model.
- Analyze the representation of the city. Discuss which road users are visible to the data infrastructure and which may be poorly represented. Explain how mobile-phone ownership, camera placement, sensor coverage, and historical planning decisions could produce aggregation bias or proxy encoding.
- Propose a decision-cost framework. Identify the costs of false congestion alarms, missed congestion, delayed emergency vehicles, pedestrian risk, pollution, and workflow failure. Explain how these costs should influence real-time control decisions rather than relying only on average accuracy or travel time.
- Treat the system as a socio-technical composite. Analyze how the model, data infrastructure, public interface, traffic-control workflow, transport policy, legal rules, and public accountability mechanisms jointly determine outcomes. Explain who should have authority to modify objectives, thresholds, and safety constraints.
:::

:::question R2(a). Critique the objective function and propose a multi-objective formulation.
:::solution Answer


Minimizing average vehicle travel time is mathematically clear but socially incomplete: it counts only vehicles (not people), weights every vehicle equally (a bus with 60 passengers counts like a car with one), ignores pedestrians and cyclists, ignores safety, pollution and where traffic goes, and ignores the distribution of costs. Optimization is "ethically blind"; it found the most efficient path to the specified objective by pushing costs onto buses, pedestrians, cyclists and low-income neighbourhoods. The 12% improvement is a success on a proxy objective.


Multi-objective formulation (minimize over signal plans):


J = w1·(person-weighted travel time) + w2·(bus delay and schedule deviation) + w3·(pedestrian waiting time) + w4·(cyclist risk) + w5·(emergency response delay) + w6·(emissions) + w7·(neighbourhood through-traffic)


Subject to hard constraints: maximum pedestrian wait (for example ≤ 60 s), minimum safe crossing times, emergency-vehicle priority, speed and safety rules, and equity constraints (no neighbourhood's through-traffic or pollution may increase by more than an agreed limit). Weights should be set by the city through public consultation, not by engineers alone, and results reported by group and area.

:::
:::

:::question R2(b). Distinguish prediction, planning, optimization and control within this system.
:::solution Answer

- Prediction/forecasting: forecasting traffic volumes, congestion and bus arrivals over the next minutes to hours from cameras, sensors, phone data and history.
- Planning: choosing sequences of signal plans and coordination across corridors (green waves), and planning routes for emergency vehicles.
- Optimization: selecting signal timings that minimize the chosen objective under constraints.
- Control: continuously observing the network and adjusting signals in real time: x_{t+1} = F(x_t, u_t, w_t); the actions change the traffic being predicted.

It cannot be described as a traffic-prediction model because its signals act on the city: it changes routes, travel behaviour and neighbourhood traffic, creating feedback loops. Harm came from the optimization objective and control actions, not from prediction error.

:::
:::

:::question R2(c). Analyze the representation of the city: who is visible and who is poorly represented?
:::solution Answer

- Vehicles are highly visible (cameras and sensors at intersections); pedestrians and cyclists are poorly represented (sensors often detect only vehicles; camera placement on major roads).
- Mobile-phone location data over-represent people who own smartphones and share location (younger, wealthier); under-represent elderly and poor residents; phone density can be mistaken for demand (proxy encoding).
- Camera and sensor coverage is uneven, often concentrated on arterial roads and wealthy districts; low-income areas may have fewer sensors, so extra traffic there is not seen.
- Historical planning decisions (which roads were built wide, where sensors were installed) are embedded in the data; optimizing on them reproduces past priorities.
- Aggregation bias: citywide average travel time hides that some groups (bus riders, pedestrians, residents of certain neighbourhoods) are worse off.
:::
:::

:::question R2(d). Propose a decision-cost framework.
:::solution Answer


C(t) = c_FP·P(false congestion alarm) + c_FN·P(missed congestion) + c_emerg·E[emergency delay] + c_ped·(pedestrian risk) + c_poll·(pollution) + c_workflow

- False congestion alarms: unnecessary signal changes, diverted traffic into neighbourhoods, wasted green time.
- Missed congestion: gridlock, delays, spillback.
- Delayed emergency vehicles: very high cost (lives), so emergency priority is a hard constraint.
- Pedestrian risk: injury and death; hard safety constraints on crossing times.
- Pollution: health costs concentrated in exposed neighbourhoods.
- Workflow failure: operators overwhelmed, manual overrides, system outages.

These costs should decide real-time control actions (for example do not shorten pedestrian phases even if it improves average travel time), rather than average accuracy or travel time alone.

:::
:::

:::question R2(e). Treat the system as a socio-technical composite and decide who may modify objectives, thresholds and safety constraints.
:::solution Answer

- Model: forecasting and optimization/control algorithms.
- Data infrastructure: cameras, sensors, phone data, transit feeds, their coverage and quality.
- Public interface: signals, public dashboards, travel apps, and channels for complaints.
- Traffic-control workflow: operators who monitor, override and respond to incidents.
- Transport policy: priorities for public transport, walking, cycling, safety (Vision Zero).
- Legal rules: traffic law, safety standards, environmental and equity law, data protection.
- Accountability: council oversight, audits, public reporting.

Authority: objectives and weights should be set by the elected city council/transport authority after public consultation; safety constraints by the transport safety authority and traffic engineers (and they cannot be traded away by the optimizer); thresholds and operational parameters by the traffic-control centre within approved limits, with changes versioned and logged; independent auditors review equity impacts. Engineers implement but should not alone define what "success" means.

:::
:::


### R3: Generative AI Adviser for University Students

:::origc R3 (Module 1 notes)
R3: Generative AI Adviser for University Students A university introduces a generative AI adviser to help students select courses, understand degree requirements, prepare study plans, and identify academic-support services. The system uses curriculum documents, course descriptions, student records, prerequisite rules, historical enrolment data, and university policies. During a pilot, students report that the adviser is fluent, patient, and available at all hours. However, it occasionally invents course prerequisites, recommends classes that are not being offered, exposes information from another student record, and presents outdated academic regulations with high confidence. Some students begin following its recommendations without consulting faculty advisers. University leadership proposes allowing the system to register students automatically in order to reduce administrative workload. Questions
- Locate this system within the AI landscape. Explain which parts involve generative AI, information retrieval, symbolic rules, search, recommendation, optimization,
automation, and human decision support. Develop a hybrid architecture that uses each approach only where it is appropriate.
- Define the boundary between intelligence and autonomy. Discuss whether the adviser should remain passive, operate as decision support, execute routine actions semi-autonomously, or be permitted to register students without immediate human approval. Justify different autonomy levels for low-risk and high-risk actions.
- Design mechanisms for grounding and reliability. Explain how retrieval from authoritative university sources, rule-based prerequisite checking, source citation, uncertainty communication, abstention, version control, and human escalation could reduce confabulation and outdated advice.
- Examine human-system interaction risks. Discuss automation bias, overreliance, interface design, unequal access to human advisers, and the possibility that professionally written but incorrect advice may be accepted without verification. Propose interface features that encourage critical review.
- Develop an end-to-end monitoring plan. Specify indicators for factual accuracy, privacy violations, outdated knowledge, student overrides, human escalations, harmful recommendations, subgroup differences, response latency, system availability, and real-world academic outcomes. Explain what events should trigger rollback or temporary suspension.
:::

:::question R3(a). Locate the system in the AI landscape and develop a hybrid architecture.
:::solution Answer


| Component | Role and appropriate use |
|---|---|
| Generative AI (LLM) | Natural-language conversation, explanation and drafting of study plans; should not be the source of facts. |
| Information retrieval | Retrieve current curriculum documents, course offerings, policies (retrieval-augmented generation) so answers are grounded. |
| Symbolic rules | Prerequisite checking, degree-requirement audits, credit limits, eligibility rules; deterministic and verifiable. |
| Search | Search over the space of course combinations and schedules that satisfy constraints. |
| Recommendation | Rank suitable courses for the student's goals and history (with care about feedback loops from historical enrolment). |
| Optimization | Build timetables that satisfy constraints (clashes, workload). |
| Automation | Routine actions such as booking an appointment with a faculty adviser or saving a draft plan. |
| Human decision support | Faculty advisers approve study plans and handle exceptions. |


Hybrid design: the LLM is only the interface. Facts come from retrieval over authoritative, versioned sources; every recommendation passes a rule-based prerequisite and requirement checker; schedule options come from search/optimization; outputs are shown as a draft with citations; registration and exceptions go to a human adviser. Student records are accessed only through an access-controlled service that returns the current user's data.

:::
:::

:::question R3(b). Define the boundary between intelligence and autonomy.
:::solution Answer


Fluency is not authority: "autonomy must not be conflated with intelligence." Levels by risk:

- Passive/informational (allowed): explaining policies, describing courses with citations.
- Decision support (default): proposing course lists and study plans that the student and adviser review.
- Semi-autonomous (low-risk actions only): booking an advising appointment, saving a plan, sending reminders, with undo.
- Not permitted without human approval: registering or dropping courses, changing degree programmes, anything affecting graduation, fees, visas, scholarships or academic standing.

Automatic registration is inappropriate now, because the pilot shows invented prerequisites, unavailable classes, outdated rules and privacy leaks; errors would be costly and hard to reverse (missed prerequisites delay graduation). If ever introduced, it should be semi-autonomous: only rule-verified, low-risk registrations, with student confirmation, an adviser sign-off queue and easy reversal.

:::
:::

:::question R3(c). Design mechanisms for grounding and reliability.
:::solution Answer

- Retrieval from authoritative sources: answers generated only from the current, official catalogue, timetable and regulations.
- Rule-based prerequisite checking: every recommended course is checked by a deterministic rule engine against the student's record and current offerings.
- Source citation: every factual statement links to the document and version used.
- Uncertainty communication: state confidence and when information may be incomplete.
- Abstention: "I cannot confirm this; please contact your adviser" when no authoritative source is found or sources conflict.
- Version control: documents and rules versioned with effective dates; outdated regulations retired; the model and prompts versioned.
- Human escalation: exceptions, conflicting rules, high-stakes questions go to a faculty adviser.

Together these reduce confabulation (NIST's first generative risk) and outdated advice.

:::
:::

:::question R3(d). Examine human-system interaction risks and propose interface features.
:::solution Answer


Risks: automation bias and overreliance (students follow fluent advice without checking); interface design that presents answers as authoritative; information integrity (professionally written but incorrect advice accepted without verification, like the junior associate and the NDA); unequal access (students with fewer human advisers or less confidence rely more on the AI, so errors fall unevenly); privacy fears.


Interface features: visible citations and "last updated" dates; a clear banner that advice is not official until approved; confidence indicators; highlighting any requirement the checker could not verify; a "check with adviser" button and easy booking; showing alternatives rather than one answer; requiring confirmation of key facts before any action; reporting of wrong answers; and guaranteed human-adviser availability for disadvantaged students.

:::
:::

:::question R3(e). Develop an end-to-end monitoring plan and rollback triggers.
:::solution Answer


| Indicator | How measured |
|---|---|
| Factual accuracy | Audited sample of answers vs official sources; hallucinated prerequisites or courses |
| Privacy violations | Any exposure of another student's data (target: zero); access-log audits |
| Outdated knowledge | Answers citing superseded document versions |
| Student overrides | How often students or advisers reject recommendations |
| Human escalations | Volume and reasons for referral to advisers |
| Harmful recommendations | Plans that would delay graduation or break rules |
| Subgroup differences | Accuracy, escalation and outcome by programme, year, international status, first-generation students |
| Latency and availability | Response time, uptime |
| Real-world outcomes | Registration errors, graduation delays, satisfaction, adviser workload |


Triggers: any confirmed exposure of another student's record → immediate suspension of record access and incident response; a rise in hallucinated prerequisites or outdated-regulation answers above an agreed rate → rollback to the previous version or retrieval-only mode; policy changes not yet ingested → temporary suspension of affected topics; subgroup gaps or harmful plans above limits → restrict to informational mode until fixed.

:::
:::


### R4: AI for Climate-Smart Agricultural Support

:::origc R4 (Module 1 notes)
R4: AI for Climate-Smart Agricultural Support An agricultural ministry wants to help smallholder farmers decide when to irrigate, fertilize, plant, and harvest. The proposed system combines satellite images, weather forecasts, soil sensors, crop records, market prices, and farmer-reported observations. It generates personalized recommendations through a mobile application. Most historical data come from large commercial farms with reliable irrigation, high-quality sensors, and stable internet connectivity. Small farms often have incomplete records, different crop varieties, irregular access to water, and limited ability to act on recommendations. The model predicts crop yield accurately, and the ministry assumes that following its recommendations will therefore increase yield. Questions
- Separate prediction from causal reasoning. Explain why accurately predicting yield does not prove that a recommended intervention will improve yield. Formulate the counterfactual questions that must be answered before recommending irrigation, fertilizer, or planting changes.
- Evaluate the target population and data representativeness. Compare the historical training population with the intended deployment population. Discuss distribution shift, missingness, sensor inequality, regional variation, and whether a Datasheet for Datasets would reveal limitations before deployment.
- Design a meaningful representation of the farming process. Explain whether static feature vectors are sufficient or whether temporal sequences, spatial maps, weather uncertainty, resource constraints, and mechanistic crop models are required. Discuss the costs of losing temporal or local context.
- Choose an appropriate combination of computational methods. Consider statistical learning, weather forecasting, optimization, rule-based agronomic constraints, causal estimation, and human expert review. Explain why a single highly complex model may be inferior to a transparent hybrid system.
- Assess the broader decision workflow. A recommendation is useful only if the farmer has water, credit, fertilizer, labor, transport, and market access. Explain how these constraints should affect problem formulation, evaluation, interface design, and claims of system success.
:::

:::question R4(a). Separate prediction from causal reasoning.
:::solution Answer


Predicting yield accurately answers "What is likely to happen?" Recommending irrigation or fertilizer requires "What would happen if the farmer did X instead of Y?" (a causal question). The yield model learned associations from commercial farms, where irrigation and fertilizer use are confounded with wealth, soil quality, seed varieties and management skill; high-yield farms irrigate more, but that does not prove irrigation causes the extra yield on a smallholder plot (like attendance and exam scores). Counterfactual questions to answer:

- Would this farmer's yield be higher if they irrigated on day d rather than day d + 5, given their water access?
- Would applying fertilizer amount a at time t increase yield on this soil and crop variety, and by how much relative to its cost?
- Would changing the planting date by two weeks increase yield under this season's uncertain rainfall?
- What is the effect for smallholders specifically, not averaged over commercial farms?

These need causal estimation τ = E[Y(1) − Y(0)] with field trials (randomized plots), agronomic mechanistic crop models, and careful control of confounding.

:::
:::

:::question R4(b). Evaluate the target population and data representativeness.
:::solution Answer


Training population: large commercial farms with reliable irrigation, good sensors, stable internet, standard varieties. Deployment population: smallholders with incomplete records, different varieties, irregular water and limited capacity. This is distribution shift (population, device and context). Missingness is not random (small farms lack sensors and records, so missing data are correlated with being poor). Sensor inequality means features available in training are absent or noisier in deployment (train-serving mismatch). Regional variation in soils, climate and pests is likely under-represented. A Datasheet for Datasets would reveal all this before deployment by documenting composition (farm types, regions, varieties), collection process (sensor types), missing populations (smallholders) and recommended uses, just as the skin-lesion datasheet would have revealed the skin-tone gap.

:::
:::

:::question R4(c). Design a meaningful representation of the farming process.
:::solution Answer


Static feature vectors (one row per farm-season) are insufficient: they cause loss of context. Farming is temporal and spatial: timing of rainfall relative to planting, soil moisture over time, growth stages. A good representation includes temporal sequences (daily weather, soil moisture, crop stage), spatial maps (satellite imagery, soil maps, neighbouring plots), weather uncertainty (probabilistic forecasts, not single values), resource constraints (water availability, labour, credit, fertilizer access) and mechanistic crop models that encode known plant physiology. Losing temporal context can make the model recommend irrigation after the critical window; losing local context can apply commercial-farm patterns to very different plots.

:::
:::

:::question R4(d). Choose an appropriate combination of computational methods.
:::solution Answer

- Statistical learning: satellite-based crop monitoring, pest and disease detection, yield estimation.
- Weather forecasting: probabilistic short- and seasonal forecasts.
- Mechanistic crop models: simulate how water and nutrients affect growth, filling gaps where smallholder data are scarce.
- Rule-based agronomic constraints: do not recommend irrigation when no water is available; fertilizer limits; local regulations.
- Causal estimation: field trials to estimate the benefit of each recommendation for smallholders.
- Optimization: choose the best feasible action given the farmer's budget, water and labour.
- Human expert review: extension officers validate recommendations and handle unusual cases.

A single complex black-box model trained on commercial farms may be inferior: it cannot encode constraints, extrapolates poorly under shift, cannot explain itself to farmers or extension workers, and confuses prediction with intervention effect. A transparent hybrid is more robust, auditable and trusted.

:::
:::

:::question R4(e). Assess the broader decision workflow.
:::solution Answer


A recommendation is useful only if the farmer can act on it: water, credit, fertilizer, labour, transport and market access. Therefore:

- Problem formulation: the decision is "what is the best feasible action for this farmer given their resources", not "maximize yield"; the objective may be income or risk reduction, not yield.
- Evaluation: measure adoption, feasibility, farmer income, yield variance and harm (debt from inputs), by farm size and region; compare with extension-officer advice (baseline).
- Interface design: low-bandwidth, local language, voice or SMS, offline mode, explanations and uncertainty, and options at different costs.
- Claims of success: do not claim impact from accurate yield prediction; claim only what field evidence shows, and report where the system does not work.
:::
:::


### R5: Automated Prioritization of Social-Welfare Applications

:::origc R5 (Module 1 notes)
R5: Automated Prioritization of Social-Welfare Applications A government agency receives more social-welfare applications than its staff can process quickly. It proposes an AI system that assigns each applicant a priority score based on income, employment history, family size, location, housing status, prior benefit use, and administrative records. The model is trained to predict which applications were approved historically. It achieves high accuracy and is used to place applicants into three queues:
- Immediate processing
- Standard processing
- Low priority processing After deployment, applicants from informal employment sectors and remote areas are frequently assigned low priority because their records are incomplete. These cases are reviewed less often, so fewer positive outcomes are observed for these groups. The agency later retrains the model using the newly collected decisions. Questions
- Determine whether the label represents the real objective. Discuss the difference between predicting historical approval and identifying present need or eligibility. Explain how historical administrative decisions may encode policy choices, documentation inequality, resource constraints, and institutional bias.
- Analyze the emerging feedback loop. Explain how low-priority assignment reduces review, how reduced review creates selective labels, and how retraining on these outcomes may make the model increasingly confident in its original decisions.
- Reformulate the problem around a decision or capability. Define the real operational need, target population, index time, prediction horizon, decision alternatives, capacity constraints, and consequences of delay. Consider whether
prioritization should be based on need, eligibility uncertainty, urgency, expected benefit, or review complexity.
- Design an evaluation and fairness framework. Identify appropriate measures beyond aggregate accuracy, including false-negative rates, waiting time, calibration, subgroup performance, appeal outcomes, human override rates, and harm caused by delayed assistance. Discuss how evaluation should account for incomplete ground truth.
- Assign responsibility across the socio-technical lifecycle. Explain the responsibilities of policy designers, data collectors, software developers, model developers, caseworkers, agency leaders, auditors, and appeal bodies. Propose safeguards such as human review, explanation requirements, an appeal channel, abstention for incomplete records, monitoring, and decommissioning criteria. Below is a list of application problems designed to help students translate the concepts into concrete planning, documentation, evaluation, and governance artifacts. They reflect the end-to-end view of AI presented in this module, including problem formulation, data documentation, model selection, deployment, monitoring, and failure analysis.
:::

:::question R5(a). Does the label represent the real objective?
:::solution Answer


No. The label is "approved historically", but the real objective is present need or eligibility. Historical approvals encode policy choices (past rules and quotas), documentation inequality (applicants with complete records were easier to approve), resource constraints (limited staff approved easy cases), and institutional bias (caseworker discretion, stereotypes). Informal-sector workers and remote applicants had incomplete records, so they were approved less, not because they were less needy. The model reproduces "historical, potentially biased institutional decisions rather than discovering an objective, optimal truth" (status quo bias). This mirrors the Obermeyer cost-as-proxy example.

:::
:::

:::question R5(b). Analyze the emerging feedback loop.
:::solution Answer


Incomplete records → low-priority queue → reviewed less often and later → fewer approvals observed for these groups (many never get a decision, or give up) → these outcomes become new labels (selective labels: we only see outcomes for cases that were reviewed) → retraining learns an even stronger link between incomplete records, informal work, remote location and non-approval → the model becomes increasingly confident in its original decisions (self-reinforcing bias). The model is judged on outcomes it produced, so it looks more accurate while harming the most vulnerable.

:::
:::

:::question R5(c). Reformulate the problem around a decision or capability.
:::solution Answer

- Real operational need: process applications so that people in urgent need receive assistance quickly and eligible applicants are not wrongly delayed, given limited staff.
- Target population: all applicants in the current period; unit: one application.
- Index time: at submission (and again when missing documents arrive).
- Prediction horizon: harm from delay over the next 2 to 4 weeks.
- Decision alternatives: fast-track, standard review, request documents with assistance, outreach visit.
- Capacity constraints: caseworker hours per week.
- Consequences of delay: hunger, eviction, loss of medical care; delay is itself harm.

Prioritization should be based on urgency and need (for example housing loss, dependants, no income), combined with review complexity (incomplete records get help, not lower priority), not on predicted historical approval. Eligibility uncertainty should trigger assistance and human review, not demotion. A transparent rule-based urgency score may be better than an opaque model.

:::
:::

:::question R5(d). Design an evaluation and fairness framework.
:::solution Answer

- False-negative rate (truly needy applicants placed in low priority) overall and by group (informal sector, remote, gender, disability, ethnicity).
- Waiting time to decision, by group and queue.
- Calibration of any urgency/need probability by group.
- Subgroup performance and intersections (remote × informal).
- Appeal outcomes: share of appeals upheld, by group.
- Human override rates: how often caseworkers move cases between queues and why.
- Harm from delayed assistance: evictions, debt, health events.
- Incomplete ground truth: outcomes are missing for unreviewed cases. Handle by randomly auditing a sample of low-priority cases (reviewing them fully to learn true eligibility), counterfactual logging of queue assignment, and not treating unreviewed as ineligible (the meaning of "negative").
:::
:::

:::question R5(e). Assign responsibility across the socio-technical lifecycle and propose safeguards.
:::solution Answer


| Actor | Responsibility |
|---|---|
| Policy designers | Define the objective (need, urgency) and eligibility rules; decide what the system may do |
| Data collectors | Make record-keeping accessible; record why data are missing; avoid penalizing informal work |
| Software developers | Build interfaces and pipelines; log decisions; enforce access control and privacy |
| Model developers | Choose appropriate labels, test for proxies (location, employment type), calibrate, document a model card |
| Caseworkers | Review and override priorities; record reasons; flag errors |
| Agency leaders | Accountable owner; approve deployment; fund capacity; suspend if harmful |
| Auditors | Independent fairness and performance audits, including random audits of low-priority cases |
| Appeal bodies | Hear challenges and feed results back into monitoring |


Safeguards: human review for every low-priority assignment; explanation of the priority and missing documents to applicants; an appeal channel with a response time; abstention for incomplete records (route to assisted review rather than low priority); monitoring by subgroup, waiting time and appeal outcomes; no automatic retraining on biased decisions (counterfactual logging, audits); and decommissioning criteria (if disparities are not reduced within an agreed period, or if the label cannot be fixed, stop using the model and revert to need-based rules).

:::
:::


## Application problems A1–A7


These are the assignment-style tasks. Your Assignment 1 already had four of these types (worksheet, model card, datasheet, failure analysis), so the quiz may ask you to produce a short version of any of them. Each answer below is complete; for the quiz, keep the headings and shorten the bullets.


### A1: Formulating an AI Problem (Reducing Unplanned Hospital Readmissions)

:::origc A1 (Module 1 notes)
A1: Formulating an AI Problem Scenario: Reducing Unplanned Hospital Readmissions A regional hospital reports that many adult patients return to the hospital shortly after discharge. Hospital leadership proposes the following project: Build an AI model that predicts which patients will be readmitted. The hospital has access to demographic information, diagnoses, medications, laboratory results, previous admissions, discharge summaries, appointment history, insurance status, and future claims data. Predictions could be generated at admission, during hospitalization, at discharge, or several days after discharge. The hospital has only 100 follow-up appointment slots each week. The discharge team must decide which patients should receive an early follow-up appointment, a telephone call, standard discharge instructions, or no additional intervention. Task Develop a complete AI problem formulation for this project. Your response must specify:
- The real-world decision or operational capability to be improved.
- The target population and exclusion criteria.
- The unit of analysis.
- The index time at which the prediction will be generated.
- The prediction horizon.
- The precise outcome definition.
- The information available at the index time.
- The decision-maker who will receive the output.
- The actions that may follow from the prediction.
- The current baseline or status quo.
- The consequences of false positives and false negatives.
- The intervention-capacity constraint.
- The primary performance and calibration measures.
- The subgroup and fairness analyses required.
- The conditions under which the system should abstain or request human review.
- A final problem statement written as one precise paragraph. Also identify any variables in the proposed data that could produce temporal leakage.
:::

:::question A1. Develop a complete AI problem formulation for the readmission project and identify variables that could cause temporal leakage.
:::solution Answer


| Element | Specification |
|---|---|
| Real-world decision | Which discharged adult patients should receive one of the 100 weekly early follow-up appointments, a telephone call, standard discharge instructions, or no additional intervention, so that preventable unplanned readmissions fall. |
| Target population and exclusions | Adult (18+) patients discharged alive from medical and surgical wards. Exclude: planned readmissions (scheduled chemotherapy, staged surgery), patients discharged to hospice or palliative care, transfers to another acute hospital, patients who leave against medical advice (handled separately), obstetric admissions, and deaths in hospital. |
| Unit of analysis | One index hospitalization (discharge episode). Patients with several admissions are kept in one data partition (patient-level split) to avoid group leakage. |
| Index time | At discharge: when the discharge order is signed, before the patient leaves (so the discharge team can book the follow-up). |
| Prediction horizon | 30 days after discharge. |
| Outcome definition | Y = 1 if the patient has an unplanned (emergency or urgent) inpatient readmission to any hospital in the network within 30 days of discharge; planned readmissions and ED visits without admission are not counted. Deaths within 30 days are recorded as a separate outcome, not coded as "no readmission". |
| Information available at index time | Demographics; diagnoses and procedures of the current stay; medications at discharge; laboratory results finalized before discharge; number of previous admissions and ED visits in the past 12 months; length of stay; appointment history before discharge (for example previous no-shows); insurance status as recorded at admission; discharge destination. |
| Decision-maker | The discharge team (discharge nurse/coordinator with the attending physician). |
| Actions | Tier 1 (highest risk, within capacity): early follow-up appointment within 7 days. Tier 2: structured telephone call within 48 to 72 hours. Tier 3: standard discharge instructions. Low risk: no additional intervention. |
| Baseline / status quo | Current clinician judgment and existing practice (for example follow-up based on discharge nurse assessment), plus a simple heuristic score (such as the LACE index: length of stay, acuity, comorbidity, ED visits) as a second comparator. |
| False positives | A low-risk patient takes one of the 100 slots, displacing someone who needed it; wasted clinic time and patient inconvenience. |
| False negatives | A high-risk patient receives only standard instructions, deteriorates at home and is readmitted (or dies); more serious and less reversible, so c_FN > c_FP. |
| Intervention-capacity constraint | Exactly 100 follow-up appointment slots per week; telephone-call capacity set by nursing staff hours. The decision rule is ranking: the top 100 by p̂ each week (k = 100) after review; the next band receives calls. |
| Primary performance and calibration measures | Primary: precision@100 and recall@100 (share of readmissions captured by the slots). Secondary: AUROC (discrimination), calibration curve and calibration slope, positive predictive value, number of preventable readmissions averted in a pilot. |
| Subgroup and fairness analyses | Age groups, sex, ethnicity, primary language, insurance type, socioeconomic area, diagnosis group, and discharge destination; report selection rates and recall per group with confidence intervals. Check whether insurance status acts as a proxy that lowers priority for uninsured patients (access bias). |
| Abstention / human review | Abstain and send to clinician review when key inputs are missing (for example no discharge medications recorded), when the patient is in a group poorly represented in training, or when p̂ lies in an uncertainty band around the slot cut-off. Clinicians can override with a logged reason. |


Final problem statement (one paragraph): At the time the discharge order is signed, for every adult medical or surgical patient discharged alive (excluding planned readmissions, hospice discharges and transfers), using only information recorded and available before discharge, estimate the calibrated probability of an unplanned inpatient readmission within 30 days, and rank patients each week so that the discharge team can allocate the 100 early follow-up appointments to the highest-ranked patients after clinical review and offer telephone follow-up to the next risk band. The system will be compared with current clinician judgment and the LACE index and evaluated using precision@100, recall@100, calibration and discrimination, reported overall and by age, sex, ethnicity, language, insurance and diagnosis group, while accounting for the higher cost of missed readmissions, the fixed appointment capacity, abstention for incomplete records, and governance requirements including a model card and post-deployment monitoring.


Temporal leakage variables:

- Future claims data: claims after discharge reveal the readmission itself (target leakage).
- Appointment history after discharge (whether they attended follow-up), which also reflects the intervention.
- Laboratory results finalized after discharge (pending labs).
- Discharge summaries completed or edited after discharge (often written days later and may mention complications).
- Diagnoses coded after discharge for billing (ICD codes finalized later).
- Predictions generated "several days after discharge" would use post-discharge information and leave little time to act; that option is rejected.
- Insurance status updated later (only the value at admission/discharge can be used).
:::
:::


### A2: Preparing a Model Card (Heart Disease Risk Prediction Model)

:::origc A2 (Module 1 notes)
A2: Preparing a Model Card Scenario: Heart Disease Risk Prediction Model A hospital has developed a random forest model to estimate the probability that an adult patient has clinically significant heart disease. The following information is available:
  - Training data: 12,000 patient records from two urban hospitals
  - Evaluation data: 3,000 records collected later from the same hospitals
  - Inputs: age, sex, blood pressure, cholesterol, chest pain category, maximum heart rate, diabetes status, body mass index, and electrocardiogram findings
  - Output: probability of heart disease
  - Overall accuracy: 86 percent
  - Precision: 0.82
  - Recall: 0.74
  - F1 score: 0.78
  - Recall for male patients: 0.80
  - Recall for female patients: 0.62
  - Recall for patients younger than 40 years: 0.55
  - The predicted probabilities are moderately overconfident
  - Family history, smoking status, ethnicity, and genetic information are unavailable
  - The model has not been externally validated
  - The intended use is clinical decision support
  - Some administrators have proposed using the model to automatically reject requests for further cardiac testing Task Prepare a complete Model Card for this system. The Model Card must contain:
- Model name, version, type, and architecture.
- Purpose and intended clinical role.
- Intended users.
- Inputs and outputs.
- Training and evaluation data.
- Preprocessing and missing-value handling.
- Overall performance measures.
- Subgroup performance.
- Calibration findings.
- Fairness observations.
- Known limitations.
- Appropriate uses.
- Inappropriate or prohibited uses.
- Human-review requirements.
- Potential harms resulting from false positives and false negatives.
- Generalizability limitations.
- Monitoring requirements after deployment.
- Conditions that should trigger recalibration, retraining, rollback, or withdrawal.
- Future work required before broader deployment. Conclude the Model Card with a clear deployment recommendation: approve, conditionally approve, or do not approve.
:::


This Model Card follows the structure of the notes' "Instructive Example of a Model Card" (Section 4.8.1): Model Overview, Data Description, Performance Metrics, Known Limitations, Intended and Inappropriate Uses, Ethical Considerations, Additional Considerations, then Takeaways. Extra items required by the task (calibration, human review, monitoring, triggers, recommendation) are added inside the most relevant section.

:::question A2. Prepare a complete Model Card for the heart disease system and give a deployment recommendation.
:::solution Answer


**Model Card: Heart Disease Risk Prediction Model**


Model Overview

- Model Name: Heart Disease Risk Prediction Model.
- Version: 1.0 (first evaluated release; internal validation only).
- Type: Binary classification (clinically significant heart disease: Yes/No), producing a probability of heart disease.
- Model Architecture: Random Forest Classifier trained on structured patient data (age, sex, blood pressure, cholesterol, chest pain category, maximum heart rate, diabetes status, BMI, ECG findings).
- Purpose: To estimate the probability that an adult patient has clinically significant heart disease based on clinical measurements.
- Intended clinical role: Clinical decision support. The model is intended to assist healthcare professionals by providing an additional tool to help identify higher-risk patients who may require further diagnostic testing (for example stress testing or angiography) or preventive care. It does not make or execute decisions.
- Intended users: Physicians, cardiologists and trained clinical staff in the two developing hospitals (and similar urban hospitals after local validation). Not patients, insurers or administrators acting without a clinician.

Data Description

- Training data: 12,000 adult patient records from two urban hospitals.
- Evaluation data: 3,000 records collected later from the same two hospitals (a temporal holdout from the same sites; this is not external validation).
- Features (inputs): age, sex, blood pressure, cholesterol, chest pain category, maximum heart rate, diabetes status, body mass index, and electrocardiogram findings.
- Output: a probability (0 to 1) of clinically significant heart disease.
- Data Preprocessing and missing-value handling: not stated in the scenario and must be documented. Recommended (following the notes' example): missing numerical values imputed with the mean or median and categorical values with the mode, using the same versioned transformation in training and serving (to avoid train-serving mismatch); a missing-value indicator retained; records with missing critical inputs (for example ECG findings) flagged for abstention rather than silently imputed.
- Exclusions: the model does not include family history, smoking status, ethnicity or genetic information, as these were not available in the dataset.

Performance Metrics

- Overall Accuracy: 86%
- Precision: 0.82 (82% of patients flagged as positive truly have heart disease)
- Recall: 0.74 (the model misses about 26% of patients who have heart disease)
- F1 Score: 0.78
- Performance by Subgroup:
- Male patients: Recall = 0.80
- Female patients: Recall = 0.62 (about 38% of women with heart disease are missed)
- Patients younger than 40 years: Recall = 0.55 (about 45% missed)
- Not reported and required: precision by subgroup, older adults, diabetic vs non-diabetic patients, ethnicity (unavailable), and intersections (for example young women).
- Calibration findings: the predicted probabilities are moderately overconfident: when the model outputs a high probability, the observed rate of heart disease is lower (and low probabilities may be too low). Probabilities should not be read literally until the model is recalibrated (for example Platt scaling or isotonic regression on held-out data) and a calibration curve is published overall and by subgroup.
- Fairness Observations: The model performs substantially better on male patients than female patients (recall 0.80 vs 0.62), indicating potential gender bias, and performs worst for patients under 40 (recall 0.55). The model therefore tends to miss heart disease in women and younger adults, groups whose symptoms are often atypical and who are already at risk of under-diagnosis.

Known Limitations

- Bias in Data: the dataset likely contains fewer female and younger patients with heart disease, and women often present with atypical chest pain categories, leading to weaker performance for these groups.
- Generalizability: the model was trained and evaluated only on two urban hospitals and has not been externally validated. Performance may differ in rural hospitals, other regions, other countries, primary care or populations with different demographics and equipment.
- Feature Limitations: family history, smoking status, ethnicity and genetic information were unavailable; these are important risk factors, which may reduce accuracy and hide ethnic disparities that cannot be measured.
- Calibration: probabilities are moderately overconfident.
- Recall: overall recall of 0.74 means one in four patients with disease is missed; this is too low for the model to be used to rule patients out.

Intended and Inappropriate Uses

- Intended (appropriate) Use: to support clinicians in identifying patients at higher risk of heart disease who may benefit from further diagnostic testing or preventive care. It should be used as an additional decision support tool alongside clinical judgment and standard risk tools, never as the sole basis for diagnosis.
- Inappropriate or prohibited Uses:
- Automatically rejecting requests for further cardiac testing (as some administrators proposed). This is prohibited: with recall of 0.74 overall, 0.62 for women and 0.55 for under-40s, a "low-risk" output would deny testing to many patients who actually have heart disease.
- Using the model as the sole basis for diagnosis or for ruling out disease.
- Use for populations not represented in training (other regions, rural settings, children) without local validation.
- Use by insurers or employers for pricing, eligibility or employment decisions.
- Using the probability as a precise value before recalibration.

Ethical Considerations

- Fairness: the model has potential gender and age biases, which should be addressed before full-scale deployment. Regular audits should be conducted to ensure fair treatment of all patient subgroups; thresholds should not produce much higher false-negative rates for women or younger patients.
- Harms from false negatives: a patient with heart disease is classified as low risk, so testing and treatment may be delayed, risking myocardial infarction or death. Because false negatives are concentrated in women and younger adults, the harm is unequal and could exacerbate health inequalities (the notes: "under-predicting heart disease in women could delay necessary interventions").
- Harms from false positives: unnecessary invasive tests (angiography carries bleeding and infection risk), anxiety, cost, and wasted diagnostic capacity.
- Human-review requirements: a clinician must review every output; the model can prompt further testing but must never block it. Low-probability outputs for patients with symptoms, women, under-40s, or incomplete records must receive full clinical assessment. Clinicians should be able to override the model with a logged reason, and outputs should be shown with uncertainty and the main contributing features.
- Impact of Misuse: using the model to automatically deny testing, or in under-represented populations, could cause serious harm and erode trust.

Additional Considerations

- Generalizability limitations: valid only for adult patients similar to those in the two urban hospitals; any new site must perform local external validation and calibration before use.
- Monitoring requirements after deployment: input quality and missingness; input drift (age, sex mix, new ECG machines, coding changes); output distribution and share of patients flagged; calibration on new outcomes; recall and precision overall and by sex, age group and site; clinician override and acceptance rates (automation bias); time to diagnosis for flagged vs non-flagged patients; adverse events among patients classified low risk.
- Conditions that should trigger action:
- Recalibration: calibration error above the agreed limit overall or in any subgroup, or a change in disease prevalence.
- Retraining: input drift (new population, equipment or coding), or subgroup recall gaps that persist after recalibration.
- Rollback: a new version lowers recall for any subgroup or widens the male-female gap; rollback requires versioned models and data.
- Withdrawal: evidence the model is being used to deny testing, adverse events linked to false negatives, or failure to reach an agreed minimum recall for women and younger patients within a set period.
- Future Work: integrate family history, smoking status and relevant genetic markers; collect a more diverse dataset (more women, younger patients, other ethnicities and rural hospitals); perform external validation at independent sites; recalibrate; examine threshold choice using the decision-cost function; and conduct a prospective silent evaluation before broader deployment.

Deployment Recommendation: Conditionally Approve (as clinical decision support only, within the two development hospitals).


Conditions: (1) recalibrate and publish calibration curves before use; (2) use a lower threshold or a separate review pathway so that recall for women and patients under 40 is raised to an agreed minimum; (3) the model may only recommend further testing and must never be used to automatically reject requests for cardiac testing; (4) every output is reviewed by a clinician, with overrides logged; (5) subgroup monitoring and the triggers above are in place at launch; (6) external validation before any use at other sites. If recall for women and younger patients cannot be improved, the recommendation becomes do not approve for general use.


Takeaways from the Model Card (as in the notes): Data transparency (users see where data came from and what is excluded); Performance by group (subgroup recall reveals the gender and age gaps that 86% accuracy hides); Known limitations (no external validation, missing risk factors, overconfidence); Ethical guidance (it supports but never replaces clinical judgment and must not be used to deny testing).

:::
:::


### A3: Preparing a Datasheet for a Dataset (Crop Disease Image Dataset)

:::origc A3 (Module 1 notes)
A3: Preparing a Datasheet for a Dataset Scenario: Crop Disease Image Dataset An agricultural research institute releases a dataset for developing AI systems that identify crop diseases from leaf images. The dataset contains: o 80,000 images
  - Four crops: wheat, maize, tomato, and potato
  - Twelve disease categories and one healthy category
  - Images collected from 35 commercial farms
  - Seventy percent of the images collected from two regions
  - Most images captured during daylight using high-resolution cameras
  - Only 5 percent captured using low-cost mobile phones
  - Disease labels assigned by field technicians
  - Ten percent of labels independently reviewed by plant pathologists
  - Diseased plants photographed more frequently than healthy plants
  - Images resized to 512 by 512 pixels
  - Backgrounds not removed
  - Farm identifiers replaced with coded values
  - No images collected during drought conditions
  - No data from smallholder farms
  - No formal procedure for adding future disease categories
  - Intended use described only as crop disease AI research Task Prepare a Datasheet for this dataset. The datasheet must document:
- Motivation for creating the dataset.
- Dataset creators, funders, and responsible maintainers.
- Dataset composition.
- Unit of observation.
- Geographic and seasonal coverage.
- Crop and disease distributions.
- Data-collection process.
- Sampling procedure.
- Label definitions.
- Labeling and verification procedures.
- Preprocessing and transformations.
- Known missing populations and conditions.
- Potential proxies and dataset artifacts.
- Possible class imbalance and selection bias.
- Consent, privacy, licensing, and access considerations.
- Recommended uses.
- Uses that are not supported.
- Risks associated with mobile-phone deployment.
- Generalization limitations.
- Maintenance, correction, versioning, and retirement procedures. Conclude by explaining whether the dataset is suitable for training a system intended for smallholder farmers using low-cost mobile phones.
:::


This follows the notes' Datasheet structure (motivation, composition, collection process, preprocessing, recommended uses, limitations) and your Assignment Problem 3.

:::question A3. Prepare a Datasheet for the crop disease image dataset and decide whether it suits smallholder farmers using low-cost mobile phones.
:::solution Answer


Motivation. Created to support research on AI systems that identify crop diseases from leaf images, enabling early, low-cost detection without waiting for a plant pathologist. The stated intended use is only "crop disease AI research", which is too vague and must be made specific.


Creators, funders and maintainers. The agricultural research institute's field and data teams, with 35 commercial partner farms. The funder must be stated. A named maintainer and contact address are required (currently missing).


Composition.

- 80,000 images; 4 crops (wheat, maize, tomato, potato); 12 disease classes + 1 healthy class.
- Unit of observation: one leaf image with one crop and one class label. Several images may come from the same plant, plot or farm, so images are not independent.
- Crop and disease distributions: counts per crop and per class must be reported; diseased plants were photographed more often than healthy plants.

Geographic and seasonal coverage. 35 commercial farms; 70% of images from two regions; no images during drought; most images captured in daylight.


Data-collection process. Field technicians photographed leaves on site, mostly with high-resolution cameras; only 5% (about 4,000 images) with low-cost mobile phones.


Sampling procedure. Not random: farms chosen through partnership (all commercial, concentrated in two regions); within farms, symptom-driven (diseased plants over-sampled). Two selection effects: site selection and outcome-dependent selection.


Label definitions. One of 13 classes per image. Must document the definition of each disease, how co-infections and abiotic stress (nutrient, water, drought stress) were handled, and that severity/stage is not recorded.


Labelling and verification. Labels assigned by field technicians; only 10% independently reviewed by plant pathologists; the agreement rate must be reported. 90% rely on non-specialist judgment, so noise is likely in visually similar diseases.


Preprocessing and transformations. Resized to 512 × 512 (may distort lesions and remove absolute scale); backgrounds not removed; farm identifiers replaced with coded values; no colour normalization reported. Transformation code and versions must be published.


Known missing populations and conditions. Smallholder farms (entirely absent); drought conditions; regions outside the two main regions; low-light, overcast, rainy or dusty conditions; low-cost phone images; other crops and diseases; no "unknown/other" class.


Potential proxies and dataset artifacts. Background (soil, mulch, irrigation equipment, row spacing) linked to farm and disease; device characteristics; photographer framing (lesions framed centrally); lighting/time of day; resizing artifacts. A model may learn these shortcuts rather than leaf symptoms.


Class imbalance and selection bias. Healthy leaves are under-represented, so a model will over-diagnose disease in the field; rare diseases have fewer images and fewer verified labels; commercial and two-region dominance is selection bias.


Consent, privacy, licensing and access. Written agreements with each farm for photography, release and model training; workers visible in images must consent or be blurred; farm codes are a start but backgrounds and EXIF/GPS metadata can re-identify farms, so strip metadata and restrict access to the code key; an explicit licence stating commercial use, redistribution and attribution.


Recommended uses. Research and benchmarking with farm-grouped splits; pre-training/transfer learning before fine-tuning on local expert-labelled data; research on distribution shift, label noise and shortcut learning; prototype decision support for large commercial farms in the two well-represented regions with agronomist confirmation.


Uses that are not supported. Sole basis for diagnosis or pesticide decisions; deployment on smallholder farms; drought regions or seasons; crops or diseases outside the 13 classes; severity grading or yield-loss estimation; insurance or regulatory decisions; identifying individual farms.


Risks associated with mobile-phone deployment. Train-serving mismatch and device shift: phone images have lower resolution, stronger compression, different colour balance, blur and variable framing and lighting; fine disease distinctions depend on exactly the texture and colour detail phones lose. Accuracy may collapse while the model stays confident. False "diseased" → unnecessary pesticide costs; false "healthy" → outbreaks spread. Need a phone-specific validation set, calibrated confidence with abstention, image-quality checks, and a route to a human agronomist.


Generalization limitations. Performance should be expected to drop with new regions, smallholder settings, drought or other stress, different lighting, cultivars, seasons or devices, especially several at once.


Maintenance, correction, versioning and retirement. A named maintainer; a process to report and correct mislabelled images with a public changelog; fixed, reproducible versions (v1.0 remains available); a formal procedure to add new disease categories; planned additions targeting the gaps (smallholders, drought, phones, new regions); a retirement policy (for example when cultivars or pathogen strains change) with user notification.


Conclusion: not suitable on its own for a system for smallholder farmers using low-cost mobile phones. The target users (smallholders), the target device (phones: only 5% of data), and the target conditions (irregular water, possible drought, varied regions) are exactly what the dataset lacks; labels are mostly unverified and healthy plants are under-sampled. The model would be "confidently wrong rather than obviously broken". It can be used for pre-training, but a purpose-built dataset from smallholder fields, captured on farmers' phones, labelled by pathologists, across seasons, is required before deployment.

:::
:::


### A4: Deciding Which Model to Deploy (Predictive Maintenance)

:::origc A4 (Module 1 notes)
A4: Deciding Which Model to Deploy Scenario: Predictive Maintenance in a Manufacturing Plant A manufacturing company wants to predict whether a critical machine will fail within the next 24 hours. The system must generate a prediction every minute using vibration, temperature, pressure, load, and maintenance-history data. Three models have been evaluated (Table 3). Additional constraints include:
- The production controller requires a response within 100 milliseconds.
- The plant has no GPU infrastructure.
- Engineers require understandable reasons before stopping a machine.
- Every unnecessary shutdown costs 20,000 dollars.
- A missed failure can cost more than 1 million dollars and may injure workers.
- The internal team has experience with statistical models and tree-based systems but limited deep-learning expertise. Task Select the model that should be deployed and justify the decision. Your analysis must consider:
- Predictive performance.
- Failure recall.
- Calibration.
- False-positive and false-negative costs.
- Latency.
- Hardware and memory requirements.
- Robustness to missing sensor values.
- Interpretability and explanation needs.
- External validation.
- Maintenance burden.
- Available team expertise.
- Long-term lifecycle cost.
- Monitoring and retraining requirements.
- Whether the selected model should operate automatically or as decision support.
- Whether a hybrid arrangement involving more than one model would be preferable. Do not select a model solely because it has the highest accuracy.
:::


Table 3 in the notes (page 167) compares the three models:


| Criterion | Model A: Logistic Regression | Model B: Random Forest | Model C: Deep Neural Network |
|---|---|---|---|
| Accuracy | 88% | 92% | 94% |
| Failure recall | 76% | 87% | 90% |
| Calibration | Good | Moderate | Poor |
| Inference latency | 5 ms | 35 ms | 240 ms |
| Explanation | Direct coefficients | Feature importance and local explanations | Unstable post-hoc explanations |
| Memory requirement | Very low | Moderate | High |
| Specialist maintenance | Low | Moderate | High |
| Performance with missing sensors | Moderate | Good | Poor |
| External-site validation | Completed | Completed | Not completed |
| Retraining frequency | Every six months | Every three months | Every month |

:::question A4. Select the model that should be deployed and justify the decision (do not choose on accuracy alone).
:::solution Answer


Decision: deploy Model B (Random Forest) as the primary model, in a hybrid arrangement, operating as decision support with an automatic safety layer. Reject Model C. Keep Model A as the interpretable fallback and benchmark.


Step 1: eliminate models that violate hard constraints. Model C's 240 ms latency breaks the controller's 100 ms requirement; the plant has no GPU and C needs high memory; its explanations are unstable, while engineers "require understandable reasons before stopping a machine"; it has poor calibration, poor performance with missing sensors, and no external validation; it needs monthly retraining and high specialist maintenance, but the team has limited deep-learning expertise. Its extra 3 points of recall cannot compensate. Model C is out.


Step 2: compare A and B using error costs, not accuracy.

- Failure recall: B catches 87% of failures vs 76% for A. For every 100 real impending failures, B catches about 11 more.
- False-positive vs false-negative costs: a missed failure costs more than \$1,000,000 and may injure workers; an unnecessary shutdown costs \$20,000. So c_FN / c_FP ≥ 50. Eleven extra caught failures are worth at least \$11 million plus avoided injuries; B would have to cause more than 550 extra unnecessary shutdowns per 100 failures before it became worse than A. The notes' rule: the best threshold and model minimize real-world cost, C(t) = c_FP·P(FP|t) + c_FN·P(FN|t) + c_delay·E[D|t] + c_workflow(t), not maximize accuracy.
- Predictive performance: B is also more accurate (92% vs 88%).
- Calibration: A is better (good vs moderate). B's probabilities must be recalibrated (for example isotonic regression or Platt scaling on held-out data) before a threshold is set; calibration is checked after every retraining.
- Latency: both are well within 100 ms (5 ms and 35 ms), leaving room for data validation within the budget.
- Hardware and memory: B needs moderate memory and no GPU; runs on the existing CPUs.
- Robustness to missing sensors: B is good (A moderate); important because sensors fail in a factory.
- Interpretability: B gives feature importance and local explanations ("vibration in the last 30 min and bearing temperature raised the risk"), which is understandable enough for engineers; A is even clearer.
- External validation: completed for both.
- Maintenance burden and team expertise: B is moderate; the team has experience with statistical and tree-based models, so B is maintainable in-house.
- Long-term lifecycle cost: B requires retraining every three months (moderate), far less than C; A is cheapest but its lower recall costs far more in missed failures.
- Monitoring and retraining: monitor sensor data quality and missingness, input drift (new machines, loads, seasons), score distribution, alert rate and shutdowns, calibration, recall and precision as outcomes arrive (failures and maintenance findings), explanation stability, latency, and engineer override rates. Retrain every three months or when drift or recall drops trigger it; validate each new version against the current one and block release if recall or calibration worsens (TFX model validation); keep rollback.

Step 3: automatic operation or decision support? Decision support for normal alerts: stopping a machine costs \$20,000, and engineers want reasons, so the model raises a prioritized alert with its probability and explanation, and an engineer decides (within a defined response time). However, for imminent-danger conditions, an explicit safety rule (symbolic, not learned) should stop the machine automatically, for example vibration or temperature above a hard engineering limit, because worker safety cannot wait for review. This is the semi-autonomous pattern: routine low-risk handling automated, ambiguous cases escalated.


Step 4: hybrid arrangement (preferable).

- Model B as the primary risk scorer (every minute), recalibrated, with a threshold set by C(t) and by maintenance-crew capacity, plus alert suppression so the same machine does not alert every minute (avoid alert fatigue).
- Model A runs in parallel as an interpretable benchmark and fallback: if B's service fails, or if too many sensors are missing, the system falls back to A (or to rules) rather than giving no prediction; large disagreement between A and B triggers review.
- Hard safety rules and a safety controller for extreme readings (automatic stop).
- Human engineers make the final stop decision for model-driven alerts, with overrides logged.
- Abstention: if critical sensors are missing or invalid, show "insufficient data" and schedule a manual inspection.

Conclusion: Random Forest (B) best balances high failure recall, latency, CPU-only deployment, robustness to missing sensors, explanation needs, external validation and team skills. Highest accuracy (C) is not the best choice because it breaks latency, hardware, explanation and maintenance constraints.

:::
:::


### A5: Identifying Hidden Technical Debt (Food Delivery Recommendation System)

:::origc A5 (Module 1 notes)
A5: Identifying Hidden Technical Debt Scenario: Food Delivery Recommendation System
A food delivery company uses a machine-learning model to rank restaurants for each customer. The system has operated for three years. The following conditions are discovered during an internal review:
- Customer, restaurant, payment, location, and promotion data are joined through several undocumented scripts.
- The mobile application team recently renamed several event fields without informing the machine-learning team.
- Training uses one implementation of restaurant distance, while production uses another.
- Fifteen separate configuration files contain ranking weights and thresholds.
- Some configuration files are edited manually on production servers.
- More than twenty internal services consume model scores, but no central list of consumers exists.
- The recommendation interface accepts only five fixed restaurant categories.
- The new model produces twelve categories and a continuous relevance score.
- A large block of custom glue code maps the new outputs into the old interface.
- User clicks are treated as direct measures of preference.
- Restaurants shown near the top receive more clicks and therefore appear more frequently in future training data.
- Promotion teams modify ranking scores after model inference.
- Feature definitions are duplicated across training, testing, and production pipelines.
- Restaurant availability is refreshed every hour, even though many restaurants open and close within minutes.
- No single person owns the complete pipeline.
- Only recommendation click-through rate is monitored. Task Prepare a hidden technical debt register. For each identified debt item, record:
- The evidence in the scenario.
- The technical debt category.
- The affected component.
- The likely failure mode.
- The possible business, fairness, or operational consequence.
- The method for detecting the problem.
- The proposed corrective action.
- The person or team that should own the corrective action.
- The urgency level. Your register should consider at least:
- Undeclared consumers
- Unstable data dependencies
- Train-serving mismatch
- Configuration debt
- Glue-code debt
- Pipeline entanglement
- Stale features
- Feedback loops
- Selective exposure
- Monitoring gaps
- Ownership gaps
- Interface rigidity
- Hidden post-processing Conclude by identifying the three items that create the greatest production risk.
:::

:::question A5. Prepare a hidden technical debt register and identify the three items that create the greatest production risk.
:::solution Answer


Summary register


| # | Debt item (category) | Affected component | Owner | Urgency |
|---|---|---|---|---|
| 1 | Undeclared consumers | Model score output / 20+ services | ML platform lead + consuming teams | High |
| 2 | Unstable data dependencies (renamed event fields) | Event ingestion / feature pipeline | Mobile app team + data engineering | Critical |
| 3 | Train-serving mismatch (two distance implementations) | Feature computation | ML engineering | Critical |
| 4 | Configuration debt (15 config files, manual production edits) | Ranking weights and thresholds | ML platform / SRE | Critical |
| 5 | Glue-code debt (mapping 12 categories to 5) | Output-to-interface adapter | ML engineering + app team | High |
| 6 | Pipeline entanglement (undocumented join scripts) | Data joins (customer, restaurant, payment, location, promotion) | Data engineering | High |
| 7 | Stale features (hourly availability refresh) | Restaurant availability feature | Data engineering | High |
| 8 | Feedback loop (top positions get more clicks) | Training data / ranking | ML team + product | High |
| 9 | Selective exposure (clicks treated as preference) | Label definition | ML team + data science | High |
| 10 | Monitoring gap (only CTR monitored) | Monitoring | ML platform / MLOps | Critical |
| 11 | Ownership gap (no pipeline owner) | Whole pipeline | Engineering leadership | Critical |
| 12 | Interface rigidity (5 fixed categories) | Recommendation UI | Product + app team | Medium |
| 13 | Hidden post-processing (promotion teams change scores) | Post-inference scoring | Promotions + ML team + leadership | High |
| 14 | Duplicated feature definitions | Train/test/production pipelines | ML engineering | High |


Detailed register entries


**1. Undeclared consumers**

- Evidence: more than twenty internal services consume model scores, with no central list.
- Category / component: undeclared consumers (data dependency) / model output.
- Failure mode: a model update changes score scale or meaning and silently breaks downstream services (pricing, marketing, ETA) that assumed the old behaviour; the ML team cannot safely change the model.
- Consequence: wrong promotions, broken features, revenue loss; hidden coupling blocks improvement.
- Detection: access logs and API-key audit of who calls the score endpoint; dependency tracing.
- Correction: a registry of consumers, access control on the score API, versioned score contracts, notice before changes.
- Owner / urgency: ML platform lead with consuming teams / High.

**2. Unstable data dependencies**

- Evidence: the mobile team renamed event fields without informing the ML team.
- Category / component: unstable data dependency / event ingestion.
- Failure mode: features become null or default silently; the model ranks on corrupted inputs (like the notes' UTC-to-local timestamp change).
- Consequence: poor recommendations, lower orders; no error is thrown (silent failure).
- Detection: schema validation and missingness checks on incoming events; alerts on sudden feature distribution changes.
- Correction: data contracts between app and ML teams; schema registry; pipeline pauses on schema violations.
- Owner / urgency: mobile app team and data engineering / Critical.

**3. Train-serving mismatch**

- Evidence: training uses one implementation of restaurant distance, production another.
- Category / component: train-serving mismatch (skew) / feature computation.
- Failure mode: the model sees different distance values in production than in training; learned relationships no longer apply.
- Consequence: far restaurants recommended, longer deliveries, cold food, cancellations.
- Detection: compare training vs serving feature values for the same requests; skew monitoring.
- Correction: a single shared, versioned transformation (feature store) for training and serving; automated consistency tests.
- Owner / urgency: ML engineering / Critical.

**4. Configuration debt**

- Evidence: fifteen separate configuration files with ranking weights and thresholds; some edited manually on production servers.
- Category / component: configuration debt / ranking parameters.
- Failure mode: nobody knows which configuration produced current behaviour; changes are untracked; rollback impossible.
- Consequence: unexplained ranking changes, outages, inability to reproduce or audit.
- Detection: configuration diff audits; file-integrity monitoring on production servers.
- Correction: consolidate into one version-controlled configuration with review, testing and deployment through the pipeline; ban manual production edits.
- Owner / urgency: ML platform / SRE / Critical.

**5. Glue-code debt**

- Evidence: a large block of custom glue code maps the new model's 12 categories and continuous score into the old interface's 5 categories.
- Category / component: glue code / output adapter.
- Failure mode: brittle mapping silently fails when outputs change (like the notes' collections example where everyone defaulted to "Standard").
- Consequence: the new model's value is lost or distorted without any error.
- Detection: monitor the distribution of final displayed categories vs model outputs.
- Correction: redesign the interface to accept the new outputs; replace glue code with a tested, documented adapter; unit tests.
- Owner / urgency: ML engineering + app team / High.

**6. Pipeline entanglement**

- Evidence: customer, restaurant, payment, location and promotion data are joined through several undocumented scripts.
- Category / component: pipeline jungles / entanglement / data joins.
- Failure mode: a change in one source or script alters features elsewhere (changing anything changes everything); failed or delayed joins produce wrong features.
- Consequence: silent degradation; privacy risk from undocumented payment/location joins.
- Detection: lineage tracking; data-quality tests on join outputs (row counts, key matches).
- Correction: document and consolidate joins into an orchestrated, tested pipeline with lineage.
- Owner / urgency: data engineering / High.

**7. Stale features**

- Evidence: restaurant availability refreshed hourly although restaurants open and close within minutes.
- Category / component: stale features / availability feature.
- Failure mode: closed restaurants recommended; open ones hidden.
- Consequence: failed orders, poor customer experience, unfair loss of orders for restaurants.
- Detection: measure order failures due to closure; feature freshness monitoring.
- Correction: streaming or event-driven availability updates; availability filter at serving time.
- Owner / urgency: data engineering / High.

**8. Feedback loop**

- Evidence: restaurants shown near the top receive more clicks and therefore appear more often in future training data.
- Category / component: direct feedback loop / training data and ranking.
- Failure mode: past exposure → observed interaction → training data → future exposure; popular restaurants become more popular regardless of quality.
- Consequence: new and small restaurants starved of exposure (fairness to restaurants), less diversity, lock-in.
- Detection: track concentration of exposure and new-restaurant exposure over time.
- Correction: counterfactual logging of what was shown and at which position; position-bias correction; exploration traffic.
- Owner / urgency: ML team + product / High.

**9. Selective exposure (clicks as preference)**

- Evidence: user clicks are treated as direct measures of preference.
- Category / component: label definition (proxy label) / training labels.
- Failure mode: clicks depend on position, interface and availability, not only preference; the model learns its own ranking.
- Consequence: optimizing clicks rather than long-term benefit (satisfaction, repeat orders).
- Detection: compare clicks with orders, ratings and retention; A/B tests.
- Correction: better labels (completed orders, ratings, repeat purchases), position-debiasing, long-term metrics.
- Owner / urgency: ML team + data science / High.

**10. Monitoring gap**

- Evidence: only recommendation click-through rate is monitored.
- Category / component: monitoring debt / whole system.
- Failure mode: input corruption, skew, stale features, drift and fairness problems are invisible while CTR looks fine.
- Consequence: silent failures and revenue loss discovered late.
- Detection: (gap itself) audit of monitoring coverage.
- Correction: multi-dimensional monitoring: input quality, drift, feature pipelines, output distributions, order conversion, delivery time, cancellations, restaurant exposure fairness, latency, overrides.
- Owner / urgency: ML platform / MLOps / Critical.

**11. Ownership gap**

- Evidence: no single person owns the complete pipeline.
- Category / component: governance / ownership debt / entire system.
- Failure mode: problems fall between teams; no one can approve, stop or roll back.
- Consequence: slow incident response; unmanaged risk (NIST Govern failure).
- Detection: RACI review; incident post-mortems showing unclear responsibility.
- Correction: name an accountable pipeline owner with authority; define team responsibilities.
- Owner / urgency: engineering leadership / Critical.

**12. Interface rigidity**

- Evidence: the interface accepts only five fixed categories while the model produces twelve plus a continuous score.
- Category / component: rigid UI categories / recommendation interface.
- Failure mode: information lost; forces glue code.
- Consequence: the new model cannot deliver its value.
- Detection: compare model output richness with displayed categories.
- Correction: redesign the interface to support new categories and scores.
- Owner / urgency: product + app team / Medium.

**13. Hidden post-processing**

- Evidence: promotion teams modify ranking scores after model inference.
- Category / component: hidden post-processing / scoring layer.
- Failure mode: the displayed ranking is not the model's ranking; evaluation and monitoring measure the wrong thing; the changed rankings feed back into training.
- Consequence: unexplained behaviour, possible unfair promotion, misleading metrics.
- Detection: log pre- and post-adjustment scores and compare.
- Correction: make promotion adjustments explicit, versioned and logged within the pipeline, with governance approval; train on logged exposure.
- Owner / urgency: promotions team + ML team + leadership / High.

**14. Duplicated feature definitions**

- Evidence: feature definitions duplicated across training, testing and production pipelines.
- Category / component: duplicated logic (skew risk) / feature pipelines.
- Failure mode: definitions drift apart, causing train-serving and test-serving mismatch.
- Consequence: evaluation results do not reflect production.
- Detection: automated comparison of feature outputs across pipelines.
- Correction: one centralized, version-controlled feature store (Feast or Tecton, as in the notes).
- Owner / urgency: ML engineering / High.

Three items with the greatest production risk:


1. Train-serving mismatch plus duplicated feature definitions (items 3 and 14): the production model is effectively running on different inputs from the ones it was trained and tested on, so every offline result is unreliable.


2. Configuration debt with manual production edits (item 4): untracked changes make the system irreproducible and impossible to roll back; one mistaken edit can change rankings for all customers.


3. Monitoring gap combined with the ownership gap (items 10 and 11): with only CTR monitored and nobody owning the pipeline, all other debts (renamed fields, stale features, broken glue code) can fail silently with no one responsible for detecting or fixing them.

:::
:::


### A6: Completing a Problem-Framing Worksheet (University Tutoring Allocation)

:::origc A6 (Module 1 notes)
A6: Completing a Problem-Framing Worksheet Scenario: University Tutoring Allocation A university can provide intensive tutoring to only 200 first-year students each semester. University leadership proposes using AI to identify students who are likely to experience serious academic difficulty. Available information includes:
- Admission scores
- Previous academic records
- Programme of study
- Course enrolment
- Attendance
- Weekly quizzes
- Assignment submissions
- Learning-platform activity
- Financial-aid information
- Midterm grades
- Final grades
- Withdrawal records Tutoring can begin at the end of week 3, week 6, or after the midterm examination. The existing process relies on voluntary student requests and faculty referrals. Some students may not seek help because of stigma, lack of awareness, or scheduling constraints. Task Complete the following problem-framing worksheet: At [decision time], for [target population or unit], using only [available information], produce [required output] concerning [prediction horizon or outcome period], so that [decision-maker] can [action]. The system will be compared with [baseline] and evaluated using [metrics], while accounting for [error costs, subgroup risks, operational constraints, and governance requirements]. After completing the statement, explain:
- Why the selected decision time is operationally appropriate.
- Which variables are available at that time.
- Which variables would cause temporal leakage.
- How serious academic difficulty should be defined.
- Whether the output should be a class, probability, ranking, or recommendation.
- How the 200-student capacity limit affects the decision rule.
- The consequences of false positives and false negatives.
- Which student groups require separate performance analysis.
- How students should be informed about the system.
- Whether students should be able to decline, appeal, or request human review.
- How the system should be compared with voluntary requests and faculty referrals.
- What evidence would justify deployment.
:::

:::question A6. Complete the problem-framing worksheet for tutoring allocation and answer the follow-up questions.
:::solution Answer


Completed statement: At [the end of week 3 of the semester, before tutoring begins], for [every first-year student enrolled on the census date (one student is the unit of analysis)], using only [information recorded by the end of week 3: admission scores, previous academic records, programme of study, course enrolment, attendance in weeks 1 to 3, weekly quizzes 1 to 3, assignment submissions due by week 3, learning-platform activity in weeks 1 to 3, and financial-aid information as recorded at enrolment], produce [a calibrated probability of serious academic difficulty, a ranked list, and an uncertainty flag for borderline or incomplete records] concerning [the remainder of the semester, from week 3 to the release of final results], so that [the academic-support office, with faculty advisers] can [offer the 200 intensive-tutoring places to the highest-ranked students after human review, with lighter support (study-skills workshops, peer mentoring) for the next band]. The system will be compared with [the current process of voluntary requests and faculty referrals] and evaluated using [recall@200, precision@200, calibration and AUROC, reported overall and by subgroup], while accounting for [the higher cost of missing a struggling student, stigma from being flagged, fairness across financial-aid, programme, gender and first-generation groups, the hard limit of 200 places, and governance requirements including student notice, opt-out, appeal, human review and monitoring].

- Why week 3 is operationally appropriate: early enough that most of the semester remains for tutoring to change the outcome (the horizon must match the window to act), yet late enough to have real behavioural signals (attendance, first quizzes and submissions). After the midterm the model would be more accurate but "accurate but operationally unhelpful": students may already have failed half the assessments. A defensible variant: allocate about 150 places at week 3 and hold 50 for a week-6 re-scoring of students who start to struggle.
- Variables available at week 3: admission scores, previous academic records, programme, course enrolment, attendance (weeks 1 to 3), weekly quizzes 1 to 3, assignment submissions to date, learning-platform activity to date, financial-aid status at enrolment.
- Variables that cause temporal leakage: midterm grades (after week 3 unless the index time is post-midterm), final grades (the outcome itself), withdrawal records (part of the outcome), attendance, quizzes, submissions and platform activity after week 3, and any financial-aid change made later (for example aid lost due to poor grades).
- Defining serious academic difficulty: Y = 1 if, by the end of the semester, the student fails one or more core first-year courses, or withdraws after the census date, or ends the term with a GPA below the academic-probation threshold. Students who leave for non-academic reasons (medical leave) are recorded separately, and missing outcomes are not coded as 0.
- Output type: a calibrated probability used to produce a ranking (not a hard class), because a fixed capacity of 200 makes this ranking under a budget; probabilities also let the team assign lighter support tiers and show unmet need. Recommendations (tutoring vs workshop) follow from risk tiers.
- Effect of the 200-student limit: the decision rule is top-200 by p̂ after review (k = 200), so the effective threshold is the p̂ of the 200th student; add a minimum risk floor so places are not wasted on low-risk students; send students near the cut-off or with incomplete records for human review.
- False positives: a place goes to a student who would have passed, displacing someone who needed it; possible stigma and wasted tutor time. False negatives: a struggling student gets no support and fails or drops out; this is more costly and harder to reverse, so recall@200 is the primary metric.
- Groups needing separate analysis: financial-aid recipients vs non-recipients; programme of study; gender; first-generation students; international and non-native speakers; students with disabilities; commuting or working students; admission route; and intersections. Report selection rate, recall and calibration with sample sizes and confidence intervals.
- Informing students: tell all students at orientation that early-warning analytics are used, what data are used, and that the goal is support, not punishment; invitations should be framed positively ("you have been offered free tutoring") and kept confidential.
- Decline, appeal, human review: yes. Students may decline tutoring without penalty; students not selected can request support (voluntary route remains open); any student can ask for human review of their data; faculty advisers make the final allocation and can override with a logged reason.
- Comparison with voluntary requests and faculty referrals: compare on the same historical cohorts (temporal validation) which approach captures more students who later had serious difficulty (recall@200), and check whether the model finds students who do not seek help because of stigma or awareness. Ideally run a pilot comparing outcomes of students selected by each route, and randomize among borderline students to estimate the causal effect of tutoring.
- Evidence to justify deployment: better recall@200 than referrals on temporal validation; good calibration; no subgroup with much worse recall; a prospective silent run; evidence from a pilot that tutoring improves outcomes for flagged students; a model card, notice and appeal process in place; monitoring plan approved.
:::
:::


### A7: Identifying Possible Failures in an AI Project (Automated Recruitment Screening)

:::origc A7 (Module 1 notes)
A7: Identifying Possible Failures in an AI Project Scenario: Automated Recruitment Screening A technology company develops an AI system to rank job applicants. The project has the following characteristics:
- The objective is stated as finding the best applicants.
- Historical hiring decisions are used as ground-truth labels.
- Most previous hires came from five universities.
- Applicants without conventional employment histories are underrepresented.
- Postal code, name, university, and employment gaps are included as features.
- Resume information submitted after the interview is included in the training records.
- All applicant records from the same year are randomly divided into training and testing sets.
- The model achieves 96 percent accuracy.
- Accuracy is the only reported metric.
- No comparison is made with the existing recruiter-review process.
- The model has not been tested on applications from another country or a later hiring year.
- Recruiters receive only a ranked list and no uncertainty information.
- The top ten applicants are highlighted in green.
- Recruiters usually review only the highlighted applicants.
- Applicants cannot request an explanation or appeal.
- The model is automatically retrained every six months using the latest hiring decisions.
- No monitoring is performed for subgroup performance, drift, override rates, or feedback loops.
- No individual or committee has formal responsibility for model governance. Task Conduct an end-to-end failure analysis. Identify possible failures associated with:
- Problem definition.
- Target and label selection.
- Data provenance.
- Historical bias.
- Proxy variables.
- Population representativeness.
- Temporal leakage.
- Train-test splitting.
- Evaluation metrics.
- External and temporal validation.
- Calibration and uncertainty.
- Model interpretability.
- Interface design.
- Automation bias.
- Human workflow.
- Appeals and procedural fairness.
- Feedback loops.
- Selective labels.
- Retraining.
- Monitoring.
- Accountability and governance.
- Legal, ethical, and organizational constraints. For every failure identified, explain:
- Why it is a failure
- Which stage of the AI pipeline it affects
- The harm it could produce
- How it could be detected
- How it should be prevented or mitigated Conclude with one of the following recommendations and defend it:
- Proceed to a controlled pilot
- Redesign the project before any pilot
- Replace the machine-learning approach with a simpler process
- Cancel the project because the proposed use is not justified
:::

:::question A7. Conduct an end-to-end failure analysis and recommend proceed, redesign, replace or cancel.
:::solution Answer


| Failure (pipeline stage) | Why it is a failure | Harm | Detection | Prevention / mitigation |
|---|---|---|---|---|
| Problem definition (formulation) | "Find the best applicants" is undefined: best at what job, measured how, over what horizon? No decision-maker or action defined. | Model optimizes an arbitrary proxy; no way to judge success | Framing review; cannot complete the worksheet | Define the decision (who is interviewed), job-relevant criteria and outcome |
| Target and label selection (formulation/data) | Historical hiring decisions record past recruiter preferences, not quality (status quo bias). | Reproduces past bias at scale | Audit labels vs job performance; adverse-impact analysis | Use a validated job-relevant outcome, or narrow to verified requirements |
| Data provenance (data) | Unknown how past decisions were made, by whom, under which policies. | Hidden bias and policy changes baked in | Provenance review, datasheet | Document sources; datasheet; exclude unreliable periods |
| Historical bias (data) | Most hires from five universities; past discrimination in labels. | Candidates from other universities excluded | Selection rates by university and group | Rebalance, remove biased labels, human review |
| Proxy variables (representation) | Postal code, name, university and employment gaps encode socioeconomic status, ethnicity, gender (gaps for caregiving) and disability. | Indirect discrimination; legal liability | Proxy tests: predict protected attributes from features; ablations | Remove or justify each feature with a job analysis; fairness testing |
| Population representativeness (data) | Non-traditional applicants under-represented. | Model is unreliable and unfair for them | Subgroup sample sizes and performance | Collect more data; abstain for out-of-distribution applicants |
| Temporal leakage (representation) | Résumé information submitted after the interview is in the training records. | Inflated accuracy; fails at screening time | Check timestamps and availability time | Snapshot features at application time only |
| Train-test splitting (evaluation) | Random split within the same year: same roles, recruiters and possibly duplicate applicants on both sides (group and temporal leakage). | Over-optimistic results | Compare with temporal split | Split by time (train on earlier years, test on later) and by applicant |
| Evaluation metrics (evaluation) | Accuracy alone (96%) with imbalance (few hires) can be achieved by rejecting almost everyone. | Misleading success claims | Report precision, recall, AUROC, selection rates | Pre-registered metrics incl. subgroup and calibration |
| External and temporal validation (evaluation) | Not tested on another country or later year. | Fails when deployed elsewhere or later | External and temporal holdouts | Validate before any use; restrict scope |
| Calibration and uncertainty (evaluation/decision) | No uncertainty shown; scores may be overconfident. | Small, meaningless score gaps decide careers | Calibration curves; intervals | Show confidence; abstain on low confidence |
| Model interpretability (model) | No explanations of rankings. | Recruiters cannot spot proxies; applicants cannot contest | Explanation audits | Interpretable model or stable explanations |
| Interface design (deployment) | Top ten highlighted in green; ranked list only. | Nudges acceptance; others invisible | Invitation rates by colour/rank | Show full pool, remove colour ranking, show uncertainty |
| Automation bias (human workflow) | Recruiters trust the list without checking. | Errors pass unchecked | Override rates (very low = rubber-stamping) | Training, required independent review, logged reasons |
| Human workflow (deployment) | Recruiters review only highlighted applicants. | Human oversight is nominal | Workflow audits | Mandatory review of a wider pool; staffing |
| Appeals and procedural fairness (governance) | Applicants cannot get an explanation or appeal. | Unchallengeable, possibly unlawful decisions | Complaints, legal review | Notice, explanation, appeal and human re-review |
| Feedback loops (monitoring) | Model-selected hires become new training data. | Bias amplified over time | Track selection concentration over retrains | Counterfactual logging; do not retrain on own selections |
| Selective labels (data/monitoring) | Outcomes only observed for those hired. | Rejected groups never get positive labels | Compare exposure vs outcomes | Random audits of rejected applicants; better labels |
| Retraining (lifecycle) | Automatic six-monthly retraining with no validation gate. | Worse or more biased versions deployed | Version comparison | Model validation gate; human approval; rollback |
| Monitoring (monitoring) | No monitoring of subgroups, drift, overrides or loops. | Silent failures and discrimination | (Absence itself) | Multi-dimensional monitoring dashboard |
| Accountability and governance (governance) | No person or committee responsible. | No one can stop harm (NIST Govern failure) | Governance review | Named accountable owner, committee, audits |
| Legal, ethical, organizational constraints | Possible violation of anti-discrimination and data-protection law; reputational risk. | Lawsuits, fines, loss of trust | Legal and ethics review | Compliance review before any pilot; model card; impact assessment |


Recommendation: Redesign the project before any pilot.


A controlled pilot is not justified now, because the core problems are in the foundations: the objective is undefined, the label encodes historical bias, proxies and post-interview leakage contaminate the features, the evaluation (random split, accuracy only, no baseline, no external or temporal validation) cannot support any claim, and there is no governance or appeal. Piloting would expose real applicants to discrimination and generate more biased data through the feedback loop. Cancelling outright is not necessary if a legitimate need exists (screening a large volume of applications), and a simpler process may be part of the redesign (for example, structured rule-based checks of verified requirements plus human review). The redesigned project must: define the decision and a job-relevant outcome; remove proxies and leaked features; use temporal and external validation with subgroup, calibration and baseline comparison against recruiter review; redesign the interface (full pool, uncertainty, no green highlighting); add notice, explanation and appeal; stop automatic retraining; add monitoring; and assign a named accountable owner. Only then should it proceed to a silent, then advisory, controlled pilot.

:::
:::


## Last-minute revision (Module 1)


### 9.1 What is most likely to come


Based on how the notes and the practice set are built, these are the highest-probability quiz items:

- Produce or critique an artifact: a problem-framing worksheet, a Model Card (heart-disease template), a Datasheet, or a failure analysis. Know the section headings by heart.
- Spot the flaw in a scenario: temporal leakage, train-serving mismatch, proxy encoding, feedback loop and selective labels, aggregation bias, random split for a temporal claim, accuracy-only evaluation, automation bias from interface design.
- Choose a model or threshold: explain why the most accurate model is not always the best (loan and predictive-maintenance examples), and how C(t), capacity and asymmetric costs set t.
- Definitions and comparisons: symbolic vs statistical, prediction vs causal reasoning, discrimination vs calibration, autonomy vs intelligence, AI vs ML vs DL vs data science, generative vs discriminative, the four Russell-Norvig views, the four autonomy levels, NIST Govern-Map-Measure-Manage.
- Case studies: Google Flu Trends, Epic Sepsis Model, TFX, Obermeyer (cost as proxy), predictive policing.
- One question from your assignment or notebook: RYDA index time and leakage, why ranking with k = 300, WePrep subgroup gaps and recommendation, datasheet suitability, résumé feedback loop and neutralization debt, MLP forward pass by hand, Bayes posterior, O(N) vs O(1).

### 9.2 One-line answers to memorize


| If asked... | Say... |
|---|---|
| Where must an AI project start? | With the decision or capability, not the algorithm or dataset. |
| What makes a feature legal to use? | It is recorded and available at or before the index time. |
| Why not a random split? | For temporal claims it leaks the future; use temporal validation (train past, test future). |
| Why not accuracy alone? | It ignores asymmetric costs, calibration, subgroups, imbalance, baselines and decision utility. |
| Discrimination vs calibration? | Ranking positives above negatives vs predicted probabilities matching observed frequencies. |
| Why probabilities over hard labels? | They keep uncertainty and let the threshold follow costs and capacity. |
| How to set t? | Minimize C(t) = c_FP·P(FP∣t) + c_FN·P(FN∣t) + c_delay·E[D∣t] + c_workflow(t), within capacity, fairness and human review. |
| Capacity-limited allocation? | Rank and take the top k; evaluate with precision@k and recall@k. |
| Train-serving mismatch? | Different preprocessing in training vs production (median vs 0 imputation). |
| Proxy encoding? | Neutral features (postal code, university) encode protected attributes. |
| Feedback loop in ranking? | Past exposure → observed interaction → training data → future exposure. |
| Selective labels? | Outcomes only observed for cases the system (or people) chose to look at. |
| Why optimization is blind? | It solves the specified objective; it cannot validate the target, sample, loss or ethics. |
| Autonomy vs intelligence? | Thermostat: autonomous, not intelligent. LLM: intelligent, no agency. |
| Socio-technical layers? | Model, Data Infrastructure, Interface, Human Workflow, Institutional Rules. |
| NIST functions? | Govern (accountability), Map (identify risks), Measure (assess), Manage (act). |
| Model Card sections? | Overview; Data Description; Performance Metrics (incl. subgroups, fairness); Known Limitations; Intended and Inappropriate Uses; Ethical Considerations; Additional Considerations (future work). |
| Datasheet sections? | Motivation; composition; collection process; preprocessing; recommended uses; limitations (plus maintenance). |
| 8 pipeline stages? | Problem, Data, Representation, Model, Evaluation, Decision, Deployment, Monitoring (iterative). |
| 8 failure modes? | Wrong problem, poor data, leakage, weak evaluation, underspecification, distribution shift, ignored workflow, no monitoring. |
| Leakage types? | Target, temporal, group, preprocessing, label, benchmark contamination. |
| Occam's razor? | A heuristic: avoid unnecessary complexity, not necessary complexity (TB + arthritis). |
| Google Flu Trends lesson? | Volume does not remove measurement bias; proxies drift; anchor to ground truth; keep lineage. |
| Epic Sepsis lesson? | External validation; label must match the event; timing matters; alert volume is a system metric. |
| TFX lesson? | A training script is not a production system; schemas, validation, shared transforms, lineage, model validation. |


### 9.3 Common traps

- Writing "the AI decided" instead of naming the human and institutional choices behind it.
- Using a default threshold of 0.5 without justification.
- Saying "high accuracy, so deploy" without calibration, subgroups, baseline and workflow.
- Forgetting exclusions, the unit of analysis, and the horizon in a problem statement.
- Treating missing or unobserved outcomes as negatives.
- Assuming high risk means high benefit from an intervention (a causal question).
- Forgetting the recommendation line at the end of a Model Card or failure analysis.

### 9.4 Numbers worth remembering from the notes

- Epic Sepsis: AUROC 0.63; 18% of hospitalizations alerted; 67% of sepsis cases missed at score ≥ 6; 183 cases found before timely antibiotics.
- Google Flu Trends: overestimated in 100 of 108 weeks; more than 2× CDC in February 2013; about 50 million terms vs 1,152 observations; combined model MAE 0.232 vs 0.486 (GFT) and 0.311 (lagged CDC).
- Loan example: DNN 94% vs logistic regression 91% with 15 features; about 50,000 applications per year.
- Baggage screening: t = 0.4 gives 96% accuracy but breaks the checkpoint; t = 0.7 gives 94% and minimizes C(t).
- Readmission example: random split 85% vs temporal 68%; AUC 0.82 overall vs 0.55 for non-English speakers; 80% predicted vs 35% observed.
- Notes' Model Card example: accuracy 85%, precision 0.80, recall 0.75, F1 0.77; male recall 0.78 vs female 0.70.
- A2 scenario: accuracy 86%, precision 0.82, recall 0.74, F1 0.78; male recall 0.80, female 0.62, under-40 0.55.

Good luck with the quiz.
