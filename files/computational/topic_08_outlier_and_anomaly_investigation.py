# ------------------------------------------------------------------------------------------- #
# Course    :   AI 500 Computational Tutorial
# Topic     :   8 - Outlier and anomaly investigation
#
# Purpose   :   This code investigates outliers and potentially anomalous values in patient 
#               health data. It uses the Interquartile Range (IQR) method and Z-scores to 
#               identify unusual heart-rate readings, checks whether heart rate, temperature, 
#               and systolic blood pressure fall within predefined plausible ranges, and 
#               prints suspicious records for further investigation. 
#               Important: The code flags unusual values but does not delete or modify them.
#
# Install   :   conda install conda-forge::scipy
#
# Run       :   python .\topic_08_outlier_and_anomaly_investigation.py
#
# Date      :   October 17, 2026
# ------------------------------------------------------------------------------------------- #

import numpy                            as np

from scipy                              import stats                    # scientific library for Python
from tutorial_common                    import load_data, section

# ------------------------------------------------------------------------------------------- #
def run():
    section("TOPIC 08 — Outlier and anomaly investigation")

    # The dataset is expected to contain columns such as 
    # heart_rate_bpm, temperature_c, and systolic_bp_mmHg.
    df                  = load_data()

    # Selects the heart_rate_bpm column.
    # .dropna() removes missing values from this temporary series because
    # statistical calculations such as quartiles and z-scores need valid numerical observations.
    s                   = df["heart_rate_bpm"].dropna()

    # Q1: the 25th percentile, below which approximately 25% of observations fall.
    # Q2: the 75th percentile, below which approximately 75% of observations fall.
    q1, q3              = s.quantile([0.25, 0.75])

    # The IQR measures the spread of the middle 50% of the observations.
    iqr                 = q3 - q1

    # Flag potential heart-rate outliers using IQR.
    # q1 - 1.5*iqr: the lower boundary.
    # q3 + 1.5*iqr: the upper boundary.
    
    # iqr_flag, is a boolean series containing True for flagged observations and False otherwise. 
    # Missing heart-rate values generally produce False in this comparison.
    iqr_flag            = (df["heart_rate_bpm"] < q1 - 1.5*iqr) | (df["heart_rate_bpm"] > q3 + 1.5*iqr)

    # Calculate absolute z-scores.
    # stats.zscore(s, ...) calculates the z-score of each observation.
    # nan_policy = "omit" tells SciPy to ignore NaN values during the calculation.
    # np.abs(...) converts negative Z-scores into positive values.
    z                   = np.abs(stats.zscore(s, nan_policy = "omit"))

    print("Heart-rate IQR flags:"               , int(iqr_flag.sum()))

    # z > 3 identifies observations whose absolute z-score exceeds 3.
    # identifies values more than 3 standard deviations away from the mean.
    print("Heart-rate |z|>3 among nonmissing:"  , int((z > 3).sum()))

    impossible = (~df["heart_rate_bpm"].between(30, 250) |
                  ~df["temperature_c"].between(30, 45) |
                  ~df["systolic_bp_mmHg"].between(40, 300))
    
    print("\nClearly implausible values:")
    print(df.loc[impossible,
                 ["encounter_id","heart_rate_bpm","temperature_c","systolic_bp_mmHg"]].head(15))

# ------------------------------------------------------------------------------------------- #
if __name__ == '__main__':
    run()

# ------------------------------------------------------------------------------------------- #