# ------------------------------------------------------------------------------------------- #
# Course    :   AI 500 Computational Tutorial
# Topic     :   15 - Basic EDA workflow
#
# Purpose   :   This code performs a basic Exploratory Data Analysis (EDA) on a dataset 
#               containing patient and hospital information. Its purpose is to understand the 
#               data before building a machine-learning model or conducting further analysis. 
#               It examines seven areas: 
#               - Dataset structure and data types. 
#               - Summary statistics for selected numerical variables. 
#               - Missing values. 
#               - Relationships between variables. 
#               - Changes in patient deterioration rates across years. 
#               - Differences between hospitals. 
#               - Documentation of findings and unanswered questions.
#
# Run       :   python .\topic_15_basic_eda_workflow.py
#
# Date      :   October 23, 2026
# ------------------------------------------------------------------------------------------- #

from tutorial_common                import load_data, section

# ------------------------------------------------------------------------------------------- #
def run():
    
    section("TOPIC 15 - Basic EDA workflow")
    
    df      = load_data(sample = 50000)

    # Examine the dataset structure. Understand the dataset's size and the types of information it contains.
    print("1. Structure")
    print(df.shape, "\n", df.dtypes.head())

    # Calculate univariate summaries.
    
    # .describe(): Calculates summary statistics for each numerical column, including:
    # count: Number of non-missing observations. 
    # mean: Average value. 
    # std: Standard deviation, measuring variability. 
    # min: Minimum value. 
    # 25%, 50%, 75%: Quartiles; 50% is the median. 
    # max: Maximum value.

    # .T: Transposes the output, placing variables in rows and statistics in columns.
    print("\n2. Univariate summaries")
    print(df[["age_years","heart_rate_bpm","glucose_mg_dl","lactate_mmol_l"]].describe().T)

    # Check missing values. Identify which variables have the most incomplete data.

    # df.isna(): Marks each missing value as True and each non-missing value as False.
    # .mean(): Calculates the proportion of missing values in each column.
    
    print("\n3. Missingness")
    print((df.isna().mean()*100).sort_values(ascending = False).head(8))

    # Examine relationships between variables. Explore which variables are associated with the outcome.
    # [Note] Correlation does not establish causation. Also, the strength of a correlation does not 
    #        by itself show whether a relationship is clinically important.
    
    # .corr(numeric_only = True): Calculates pairwise Pearson correlations between the numerical columns.
    # Correlation coefficients range from -1 to +1:
    # - +1: Perfect positive linear relationship. 
    # -  0: No linear relationship. 
    # - -1: Perfect negative linear relationship.

    print("\n4. Relationships")
    print(df[["age_years","heart_rate_bpm","respiratory_rate_bpm",
              "oxygen_saturation_pct","deterioration_within_12h"]].corr(numeric_only = True).round(2))

    # Analyze changes over time. Determine whether the observed deterioration rate changes over time.
    print("\n5. Time")

    # .groupby("admission_year"): Groups records by the year of hospital admission. 
    # ["deterioration_within_12h"]: Selects the outcome variable. 
    # .mean(): Calculates the mean outcome for each year. 
    # .round(3): Rounds the results to three decimal places.
    print(df.groupby("admission_year")["deterioration_within_12h"].mean().round(3))

    # Compare hospitals. Compare hospital sample sizes and observed deterioration rates.
    print("\n6. Subgroups")

    # .groupby("hospital_id"): Groups patients according to their hospital. 
    # ["deterioration_within_12h"]: Selects the outcome variable. 
    # .agg(["size", "mean"]): Calculates two statistics for each hospital: 
    #       size: Number of records in the group, including records where the outcome is missing. 
    #       mean: Average deterioration outcome, excluding missing outcome values. 
    # .round(3): Rounds numerical results to three decimal places.

    # Differences could reflect patient severity, missing data, hospital practices, 
    # or differences in the populations being treated—not necessarily hospital quality.
    print(df.groupby("hospital_id")["deterioration_within_12h"].agg(["size", "mean"]).round(3))

    # Document the findings.
    # What you learned          : Important patterns, unusual values, missingness, and observed relationships. 
    # What remains uncertain    : Questions that the current analysis cannot answer. 
    # What requires follow-up   : Data-quality checks, additional statistical analysis, and further investigation.
    
    print("\n7. Document what you learned, what remains uncertain, and what requires follow-up.")

# ------------------------------------------------------------------------------------------- #
if __name__ == '__main__':
    run()

# ------------------------------------------------------------------------------------------- #