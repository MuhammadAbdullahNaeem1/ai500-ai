# ------------------------------------------------------------------------------------------- #
# Course    :   AI 500 Computational Tutorial
# Topic     :   2 - Initial dataset inventory
#
# Purpose   :   - This code performs an initial inventory of a dataset using pandas.
#               - It helps you understand the dataset's size, column data types, number of 
#                 encounters and patients, hospitals represented, time coverage, 
#                 target prevalence, and memory requirements.
#
# Run       :   python .\topic_02_initial_dataset_inventory.py
#
# Date      :   October 10, 2026
# ------------------------------------------------------------------------------------------- #

from tutorial_common            import load_data, report_shape, section

# ------------------------------------------------------------------------------------------- #
def run():
    # Print a section heading.

    section("TOPIC 02 — Initial dataset inventory")

    df                  = load_data()                           # load the dataset.
    report_shape(df)                                            # Report the dataset's shape (number_of_rows, number_of_columns).

    print("\nColumn types:")
    print(df.dtypes.value_counts())                             # Count the column data types
                                                                # df.dtypes Returns the data type of every column in the DataFrame.

    print("\nCore identifiers and scope:")                      # Print a heading for identifiers and dataset scope.
   
    print("Unique encounters:", df["encounter_id"].nunique())                                               # An encounter ID is a unique identifier for a single episode of care.
                                                                                                            # .nunique() counts the number of distinct values in that column.
    print("Unique patients  :", df["patient_id"].nunique())                                                 # Count unique patients
    print("Hospitals        :", sorted(df["hospital_id"].dropna().unique()))                                # sorted(...) sorts the unique identifiers into ascending order.
    print("Time span        :", df["admission_timestamp"].min(), "to", df["admission_timestamp"].max())     # identifies the earliest and latest admission timestamps.
    print("Target prevalence:", df["deterioration_within_12h"].mean().round(4))

    # Approximate memory usage of Pandas DataFrame df in megabytes (MB).

    # df.memory_usage(deep = True) calculates the memory used by each column, 
    # including the DataFrame's index by default.
    # .sum() adds the memory usage of all columns and the index.

    print("\nApproximate memory use (MB):",                                 # "\n" inserts a blank line before the output for readability.
          round(df.memory_usage(deep = True).sum()/1024**2, 2))

# ------------------------------------------------------------------------------------------- #
if __name__ == '__main__':
    run()

# ------------------------------------------------------------------------------------------- #