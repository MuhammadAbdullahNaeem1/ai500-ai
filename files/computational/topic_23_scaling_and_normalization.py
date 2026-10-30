# ------------------------------------------------------------------------------------------- #
# Course    :   AI 500 Computational Tutorial
# Topic     :   23 - Scaling and normalization
#
# Purpose   :   This code demonstrates feature scaling and normalization using three techniques: 
#               StandardScaler, MinMaxScaler, and RobustScaler. It loads a sample of data, 
#               selects four health-related numerical columns, removes rows with missing values, 
#               and applies each scaling method. Finally, it prints summary statistics to show 
#               how each method transforms the data.
#
# Run       :   python .\topic_23_scaling_and_normalization.py
#
# Date      :   October 24, 2026
# ------------------------------------------------------------------------------------------- #

import pandas                               as pd

from tutorial_common                        import load_data, section
from sklearn.preprocessing                  import StandardScaler, MinMaxScaler, RobustScaler

# ------------------------------------------------------------------------------------------- #
def run():
    
    section("TOPIC 23 — Scaling and normalization")
    
    df                  = load_data(sample = 30000)
    cols                = ["age_years", "heart_rate_bpm", "systolic_bp_mmHg", "glucose_mg_dl"]

    X                   = df[cols].dropna()         # .dropna() removes rows that contain missing values in any of those columns.

    scalers             = {"StandardScaler" : StandardScaler(),         # Centers values around a mean of 0 and scales them to a standard deviation of 1.
                           "MinMaxScaler"   : MinMaxScaler(),           # Typically transforms values to a range of 0 to 1.
                           "RobustScaler"   : RobustScaler()}           # Centers values around the median and scales using the interquartile range (IQR).
    
    for name, scaler in scalers.items():
        Z               = pd.DataFrame(scaler.fit_transform(X),         # scaler.fit(X) learns the scaling parameters from the data and applies the scaling transformation.
                                       columns = cols)                  # stores the transformed data in a new DataFrame called Z, keeping the original column names.

        print(f"\n{name}")

        # Z.describe() calculates descriptive statistics for each column.
        # .loc[["min", "25%", "50%", "75%", "max"]] selects the minimum, 25th percentile, median (50th percentile), 75th percentile, and maximum.
        print(Z.describe().loc[["min", "25%", "50%", "75%", "max"]].round(2))

# ------------------------------------------------------------------------------------------- #
if __name__ == '__main__':
    run()

# ------------------------------------------------------------------------------------------- #