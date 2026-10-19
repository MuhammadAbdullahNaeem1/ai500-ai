# Assignments & computational training

Both written assignments, your submissions, and the Module 2 computational tutorial. Assignment 1 covered Module 1 (problem framing, model card, datasheet, failure analysis); Assignment 2 covers Module 2 (MissedCare) — its Part A is the closest thing to Quiz 2 practice you have already done.

<div class="pdf-links">
<a href="a2-missedcare.html">★ A2 Part A — your answers (Module 2)</a>
<a href="pdfs/assignments/Assignment-1.pdf">Assignment 1</a>
<a href="pdfs/assignments/Assignment-2.pdf">Assignment 2</a>
<a href="pdfs/tutorials/Computational-Tutorial-2026.pdf">Computational tutorial</a>
</div>

## Assignment 1 — AI Landscape and Computational Foundations

**Section 1 (80 points, theory):** P1 problem formulation (RYDA youth-unemployment, 20) · P2 model card (WePrep) · P3 datasheet (crop-disease images) · P4 failure analysis (résumé screening). **Section 2 (programming):** vectors/matrices, probability, optimization, complexity in Python.

| File | |
|---|---|
| Assignment brief | [PDF](pdfs/assignments/Assignment-1.pdf) |
| Your report (26280047) | [PDF](pdfs/assignments/Assignment-1-Report-26280047.pdf) |
| Your PA1 notebook | [.ipynb](files/26280047_Naeem_PA1.ipynb) |

## Assignment 2 — Data Collection, Curation, Cleaning, Governance & EDA (MissedCare)

**Section 1 (50 points, Module 2 theory):** A1 constructing the dataset (8) · A2 synthetic data (3) · A3 data-quality flaws + Cohen's κ (10) · A4 missingness MCAR/MAR/MNAR (9) · A5 leakage in a pipeline (8) · A6 calculations: IQR/z-scores, preprocessing contamination, accuracy vs recall, Platt scaling, fairness from counts (12). **Section 2 (50 points, programming):** dataset assessment, distributions, subgroup and intersectional no-show rates, temporal features (WaitingDays), leakage-free preprocessing.

| File | |
|---|---|
| Assignment brief | [PDF](pdfs/assignments/Assignment-2.pdf) |
| Coding guide (Part B) | [PDF](pdfs/assignments/Assignment-2-Coding-Guide.pdf) |
| Your PA2 notebook | [.ipynb](files/26280047_Naeem_PA2.ipynb) |
| Your Part A answers, readable | [A2 Part A page](a2-missedcare.html) |

## Computational training — Module 2 in code

Synthetic multi-hospital deterioration dataset (~250,000 encounters, 118,000 patients, 8 hospitals, 2021–2026): predict deterioration in the next 12 h using only information available 1 h after admission. Leakage fields: ICU transfer, rapid-response activation, discharge disposition, length of stay. ([Tutorial PDF](pdfs/tutorials/Computational-Tutorial-2026.pdf) · [data dictionary](files/computational/AI500_synthetic_multihospital_data_dictionary.csv) · [shared helpers](files/computational/tutorial_common.py))

| # | Topic | Notes section | Script |
|---|---|---|---|
| 1 | Data acquisition from heterogeneous sources | 2.2 | [py](files/computational/topic_01_data_acquisition_from_heterogeneous_sources.py) |
| 2 | Initial dataset inventory | 2.4.3 | [py](files/computational/topic_02_initial_dataset_inventory.py) |
| 3 | Automated data profiling | 2.4.4 | [py](files/computational/topic_03_automated_data_profiling.py) |
| 4 | Schema and data validation | 2.4.5 | [py](files/computational/topic_04_schema_and_data_validation.py) |
| 5 | Data-quality dimensions | 2.3 | [py](files/computational/topic_05_data_quality_dimensions.py) |
| 6 | Missing-data investigation | 2.5.1 | [py](files/computational/topic_06_missing_data_investigation.py) |
| 7 | Missing-value treatment | 2.5.1 | [py](files/computational/topic_07_missing_value_treatment.py) |
| 8 | Outlier and anomaly investigation | 2.5.2 | [py](files/computational/topic_08_outlier_and_anomaly_investigation.py) |
| 9 | Duplicates and entity resolution | 2.5.3 | [py](files/computational/topic_09_duplicate_and_entity_resolution_problems.py) |
| 10 | Units, labels and consistency checks | 2.5.3 | [py](files/computational/topic_10_units_labels_and_consistency_checks.py) |
| 11 | Class imbalance | 2.5.4 | [py](files/computational/topic_11_class_imbalance.py) |
| 12 | Split before preprocessing | 2.6.3 | [py](files/computational/topic_12_train_validation_test_splitting_before_preprocessing.py) |
| 13 | Data-leakage demonstration | 2.6 | [py](files/computational/topic_13_data_leakage_demonstration.py) |
| 14 | Cross-validation appropriate to data structure | 2.6.4 | [py](files/computational/topic_14_cross_validation_appropriate_to_data_structure.py) |

## Python tutorials

[NumPy](files/tutorials/01_numpy_tutorial.ipynb) · [pandas](files/tutorials/02_pandas_tutorial.ipynb) · [matplotlib](files/tutorials/03_matplotlib_tutorial.ipynb) · [Colab quick-start](files/tutorials/Colab_quickstart.ipynb) · [Environment & notebook guide](files/tutorials/environment_and_notebook_guide.ipynb) · [requirements.txt](files/tutorials/requirements.txt)


## Assignment 1 — likely quiz questions about your report (from your prep guide)


Sir said one quiz question will come from the report or the notebook. This part summarizes what you submitted and gives ready answers to the questions most likely to be asked. Learn the numbers and the reasoning, not just the conclusions.


### 3.1 Report overview


| Problem | What you produced | Core concepts tested |
|---|---|---|
| 1. RYDA problem framing | Completed the Figure 6 worksheet for allocating 300 bootcamp seats; justified index time, leakage, outcome definition, capacity rule, error costs and subgroups. | Index time, horizon, temporal leakage, label definition, ranking under capacity (precision@k), C(t), subgroup analysis |
| 2. WePrep Model Card | Model card for a multimodal mock-interview emotion and "Interview Readiness" system; recommended Conditionally Approve (self-practice only). | Model card sections, subgroup performance, calibration, construct validity, appropriate vs prohibited uses, monitoring triggers |
| 3. Crop disease Datasheet | Datasheet for an 80,000-image leaf dataset; concluded it is not suitable on its own for smallholders on low-cost phones. | Datasheet sections, selection bias, proxies and shortcuts, device shift, label verification, versioning |
| 4. Résumé screening failure (2014 to 2015) | End-to-end failure analysis of the automated hiring tool; listed mandatory safeguards for a controlled pilot. | Status quo bias, proxy encoding, feedback loops, technical debt, automation bias, procedural fairness, NIST functions |


### 3.2 Likely questions from Problem 1 (RYDA worksheet)


Why did you choose "end of orientation" as the index time rather than registration or the three-month mark?


At registration the record is thin (no aptitude score) and the population is unstable, and early registration depends on internet access (the source of the first-come bias). At three months the model would be more accurate, but half of the 180-day window is gone; as the notes say about sepsis, a prediction made after the problem is visible "may be accurate but operationally unhelpful". End of orientation is the only point where all pre-intervention features exist and almost the whole horizon remains, so the horizon matches the window to act.


Which variables would cause temporal leakage in RYDA?


Interview callbacks during the job search (future information and almost a direct measure of the outcome); verified employment at six months (the label itself, target leakage); anything created after orientation (support tier received, module completion, workshop attendance, three-month status); and fields edited after the fact (updated education or skills, aptitude score recorded late). The rule: every input must be known at or before the index time, and timestamp semantics (event time vs recording time) must be checked.


How did you make "high risk of remaining unemployed" measurable?


Event: Y = 1 if the candidate is not in verified employment at day 180 (paid work of at least 20 hours a week, lasting at least four consecutive weeks, confirmed by a document). Formal, temporary, apprenticeship and freelance work count; one-off gigs and unpaid internships do not; full-time education is a separate outcome; unreachable candidates are recorded as missing, not coded 0 (the meaning of "negative"). High risk: inside the top 300 by p̂ and above a minimum floor t. Label checks: construct validity, measurement disparity (informal rural work is harder to verify), status quo bias, and the fact that high risk does not prove the bootcamp will help (a causal question).


Why is the output a ranking with k = 300 rather than a binary classifier?


With a fixed 0.5 threshold the number of positives changes every cycle (it might flag 700 people for 300 seats, or fewer than 300 and leave seats empty). The capacity constraint turns the problem into ranking under a fixed budget, evaluated with Precision@300 and Recall@300; the effective threshold is the p̂ of the 300th candidate. Calibration still matters for assigning lower tiers, showing unmet need, and judging whether the 300th and 320th candidates are really different. Borderline and incomplete records go to human review (abstention).


What are the consequences of false positives and false negatives in RYDA?


A false positive spends an expensive seat on someone who would have found work anyway, and because seats are fixed it displaces someone who needed it. A false negative leaves a vulnerable candidate with only job alerts: six more months unsupported, lost income, and a risk of long-term unemployment, which is harder to reverse. Therefore c_FN > c_FP, Recall@300 is the primary metric, and subgroups (rural vs urban, income, gender, education, intersections such as rural × female) are reported separately with sample sizes and confidence intervals.


### 3.3 Likely questions from Problem 2 (WePrep Model Card)


What did the WePrep subgroup results show, and why does 84% overall accuracy mislead?


Native English speakers 89% vs non-native 62% (27-point gap); lighter skin 87% vs darker 68% (19 points); glasses or low light 55%. The aggregate hides these gaps (aggregation bias). Errors from the speech-to-text branch and the facial branch compound for users who belong to several groups, and intersectional results were not reported.


Why is calibration a concern for WePrep even though no calibration was reported?


A CNN trained mostly on well-lit, lighter-skinned faces still produces confident outputs on dark, poorly lit or partly covered faces, because nothing tells it the input is out of distribution. Confidence stays high while accuracy falls to 55 to 68%, so the gap between confidence and accuracy is widest for the worst-served groups. The 0 to 100 Readiness score makes it worse by compressing two uncertain outputs into one precise-looking number. Remedy: reliability diagrams per subgroup and abstention ("conditions insufficient for feedback").


What was your deployment recommendation and why?


Conditionally approve, for low-stakes voluntary self-practice only: hide the numeric score until the worst subgroups reach an accuracy floor, disclose accuracy gaps before recording, make scores impossible to share with employers, abstain on low-quality input, provide a correction channel, and monitor per subgroup. Any hiring or assessment use is not approved. This mirrors the notes: "information is not automatically meaning" (a smile can signal politeness or nervousness, the facial-emotion example).


### 3.4 Likely questions from Problem 3 (Crop disease Datasheet)


Why is the dataset not suitable for smallholder farmers using low-cost phones?


Every factor deployment depends on is missing: no smallholder farms; no drought images (drought stress can look like disease); 95% high-resolution camera images vs a phone deployment (train-serving mismatch and device shift); 70% of images from two regions; 90% of labels unverified by pathologists; healthy plants under-sampled (pushes the model toward over-diagnosis); and farm backgrounds available as shortcuts. The model would be "confidently wrong rather than obviously broken", and the cost falls on the farmers least able to absorb it. It is still useful for pre-training, benchmarking and research on shift and label noise.


What shortcuts or proxies could a model learn from this dataset?


Background (soil, mulch, staking, irrigation equipment differ by farm and farms differ in disease); device characteristics; photographer framing (lesions framed closely and centrally); lighting and time of day; and resizing artifacts. Splits should be made by farm code (or plot) to avoid group leakage.


### 3.5 Likely questions from Problem 4 (Résumé screening failure)


How did the model learn to prefer men without a gender field?


The label was ten years of past hiring decisions, which records what past recruiters did (status quo bias), not candidate quality. In a male-dominated corpus the model learned what a historically successful résumé looks like, and many features correlate with gender (women's clubs, women's colleges, verbs, career gaps). A high-capacity model combines these weak signals and effectively reconstructs gender (proxy encoding).


Why was "neutralizing" specific words flawed, and what technical debt did it create?


It treats the symptom, not the cause (the label); it can never be shown to be complete; it hides the evidence, turning a visible failure into a silent one; and the list grows with every retraining. It creates hidden post-processing and configuration debt (an unversioned, ownerless list outside the model), entanglement (changing one term shifts the whole decision surface), and a monitoring gap.


Describe the feedback loop in the hiring tool.


Biased labels in → the ranking decides who is interviewed (biased exposure) → low-ranked women are never observed (selective labels) → new hires chosen under the model's influence become fresh training data → the model appears more accurate because it is evaluated on people it selected (self-confirmation).


What safeguards are mandatory for a controlled pilot?


Fix the label first (a validated, job-relevant target) and pre-register the evaluation with a stop rule; staged deployment (silent/shadow mode, then advisory with a comparison group, with rollback ready); interface controls (show the full pool with confidence and explanations, never auto-reject, log overrides with reasons); continuous monitoring and release gates (subgroup selection rates, counterfactual logging, automated model validation); procedural safeguards (notice, appeal, audit, a model card, a named accountable owner, NIST Govern-Map-Measure-Manage, and a sunset condition).


### 3.6 Notebook (PA1) — worked answers


**Problem 1: Forward pass of an MLP (one hidden layer)**


Layer rule: z = W·x + b. Hidden activation: ReLU, f(x) = max(0, x). Output activation: sigmoid, σ(x) = 1 / (1 + e^(−x)).


Input x = [0.5, −1.2, 3.0]. Hidden layer (4 neurons), b1 = [0.1, −0.1, 0.2, 0.0]:


| Neuron | W1 row · x + b1 | z1 | a1 = ReLU(z1) |
|---|---|---|---|
| 1 | 0.2(0.5) + (−0.5)(−1.2) + 0.1(3.0) + 0.1 = 0.1 + 0.6 + 0.3 + 0.1 | 1.10 | 1.10 |
| 2 | (−0.4)(0.5) + 0.8(−1.2) + (−0.2)(3.0) − 0.1 = −0.2 − 0.96 − 0.6 − 0.1 | −1.86 | 0 |
| 3 | 0.6(0.5) + 0.1(−1.2) + (−0.3)(3.0) + 0.2 = 0.3 − 0.12 − 0.9 + 0.2 | −0.52 | 0 |
| 4 | (−0.1)(0.5) + (−0.2)(−1.2) + 0.9(3.0) + 0.0 = −0.05 + 0.24 + 2.7 | 2.89 | 2.89 |


Output layer: W2 = [0.5, −0.6, 0.3, −0.1], b2 = −0.2.


z2 = 0.5(1.1) − 0.6(0) + 0.3(0) − 0.1(2.89) − 0.2 = 0.55 − 0.289 − 0.2 = 0.061


final output = σ(0.061) = 1 / (1 + e^(−0.061)) ≈ 0.5152


Matches the notebook output: a1 = [1.1, 0, 0, 2.89], final output = 0.51524527.


Why is ReLU used in the hidden layer and sigmoid at the output?


ReLU adds non-linearity cheaply (without it, stacked linear layers collapse into one linear map) and zeroes negative pre-activations (neurons 2 and 3 above are "switched off"). Sigmoid squashes the final value into (0, 1) so it can be read as a probability p̂. Link to the notes: an MLP is a deep learning model f_θ: X → Y whose parameters θ are the weights and biases; a probability output is preferable to a hard label because it keeps uncertainty and lets the threshold t be set by error costs and capacity. Note that sigmoid output is not automatically calibrated.


**Problem 2: Bayes' theorem (spam given "urgent")**


P(Spam) = 2000/10000 = 0.2     P(Not Spam) = 8000/10000 = 0.8


P("urgent") = 0.80 × 0.2 + 0.05 × 0.8 = 0.16 + 0.04 = 0.20   (law of total probability)


P(Spam | "urgent") = (0.80 × 0.2) / 0.20 = 0.16 / 0.20 = 0.80


Interpret the Bayes result. Why is the posterior (0.8) much higher than the prior (0.2)?


The word "urgent" is 16 times more likely in spam (0.80) than in non-spam (0.05), so observing it strongly updates the belief toward spam. This is the notes' view of probabilistic intelligence: "learning uncertain relationships from evidence; updating beliefs when new information becomes available; quantifying confidence". Note the base rate still matters: even with a strong signal, 20% of emails containing "urgent" are legitimate, so auto-deleting them would cause false positives (quarantining a critical client email is costly, per the notes' asymmetric-cost example). Naive Bayes extends this by multiplying likelihoods of many words under a conditional-independence assumption.


**Problem 3: List vs set lookup (algorithmic complexity)**


| Vocabulary size N | List time (s) | Set time (s) | List/Set ratio |
|---|---|---|---|
| 10,000 | 0.000163 | 0.0000027 | ~60× |
| 50,000 | 0.000967 | 0.0000032 | ~300× |
| 100,000 | 0.002044 | 0.0000034 | ~600× |
| 250,000 | 0.005821 | 0.0000041 | ~1,400× |
| 500,000 | 0.009852 | 0.0000031 | ~3,200× |


How do the curves confirm O(N) for a list and O(1) for a set?


The target is the last token, so the list must compare against every element: time grows roughly in proportion to N (500,000 costs about 60 times 10,000; a straight line through the origin). The set computes one hash and probes one bucket, so its time stays flat near the timer's resolution regardless of N.


What is the trade-off of a hash set in a memory-constrained production environment?


Memory and construction cost. The hash table is kept deliberately sparse to limit collisions, so it takes several times the list's memory, and building it requires hashing every token once. On a memory-limited edge device, a sorted array with binary search (O(log N)) may be preferable. Link to the notes: this is exactly the operational constraints criterion of model and system selection (latency, memory footprint, computational limits) and the technical and infrastructure constraints of Section 1.7.9; lower latency is not free.
