# ------------------------------------------------------------------------------------------- #
# Course    :   AI 500 Computational Tutorial
# Topic     :   3 - Automated data profiling
#
# Purpose   :   The purpose of this code is to automatically profile a dataset and identify 
#               potential data-quality issues, such as missing values, duplicate records, and 
#               columns with many distinct values. It also generates an optional HTML report 
#               for further analysis.
#
# Install   :   conda install conda-forge::ydata-profiling
#               python -m pip install --upgrade setuptools (IF required)
#               python -m pip install "setuptools<81" (IF required)
#
# Run       :   python .\topic_03_automated_data_profiling.py
#
# Date      :   October 10, 2026
# ------------------------------------------------------------------------------------------- #

import pandas               as pd

from tutorial_common        import load_data, section
from ydata_profiling        import ProfileReport                # YData Profiling used for automated Exploratory Data Analysis (EDA).
                                                                # ProfileReport helps generate an automatic report about your dataset.

# ------------------------------------------------------------------------------------------- #
def run():
    
    section("TOPIC 03 — Automated data profiling")
    df              = load_data(sample = 50000)

    # Create a dataset profile. It creates a summary of every column in the dataset.
    profile         = pd.DataFrame({"dtype"         : df.dtypes.astype(str),                # .astype(str) converts those types into strings so they can be displayed easily.
                                    "missing_pct"   : (df.isna().mean()*100).round(2),      # Calculate the percentage of missing values in each column.

                                    # Count the number of distinct, non-missing values in each column.
                                    "n_unique"      : df.nunique(dropna = True),}).sort_values("missing_pct", ascending = False)
                                                                                            # Sort the columns from the highest missing percentage to the lowest.
    print(profile.head(20))                                                                 # Print the first 20 columns.

    # df.duplicated() identifies rows that duplicate an earlier row across all columns. 
    print("\nDuplicate rows:"               , int(df.duplicated().sum()))                   # Count duplicate rows

    print("Duplicate encounter_id values:"  , int(df["encounter_id"].duplicated().sum()))   # Count duplicate encounter IDs

    # Generate an optional HTML profiling report
    try:        
        small       = df.sample(min(10000, len(df)), random_state = 500)                    # min(10000, len(df)) selects the smaller of 10,000 and the total row count.

        # ProfileReport comes from the ydata-profiling library. It analyzes the 
        # sampled dataset and prepares a report that can include: Column data types; 
        # Missing-value statistics; Distinct-value counts; Summary statistics for 
        # numerical columns; Frequency distributions for categorical columns; 
        # Correlations and other data-quality indicators.

        # minimal = True requests a lighter report with fewer expensive analyses.
        report      = ProfileReport(small, minimal = True, title = "AI500 Dataset Profile")
        
        out         = "outputs/topic03_profile.html"
        report.to_file(out)                                                                 # writes the HTML report to the specified path.
        
        print("Optional HTML profile written to", out)

    # Handle errors gracefully.
    except Exception as exc:                                                                # catches the exception.
        print("\nOptional ydata-profiling step skipped:", type(exc).__name__)               # type(exc).__name__ extracts its class name, such as 
                                                                                            # ModuleNotFoundError, FileNotFoundError, or PermissionError.

# ------------------------------------------------------------------------------------------- #
if __name__ == '__main__':
    run()

# ------------------------------------------------------------------------------------------- #