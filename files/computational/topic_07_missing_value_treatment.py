# ------------------------------------------------------------------------------------------- #
# Course    :   AI 500 Computational Tutorial
# Topic     :   7 - Missing-value treatment
#
# Purpose   :   This code demonstrates three techniques for handling missing values in a dataset 
#               using Python and pandas and scikit-learn:
#               - Median imputation — replacing missing values with the median.
#               - Groupwise imputation — replacing missing values using the median for each hospital.
#               - KNN imputation — estimating missing values based on similar rows.
#
# Install   :   conda install anaconda::scikit-learn
#
# Run       :   python .\topic_07_missing_value_treatment.py
#
# Date      :   October 10, 2026
# ------------------------------------------------------------------------------------------- #

import pandas               as pd

from sklearn.impute         import SimpleImputer, KNNImputer
from tutorial_common        import load_data, section

# ------------------------------------------------------------------------------------------- #
def run():
    
    section("TOPIC 07 — Missing-value treatment")
    
    df              = load_data(sample = 40000)

    # List of four medical measurements.
    cols            = ["creatinine_mg_dl",
                       "sodium_mmol_l",
                       "glucose_mg_dl",
                       "lactate_mmol_l"]
    X               = df[cols].copy()               # .copy() creates a separate copy so that changes to X do not unintentionally modify the original DataFrame.

    # Checking missing values before imputation. This shows which columns have the most missing data.
    print("Missingness before (%):")
    print((X.isna().mean()*100).round(1))

    # ------------------------------------------------------------------------------------------- #
    # Median imputation.
    # SimpleImputer is a scikit-learn class for filling in missing values.
    # strategy      = "median" tells it to calculate a median for each feature.
    # add_indicator = True adds extra binary columns indicating which values were originally missing.
    # fit_transform(X) learns the medians from X and then fills the missing values.

    median_imp      = SimpleImputer(strategy = "median", add_indicator = True)
    Xm              = median_imp.fit_transform(X)
    print("\nMedian imputation output shape:", Xm.shape)

    # Confirming.
    # Convert imputed array back to a DataFrame
    Xm_df           = pd.DataFrame(Xm[:, :len(cols)], columns = cols, index = X.index)
    
    # Display rows where at least one original value was missing
    missing_rows    = X.isna().any(axis = 1)

    print("\nOriginal vs Median-Imputed Values:")
    print(pd.concat([X[missing_rows].add_suffix("_original"),
                     Xm_df[missing_rows].add_suffix("_imputed")], axis = 1).head(10))

    # ------------------------------------------------------------------------------------------- #
    # Groupwise imputation (Hospital-specific median imputation)
    groupwise                   = X.copy()                          # creates a copy of X.
    groupwise["hospital_id"]    = df["hospital_id"].values          # and adds a hospital_id column.

    # Loop over the selected columns
    for c in cols:
        # Group the data by hospital.
        # Calculate each hospital's median.
        # .fillna() fill missing values
        groupwise[c]            = groupwise[c].fillna(groupwise.groupby("hospital_id")[c].transform("median"))

    # Checking missingness afterward.
    print("\nMissingness after hospital-wise median imputation (%):")
    print((groupwise[cols].isna().mean()*100).round(1))

    print("\nOriginal vs Hospital-wise Imputed Values:")
    print(pd.concat([X[missing_rows].add_suffix("_original"), 
                     groupwise.loc[missing_rows, cols].add_suffix("_imputed")],axis = 1).head(10))

    # ------------------------------------------------------------------------------------------- #
    # KNN imputation shown on a small subset (for quickness).
    # KNN stands for K-Nearest Neighbors.

    small           = X.head(3000)                          # selects the first 3,000 rows of X.
    knn             = KNNImputer(n_neighbors = 5)           # Configure the KNN imputer; algorithm looks for rows with similar observed measurements.
    Xk              = knn.fit_transform(small)              # fits the imputer and produces an array with missing values imputed.

    print("KNN-imputed matrix shape:", Xk.shape)
    print("\nImportant: fit imputers on TRAINING data only.")

    # Convert KNN output to DataFrame
    Xk_df               = pd.DataFrame(Xk, columns = cols, index = small.index)

    # Identify rows with missing values in the subset
    knn_missing_rows    = small.isna().any(axis = 1)

    print("\nOriginal vs KNN-Imputed Values:")
    print(pd.concat([small[knn_missing_rows].add_suffix("_original"),
                     Xk_df[knn_missing_rows].add_suffix("_imputed")], axis = 1).head(10))

# ------------------------------------------------------------------------------------------- #
if __name__ == '__main__':
    run()

# ------------------------------------------------------------------------------------------- #