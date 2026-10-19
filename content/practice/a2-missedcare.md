# Assignment 2 — MissedCare, Part A (Module 2 theory)

Assignment 2 Section 1 (50 points) is **pure Module 2**: constructing the dataset, synthetic data, data-quality flaws, missingness, leakage, and short calculations (outliers, contamination, metrics, fairness). Below are the questions and **your submitted answers** from the PA2 notebook — re-read them before Quiz 2; Quiz 2 has no numericals, but the reasoning parts (A1, A2, A4, A5) are exactly Quiz-2 style.

<div class="pdf-links">
<a href="pdfs/assignments/Assignment-2.pdf">Assignment 2 (PDF)</a>
<a href="pdfs/assignments/Assignment-2-Coding-Guide.pdf">Coding guide (Part B)</a>
<a href="files/26280047_Naeem_PA2.ipynb">Your PA2 notebook (.ipynb)</a>
<a href="assignments.html">All assignments</a>
</div>

:::orig The MissedCare scenario
Public health clinics in Vitória (Espírito Santo, Brazil) lose about one appointment in five to no-shows. Proposal: *"Build an AI model that runs every evening and produces a list of the patients who are most likely to miss their appointment the next day, so that clinic staff can phone them first."* Data: April–June 2016, ~110,000 appointments by ~62,000 patients — patient ID, gender, age, clinic neighbourhood, Bolsa Família enrolment, hypertension, diabetes, alcoholism, disability, SMS reminder sent, booking date-time, appointment date, and **No-show** ("Yes" = missed).
:::


## **A1. Build the dataset in your head (8 marks)**

> **📖 Read:** 2.1 Data as a Constructed Record of Reality, especially 2.1.1 Data are produced, not simply found, 2.1.2 Fitness for Purpose (Q(D,T,C)) and Example 38, Predicting student dropout risk **pp. 173–179.**
>

### **A1.1 Target definitions (2 marks)**

Write three different definitions of "no-show". For each one, give the label of a patient who arrives **40 minutes late** (1 = no show, 0 = showed up).

**Your answer:**

| # | Definition of "no-show" (one sentence) | Label for the 40-minutes-late patient (0 or 1) |
|---|---|---|
| 1 | Strict/administrative, which is that the patient did not arrive for check-in by the scheduled start time (no grace period). | 1 |
| 2 | Grace-period rule, that is the patient did not arive within 15 minutes of the scheduled time, so the slot was released to someone else. | 1 |
| 3 | Clinical-encounter rule, meaning the patient was never seen by a clinician that day, regardless of how late they arrived. | 0 (if the clinic still saw them) |

### **A1.2 Variables (2 marks)**

Choose 4 variables to include and 2 to exclude. For each one, write Relevance, Privacy or Reliability as the reason type, then give a one line reason.

**Your answer:**

| Decision | Variable | Reason type | Reason (one line) |
|---|---|---|---|
| Include | Lead time, which is days between booking and appointment | Relevance | Longer waits give more time for plans to change and are a known strong driver of missed appointmnets. |
| Include | Patient's own prior no-show history (computed only from *earlier* appointments) | Relevance | Past behaviour is one of the best predictors of future attendance and is known at prediction time. |
| Include | SMS reminder sent (0/1) | Relevance | an intervention that the clinic controls and can act on, and that may change attendance. |
| Include | Age | Reliability | recorded routinely at registration, has few missing values and relates to attendance patterns. |
| Exclude | Full name, phone number or exact home address | Privacy | Directly identifying and adds no predictive value beyond coarser features such as neighbourhood. |
| Exclude | Self-reported alcoholism flag | Reliability | Heavily under-reported and recorded inconsistantly, so the flag reflects disclosure habits more than the condition. |

### **A1.3 Sampling (1 mark)**

The data come only from public clinics in one city

**Your answer:**

| | |
|---|---|
| Who is missing from the data? | patients of private clinics and insurance-based care. people in other cities and rural areas of Brazil, and people who never book an appointment at all (e.g. those who face access barriers). |
| one deployment where this would matter | deploying the call-list model in a rural municipality or a private hospital network. travel distances, income and booking habits differ there, so the learned patterns may not transfer and risk scores would be miscalibrated. |

### **A1.4 What could "NA" mean? (1 mark).**

Suppose `SMS_received` is blank for some rows. Give three different realities that the blank could stand for.

**Your answer:**

| # | What the blank could mean |
|---|---|
| 1 | No SMS was sent (it could be that the field was simply left empty instead of being recorded as 0). |
| 2 | An SMS was sent, but the delivery log was lost or never writen (such as a system outage or failed export). |
| 3 | SMS was not applicable: the patient has no mobile number on file or opted out of reminders. |

### **A1.5 Same name, different meaning (1 mark)**

Clinic A marks a no-show after 15 minutes. Clinic B marks it only if the patient never arrives. What goes wrong if their data are merged? Answer in 2–3 lines.

**Your answer**

The label `No-show = Yes` would mean two different things in the same column. a Clinic A patient who came 20 minutes late counts as a no-show, but the same patient at Clinic B counts as attended. the merged target is therefore inconsistent, so the model learns clinic-specific recording rules (and clinic can act as a proxy for the label) instead of real patient behaviour, and Clinic A will look artificially worse. the definitions must be harmonised to one rule, using arrival times if availble, before the data are combined.

### **A1.6 Fit for purpose? (1 mark)**

Is this dataset fit for each use?

**Your answer**

| Use | Fit? (Yes / No) | Reason (one line) |
|---|---|---|
| (i) Monthly attendance report | Yes | It is descriptive counting of recorded appointments over April–June, which the data cover well (with the caveat of only three months). |
| (ii) Tomorrow's call list | Partly / with conditions | It can work only if features are restricted to information available the evening before (no post-appointment fields) and the model is validated on later dates. |
| (iii) One national model for all of Brazil | No | the data come from public clinics in a single city, so they do not represent other regions, rural areas or private care. |
| (iv) Proving that SMS reminders *cause* attendance | No | This is observational data. SMS was not randomly assigned (e.g. it is sent mainly for appointments booked well in advance), so confounding prevents causal claims. |

## **A2. Synthetic data (3 marks)**

> **📖 Read:** 2.2.8 Synthetic Data (its uses, risks and validation dimensions), Example 43 and Table 6. **pp. 195–199.**
>

### **A2(a) (2 marks)**

Name two risks of sharing the synthetic copy. For each risk, name the validation dimension that would catch it. Choose one of: Fidelity, Utility, Privacy, Fairness, Coverage, Realism.

**Your answer:**

| # | Risk (one line) | Validation dimension |
|---|---|---|
| 1 | Re-identification, which is that the generator may memorise and also reproduce near-copies of real patients (especially rare combinations such as a 102-year-old in a small neighbourhood). | Privacy |
| 2 | The synthetic data may not preserve the real relationships (e.g. lead time vs no-show, age vs no-show), so the vendor's scheduling product is tuned on false patterns. | Fidelity (checked in practice by Utility, such as train on synthetic, test on real) |

### **A2(b) (1 mark)**

Statement: *"It's synthetic, so it's anonymous."*

**Your answer**

| True / False | Justification (one line) |
|---|---|
| False | Synthetic records can still leak information about real patients through memorised near-duplicates, or it could be rare outliers or membership inference, so privacy must be tested, not assumed. |

## **A3. Spot the flaw (10 Marks)**

> **📖 Read:**
> - 2.3 Data Quality, the six dimensions, **pp. 200–213** (Example 44 is a close model for this question)
> - 2.5.2 Outliers, **pp. 222–226**
> - 2.5.3 Duplicate records, Inconsistent labels, Inter-annotator agreement, Unit-aware schemas, **pp. 226–231**
> - 2.5.4 Class imbalance, **pp. 232–234**
>




<br>

| # | AppointmentID | PatientId | Gender | Age | Weight_kg | Neighbourhood | ScheduledDay | AppointmentDay | SMS | No-show |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 5642903 | 2.98725e+13 | F | 62 | 71 | JARDIM DA PENHA | 2016-04-29 | 2016-04-29 | 0 | No |
| 2 | 5642503 | 558997776694438 | M | 56 | 80 | JARDIM DA PENHA | 2016-04-29 | 2016-04-29 | 0 | No |
| 3 | 5642549 | 4262962299951 | Female | 8 | 27 | MATA DA PRAIA | 2016-04-29 | 2016-04-29 | 0 | No |
| 4 | 5642828 | 867951213174 | f | N/A | 64 | PONTAL DE CAMBURI | 2016-04-27 | 2016-04-29 | 0 | No |
| 5 | 5642494 | 8841186448183 | F | 34 | 154 | JARDIM DA PENHA | 2016-04-29 | 2016-04-29 | 0 | No |
| 6 | 5626772 | 95985133231274 | F | 76 |  | REPÚBLICA | 2016-04-27 | 2016-04-29 | 0 | Yes |
| 7 | 5630279 | 733688164476661 | M | 23 | 78 | GOIABEIRAS | 2016-04-27 | 2016-04-29 | 0 | Yes |
| 8 | 5630279 | 733688164476661 | M | 23 | 78 | GOIABERAS | 2016-04-27 | 2016-04-29 | 0 | Yes |
| 9 | 5633460 | 12154843752835 | M | -1 | 3.2 | CONQUISTA | 2016-04-28 | 2016-04-29 | 0 | No |
| 10 | 5650093 | 78124564369297 | F | 115 | 58 | ANDORINHAS | 2016-05-03 | 2016-04-29 | 1 | No |
| 11 | 5634718 | 3449833394123 | F | 38 | 65 | NOVA PALESTINA | 2016-04-26 | 2016-04-29 | 1 | 1 |
| 12 | 5639264 | 2263865652 | male | 19 | 70 | SANTO ANDRÉ | 2016-04-26 | 2016-04-29 | 1 | No |

### **A3(a) (7 Marks).**

List every issue you can find. There are at least 12. Give each issue its own row, and add rows if you need them.
- **Quality dimension:** choose one of Completeness, Accuracy, Consistency, Timeliness, Representativeness, Measurement error.
- **Row(s):** write "All" if the issue affects the whole table.

**Your answer:**

| # | Row(s) | Issue (what is wrong) | Quality dimension | Fix (what you would do) |
|---|---|---|---|---|
| 1 | 1 | `PatientId` is stored in scientific notation like (2.98725e+13), so digits are lost and the ID cannot be matched to other rows. | Accuracy | Store IDs as strings/int64 and re-export from the source system. |
| 2 | All | `PatientId` has inconsistent lengths/formats (10 to 15 digits, some floats), which suggests IDs were truncated or cast differently. | Consistency | define an ID schema (fixed type and length) and validate every row against it. |
| 3 | 3, 4, 12 | Gender is coded inconsistently: `Female`, `f`, `male` alongside `F`/`M`. | Consistency | Map all variants to a controlled vocabulary {F, M}. |
| 4 | 4 | Age is `N/A` (a missing value hidden as a text string). | Completeness | Convert to a true NaN, recover it from the patient's other records if possible, or flag it and impute. |
| 5 | 5 | Weight 154 kg for a 34-year-old stands out and could be a unit error (lb vs kg) or a typing error. | Measurement error | Check the source/unit. flag it as a suspect outlier instead of silently deleting it. |
| 6 | 6 | `Weight_kg` is blank. | Completeness | Treat as NaN, add a missing-indicator and use a suitable imputation (or leave missing if weight is not needed). |
| 7 | 7, 8 | Same `AppointmentID` and patient appear twice, so it is a duplicate record (one copy has a spelling variant). | Accuracy (duplicate) | De-duplicate on `AppointmentID`, keeping the version with the valid neighbourhood name. |
| 8 | 8 | Neighbourhood mispelt `GOIABERAS` instead of `GOIABEIRAS`. | Consistency | Validate against the official neighbourhood list and correct misspellings with fuzzy matching. |
| 9 | 9 | Age = −1 is an impossible value (and weight 3.2 kg only fits a newborn). | Accuracy | Treat −1 as a code (e.g. an infant under 1 year / unknown), decode it to age 0, and document the rule. |
| 10 | 10 | `ScheduledDay` (2016-05-03) is *after* `AppointmentDay` (2016-04-29), so the booking happens after the appointment. | Consistency | Flag rows with negative lead time. verify the timestamps or exclude them from the analysis. |
| 11 | 10 | Age 115 is implausible (and a weight of 58 kg is not decisive either way). | Accuracy | Check against date of birth. set to NaN if it cannot be verified. |
| 12 | 11 | Target `No-show` = `1` while all other rows use `Yes`/`No`. | Consistency | Map the target to one encoding (Yes/No, then 1/0) and confirm what `1` meant in the source. |
| 13 | All (esp. 9) | `Weight_kg` is recorded at different precisions (whole kg in most rows, 3.2 in row 9), which suggests different scales or protocols at the triage desk. | Measurement error | Record the instrument and protocol, standardise the precision, and store units in the schema. |
| 14 | All | Date columns are dates only. the booking *time* and the appointment time are lost, so the same-day lead time (e.g. rows 1–3, 5) cannot be measured precisly. | Timeliness | Keep the full timestamps from the source system. |
| 15 | All | Every appointment is on 2016-04-29 (one day) and from a few neighbourhoods. the sample does not represent the whole period or city. | Representativeness | Sample across dates and neighbourhoods. do not draw conclusions from this extract alone. |

### **A3(b) (1 mark).**

Row 9 has an age of −1 and a weight of 3.2 kg.

**Your answer:**

| Decision (*Delete as error* / *Decode as a code*) | Reasoning (one line) |
|---|---|
| Decode as a code | A weight of 3.2 kg is exactly what a newborn weighs, so −1 is most likely a system code for "under 1 year old" (an infant), and deleting it would systematically remove babies from teh data. |

### **A3(c) (2 marks).**

Two receptionists independently coded the reason for 50 missed appointments as "patient-side" or "clinic-side". They agreed on 40. Receptionist 1 chose "patient-side" 30 times. Receptionist 2 chose it 28 times.

Working (show p_o, p_e and κ; see footnote 221 on p. 229 for Cohen's κ):

**Your answer**

**Working:**

- Observed agreement: $p_o = 40/50 = 0.80$
- Receptionist 1: patient-side $= 30/50 = 0.60$, clinic-side $= 20/50 = 0.40$
- Receptionist 2: patient-side $= 28/50 = 0.56$, clinic-side $= 22/50 = 0.44$
- Chance agreement: $p_e = (0.60)(0.56) + (0.40)(0.44) = 0.336 + 0.176 = 0.512$
- $\kappa = \dfrac{p_o - p_e}{1 - p_e} = \dfrac{0.80 - 0.512}{1 - 0.512} = \dfrac{0.288}{0.488} = 0.59$

| Quantity | Value |
|---|---|
| Observed agreement p_o | 0.80 |
| Chance agreement p_e | 0.51 |
| Cohen's κ | 0.59 |
| Interpretation (one line) | Moderate agreement: much of the raw 80% agreement is what chance alone would produce, so the labels are only moderately reliable. |
| Why a majority vote would not guarantee the true reason (one line) | Receptionists share the same information and biases (they never talk to the patient about why they missed), so a majority can agree on the same wrong reason. agreement measures consistency, not truth. |

## **A4. Why is it missing? (9 marks)**

> **📖 Read:** 2.5.1 Missing values, pp. 218–222. Focus on:
> - the three mechanisms MCAR, MAR and MNAR, with Examples 45–47 (pp. 219–220)
> - Approaches to handling missing values and Model-based imputation, especially the Caution about lactate and footnote 212 (pp. 221–222)
>




<br>

**The cases: (3 marks each)**
1. A server outage wiped the SMS logs for three randomly timed afternoons.
2. `HbA1c` is recorded only when a doctor suspects poorly controlled diabetes. A teammate wants to fill the blanks with a KNN imputer.
3. `Neighbourhood` is blank for patients who have no fixed address.

**Your answer:**

| Case | Mechanism | Handling strategy | Justification (one line) |
|---|---|---|---|
| 1 | MCAR | Complete-case analysis (drop the affected rows) or simple imputation, and record the outage. | The outage timing is random and unrelated to patients or attendance, so the remaining rows are an unbiased sample and only statistical power is lost. |
| 2 | MNAR | Do not impute the value. add a binary indicator `HbA1c_measured`, keep the value where present, and use domain knowledge or a sensitivity analysis. | Whether HbA1c is missing depends on the (unobserved) level of diabetes control itself, so the fact that it was *measured* is informative in its own right. |
| 3 | MNAR | Keep the rows and code the blank as its own category, e.g. `No fixed address`, plus a missing-indicator. | The missingness is caused by the patient's housing situation, which is itself linked to attendance, so dropping or imputing would erase a vulnerable group. |

**Case 2, extra line (counts toward case 2's 3 marks):** Why would the KNN imputer be a mistake here?

**Your answer**

**Answer:**

KNN imputation assumes the missing values resemble those of similar patients who *were* tested (i.e. MAR), but here the patients with a recorded HbA1c are exactly the ones suspected of poor control. the imputer would therefore fill untested, probably well-controlled patients with high, "poorly controlled" values borrowed from tested patients. this creates fake clinical information and distorts the distribution. it also throws away the informative signal that *no test was ordered*.

## **A5. Find every leak (8 marks)**

> **📖 Read:** 2.6 *Data Leakage*, pp. 239–248. Focus on:
> - 2.6.2 Target leakage, and Example 54 on sepsis (p. 240)
> - 2.6.3 Train–test contamination (pp. 241–242)
> - 2.6.4 Cross-validation variants (pp. 242–244)
> - 2.6.5 Temporal leakage (pp. 244–245)
> - 2.6.6 Group leakage, and Example 55 on churn (pp. 245–247)
> - 2.6.7 Site leakage (p. 247)
> - 2.6.8 the prevention checklist (pp. 247–248)
>
> **What to do:** A teammate reports **AUC = 0.97** from the pipeline below. Find the leak in each step.




 <br>

**The pipeline:**
1. For each patient, `past_noshow_rate` is the share of **all** of that patient's appointments in the file that were missed.
2. `reminder_call_outcome` is added. Staff log this the day *after* the appointment.
3. StandardScaler and SMOTE are run on the full dataset, and then 5-fold `KFold` is used.
4. Many patients have 10 or more appointments, and they appear in both training and validation folds.
5. The model will be deployed next in a different city, but it was tested only on Vitória's neighbourhoods.
<br>

### **A5(a) (5 marks).**

For each step, name the leakage type (Target, Train-test contamination, Temporal, Group or Site) and give the fix. A step can have more than one type.

**Your answer**

| Step | Leakage type | Fix (one line) |
|---|---|---|
| 1 | Target leakage + Temporal leakage | Compute `past_noshow_rate` only from the patient's appointments *before* the current appointment date (an expanding window that excludes the current row). |
| 2 | Target leakage (Temporal) | Drop `reminder_call_outcome`. it is recorded the day after the appointment, so it is not available when the call list is produced the evening before. |
| 3 | Train–test contamination | Put StandardScaler and SMOTE inside an (imblearn) pipeline that is fitted only on each training fold. never oversample the validation/test data. |
| 4 | Group leakage | Split by patient (`GroupKFold` / `StratifiedGroupKFold` on `PatientId`) so all of a patient's appointments are in the same fold. |
| 5 | Site leakage | Evaluate on held-out sites (leave-neighbourhood-out), and validate on data from the new city before deployment, recalibrating if neccessary. |

### **A5(b) (3 marks)**

Which pipeline step does each evaluation setup fix?

**Your answer**

| Evaluation setup | Step(s) it fixes | Why (one line) |
|---|---|---|
| `StratifiedGroupKFold` | Step 4 (and it helps step 1) | Groups by `PatientId` so the same patient never appears in both training and validation, while keeping the no-show ratio similar in every fold. |
| `TimeSeriesSplit` | Steps 1 and 2 (temporal) | Always trains on earlier appointments and validates on later ones, which mirrors deployment and exposes features that use future information. |
| Neighbourhood hold-out | Step 5 | Tests the model on neighbourhoods it never saw during training, which estimates how it will perform at a new site such as a different city. |

## **A6. Crunch the numbers (12 marks)**

> **What to do:** Show your working in each **Working** box, then fill in the result table. Round to 2 decimal places.

### **6.1 Outliers in waiting time (3 marks)**

> **📖 Read:** 2.5.2 Outliers: z-score and IQR on p. 223 (with footnote 213), and the Box-Cox and shifted Box-Cox transforms on pp. 224–225 (Table 18).

Data (`wait_days` for 11 appointments): **0, 0, 1, 2, 3, 4, 6, 7, 10, 14, 60**

<br>

**(a) IQR rule (1.5 marks).**

Use linear interpolation, as `np.percentile` does.

**Your answer**

**Working:**

Sorted data ($n = 11$): 0, 0, 1, 2, 3, 4, 6, 7, 10, 14, 60. with linear interpolation the position of the $p$-th percentile (0-indexed) is $(n-1)p$.

- Q1: position $10 \times 0.25 = 2.5$ → between $x_{(2)} = 1$ and $x_{(3)} = 2$ → $1 + 0.5(2-1) = 1.5$
- Q3: position $10 \times 0.75 = 7.5$ → between $x_{(7)} = 7$ and $x_{(8)} = 10$ → $7 + 0.5(10-7) = 8.5$
- IQR $= 8.5 - 1.5 = 7$
- Lower fence $= 1.5 - 1.5(7) = 1.5 - 10.5 = -9$
- Upper fence $= 8.5 + 1.5(7) = 8.5 + 10.5 = 19$
- Only 60 lies outside [−9, 19].

| Q1 | Q3 | IQR | Lower fence | Upper fence | Points flagged |
|---|---|---|---|---|---|
| 1.50 | 8.50 | 7.00 | −9.00 | 19.00 | 60 |

**(b) z-score rule (1.5 marks)**

Using the sample standard deviation (divisor n − 1), compute the z-scores of 14 and 60. Which values does the rule |z| > 3 flag?

**Your answer**

**Working:**

- Mean: $\bar x = 107 / 11 = 9.73$
- $\sum x^2 = 4011$, so $\sum (x-\bar x)^2 = 4011 - 107^2/11 = 4011 - 1040.82 = 2970.18$
- Sample variance $s^2 = 2970.18 / 10 = 297.02$ → $s = 17.23$
- $z(14) = (14 - 9.73)/17.23 = 0.25$
- $z(60) = (60 - 9.73)/17.23 = 2.92$
- No value has $|z| > 3$: the outlier 60 inflates both the mean and the SD, so it hides itself (the masking effect).

| Mean | Sample SD | z(14) | z(60) | Values flagged |
|---|---|---|---|---|
| 9.73 | 17.23 | 0.25 | 2.92 | None |

### **6.2 A leak you can calculate (3 marks)**

> **📖 Read:** 2.6.3, Preprocessing contamination: μ_train vs μ_all, pp. 241–242.

**(a) (1.5 marks).** The training-set ages are **20, 30, 40, 50** and the test-set ages are **80, 90**. Use the population SD (divide by n), as `StandardScaler` does.

**Your answer**

**Working:**

(a) Training data only (20, 30, 40, 50):
- $\mu = 140/4 = 35$
- $\sigma^2 = [(-15)^2 + (-5)^2 + 5^2 + 15^2]/4 = 500/4 = 125$ → $\sigma = 11.18$
- $z(90) = (90 - 35)/11.18 = 4.92$

(b) All six patients (20, 30, 40, 50, 80, 90):
- $\mu = 310/6 = 51.67$
- $\sigma^2 = [31.67^2 + 21.67^2 + 11.67^2 + 1.67^2 + 28.33^2 + 38.33^2]/6 = 3883.33/6 = 647.22$ → $\sigma = 25.44$
- $z(90) = (90 - 51.67)/25.44 = 1.51$

| Method | Mean | SD | Standardized value for age 90 |
|---|---|---|---|
| (a) Training data only | 35.00 | 11.18 | 4.92 |
| (b) All six patients (leaky) | 51.67 | 25.44 | 1.51 |

**(b) (1.5 marks).** Why does the leaky value look "tamer"? Answer in one line.

**Your answer**

**Answer:**

The test patients' own ages pull the mean up and widen the SD, so the scaler has already "seen" the test data. age 90 then looks ordinary (1.51) instead of far outside the training range (4.92), which hides the distribution shift the model will face.

### **6.3 Why accuracy lies (3 marks)**

> **📖 Read:** §2.5.4, Why accuracy can be misleading (p. 232) and Platt scaling, with Examples 53–54 (pp. 235–237).

The test set has 1,000 appointments, of which 200 were missed. The model flags 210 patients, and 120 of them really do miss.

**(a) (2 marks).** Fill in the model's confusion counts, then the metrics.

**Your answer**

Working: TP = 120 (flagged and missed), FP = 210 − 120 = 90, FN = 200 − 120 = 80, TN = 1000 − 120 − 90 − 80 = 710.
Baseline: predicts no one misses → accuracy = 800/1000 = 0.80, recall = 0/200 = 0.
Model: accuracy = (120 + 710)/1000 = 0.83; precision = 120/210 = 0.57; recall = 120/200 = 0.60.

| TP | FP | FN | TN |
|---|---|---|---|
| 120 | 90 | 80 | 710 |

| Model | Accuracy | Precision | Recall |
|---|---|---|---|
| Baseline ("always shows up") | 0.80 | n/a | 0.00 |
| Your model | 0.83 | 0.57 | 0.60 |

**(b) (1 mark).** Using P(miss) = 1 / (1 + exp(A·s + B)) with A = −2, B = 1.5 and s = 1:

**Your answer**

**Working:**

- $A s + B = (-2)(1) + 1.5 = -0.5$
- $\exp(-0.5) = 0.6065$
- $P(\text{miss}) = 1/(1 + 0.6065) = 1/1.6065 = 0.62$

| P(miss) |
|---|
| 0.62 |

### **6.4 Fairness from counts (3 marks)**

> **📖 Read:** 2.8.8 Fairness, with the metric definitions and Example 62 (pp. 266–267).

| | Appointments | Missed | Flagged | Flagged *and* missed |
|---|---|---|---|---|
| Women | 600 | 150 | 150 | 90 |
| Men | 400 | 50 | 60 | 30 |

**(a) (1.5 marks).** Compute each metric for each group.

**Your answer**

**Working:**

- Women: TP = 90, FP = 150 − 90 = 60, positives = 150, negatives = 600 − 150 = 450.
  PPR = 150/600 = 0.25; TPR = 90/150 = 0.60; FPR = 60/450 = 0.13; PPV = 90/150 = 0.60.
- Men: TP = 30, FP = 60 − 30 = 30, positives = 50, negatives = 400 − 50 = 350.
  PPR = 60/400 = 0.15; TPR = 30/50 = 0.60; FPR = 30/350 = 0.09; PPV = 30/60 = 0.50.

| Group | Positive prediction rate | TPR | FPR | PPV |
|---|---|---|---|---|
| Women | 0.25 | 0.60 | 0.13 | 0.60 |
| Men | 0.15 | 0.60 | 0.09 | 0.50 |

**(b) (1.5 marks).** Which criteria hold?
Give a one-line justification for each.

**Your answer**

| Criterion | Holds? (Yes / No) | Evidence (which numbers) |
|---|---|---|
| Demographic parity | No | Positive prediction rates differ: 0.25 for women vs 0.15 for men. |
| Equal opportunity | Yes | TPRs are equal: 0.60 for both groups. |
| Equalized odds | No | TPRs match, but FPRs differ (0.13 vs 0.09), and equalized odds needs both to match. |
| Predictive parity | No | PPVs differ: 0.60 for women vs 0.50 for men. |


