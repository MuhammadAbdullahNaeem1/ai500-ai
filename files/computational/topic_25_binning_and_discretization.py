# ------------------------------------------------------------------------------------------- #
# Course    :   AI 500 Computational Tutorial
# Topic     :   25 - Binning and discretization
#
# Purpose   :   This code demonstrates binning and discretization, a data preprocessing 
#               technique that converts continuous numerical values into discrete groups or 
#               categories. 
#               - Age binning: Groups patients into age ranges and calculates the number of 
#                              patients and the average rate of deterioration within 12 hours 
#                              for each group. 
#               - Heart-rate binning: Divides heart rates into five quantile-based bins and 
#                                     counts how many patients fall into each bin.
#               - Goal: Make data easier to interpret while recognizing that binning loses 
#                       some information.
#
# Run       :   python .\topic_25_binning_and_discretization.py
#
# Date      :   October 24, 2026
# ------------------------------------------------------------------------------------------- #

import pandas                               as pd

from tutorial_common                        import load_data, section
from sklearn.preprocessing                  import KBinsDiscretizer

# ------------------------------------------------------------------------------------------- #
def run():
    
    section("TOPIC 25 — Binning and discretization")

    df                      = load_data(sample = 30000)

    # Creates a new DataFrame column called age_group.
    df["age_group"]         = pd.cut(df["age_years"],                               # Uses pd.cut() to divide a numerical variable into specified intervals.
                                     bins   = [17, 40, 60, 80, 120],                # bins defines the interval boundaries: 17, 40, 60, 80, and 120.
                                     labels = ["18-40", "41-60", "61-80", "81+"])   # These boundaries create four age intervals.

    # Calculate statistics for each age group.
    print(df.groupby("age_group", observed = False)["deterioration_within_12h"]     # Groups the dataset according to the age_group column. observed = False requests that unobserved categorical groups also be included in the result.
          .agg(["size", "mean"]).round(3))                                          # Calculates two statistics for each age group.
                                                                                    # size: Number of rows in the group, including rows where the selected outcome is missing.
                                                                                    # mean: Average value of the deterioration variable, excluding missing outcome values.

    # Create the heart-rate discretizer.
    # If heart rates range from low to high, the bins could represent the lowest 20%, the next 20%, and so on.
    
    # encode = "ordinal": Represents each bin with an integer code, normally 0 through 4.
    # strategy = "quantile": Chooses bin boundaries based on quantiles of the data, 
    # aiming to place approximately equal numbers of observations in each bin.

    kb                      = KBinsDiscretizer(n_bins = 5, encode = "ordinal", strategy = "quantile")

    # Fit the discretizer and transform heart rates.
    # Fit: Learns the quantile-based bin boundaries from the heart-rate data.
    # Transform: Assigns each heart-rate observation to a bin.

    # .ravel(): Flattens the two-dimensional result into a one-dimensional array.
    # Stores the resulting bin codes in a new column named hr_quantile_bin.

    df["hr_quantile_bin"]   = kb.fit_transform(df[["heart_rate_bpm"]]).ravel()      # The double brackets return a two-dimensional DataFrame, which is the input format expected by scikit-learn.

    print("\nHeart-rate quantile-bin counts:")
    print(df["hr_quantile_bin"].value_counts().sort_index())                        # Counts the observations assigned to each bin.
                                                                                    # Sorts the results by bin code, from the lowest bin to the highest.

    print("\nBinning can aid interpretability but loses within-bin information "
          "and creates artificial discontinuities at cut points.")

    # Information loss: Patients with different heart rates may receive the same bin code. 
    # For example, heart rates of 71 and 79 might fall into the same bin.

    # Artificial discontinuities: Two nearly identical values on opposite sides of a bin boundary 
    # receive different categories, even though their actual values are very similar.

# ------------------------------------------------------------------------------------------- #
if __name__ == '__main__':
    run()

# ------------------------------------------------------------------------------------------- #