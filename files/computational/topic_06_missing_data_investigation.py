# ------------------------------------------------------------------------------------------- #
# Course    :   AI 500 Computational Tutorial
# Topic     :   6 - Missing-data investigation
#
# Purpose   :   This code performs a missing data analysis using Python, Pandas, Matplotlib, 
#               and Seaborn. It examines how much data is missing, which variables have the 
#               most missing values, whether some hospitals or regions have more missing 
#               lactate measurements, and whether missing values tend to occur together.
#
# Run       :   python .\topic_06_missing_data_investigation.py
#
# Date      :   October 10, 2026
# ------------------------------------------------------------------------------------------- #

import seaborn                              as sns                              # A Python library used to create statistical graphs and visualizations.
import matplotlib.pyplot                    as plt

from tutorial_common                        import load_data, section, savefig

# ------------------------------------------------------------------------------------------- #
def run():

    section("TOPIC 06 — Missing-data investigation")

    df                  = load_data()

    # Calculate missingness for each variable.
    # Helps identify variables that might be unreliable or require special handling before 
    # statistical analysis or machine learning.

    miss                = (df.isna().mean()*100).sort_values(ascending = False)
    
    print("Highest variable-level missingness:")
    print(miss.head(12))

    # Calculate missingness for each patient record.
    # .mean(axis = 1) calculates the proportion of missing columns in each row. 
    # axis = 1 means calculate across columns for each record.
    record_missing      = df.isna().mean(axis = 1)

    # .quantile([...]) summarizes the distribution of these proportions at selected percentiles.
    # 0     - Minimum record-level missingness.
    # 0.25  - 25% of records have missingness at or below this value.
    # 0.5   - Median missingness. 
    # 0.75  - 75% of records have missingness at or below this value.
    # 0.9   - 90% of records have missingness at or below this value.
    # 0.95  - 95th percentile.
    # 0.99  - 99th percentile.
    # 1     - Maximum record-level missingness.

    # For instance, if the median is 0.10, a typical patient record is missing 10% of its variables.
    # If the 99th percentile is 0.70, approximately 99% of records have missingness at or below 70%, 
    # while the remaining 1% may have even more missing data.

    print("\nRecord-level missingness quantiles:")
    print(record_missing.quantile([0, 0.25, 0.5, 0.75, 0.9, 0.95, 0.99, 1]))

    # Analyze lactate missingness by hospital and region
    subgroup            = (df.assign(lactate_missing = df["lactate_mmol_l"].isna())         # adds a new column named lactate_missing.
                                                                                            # The original DataFrame is not modified by assign() unless you explicitly save the result back to df.                            
                           .groupby(["hospital_id","region_type"])["lactate_missing"]       # group by hospital and region.
                                                                                            # Selects the lactate_missing column within those groups.
                           .mean().mul(100).round(1))
    
    print("\nLactate missingness by hospital and region type (%):")
    print(subgroup)

    # Calculate correlations between missingness indicators.
    # Examines whether missing values in different laboratory variables tend to occur together.

    corr                = df[["creatinine_mg_dl",
                              "sodium_mmol_l",
                              "wbc_10e9_l",
                              "glucose_mg_dl",
                              "lactate_mmol_l"]].isna().corr()                  # .corr() Pearson correlation between the Boolean missingness indicators.
                                                                                # The resulting correlation matrix has values between -1 and 1.

    # Visualize the correlation matrix as a heatmap.
    plt.figure(figsize = (7, 5))                                                # Creates a figure that is 7 inches wide and 5 inches tall.

    # Draws the heatmap, where each cell represents a correlation between two missingness indicators.
    sns.heatmap(corr, annot = True, fmt = ".2f", cmap = "viridis")              # annot = True: prints the numerical correlation inside each cell.          
                                                                                # fmt = ".2f": displays numbers to two decimal places, such as 0.75.
                                                                                # cmap = "viridis": uses the Viridis color palette to represent the values.
    plt.title("Correlation of Missingness Indicators")                          # Adds a descriptive title to the plot.
    
    savefig("topic06_missingness_correlation.png")                              # Saves the figure to a PNG file named topic06_missingness_correlation.png.

# ------------------------------------------------------------------------------------------- #
if __name__ == '__main__':
    run()

# ------------------------------------------------------------------------------------------- #

# Quantile results.
#
# The values suggest that each record contains approximately 49 variables, 
# because the percentages correspond to fractions of (1/49). For example:
#
# 2.04%     = 1 missing value out of 49 variables.
# 4.08%     = 2 missing values out of 49 variables.
# 6.12%     = 3 missing values out of 49 variables.
# 8.16%     = 4 missing values out of 49 variables.
# 14.29%    = 7 missing values out of 49 variables.

# ------------------------------------------------------------------------------------------- #