# ------------------------------------------------------------------------------------------- #
# Course    :   AI 500 Computational Tutorial
# Topic     :   4 - Schema and data validation
#
# Purpose   :   Check the quality and reliability of healthcare data before using it for 
#               machine learning or clinical prediction. It ensures that patient records are 
#               reasonably complete, values fall within expected ranges, timestamps are 
#               consistent, and encounter IDs are unique.
#
# Install   :   conda install -c conda-forge pandera-pandas
#
# Run       :   python .\topic_04_schema_and_data_validation.py
#
# Date      :   October 10, 2026
# ------------------------------------------------------------------------------------------- #

import pandera.pandas                   as pa                           # Pandera is an open-source data validation framework designed to verify data structures at runtime.

from tutorial_common                    import load_data, section

# ------------------------------------------------------------------------------------------- #
def run():

    section("TOPIC 04 — Schema and data validation")

    df              = load_data()

    # Define the data quality checks
    checks          = {"required encounter_id present"  : df["encounter_id"].notna().all(),                                             # Check that encounter IDs are present.
                       "age in plausible range"         : df["age_years"].between(0, 120).all(),                                        # Check whether age is plausible.
                       "oxygen saturation 0-100"        : df["oxygen_saturation_pct"].between(0, 100).all(),                            # Check oxygen saturation.
                       "prediction after admission"     : (df["prediction_timestamp"] >= df["admission_timestamp"]).all(),              # Check timestamp order: prediction after admission.
                       "arrival after recording"        : (df["data_arrival_timestamp"] >= df["vitals_recorded_timestamp"]).all(),      # Check timestamp order: data arrival after vital recording.
                       "encounter_id unique"            : ~df["encounter_id"].duplicated().any(),}                                      # Check whether encounter IDs are unique.

    # Print the validation results.
    # These checks only report problems. 
    # They do not automatically correct the data or stop the program when a check fails.

    for name, passed in checks.items():                             # checks.items() returns each dictionary key and value.
                                                                    # name stores the descriptive name of the check.
                                                                    # passed stores its Boolean result.
        print(f"{name:38s}: {'PASS' if passed else 'FAIL'}")        # f-string formats the output.
                                                                    # :38s means to display the string in a field 38 characters wide, padding it with spaces if necessary.

    # Identify rows with suspicious physiological measurements.
    print("\nRows violating selected physiological ranges:")        # ~ means logical NOT for a Boolean Pandas Series.
    physiological   = (~df["heart_rate_bpm"].between(30, 250) |     # | means element-wise logical OR.
                       ~df["temperature_c"].between(30, 45) |
                       ~df["systolic_bp_mmHg"].between(40, 300))

    # Display the flagged rows.
    # df.loc[...] selects rows and columns by label.
    print(df.loc[physiological,                                     # physiological selects only rows flagged by the previous expression.
                 ["encounter_id",
                  "heart_rate_bpm",
                  "temperature_c",
                  "systolic_bp_mmHg"]].head(10))                    # .head(10) displays at most the first 10 matching rows.

    # Validate the data using Pandera.
    try:
        # Define the schema.
        # Defines two column-level rules: Rule 1 is Age and Rule 2 is Deterioration label.
        # pa.Column(...) defines a column specification.

        schema      = pa.DataFrameSchema({"age_years"               : pa.Column(int, pa.Check.in_range(0, 120)),
                                          "deterioration_within_12h": pa.Column(int, pa.Check.isin([0, 1])),})

        # Select the columns to validate. 
        # This creates a smaller DataFrame containing only the two columns defined in the schema.
        # The schema is therefore not validating every column in the original DataFrame.
        
        # .validate() method checks whether the selected DataFrame satisfies the schema.
        # lazy = True tells Pandera to collect validation failures rather than stopping at 
        # the first failed check. It can report multiple issues together.
        
        schema.validate(df[["age_years","deterioration_within_12h"]], lazy = True)

        print("\nPandera core-schema validation: PASS")

    except Exception as exc:
        print("\nPandera optional validation skipped or found issues:", type(exc).__name__)

# ------------------------------------------------------------------------------------------- #
if __name__ == '__main__':
    run()

# ------------------------------------------------------------------------------------------- #