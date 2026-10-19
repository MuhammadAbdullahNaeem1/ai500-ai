# ------------------------------------------------------------------------------------------- #
# Course    :   AI 500 Computational Tutorial
# Topic     :   10 - Units, labels and consistency checks
#
# Purpose   :   The purpose of this code is to identify duplicate records and potential 
#               entity-resolution problems in a dataset containing hospital encounters. It 
#               checks for exact duplicate rows, repeated encounter IDs, the number of 
#               encounters per patient, and records that share the same patient, hospital, 
#               and admission timestamp. This helps detect data-quality issues and possible 
#               duplicate hospital visits.
#
# Run       :   python .\topic_10_units_labels_and_consistency_checks.py
#
# Date      :   October 17, 2026
# ------------------------------------------------------------------------------------------- #

from tutorial_common                    import (load_data, clean_basic_categories, 
                                                convert_weight_to_kg, section)

# ------------------------------------------------------------------------------------------- #
def run():
    section("TOPIC 10 — Units, labels and consistency checks")
    
    df                  = load_data()

    # .value_counts() counts how often each distinct value occurs.
    # dropna = False includes missing values (NaN) in the counts.
    # To identify inconsistent labels, such as "Male", "male", "M", or missing values.
    print("Raw sex labels:")
    print(df["sex_raw"].value_counts(dropna = False).head(12))
    
    print("\nRaw smoking labels:")

    # Counts the occurrences of each smoking-status value, including missing values.
    print(df["smoking_status_raw"].value_counts(dropna = False).head(12))

    clean               = clean_basic_categories(df)
    print("\nClean sex labels:")

    # Counts the occurrences of each cleaned category.
    # Includes missing values in the counts.
    print(clean["sex_clean"].value_counts(dropna = False))

    clean               = convert_weight_to_kg(clean)
    print("\nConverted weight_kg summary:")

    # Summarize the converted weights.
    print(clean["weight_kg"].describe())

    # Suspect records after conversion
    suspect             = ~clean["weight_kg"].between(30, 250)
    print("\nPotential unit/coding problems:")
    print(clean.loc[suspect,
                    ["encounter_id","weight_value","weight_unit","weight_kg","height_cm"]].head(15))

# ------------------------------------------------------------------------------------------- #
if __name__ == '__main__':
    run()

# ------------------------------------------------------------------------------------------- #