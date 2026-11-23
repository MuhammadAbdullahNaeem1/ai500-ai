# ------------------------------------------------------------------------------------------- #
# Course    :   AI 500 Computational Tutorial
# Topic     :   Clinical Data Preprocessing and Patient-Level Train-Test Splitting for 
#               Deterioration Prediction
#
# Purpose   :   This code prepares a clinical dataset for a machine learning model that predicts 
#               whether a patient will experience clinical deterioration within the next 12 hours. 
#               It cleans duplicate records, processes features, prevents data leakage using 
#               timestamps, validates clinical measurements, and splits data into training and 
#               testing sets while keeping each patient's encounters together.
#
# Install   :   pip install pandas scikit-learn
#
# Date      :   November 13, 2026
# ------------------------------------------------------------------------------------------- #

"""Load and prepare the synthetic encounter dataset for 1-hour prediction."""
import numpy                    as np
import pandas                   as pd

from pathlib                    import Path

# Imports GroupShuffleSplit from Scikit-learn.
# It is used to divide the dataset into training and testing sets based on groups.
# In this code, patients are treated as groups so that records belonging to the same patient cannot appear in both sets.
from sklearn.model_selection    import GroupShuffleSplit

# ------------------------------------------------------------------------------------------- #
# Defining the Target Variable and Features.

# Defines the target variable that the machine learning model will predict.
# deterioration_within_12h indicates whether a patient experiences clinical deterioration within 12 hours.
# 1 = Patient experiences deterioration within 12 hours.
# 0 = Patient does not experience deterioration within 12 hours.
TARGET                  = "deterioration_within_12h"

# Defines a list of five vital-sign measurements.
# These measurements describe the patient's current physiological condition.
VITALS                  = ["heart_rate_bpm", "respiratory_rate_bpm", "temperature_c", 
                           "oxygen_saturation_pct", "systolic_bp_mmHg"]

# Defines a list of five laboratory test measurements.
# These features provide information about the patient's internal physiological and biochemical condition
LABS                    = ["creatinine_mg_dl", "sodium_mmol_l", "wbc_10e9_l", 
                           "glucose_mg_dl", "lactate_mmol_l"]

# Defines all numerical features that will be used by the machine learning model.
# The first section contains demographic, medical history, and admission-related information.
# + VITALS + LABS combines the previously defined vital-sign and laboratory feature lists with these variables.
NUMERIC                 = ["age_years", "socioeconomic_quintile", "diabetes", "hypertension",
                           "chronic_kidney_disease", "copd", "height_cm", "weight_kg",
                           "previous_admissions_12m", "days_since_prior_discharge",
                           "admission_hour", "admission_month"] + VITALS + LABS

# Defines the categorical features.
# Categorical features represent groups, labels, or classifications rather than continuous numerical measurements.
# These features may require encoding (such as one-hot encoding) before being used by many machine learning algorithms.
CATEGORICAL             = ["hospital_id", "region_type", "sex", "preferred_language",
                           "insurance_type", "smoking_status", "admission_type", "bp_device_model"]

# Combines all numerical and categorical features into a single list.
# This list represents the complete set of input variables used by the prediction model.
# [Very Important] The target variable is not included in this list.
FEATURES                = NUMERIC + CATEGORICAL

# ------------------------------------------------------------------------------------------- #
# Loading and Removing Duplicate Records.
# Deduplicate exact and near-duplicate encounters; retain one record per encounter.
def load_csv(path):
    # low_memory = False instructs Pandas to process the file without performing low-memory, 
    # chunk-based type inference, which can help avoid inconsistent column data types.
    
    # [Use it] when:
    # - working with large CSV files.
    # - encounter DtypeWarning.
    # - some columns contain mixed data types
    # - one wants more consistent data-type inference.

    df                  = pd.read_csv(path, low_memory = False)

    # Calculates the original number of rows in the dataset.
    # This is used later to report how many records were removed.
    n0                  = len(df)

    # df.drop_duplicates() removes completely identical rows from the dataset.
    # .drop_duplicates([...], ...) removes duplicate encounters based on three columns.
    # If multiple records have the same patient, hospital, and admission timestamp, only the first record is retained
    
    # keep = "first" means the first occurrence is preserved.
    # .copy() creates an independent copy of the resulting DataFrame.
    # This helps avoid unintended modifications to the original DataFrame.

    df                  = (df.drop_duplicates()
                           .drop_duplicates(["patient_id", "hospital_id", "admission_timestamp"], 
                                            keep = "first").copy())

    # Displays the number of rows before and after duplicate removal.
    # f indicates an f-string, which allows variables to be inserted into a string.
    # :, formats numbers with thousands separators.
    print(f"Loaded {n0:,} rows; kept {len(df):,} after exact/near duplicate removal.")
    
    return df

# ------------------------------------------------------------------------------------------- #
# Feature Engineering and Data Cleaning
def make_features(df):
    """
    - Generate admissible predictors using only information available at prediction time.
    - The synthetic dataset uses a single result-availability timestamp shared across all
      laboratory measurements and a single arrival timestamp shared across all vital signs.
    - Mask any values that become available after the prediction time.
    """
    # Creates a copy of the input DataFrame.
    # This prevents changes made inside the function from directly modifying the original dataset.
    df                  = df.copy()

    # Converting Timestamp Columns.
    # admission_timestamp           : Time when the patient was admitted.
    # prediction_timestamp          : Time when the model is expected to make a prediction.
    # vitals_recorded_timestamp     : Time when vital signs were recorded.
    # data_arrival_timestamp        : Time when vital-sign data became available.
    # lab_result_available_timestamp: Time when laboratory results became available.


    for c in ["admission_timestamp", "prediction_timestamp", "vitals_recorded_timestamp", 
              "data_arrival_timestamp", "lab_result_available_timestamp"]:

        # Converts the selected column into Pandas datetime format.
        # pd.to_datetime() allows the program to compare timestamps correctly.
        # errors = "coerce" converts invalid or unrecognized timestamps into NaT (Not a Time).
        # This prevents invalid timestamp strings from causing conversion errors.
        df[c]           = pd.to_datetime(df[c], errors = "coerce")

    # ------------------------------------------------------------------------------------------- #
    # Checking Whether Vital Signs Were Available at Prediction Time.

    # Extracts the prediction timestamp for every patient encounter.
    # This timestamp acts as the reference point for determining which information is available to the model.
    predicted_at        = df["prediction_timestamp"]

    # Checks whether vital-sign measurements were available before or at prediction time.
    # - Checks whether vital signs were recorded before or at prediction time.
    # - Checks whether the vital-sign data had arrived before or at prediction time.
    
    # Both conditions must be true for the vital signs to be considered valid.
    # In other words, vital signs are considered available only if they were both recorded and received by the prediction time.
    valid_vitals        = (df["vitals_recorded_timestamp"] <= predicted_at) & (df["data_arrival_timestamp"] <= predicted_at)

    # ------------------------------------------------------------------------------------------- #
    # Checking Whether Laboratory Results Were Available.
    
    # Checks whether laboratory results were available before or at prediction time.
    # If the result became available after prediction time, it is considered unavailable to the model.
    valid_labs                      = df["lab_result_available_timestamp"] <= predicted_at

    # ------------------------------------------------------------------------------------------- #
    # Masking Unavailable Measurements.
    # Prevents the model from using vital-sign information that was recorded or received after prediction time.

    # ~valid_vitals selects encounters where the vital signs are invalid or unavailable.
    # df.loc[] selects specific rows and columns.
    # VITALS selects all five vital-sign columns.
    # np.nan replaces their values with missing values.
    df.loc[~valid_vitals, VITALS]   = np.nan

    # Selects encounters where laboratory results were not available at prediction time.
    # Replaces the five laboratory measurements with NaN.
    # Prevents future laboratory results from leaking into the model's input features.
    df.loc[~valid_labs, LABS]       = np.nan

    # ------------------------------------------------------------------------------------------- #
    # Normalizing Categorical Variables.

    # .str.strip()      : Removes unnecessary spaces from the beginning and end of text.
    # .str.lower()      : Converts all text to lowercase.
    # .replace({...})   : Replaces abbreviated categories with standardized labels.
    df["sex"]               = df["sex_raw"].str.strip().str.lower().replace({"f": "female", "m": "male", "u": "unknown"})

    # Standardizes the smoking-status information.
    # Removes extra spaces and converts text to lowercase.
    # Replaces abbreviated smoking categories with understandable labels.
    df["smoking_status"]    = df["smoking_status_raw"].str.strip().str.lower().replace({"n": "never", "fmr": "former", "c": "current"})

    # Converting Weight into Kilograms.
    # Extracts the original weight values. Converts them into numerical format.
    # If a value cannot be converted into a number, it becomes NaN.
    weight                  = pd.to_numeric(df["weight_value"], errors = "coerce")

    # df["weight_unit"]             : Retrieves the unit associated with each weight measurement.
    # .str.lower()                  : Converts the unit to lowercase.
    # .ne("lb")                     : Checks whether the unit is not equal to "lb".
    # weight.where(condition, other): Keeps the original weight when the condition is true; otherwise, 
    #                                 it uses the alternative value.
    df["weight_kg"]         = weight.where(df["weight_unit"].str.lower().ne("lb"), weight / 2.2046226218)
    
    # Plausibility checks: Checking Clinical Measurement Ranges.
    # It defines acceptable minimum and maximum values for selected clinical measurements.
    # These ranges are used to identify potentially implausible measurements.
    ranges                  = {"weight_kg"              : (30, 250), 
                               "heart_rate_bpm"         : (30, 250),
                               "temperature_c"          : (30, 45), 
                               "systolic_bp_mmHg"       : (40, 300),
                               "oxygen_saturation_pct"  : (0, 100)}

    # .items() returns each feature name and its corresponding range.
    # col stores the feature name.
    for col, (lo, hi) in ranges.items():
        # df[col].between(lo, hi) checks whether each value falls within the specified range.
        # ~ reverses the condition and identifies values outside the range.
        # df.loc[...] selects those invalid values.
        # np.nan replaces them with missing values.

        # Prevents clearly implausible measurements from being treated as valid clinical data.
        df.loc[~df[col].between(lo, hi), col] = np.nan

    # Returning the Final Features. Returns only the columns listed in the FEATURES list.
    # reindex(columns = FEATURES) ensures that the output contains the required feature columns in the specified order.
    # Produces a clean feature DataFrame containing only the selected model input variables.
    
    # [Very Important] because patient_id and TARGET are not included in FEATURES, they will not 
    # be present in the returned DataFrame.
    return df.reindex(columns = FEATURES)

# ------------------------------------------------------------------------------------------- #
# Grouped Train-Test Splitting.

# [Very Important] GroupShuffleSplit uses the groups for splitting; it does not use the target 
# values to perform stratification. Consequently, the proportion of deterioration cases may 
# differ between training and testing

def grouped_split(df, seed = 500, test_fraction = 0.20):
    # Extracts the patient identifiers. Stores them in groups.
    # These identifiers tell the splitting algorithm which records belong to the same patient.
    groups                  = df["patient_id"]

    # Creates a GroupShuffleSplit object. This object is responsible for splitting the dataset based on patient groups.
    splitter                = GroupShuffleSplit(n_splits        = 1,                    # Performs one train-test split.
                                                test_size       = test_fraction,        # Assigns approximately 20% of patient groups to testing.
                                                random_state    = seed)                 # Ensures that the same split can be reproduced when the dataset and parameters remain unchanged.
    # Perform the actual split.
    # splitter.split(...)   : Generates indices for the training and testing sets.
    # df                    : The complete dataset.
    # df[TARGET]            : The target variable supplied to the splitting method.
    # groups = groups       : Specifies patient identifiers so all encounters from the same patient stay together.
    # next(...)             : Retrieves the first (and only) generated split.
    tr, te                  = next(splitter.split(df, 
                                                  df[TARGET], 
                                                  groups        = groups))

    # Creates the training and testing DataFrames using the generated indices.
    # df.iloc[tr] selects rows assigned to training. Approximately 80% of patient groups.
    # df.iloc[te] selects rows assigned to testing. Approximately 20% of patient groups.
    # .copy() creates independent copies of both datasets.
    train, test             = df.iloc[tr].copy(), df.iloc[te].copy()

    # Performs an assertion to verify that no patient appears in both datasets.
    # set(train.patient_id) creates a set of training patient identifiers.
    # set(test.patient_id) creates a set of testing patient identifiers.
    # .isdisjoint() checks whether the two sets have no elements in common.

    # If even one patient appears in both datasets, Python raises an AssertionError.
    # Acts as a safety check to ensure patient-level separation and reduce data leakage.
    assert set(train.patient_id).isdisjoint(test.patient_id)

    # Returns both datasets.
    # train is used to train the machine learning model.
    # test is used to evaluate the model's performance on previously unseen patients.
    return train, test

# ------------------------------------------------------------------------------------------- #