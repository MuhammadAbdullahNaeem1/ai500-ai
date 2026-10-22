# M2 · Notes-exact definitions

Every key definition in Module 2 **in the exact words of the notes** (checked word-for-word against the notes PDF). Sir prioritizes the notes' wording — when a question says *define*, write the sentence below first, then add the mechanism and an example from the notes.

<div class="pdf-links">
<a href="quiz2-guide.html">Quiz 2 guide</a>
<a href="m2a-notes.html">Notes A</a>
<a href="m2b-notes.html">Notes B</a>
<a href="m2c-notes.html">Notes C</a>
<a href="pdfs/notes/Module-2-Notes.pdf">Module 2 notes (PDF)</a>
</div>

## 2.1 Data as a constructed record of reality

| Term | Notes wording | § |
|---|---|---|
| **Raw data** | The phrase raw data is a dangerous oxymoron. | 2.1 |
| **Data are produced, not found** | Every dataset is actively produced through a long chain of subjective, technical, and systemic choices. | 2.1.1 |
| **Datasheet (purpose)** | A datasheet rigorously documents a dataset’s underlying motivation, composition, collection mechanics, preprocessing steps, intended uses, distribution, and maintenance … | 2.1.1 |
| **Fitness for purpose** | There is no such thing as a universally good or high-quality dataset in a vacuum. A dataset is only good for a specific purpose under specific conditions. | 2.1.2 |
| **Data as a map** | Data is not a flawless mirror reflecting reality; it is a constructed map. | 2.1.2 |
| **Wrong target** | Accurate prediction of the wrong target is failure. | 2.11.2 |

## 2.2 Data sources and their inherent realities

| Term | Notes wording | § |
|---|---|---|
| **Surveys** | Surveys collect information by prompting respondents with structured or semi-structured questions … | 2.2.1 |
| **Coverage error** | The sampling frame misses parts of the target population. | 2.2.1 |
| **Sampling error** | The selected sample differs from the population purely by chance. | 2.2.1 |
| **Nonresponse bias** | Respondents differ systematically from those who refuse to participate. | 2.2.1 |
| **Recall bias** | Inaccurate memory of past events. | 2.2.1 |
| **Social-desirability bias** | Respondents provide answers they believe are socially acceptable rather than truthful. | 2.2.1 |
| **Instrument effects** | Responses shift based on question wording, sequencing, or cultural/linguistic translation. | 2.2.1 |
| **Survey AI implication** | A model trained on survey data may learn response behavior rather than the intended construct … | 2.2.1 |
| **Sensors** | Sensors convert physical phenomena into recorded digital signals … | 2.2.2 |
| **Sensor takeaway** | Sensor data may appear highly objective, but the physical instrument and the acquisition process fundamentally shape what is observed. | 2.2.2 |
| **Platform as measurement** | Observed web behavior is not a direct measure of stable human preference. It is a reaction within an engineered environment, defined by a combination of user, interface, ranking algorithm, moderation, and platform incentives. | 2.2.3 |
| **Logs** | Logs are automated records produced by software systems, applications, networks, and devices … | 2.2.4 |
| **Log limitation** | A logged event only proves that software recorded something – not necessarily that the real-world event happened exactly as interpreted. | 2.2.4 |
| **Event time** | When the real-world action actually occurred. | 2.2.4 |
| **Recording time** | When the local system logged it. | 2.2.4 |
| **Arrival time** | When it reached the central data pipeline. | 2.2.4 |
| **Processing time** | When the pipeline actually handled it. | 2.2.4 |
| **Administrative records** | Administrative records are generated to support organizational operations, not scientific research … | 2.2.5 |
| **Administrative data** | Administrative data encodes institutional behavior not objective reality. | 2.2.5 |
| **Administrative formulation** | Observed outcome is a function of Underlying Condition, Access, Policy, and Institutional Practice. | 2.2.5 |
| **Controlled experiments** | Controlled experiments deliberately assign or manipulate conditions to estimate causal effects. | 2.2.6 |
| **Experiments takeaway** | Experimental data is not automatically unbiased. | 2.2.6 |
| **Attrition** | Attrition is the loss of participants from a research study before it is completed … | 2.2.6 fn |
| **Public datasets** | Public datasets are released for research, education, benchmarking, or policy use … | 2.2.7 |
| **Provenance (footnote)** | Provenance refers to the documented origin, history, and chain of custody of a dataset … | 2.2.7 fn |
| **Synthetic data** | Synthetic data consists of artificially generated observations designed to mimic the statistical properties of real data. | 2.2.8 |
| **Fidelity** | Does it preserve relevant distributions and relationships? | 2.2.8 |
| **Utility** | Does it actually support the intended analysis or model training? | 2.2.8 |
| **Privacy (synthetic)** | Can original individuals be inferred or reconstructed? | 2.2.8 |
| **Fairness (synthetic)** | Are subgroup properties preserved appropriately without amplifying bias? | 2.2.8 |
| **Coverage** | Are rare but critical edge cases represented? | 2.2.8 |
| **Realism** | Do the generated combinations obey real-world domain constraints? | 2.2.8 |

## 2.3 Data quality

| Term | Notes wording | § |
|---|---|---|
| **Completeness** | Completeness measures whether all required data is actually present. | 2.3.1 |
| **Accuracy** | Accuracy measures how closely recorded values correspond to the true or accepted reference values. | 2.3.2 |
| **Accuracy caution** | Agreement within a database does not, by itself, establish correctness. | 2.3.2 |
| **Consistency** | Consistency asks whether data values agree logically across formats, records, systems, and established rules. | 2.3.3 |
| **Timeliness** | Timeliness concerns whether data is sufficiently current and available exactly when it is needed for a decision. | 2.3.4 |
| **Freshness** | How old the underlying information actually is. | 2.3.4 |
| **Latency** | The delay between the real-world event occurring and the data becoming available in the system. | 2.3.4 |
| **Update frequency** | How often the values are refreshed. | 2.3.4 |
| **Validity period** | How long a specific data point remains operationally relevant. | 2.3.4 |
| **Representativeness** | Representativeness asks whether the data adequately reflects the intended target population and the actual operating conditions of deployment. | 2.3.5 |
| **Measurement error** | Measurement error is the fundamental difference between an observed value and the true underlying construct or quantity it is intended to measure. | 2.3.6 |
| **Construct validity** | The most dangerous measurement error occurs before the instrument is even used: the chosen variable simply does not measure the intended concept. | 2.3.6 |

## 2.4 Data profiling and curation

| Term | Notes wording | § |
|---|---|---|
| **Data curation** | Data curation is the systematic process of acquiring, organizing, validating, documenting, preserving, and maintaining data to ensure that they remain accurate, accessible, and suitable for their intended purposes throughout their lifecycle. | 2.4 |
| **Data cleaning (vs curation)** | Data cleaning focuses primarily on identifying and correcting errors, inconsistencies, and missing values. | 2.4 |
| **Data profiling** | Data profiling examines the statistical and structural characteristics of a dataset to identify potential quality issues before cleaning begins. | 2.4.4 |
| **Validation** | Validation determines whether the dataset satisfies predefined structural, logical, and domain-specific requirements. | 2.4.5 |
| **Immutable raw data** | Data cleaning must never overwrite raw data without absolute traceability. | 2.4.6 |

## 2.5 Data cleaning

| Term | Notes wording | § |
|---|---|---|
| **Data cleaning** | Data cleaning is the process of identifying, investigating, and correcting errors, inconsistencies, and quality issues that may compromise the reliability of a dataset. | 2.5 |
| **Missing values** | Missing values occur when one or more observations are unavailable. | 2.5.1 |
| **MCAR** | Under MCAR, the probability of missingness is unrelated to either observed or unobserved data. | 2.5.1 |
| **MAR** | Here, missingness may depend on observed variables but not on the missing values themselves after conditioning on the observed data. | 2.5.1 |
| **MNAR** | Under MNAR, the probability of missingness continues to depend on the unobserved values even after accounting for observed information. | 2.5.1 |
| **Mechanisms are assumptions** | These mechanisms describe assumptions about the data-generating process rather than properties that can usually be verified directly from the dataset. | 2.5.1 |
| **Imputation without leakage** | imputation parameters must be estimated using only the training data and then applied unchanged to validation and test datasets. | 2.5.1 |
| **Outlier** | An outlier is an observation that differs substantially from the expected pattern of the data. | 2.5.2 |
| **Outlier handling** | outliers should be investigated rather than automatically removed. | 2.5.2 |
| **Cleaning principle** | Data cleaning should remove errors, not meaningful complexity. | 2.5.2 |
| **Duplicate records** | Duplicate records occur when multiple entries represent the same observation or entity. | 2.5.3 |
| **Exact duplicates** | Exact duplicates are identical across all relevant fields. | 2.5.3 |
| **Near duplicates** | Near duplicates differ only slightly because of spelling variations, formatting differences, timestamps, abbreviations, or minor recording inconsistencies. | 2.5.3 |
| **Entity resolution** | Entity resolution seeks to determine whether multiple records refer to the same underlying entity. | 2.5.3 |
| **False merges / false splits** | false merges (combining different entities) and false splits (failing to combine identical entities) … | 2.5.3 |
| **Majority voting** | Majority voting provides a practical method for producing consensus labels but may suppress legitimate expert disagreement or overlook genuinely ambiguous cases. | 2.5.3 |
| **Class imbalance** | Class imbalance occurs when one or more classes are substantially less frequent than others. | 2.5.4 |
| **Resampling rule** | Resampling should therefore be performed only within the training partition or within each training fold during cross-validation … | 2.5.4 |
| **Balancing vs prevalence** | Balancing the training data improves learning but does not alter the underlying frequencies of events in real-world applications. | 2.5.4 |
| **Platt scaling** | Platt scaling is performed by training a logistic regression model on a classifier's output scores (not the original features) to convert those scores into calibrated probabilities. | 2.5.4 |

## 2.6 Data leakage

| Term | Notes wording | § |
|---|---|---|
| **Data leakage** | Data leakage occurs when information that would not legitimately be available at the intended prediction or evaluation time is inadvertently used during model development. | 2.6.1 |
| **Leakage test question** | Could this feature, preprocessing statistic, or related record genuinely be available in the same form at the time a prediction is made for a new observation? | 2.6.1 |
| **Target leakage** | Target leakage occurs when one or more input features directly or indirectly reveal the outcome that the model is intended to predict. | 2.6.2 |
| **Train–test contamination** | Train-test contamination occurs when information from the evaluation dataset influences model development, parameter estimation, or model selection. | 2.6.3 |
| **Temporal leakage** | Temporal leakage occurs when information from the future is used to predict an earlier outcome. | 2.6.5 |
| **Availability time** | The relevant timestamp is the moment at which the information became available, not necessarily when the underlying event occurred. | 2.6.5 |
| **Group leakage** | Group leakage occurs when related observations from the same entity appear in multiple data partitions. | 2.6.6 |

## 2.7 Data documentation

| Term | Notes wording | § |
|---|---|---|
| **Data dictionary** | A data dictionary provides field-level documentation describing the meaning, structure, and interpretation of individual variables. | 2.7.2 |
| **Data provenance** | Data provenance describes the origin of data and the processes used to generate them. | 2.7.3 |
| **Data lineage** | Data lineage records how data evolve as they move through processing pipelines. | 2.7.3 |
| **Consent documentation** | Consent should not be represented merely as a binary indicator such as consent obtained: Yes/No. | 2.7.4 |
| **Data license** | A data license specifies the conditions under which a dataset may be accessed, used, modified, or redistributed. | 2.7.5 |
| **Copyright vs privacy** | Legal permission to access a dataset does not automatically mean that every possible use is acceptable. | 2.7.6 |
| **Consent vs licensing** | Consent explains what participants agreed to, while licensing defines what users are legally permitted to do with the data. | 2.7 Ex. 57 |

## 2.8 Governance and ethics

| Term | Notes wording | § |
|---|---|---|
| **Data governance** | Data governance is the framework of policies, roles, processes, and technical controls through which data are managed, protected, and used throughout their lifecycle. | 2.8.1 |
| **Privacy** | Privacy concerns an individual's ability to control, understand, and be protected from inappropriate collection, processing, inference, sharing, or disclosure of information about them. | 2.8.2 |
| **De-identification** | de-identification should be viewed as a risk-reduction strategy rather than a guarantee of anonymity. | 2.8.3 |
| **Data minimization** | Data minimization is the principle that organizations should collect, retain, and process only the information reasonably necessary to achieve a clearly defined and legitimate purpose. | 2.8.5 |
| **Sensitive attributes** | Sensitive attributes are variables whose misuse may expose individuals to discrimination, privacy violations, or other forms of harm. | 2.8.6 |
| **Removing sensitive attributes** | Excluding a sensitive variable from a predictive model does not necessarily prevent discriminatory outcomes. | 2.8.6 |
| **Fairness** | Fairness is a context-dependent concept that cannot be adequately characterized by a single universal metric. | 2.8.8 |
| **Demographic parity** | Predicted positive rates are equal across groups. | 2.8.8 |
| **Equal opportunity** | True positive rates are equal across groups. | 2.8.8 |
| **Equalized odds** | Equalized odds require equality of both true positive rates and false positive rates across demographic groups. | 2.8.8 |
| **Predictive parity** | The probability that a positive prediction is correct is equal across groups. | 2.8.8 |
| **Secondary use** | The technical ability to access data does not by itself justify new uses. | 2.8.9 |
| **Data owner** | Holds formal authority and ultimate responsibility for the data resource. | 2.8.11 |
| **Data steward** | Maintains data definitions, quality standards, documentation, metadata, and access policies. | 2.8.11 |
| **Data custodian** | Manages the technical infrastructure supporting data storage, security, backup, and access. | 2.8.11 |
| **Data producer** | Creates, measures, or collects the original observations. | 2.8.11 |
| **Data consumer** | Uses the data for research, analysis, reporting, or predictive modeling. | 2.8.11 |
| **Model owner** | Assumes responsibility for the development, deployment, monitoring, and operational performance of predictive models. | 2.8.11 |

## 2.9–2.11 Misleading datasets and case studies

| Term | Notes wording | § |
|---|---|---|
| **True construct** | The true construct is the concept that the project seeks to predict, but it is often difficult or impossible to observe directly. | 2.9.1 |
| **Wrong target** | Accurate prediction of the wrong target is failure. | 2.11.2 |

:::remember
Definition in the notes' words → mechanism → example from the notes. That is the order Quiz 1's rubric rewarded.
:::
