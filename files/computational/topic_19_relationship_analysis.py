# ------------------------------------------------------------------------------------------- #
# Course    :   AI 500 Computational Tutorial
# Topic     :   19 - Relationship analysis
#
# Purpose   :   This code analyses relationships between patient vital signs and the likelihood 
#               of deterioration within 12 hours. It creates two visualisations: 
#               - Scatter plot: Shows the relationship between respiratory rate and oxygen 
#                               saturation, with colours indicating whether the patient 
#                               deteriorated within 12 hours. 
#               - Correlation heatmap: Shows the strength and direction of relationships between 
#                                      selected numerical variables, such as age, heart rate, 
#                                      blood pressure, and oxygen saturation. 
#               Both charts are saved as image files for later use. 
#               Correlation does not necessarily imply causation.
#
# Run       :   python .\topic_19_relationship_analysis.py
#
# Date      :   October 23, 2026
# ------------------------------------------------------------------------------------------- #

import seaborn                          as sns
import matplotlib.pyplot                as plt
    
from tutorial_common                    import load_data, section, savefig

# ------------------------------------------------------------------------------------------- #
def run():
    
    section("TOPIC 19 — Relationship analysis")
    df                  = load_data(sample = 20000)

    plt.figure(figsize = (8, 5))

    # Create the scatter plot.
    # The plot can help reveal whether higher respiratory rates tend to occur alongside 
    # lower oxygen saturation, and whether the pattern differs between the two deterioration groups.

    sns.scatterplot(data    = df,                               # data = df: Uses the loaded patient dataset.
                    x       = "respiratory_rate_bpm",           # x = "respiratory_rate_bpm": Places respiratory rate (bpm) on the horizontal axis.
                    y       = "oxygen_saturation_pct",          # y = "oxygen_saturation_pct": Places oxygen saturation (%) on the vertical axis.
                    hue     = "deterioration_within_12h",       # hue = "deterioration_within_12h": Colours points according to the deterioration variable.
                    alpha   = 0.35,                             # alpha = 0.35: Makes the points partially transparent, helping reveal overlapping observations.
                    s       = 18)                               # s = 18: Sets the marker size.
    
    plt.title("Respiratory Rate vs Oxygen Saturation")
    savefig("topic19_scatter_relationship.png")

    # Select numerical variables. Creates a list of the columns to include in the correlation analysis.
    # Including deterioration allows the analysis to examine which variables are associated with that outcome.
    numeric             = ["age_years","heart_rate_bpm","respiratory_rate_bpm",
                           "oxygen_saturation_pct","systolic_bp_mmHg",
                           "glucose_mg_dl","deterioration_within_12h"]

    # Calculate the correlation matrix.

    # df[numeric]           : Selects only the specified columns from the DataFrame.
    # .corr()               : Calculates pairwise correlations between the selected numerical variables.
    # numeric_only = True   : Restricts the calculation to numerical data types.
    # The resulting corr object is a correlation matrix containing values from −1 to +1.

    corr                = df[numeric].corr(numeric_only = True)

    # Create the correlation heatmap.
    plt.figure(figsize = (8, 6))

    sns.heatmap(corr,                                   # corr: Supplies the calculated correlation values.
                annot   = True,                         # annot = True: Displays the numerical correlation value inside each cell.
                fmt     = ".2f",                        # fmt = ".2f": Formats values to two decimal places, such as 0.75 or -0.42.
                cmap    = "coolwarm",                   # cmap = "coolwarm": Uses a colour palette with contrasting cool and warm colours to distinguish correlation values.
                center  = 0)                            # center = 0: Centres the colour scale at zero, making positive and negative correlations easier to distinguish.
    
    plt.title("Correlation Matrix")
    savefig("topic19_correlation_heatmap.png")

# ------------------------------------------------------------------------------------------- #
if __name__ == '__main__':
    run()

# ------------------------------------------------------------------------------------------- #