# ------------------------------------------------------------------------------------------- #
# Course    :   AI 500 Computational Tutorial
# Topic     :   9 - Duplicate and entity-resolution problems
#
# Purpose   :   The purpose of this code is to identify duplicate records and potential 
#               entity-resolution problems in a dataset containing hospital encounters. It 
#               checks for exact duplicate rows, repeated encounter IDs, the number of 
#               encounters per patient, and records that share the same patient, hospital, 
#               and admission timestamp. This helps detect data-quality issues and possible 
#               duplicate hospital visits.
#
# Run       :   python .\topic_09_duplicate_and_entity_resolution_problems.py
#
# Date      :   October 17, 2026
# ------------------------------------------------------------------------------------------- #

from tutorial_common            import load_data, section

# ------------------------------------------------------------------------------------------- #
def run():

    section("TOPIC 09 — Duplicate and entity-resolution problems")
    
    df                      = load_data()

    # Identify exact duplicate rows. Checks whether entire rows are duplicated across all columns. 
    # keep = False marks every occurrence of a duplicate row as True, including the first occurrence. 
    # The result is a boolean series stored in exact.
    exact                   = df.duplicated(keep = False)

    # Selects the encounter_id column. Checks whether encounter IDs appear more than once. 
    # keep = False marks all rows with a repeated encounter ID as True. 
    # Stores the results in dup_id.
    dup_id                  = df["encounter_id"].duplicated(keep = False)
    
    print("Rows involved in exact duplicates:", int(exact.sum()))
    print("Rows with duplicated encounter_id:", int(dup_id.sum()))

    # Display example duplicate encounter IDs.
    print("\nExample duplicate encounter IDs:")

    # To inspect duplicated encounter IDs and see whether the records refer to the 
    # same patient, hospital, and admission time.
    print(df.loc[dup_id, ["encounter_id","patient_id","hospital_id","admission_timestamp"]].head(12))

    # Count encounters per patient.
    patient_counts          = df["patient_id"].value_counts()           # value_counts() counts how many times each patient ID appears.

    # Summarize the encounter counts.
    print("\nRepeated encounters per patient:")

    # .describe() calculates summary statistics for the patient encounter counts.
    # percentiles = [.5, .9, .95, .99] requests four additional percentile values.

    # The output includes: 
    # count :Number of distinct patient IDs represented in patient_counts. 
    # mean  : Average number of recorded encounters per patient. 
    # std   : Standard deviation, which measures variation in encounter counts. 
    # min   : Smallest encounter count for any patient. 50%: Median encounter count.
    # 50%   : Median encounter count. 
    # 90%   : The 90th percentile. 
    # 95%   : The 95th percentile. 
    # 99%   : The 99th percentile.
    # max   : Largest encounter count for any patient.
    print(patient_counts.describe(percentiles = [.5, .9, .95, .99]))

    # Near-duplicate candidate key.
    # Creates a list of three columns to use together as a candidate key.
    # The combination represents a patient at a particular hospital at a particular admission time.
    # The idea is that two records sharing all three values might represent the 
    # same admission recorded more than once.
    key                     = ["patient_id","hospital_id","admission_timestamp"]
    near                    = df.duplicated(key, keep = False)

    print("Rows sharing patient-hospital-admission key:", int(near.sum()))

# ------------------------------------------------------------------------------------------- #
if __name__ == '__main__':
    run()

# ------------------------------------------------------------------------------------------- #