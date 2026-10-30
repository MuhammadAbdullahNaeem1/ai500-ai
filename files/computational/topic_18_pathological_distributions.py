# ------------------------------------------------------------------------------------------- #
# Course    :   AI 500 Computational Tutorial
# Topic     :   18 - Pathological distributions
#
# Purpose   :   This code analyzes pathological distributions in healthcare data by examining 
#               five variables, such as healthcare costs, glucose levels, and hospital stay 
#               duration. It calculates statistical measures to identify skewness, heavy tails, 
#               and unusually frequent zero values. The results help determine whether the data 
#               needs transformations, robust statistical summaries, or specialized models.
#
# Install   :   conda install conda-forge::scipy
#
# Run       :   python .\topic_18_pathological_distributions.py
#
# Date      :   October 23, 2026
# ------------------------------------------------------------------------------------------- #

import pandas                               as pd

from scipy.stats                            import skew, kurtosis
from tutorial_common                        import load_data, section

# ------------------------------------------------------------------------------------------- #
def run():    

    section("TOPIC 18 — Pathological distributions")

    df                  = load_data(sample = 100000)
    cols                = ["healthcare_cost_usd","glucose_mg_dl","wbc_10e9_l",
                           "lactate_mmol_l","length_of_stay_days"]

    # The statistical results for each variable will be stored as dictionaries in this list.
    rows                = []                        # Creates an empty list.
    for c in cols:
        x               = df[c].dropna()            # Selects the current column from the DataFrame. .dropna() removes missing values (NaN).

        rows.append({"variable"         : c,                                    # Records the name of the variable being analyzed.
                     "n"                : len(x),                               # Counts the number of non-missing observations.
                     "skew"             : skew(x),                              # Measures the asymmetry of the distribution.
                     "excess_kurtosis"  : kurtosis(x),                          # Measures tail heaviness relative to a normal distribution, using the Fisher definition.
                                                                                # Near 0: similar kurtosis to a normal distribution.
                                                                                # Positive: potentially heavier tails and/or more extreme observations.
                                                                                # Negative: lighter tails than a normal distribution.
                                                                                # High excess kurtosis can indicate that extreme values deserve further investigation.
                     "zero_fraction"    : (x == 0).mean(),                      # Calculates the proportion of observations that equal zero.
                     "p99/p50"          : x.quantile(.99)/x.quantile(.50),})    # Calculates the ratio of the 99th percentile to the 50th percentile (the median).
        
    print(pd.DataFrame(rows).round(3))                                          # Converts the list of dictionaries into a pandas DataFrame.

# ------------------------------------------------------------------------------------------- #
if __name__ == '__main__':
    run()

# ------------------------------------------------------------------------------------------- #