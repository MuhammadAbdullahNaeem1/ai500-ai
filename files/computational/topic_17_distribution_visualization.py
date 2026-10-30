# ------------------------------------------------------------------------------------------- #
# Course    :   AI 500 Computational Tutorial
# Topic     :   17 - Distribution visualization
#
# Purpose   :   This code visualizes the distribution of glucose levels in a dataset using four 
#               different plots. These plots help us understand how glucose values are spread, 
#               identify outliers, examine cumulative percentages, and check whether the data 
#               follows a normal distribution. It generates and saves four images: 
#               - Histogram with KDE,
#               - Box Plot,
#               - ECDF Plot, and 
#               - Normal Q-Q Plot.
#
# Install   :   conda install conda-forge::scipy
#
# Run       :   python .\topic_17_distribution_visualization.py
#
# Date      :   October 23, 2026
# ------------------------------------------------------------------------------------------- #

import seaborn                                  as sns
import scipy.stats                              as st
import matplotlib.pyplot                        as plt

from tutorial_common                            import load_data, section, savefig

# ------------------------------------------------------------------------------------------- #
def run():
    
    section("TOPIC 17 — Distribution visualization")

    df              = load_data(sample = 25000)
    x               = df["glucose_mg_dl"].dropna()              # .dropna() removes missing values (NaN).

    plt.figure(figsize = (8, 5))                                # Creates a new figure for the plot. Sets its size to 8 inches wide and 5 inches tall.
    
    # Creates a histogram of glucose values.
    # bins = 50 divides the data range into 50 intervals, showing how many observations fall within each interval.
    # kde = True overlays a Kernel Density Estimate (KDE), a smooth curve that approximates the distribution's shape.    
    
    sns.histplot(x, bins = 50, kde = True)
    plt.title("Glucose: Histogram + KDE")                       # Adds a title to the chart.
    savefig("topic17_glucose_hist_kde.png")                     # Saves the figure as a PNG image.

    plt.figure(figsize = (8, 4))

    # Creates a box plot of the glucose measurements.
    # The box represents the middle 50% of values, from the first quartile (Q1) to the third quartile (Q3).
    # The line inside the box represents the median.
    # Whiskers show the range according to the plotting convention, and individual points 
    # beyond them may indicate potential outliers.
    
    sns.boxplot(x = x)
    plt.title("Glucose: Box Plot")                              # Adds a title to the box plot.
    savefig("topic17_glucose_box.png")                          # Saves the chart as topic17_glucose_box.png.

    plt.figure(figsize = (8, 5))

    # Creates an Empirical Cumulative Distribution Function (ECDF) plot.
    # The horizontal axis shows glucose values.
    # The vertical axis shows the proportion of observations less than or equal to each value.

    sns.ecdfplot(x = x)
    plt.title("Glucose: ECDF")
    savefig("topic17_glucose_ecdf.png")

    # Creates a square figure measuring 6 × 6 inches.
    # A square figure is useful for visually comparing the data against a theoretical distribution.
    plt.figure(figsize = (6, 6))

    # Create a Normal Q-Q plot.
    # A Q-Q plot compares the observed data quantiles with the quantiles expected under a normal distribution.
    # - Points roughly along a straight line suggest that the data may be approximately normal. 
    # - Curved patterns suggest departures from normality. 
    # - Large deviations at the ends may indicate unusual tails or extreme values.

    # x.sample(...) selects a random subset of the glucose values.
    # min(5000, len(x)) chooses up to 5,000 observations, or all available observations if fewer than 5,000 exist.
    # random_state = 500 makes the random selection reproducible, provided the data and its ordering remain unchanged.
    # dist = "norm" compares the sample against a theoretical normal distribution.
    # plot = plt tells SciPy to draw the Q-Q plot using Matplotlib.

    st.probplot(x.sample(min(5000, len(x)), random_state = 500), dist = "norm", plot = plt)
    plt.title("Glucose: Normal Q-Q Plot")
    savefig("topic17_glucose_qq.png")

    # x-axis of Q-Q plot (z-scores)
    # -3    : Lower than ~99.9% of the population (extreme low outlier).
    # -2    : Lower than ~97.5% of the population (bottom 2.5%).
    # -1    : Lower than ~84% of the population (bottom 16%).
    # 0     : This is the exact average (mean). In a perfect normal distribution, 50% of the data is below 0, and 50% is above 0.
    # 1     : This is the boundary for the top ~16% of the data. If you are at "1", you are higher than 84% of the population.
    # 2     : This is the boundary for the top ~2.5% of the data. If you are at "2", you are higher than 97.5% of the population.
    # 3     : This is the boundary for the top ~0.1% of the data. If you are at "3", you are an extreme outlier, higher than 99.9% of the population.

    # y-axis of Q-Q plot
    # This axis represents the actual, observed values from your specific dataset, sorted from smallest to largest.
    # It takes your real data and divides it into the exact same probability chunks as the X-axis. 

# ------------------------------------------------------------------------------------------- #
if __name__ == '__main__':
    run()

# ------------------------------------------------------------------------------------------- #