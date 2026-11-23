# ------------------------------------------------------------------------------------------- #
# Course    :   AI 500 Computational Tutorial
# Topic     :   Visualizing a Classification Decision Boundary Using PCA and Feature Importance
#
# Purpose   :   This code visualizes a classifier's decision boundary in a two-dimensional PCA 
#               space using the most important numerical features selected from a 
#               feature-importance CSV file. It generates and saves a plot showing the 
#               classification regions and test data points.
#
# Date      :   November 13, 2026
# ------------------------------------------------------------------------------------------- #

import numpy                            as np
import pandas                           as pd
import matplotlib.pyplot                as plt

from pathlib                            import Path

from sklearn.base                       import clone                        # Creates a fresh, unfitted copy of an existing machine-learning estimator.
from sklearn.decomposition              import PCA
from sklearn.impute                     import SimpleImputer
from sklearn.preprocessing              import StandardScaler
from sklearn.pipeline                   import make_pipeline

# ------------------------------------------------------------------------------------------- #
# model             - Previously trained machine-learning pipeline containing a classifier.
# X_train           - Training dataset containing input features.
# y_train           - Target labels corresponding to training data.
# X_test            - Testing dataset containing input features.
# y_test            - Actual target labels for the testing dataset.
# output            - Directory where the generated plot will be saved.
# importance_csv    - CSV file containing feature-importance rankings.
# top_k     = 5     - Selects the top five important numerical features.
# max_rows  = 4000  - Limits training samples to 4,000 for computational efficiency.
# seed      = 500   - Random seed to ensure reproducible sampling.

def plot_decision_boundary(model, X_train, y_train, X_test, y_test, output,
                           importance_csv = "feature_importance.csv", top_k = 5,
                           max_rows = 4000, seed = 500):
    
    # Reading feature importance.
    # index_col = 0 uses the first CSV column as the row index.
    # .iloc[:, 0] selects the first remaining column.
    importance                  = pd.read_csv(importance_csv, index_col = 0).iloc[:, 0]

    # pd.to_numeric() converts importance values into numerical format.
    # errors = "coerce" converts invalid values into NaN.
    # .dropna() removes missing or invalid values.
    # .sort_values(ascending = False) sorts the features from highest to lowest importance.

    importance                  = pd.to_numeric(importance, errors = "coerce").dropna().sort_values(ascending = False)

    # Selecting important numerical features.
    # A list containing the top five important numerical features that are actually available in the training dataset.

    # importance.index retrieves the feature names from the importance ranking.
    # X_train.select_dtypes(include = "number") selects only numerical columns from the training dataset.
    # .columns retrieves their column names.
    # if f in ... checks whether each ranked feature exists in the numerical training features.
    # [:top_k] selects only the first five features.

    features                    = [f for f in importance.index if f in X_train.select_dtypes(include = "number").columns][:top_k]

    # Checks whether at least two numerical features have been selected.
    # PCA requires at least two features to create two principal components.
    # If fewer than two features are available, the function raises a ValueError and stops execution.
    if len(features) < 2:
        raise ValueError("The importance CSV must rank at least two numerical training features.")

    # Sampling training data. Reduces computational cost when processing large datasets.

    # X_train[features] extracts only the selected important features.
    # len(X_train) calculates the total number of training rows.
    # min(max_rows, len(X_train)) ensures that the sample size does not exceed the available training rows.
    # .sample() randomly selects the required number of rows.
    # random_state = seed ensures reproducibility.

    train                       = X_train[features].sample(min(max_rows, len(X_train)), random_state = seed)

    # Selects the target labels corresponding to the sampled training rows.
    # .loc[train.index] ensures that the labels match the exact indices of the sampled training observations.
    y                           = y_train.loc[train.index]

    # Creating the preprocessing pipeline. Creates a pipeline containing three sequential operations.

    # SimpleImputer(strategy = "median"): Replaces missing values with the median of each feature.
    # StandardScaler()                  : Standardizes the features to make them comparable.
    # PCA(n_components = 2)             : Reduces the feature dimensions to two principal components, PC1 and PC2.
    
    transformer                 = make_pipeline(SimpleImputer(strategy = "median"), 
                                                StandardScaler(), 
                                                PCA(n_components = 2))

    # Applying PCA transformation. The resulting Z contains the training data transformed into two-dimensional PCA space.

    # fit() learns the median values, scaling parameters, and PCA components from the sampled training data.
    # transform() applies these learned transformations.
    # fit_transform() performs both operations together.
    Z                           = transformer.fit_transform(train)

    # Extracts the same selected features from the testing dataset.
    # Applies the preprocessing transformations learned from the training dataset.
    # Converts testing observations into the same two-dimensional PCA space.

    # [Very Very Important] It uses transform() rather than fit_transform() to AVOID learning 
    # new preprocessing parameters from the test data.

    Z_test                      = transformer.transform(X_test[features])

    # Training an auxiliary classifier.

    # model.named_steps["classifier"] retrieves the classifier named "classifier" from the original machine-learning pipeline.
    # clone() creates a fresh copy of that classifier without carrying over its previously learned parameters.
    # .fit(Z, y) trains this new classifier using the two-dimensional PCA-transformed training data and 
    # their corresponding target labels.

    # [WHY?] The original classifier may have been trained using many features. 
    # Visualizing its decision boundary directly in a two-dimensional graph is difficult.

    clf                         = clone(model.named_steps["classifier"]).fit(Z, y)

    # Generating the coordinate grid.

    # Z[:, 0] extracts the first principal component (PC1).
    # np.percentile(..., [1, 99]) calculates its 1st and 99th percentiles.
    # This determines the horizontal plotting range while excluding extreme values.
    # np.linspace() generates 130 evenly spaced values.
    # * operator unpacks the lower and upper percentile values as separate arguments.

    x, yy                       = np.meshgrid(np.linspace(*np.percentile(Z[:, 0], [1, 99]), 130),
                                              np.linspace(*np.percentile(Z[:, 1], [1, 99]), 130))

    # Converts the coordinate grid into a two-column array.
    # x.ravel() flattens the horizontal coordinate matrix.
    # yy.ravel() flattens the vertical coordinate matrix.
    # np.c_[] combines both arrays column-wise.
    grid                        = np.c_[x.ravel(), yy.ravel()]

    # Calculating classification scores.

    # hasattr(clf, "decision_function") checks whether the classifier provides a decision function.
    # If available, decision_function(grid) calculates decision scores.
    # Otherwise, predict_proba(grid)[:, 1] calculates the predicted probability of the positive class.  

    scores                      = clf.decision_function(grid) if hasattr(clf, "decision_function") else clf.predict_proba(grid)[:, 1]

    # Uses 0 for decision-function scores.
    # Uses 0.5 for predicted probabilities.
    threshold                   = 0 if hasattr(clf, "decision_function") else 0.5

    # Converts the flattened prediction scores back into the original two-dimensional grid shape.
    # This is necessary for creating contour plots.
    scores                      = scores.reshape(x.shape)

    # Creating the figure. fig represents the complete figure. ax represents the plotting area.
    fig, ax                     = plt.subplots(figsize = (8, 6))

    # Plotting the decision regions. Creates filled contour regions representing the classifier's predicted classes.
    
    # scores >= threshold   : Converts prediction scores into Boolean classifications.
    # levels                : Defines the contour boundaries.
    # cmap  = "coolwarm"    : Applies a blue-to-red color scheme.
    # alpha = .25           : Makes the background regions transparent.

    ax.contourf(x, yy, scores >= threshold, levels = [-.5, .5, 1.5], cmap = "coolwarm", alpha = .25)

    # Condition checks whether the decision threshold falls within the range of prediction scores.
    # scores.min() finds the minimum score. scores.max() finds the maximum score.
    # If the threshold lies between these values, a contour line is drawn.
    
    if scores.min() < threshold < scores.max():
        # ax.contour() draws the decision boundary as a black line.
        # levels = [threshold] specifies the classification threshold.
        # colors = "black" makes the boundary black.
        # linewidths = 1.4 sets the line thickness.
        ax.contour(x, yy, scores, levels = [threshold], colors = "black", linewidths = 1.4)

    # Selecting test observations. Prevents overcrowding the plot when the testing dataset is large.
    
    # np.random.default_rng(seed) creates a reproducible random-number generator.
    # len(X_test) calculates the total number of testing observations.
    # .choice() randomly selects observation indices.
    # size      = min(700, len(X_test)) selects at most 700 observations.
    # replace   = False prevents selecting the same observation more than once.
    
    positions                   = np.random.default_rng(seed).choice(len(X_test), size = min(700, len(X_test)), replace = False)

    # Creates a scatter plot of the selected test observations.

    # Z_test[positions, 0]          : Horizontal coordinates (PC1).
    # Z_test[positions, 1]          : Vertical coordinates (PC2).
    # np.asarray(y_test)[positions] : Uses actual test labels to determine point colors.
    # cmap      = "coolwarm"        : Uses the blue-to-red color scheme.
    # s         = 14                : Sets the marker size.
    # alpha     = .55               : Controls point transparency.
    # edgecolors = "none"           : Removes marker outlines.

    ax.scatter(Z_test[positions, 0], Z_test[positions, 1], c=np.asarray(y_test)[positions],
               cmap = "coolwarm", s = 14, alpha = .55, edgecolors = "none")

    # Adding labels and title. 
    # type(clf).__name__: Retrieves the classifier's class name.
    ax.set(xlabel = "PC1", ylabel = "PC2", title = f"{type(clf).__name__}: PCA of {len(features)} CSV-ranked features")

    # Adds a small explanatory note at the bottom of the figure.
    # It clarifies that the displayed decision boundary belongs to the auxiliary two-dimensional 
    # classifier, not the original high-dimensional model.
    fig.text(.12, .01, "Auxiliary 2D model; NOT the original high-dimensional boundary.", fontsize = 8)
    
    # Automatically adjusts the spacing between plot elements.
    # rect reserves a small amount of space at the bottom for the explanatory note.
    fig.tight_layout(rect = (0, .03, 1, 1))

    # Creating the output directory.
    output                      = Path(output)
    output.mkdir(parents = True, exist_ok = True)
    
    path                        = output / "decision_boundary_pca.png"

    # Saving and closing the figure.
    fig.savefig(path, dpi = 150)
    plt.close(fig)

    # Displaying information.
    print("Selected predictors:", features)

    # Displays the proportion of variance explained by each principal component.
    
    # transformer[-1] accesses the last pipeline step, which is PCA.
    # .explained_variance_ratio_ retrieves the variance explained by each principal component.
    # .round(3) rounds the values to three decimal places.
    print("PCA explained variance:", transformer[-1].explained_variance_ratio_.round(3))

    # Displays the location where the decision boundary image was saved.
    print("Saved:", path)
    
    return path

# ------------------------------------------------------------------------------------------- #