# ------------------------------------------------------------------------------------------- #
# Course    :   AI 500 Computational Tutorial
# Topic     :   5 - Data-quality dimensions
#
# Purpose   :   This code performs a data quality assessment on a dataset, likely containing 
#               hospital vital-sign records such as blood pressure measurements. It calculates 
#               metrics for completeness, duplicate rows, data arrival timeliness, hospital 
#               representation, and consistency of blood pressure measurements across device 
#               models.
#
# Run       :   python .\topic_05_data_quality_dimensions.py
#
# Date      :   October 10, 2026
# ------------------------------------------------------------------------------------------- #

import pandas                       as pd

from tutorial_common                import load_data, section

# ------------------------------------------------------------------------------------------- #
def run():

    section("TOPIC 05 — Data-quality dimensions")
    
    df                  = load_data()                   # loads the dataset and returns it as a pandas DataFrame.
                                                        # df stores the dataset in a table-like structure.

    quality             = {}                            # creates an empty Python dictionary to store the calculated data quality metrics.

    # Calculate data completeness. What percentage of all cells in the dataset contain 
    # values rather than missing data.

    # df.isna() returns True for missing values (NaN or None) and False for non-missing values.
    # .mean() calculates the proportion of missing values in each column because True is treated as 1 and False as 0.
    # The second .mean() calculates the average missing-value proportion across the columns.
    quality["completeness_pct"]     = round((1 - df.isna().mean().mean())*100, 2)

    # Calculate the percentage of duplicate rows.

    # df.duplicated() returns a Boolean value for every row. 
    # True means the row duplicates a preceding row.
    # False means it is not a duplicate.
    # .mean() calculates the fraction of rows marked True.
    quality["duplicate_row_pct"]    = round(df.duplicated().mean()*100, 3)

    # Measure data arrival timeliness.
    # How long it takes for recorded vital-sign data to arrive in the system.
    # .dt.total_seconds() to express the time difference in seconds.
    # Divide by 60 to convert seconds to minutes.
    # .median() to calculate the median latency across all rows.

    latency_min                             = (df["data_arrival_timestamp"] - df["vitals_recorded_timestamp"]).dt.total_seconds()/60

    # The median is preferred over the mean when a few records have unusually 
    # long delays, because extreme values have less influence on it.

    # Potential issue: Missing timestamps can produce missing latency values. 
    # Also, negative latencies may indicate clock synchronization issues or 
    # incorrect timestamps, so these should be checked separately.
    quality["median_arrival_latency_min"]   = round(latency_min.median(), 2)

    # Measure hospital representation.
    # What percentage of the dataset comes from each hospital.

    # df["hospital_id"] selects the hospital identifier column.
    # .value_counts() counts the records associated with each hospital.
    # normalize = True converts the counts into proportions.
    # This helps identify whether the dataset is dominated by a particular hospital.
    # Note: unequal hospital representation does not automatically mean poor data quality.

    hospital_share      = (df["hospital_id"].value_counts(normalize = True)*100).round(2)

    # Compare blood pressure measurements by device model to assess measurement consistency.
    # Compares systolic blood pressure measurements across different device models.

    # df.groupby("bp_device_model") groups the records by blood pressure device model.
    # ["systolic_bp_mmHg"] selects the systolic blood pressure measurement column.
    # .agg(["count", "mean", "std"]) calculates three statistics for each group.
    # .round(2) rounds the numerical results to two decimal places.

    # count - Number of non-missing blood pressure measurements.
    # mean  - Average systolic blood pressure in mmHg.
    # Std   - Standard deviation, showing the spread of measurements. 

    bp_by_device        = df.groupby("bp_device_model")["systolic_bp_mmHg"].agg(["count", "mean", "std"]).round(2)

    # Print the results
    print(pd.Series(quality))                       # Converts the dictionary into a pandas Series, which displays the quality metrics as labeled values.
    print("\nHospital composition (%):")

    print(hospital_share)
    print("\nSystolic BP by device model:")
    
    print(bp_by_device)

# ------------------------------------------------------------------------------------------- #
if __name__ == '__main__':
    run()

# ------------------------------------------------------------------------------------------- #