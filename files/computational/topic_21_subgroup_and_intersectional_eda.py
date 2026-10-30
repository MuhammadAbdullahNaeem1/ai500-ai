# ------------------------------------------------------------------------------------------- #
# Course    :   AI 500 Computational Tutorial
# Topic     :   21 - Subgroup and intersectional EDA
#
# Purpose   :   This code performs subgroup and intersectional Exploratory Data Analysis (EDA) 
#               to examine how patient deterioration and missing lactate measurements vary 
#               across combinations of region type, sex, and socioeconomic quintile. It groups 
#               patients by these characteristics, calculates the number of encounters, 
#               the deterioration rate within 12 hours, and the lactate missingness rate. 
#               It then displays the 20 largest groups and warns that results from small groups 
#               should be interpreted cautiously.
#
# Run       :   python .\topic_21_subgroup_and_intersectional_eda.py
#
# Date      :   October 23, 2026
# ------------------------------------------------------------------------------------------- #

from tutorial_common                    import load_data, clean_basic_categories, section

# ------------------------------------------------------------------------------------------- #
def run():

    section("TOPIC 21 — Subgroup and intersectional EDA")
    
    df                      = clean_basic_categories(load_data())                   # cleans or standardizes categorical variables in the loaded data.
    
    # Checks whether each row has a missing value in the lactate_mmol_l column.
    # .isna() returns True if the value is missing and False otherwise.
    # Stores these results in a new column called lactate_missing.
    df["lactate_missing"]   = df["lactate_mmol_l"].isna()

    # It groups encounters by three characteristics and calculates statistics for each combination.
    
    # Group the data
    # - region_type             : Groups encounters by region category.
    # - sex_clean               : Groups encounters by cleaned sex category.
    # - socioeconomic_quintile  : Groups encounters by socioeconomic group, typically one of five levels.
    # dropna = False            : Retains groups with missing values in the grouping columns rather than automatically excluding them.

    # Calculate the group statistics.
    # - n = ("encounter_id", "size"): Counts the number of rows in each group. 
    #                                 The size operation counts rows, even if an encounter_id value is missing.
    # - deterioration_rate = ("deterioration_within_12h", "mean"): Calculates the mean of the deterioration indicator.
    # - lactate_missing_rate = ("lactate_missing", "mean"): Calculates the proportion of encounters with missing lactate measurements.

    grp = (df.groupby(["region_type", "sex_clean", "socioeconomic_quintile"], dropna = False)
           .agg(n                   = ("encounter_id","size"), 
                deterioration_rate  = ("deterioration_within_12h", "mean"),
               lactate_missing_rate = ("lactate_missing","mean"))
           .reset_index())                                          # Converts the grouping columns from index levels back into ordinary columns.
                                                                    # Makes grp easier to display, filter, or export.
    
    grp["deterioration_rate"]       *= 100
    grp["lactate_missing_rate"]     *= 100

    print(grp.sort_values("n", ascending = False).head(20).round(2))
    
    print("\nSmall intersectional groups should be interpreted with uncertainty, not only point estimates.")

# ------------------------------------------------------------------------------------------- #
if __name__ == '__main__':
    run()

# ------------------------------------------------------------------------------------------- #