# ------------------------------------------------------------------------------------------- #
# Course    :   AI 500 Computational Tutorial
# Topic     :   16 - Numerical descriptive statistics
#
# Purpose   :   This code performs numerical descriptive statistics on six healthcare-related 
#               variables, such as age, heart rate, blood pressure, and healthcare costs. It 
#               calculates summary statistics, including the mean, standard deviation, 
#               percentiles, interquartile range (IQR), and skewness. These help us understand 
#               the distribution, spread, and asymmetry of the data.
#
# Run       :   python .\topic_16_numerical_descriptive_statistics.py
#
# Date      :   October 23, 2026
# ------------------------------------------------------------------------------------------- #

from scipy.stats                    import skew
from tutorial_common                import load_data, section

# ------------------------------------------------------------------------------------------- #
def run():

    section("TOPIC 16 — Numerical descriptive statistics")
    
    df                  = load_data(sample = 80000)
    cols                = ["age_years","heart_rate_bpm","systolic_bp_mmHg",
                           "glucose_mg_dl","lactate_mmol_l","healthcare_cost_usd"]

    # percentiles = [...]: Requests these percentiles:
    # 1%    : Value below which approximately 1% of observations fall. 
    # 5%    : Value below which approximately 5% fall. 
    # 25%   : First quartile (Q1). 
    # 50%   : Median (Q2). 
    # 75%   : Third quartile (Q3). 
    # 95%   : Value below which approximately 95% fall. 
    # 99%   : Value below which approximately 99% fall.

    desc                = df[cols].describe(percentiles = [.01,.05,.25,.5,.75,.95,.99]).T

    # Calculates the interquartile range by subtracting Q1 from Q3.
    # IQR measures the spread of the middle 50% of observations.
    # A larger IQR indicates greater variability in that middle portion of the data.
    desc["IQR"]         = desc["75%"] - desc["25%"]

    # Computes skewness of each variable.
    # for c in cols : Iterates through each of the six column names. 
    # df[c]         : Selects the current column. 
    # .dropna()     : Removes missing values before calculation. 
    # skew(...)     : Calculates the skewness using the skew function. 
    
    # The list comprehension collects the six results and stores them in a new skewness column.
    # Skewness near 0   : Approximately symmetric distribution. 
    # Positive skewness : Longer tail toward higher values (right-skewed). 
    # Negative skewness : Longer tail toward lower values (left-skewed).
    
    desc["skewness"]    = [skew(df[c].dropna()) for c in cols]
    
    print(desc.round(2))

# ------------------------------------------------------------------------------------------- #
if __name__ == '__main__':
    run()

# ------------------------------------------------------------------------------------------- #