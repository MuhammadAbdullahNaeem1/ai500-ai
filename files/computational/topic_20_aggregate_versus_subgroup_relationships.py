# ------------------------------------------------------------------------------------------- #
# Course    :   AI 500 Computational Tutorial
# Topic     :   20 - Aggregate versus subgroup relationships
#
# Purpose   :   This code demonstrates how overall relationships can differ from relationships 
#               within subgroups in hospital data. It calculates the correlation between patient 
#               age and deterioration within 12 hours for all patients and separately for each 
#               hospital. It also compares deterioration rates across region types and age 
#               groups. The main lesson is that aggregate data can hide important differences 
#               between subgroups, potentially due to confounding or interactions.
#
# Run       :   python .\topic_20_aggregate_versus_subgroup_relationships.py
#
# Date      :   October 23, 2026
# ------------------------------------------------------------------------------------------- #

import pandas                                           as pd
import statsmodels.api                                  as sm

from tutorial_common                                    import load_data, section

# ------------------------------------------------------------------------------------------- #
def run():  

    section("TOPIC 20 — Aggregate versus subgroup relationships")

    df                  = load_data(sample = 80000)
    d                   = df[["age_years","deterioration_within_12h","hospital_id","region_type"]].dropna()

    # Calculate the overall, or pooled, correlation between age and deterioration.

    # d[["age_years", "deterioration_within_12h"]] selects the two variables of interest.
    # .corr() calculates their Pearson correlation matrix.
    # .iloc[0, 1] extracts the correlation between the first and second variables.

    pooled              = d[["age_years","deterioration_within_12h"]].corr().iloc[0, 1]
    print("Pooled correlation(age, deterioration):", round(pooled, 4))

    # d.groupby("hospital_id") divides the data into groups based on hospital.
    # .apply(...) applies a calculation to each hospital's data.
    # lambda g: defines a small anonymous function, where g represents one hospital's records.
    # g[["age_years", "deterioration_within_12h"]] selects the two relevant variables for that hospital.
    # .corr().iloc[0, 1] calculates and extracts the correlation within that hospital.
    # .rename("correlation") labels the resulting series correlation.

    # These values may differ from the pooled correlation because hospitals can have 
    # different patient populations, clinical practices, and outcome patterns.

    subgroup            = (d.groupby("hospital_id")
                           .apply(lambda g: g[["age_years", "deterioration_within_12h"]].corr().iloc[0, 1])
                           .rename("correlation"))
    
    print("\nWithin-hospital correlations:")
    print(subgroup.round(4))

    # Calculate deterioration rates for combinations of region type and age group.
    # These results help reveal whether age-specific deterioration rates differ across region types.

    # pd.cut(d["age_years"], [17, 40, 60, 80, 120]) divides ages into intervals.
    # Technically, pandas uses intervals that are open on the left and closed on the right by default, 
    # so the exact boundaries matter. The first interval excludes age 17.

    # d.groupby(["region_type", ...]) groups patients by both region type and age interval.
    
    # observed = False asks pandas to include unobserved categorical combinations where supported by the grouping settings.
    # It helps you see which combinations have no observations, rather than simply omitting them from the output.
    
    # ["deterioration_within_12h"] selects the outcome column.
    # .mean() calculates the average outcome in each group.

    rates               = d.groupby(["region_type", pd.cut(d["age_years"], [17, 40, 60, 80, 120])],
                                    observed = False)["deterioration_within_12h"].mean()
    
    print("\nStratified outcome rates:")
    print(rates.round(3))
    
    print("\nAggregate relationships can conceal heterogeneity, confounding, or interactions.")

# ------------------------------------------------------------------------------------------- #
if __name__ == '__main__':
    run()

# ------------------------------------------------------------------------------------------- #