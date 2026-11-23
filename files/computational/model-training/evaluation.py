# ------------------------------------------------------------------------------------------- #
# Course    :   AI 500 Computational Tutorial
# Topic     :   Machine Learning Model Evaluation and Permutation-Based Feature Importance
#
# Purpose   :   This code evaluates a trained binary classification model using multiple 
#               performance metrics, generates evaluation plots, and identifies the most 
#               influential input features using permutation importance. It saves all 
#               evaluation results, graphs, and feature importance rankings to specified 
#               output files. The code is particularly useful for evaluating classification 
#               models on held-out test data, such as patient-level datasets.
#
# Date      :   November 13, 2026
# ------------------------------------------------------------------------------------------- #

import pandas                       as pd
import matplotlib.pyplot            as plt


from pathlib                        import Path

# permutation_importance is used to determine how important each input feature is to the model's predictive performance.
# It works by randomly shuffling one feature at a time and measuring how much the model's performance decreases.
from sklearn.inspection             import permutation_importance

# Imports different evaluation metrics and visualization functions from Scikit-learn.

# accuracy_score            - Calculates the overall percentage of correct predictions.
# balanced_accuracy_score   - Calculates average recall across both classes, accounting for class imbalance.
# confusion_matrix          - Calculates true positives, true negatives, false positives, and false negatives.
# ConfusionMatrixDisplay    - Visualizes the confusion matrix.
# f1_score                  - Calculates the harmonic mean of precision and recall.
# precision_score           - Measures how many predicted positive cases are actually positive.
# recall_score              - Measures how many actual positive cases the model correctly identifies.
# roc_auc_score             - Measures the model's ability to distinguish between positive and negative classes using AUROC.
# average_precision_score   - Summarizes the precision-recall performance using average precision.
# RocCurveDisplay           - Generates the ROC curve.
# PrecisionRecallDisplay    - Generates the precision-recall curve.

from sklearn.metrics                import (accuracy_score, balanced_accuracy_score, confusion_matrix,
                                            ConfusionMatrixDisplay, f1_score, precision_score,
                                            recall_score, roc_auc_score, average_precision_score,
                                            RocCurveDisplay, PrecisionRecallDisplay)

# ------------------------------------------------------------------------------------------- #
# Obtain continuous prediction scores rather than only predicted class labels.

# ROC-AUC and Average Precision require continuous prediction scores rather than just binary 
# predictions (0 or 1). This function provides a common way to obtain those scores from 
# different types of classification models.

# model : The trained machine learning classification model.
# X     : The input features or test dataset.

def decision_scores(model, X):
    # hasattr(model, "predict_proba") checks whether the model has a method called predict_proba.
    # predict_proba(X) calculates the predicted probability of each class for every observation.
    # [:, 1] selects the probability of class 1 (the positive class).

    if hasattr(model, "predict_proba"): return model.predict_proba(X)[:, 1]

    # If the model does not support predict_proba, the function uses decision_function(X) instead.
    # This method returns continuous decision scores indicating how strongly the model favours a particular class.
    # Positive and negative score values generally indicate different sides of the classification decision boundary.

    return model.decision_function(X)

# ------------------------------------------------------------------------------------------- #
# Evaluation function.

# model : The trained classification model.
# X     : The test input features.
# y     : The actual test labels.
# output: The directory where evaluation results and plots will be saved.
def evaluate(model, X, y, output):
    # Creating the output directory.
    output                  = Path(output)

    # parents   = True: Creates any missing parent directories.
    # exist_ok  = True: Prevents an error if the directory already exists.
    output.mkdir(parents = True, exist_ok = True)

    # Generating predictions.
    # Uses the trained model to predict the class labels for the test observations.
    # Returns binary predictions, typically 0 or 1.
    prediction              = model.predict(X)

    # Obtains continuous prediction scores or probabilities for the positive class.
    # These scores are used to calculate ROC-AUC, Average Precision, and generate performance curves.
    score                   = decision_scores(model, X)

    # Calculating the confusion matrix.
    # This calculates the confusion matrix by comparing actual labels (y) with predicted labels (prediction).

    # labels = [0, 1] argument ensures that the matrix follows the specified class order.
    # .ravel() method converts the 2 × 2 confusion matrix into a one-dimensional array 
    # so that its four values can be assigned to the variables.

    tn, fp, fn, tp          = confusion_matrix(y, prediction, labels = [0, 1]).ravel()

    # Calculating evaluation metrics.
    # Creates a Python dictionary called metrics to store all model evaluation results.

    # zero_division = 0 ensures that the function returns zero instead of raising a warning when there are no positive predictions.
    metrics = {"accuracy"               : accuracy_score(y, prediction),                        # (TP + TN)/(TP + TN + FP + FN).
               "balanced_accuracy"      : balanced_accuracy_score(y, prediction),               # 0.5 * (sensitivity + specificity).
               "precision"              : precision_score(y, prediction, zero_division = 0),    # TP/(TP + FP).
               "recall_sensitivity"     : recall_score(y, prediction, zero_division = 0),       # TP/(TP + FN).
               "specificity"            : tn / (tn + fp),                                       # TN/(TN + FP).
               "f1"                     : f1_score(y, prediction, zero_division = 0),           # (2 * Precision * Recall)/(Precision + Recall).
               
               # Measures how effectively the model distinguishes positive cases from 
               # negative cases across different classification thresholds.
               "roc_auc"                : roc_auc_score(y, score),

               # Calculates Average Precision (AP) using the precision-recall curve.
               # Evaluates the balance between precision and recall across different classification thresholds. 
               "average_precision"      : average_precision_score(y, score),

               # Calculates the proportion of positive observations in the actual test dataset.
               "positive_prevalence"    : y.mean(),}                                            # No. of positive cases/Total No. of cases.

    # Saving evaluation metrics.

    # pd.Series(metrics)    : Converts the dictionary into a Pandas Series.
    # .rename("value")      : Names the output column value.
    # .to_csv()             : Saves the evaluation metrics as a CSV file.
    # output / "metrics.csv": Specifies the output file location.
    # header    = True      : Includes the column name in the CSV file.

    pd.Series(metrics).rename("value").to_csv(output / "metrics.csv", header = True)

    # Displaying evaluation metrics.
    # .round(4)             : Rounds the metric values to four decimal places.
    # .to_string()          : Converts the Series into a readable text representation.
    print("\nHeld-out patient-level test metrics:\n", pd.Series(metrics).round(4).to_string())

    # Generating the confusion matrix plot.
    # labels    = [0, 1]    : Specifies the order of the classes.
    # cmap      = "Blues"   : Uses a blue colour scheme to represent the matrix values.
    ConfusionMatrixDisplay.from_predictions(y, prediction, labels = [0, 1], cmap = "Blues")

    # Automatically adjusts spacing so that plot elements do not overlap.
    # Saves the confusion matrix as a PNG image.
    # dpi       = 160       : Sets the image resolution to 160 dots per inch.
    # Closes the current figure and releases memory.
    plt.tight_layout(); plt.savefig(output / "confusion_matrix.png", dpi = 160); plt.close()

    # Generating the ROC curve. 
    # It illustrates how the model's classification performance changes at different decision thresholds.
    
    # Uses actual labels (y) and continuous prediction scores (score).
    # True Positive Rate (Sensitivity) on the Y-axis.
    # False Positive Rate (1 − Specificity) on the X-axis.
    RocCurveDisplay.from_predictions(y, score)
    plt.tight_layout(); plt.savefig(output / "roc_curve.png", dpi = 160); plt.close()

    # Generating the Precision-Recall curve.
    # Generates a Precision-Recall curve using actual labels and continuous prediction scores.
    # Plots precision against recall at different classification thresholds.
    # This curve is particularly useful when the dataset is imbalanced.
    PrecisionRecallDisplay.from_predictions(y, score)
    plt.tight_layout(); plt.savefig(output / "precision_recall_curve.png", dpi = 160); plt.close()

    # Returning the metrics.
    return metrics

# ------------------------------------------------------------------------------------------- #
# Defines a function to calculate permutation-based feature importance.
# Calculates permutation importance using the original input features and held-out observations.

# model                     : The trained classification model.
# X                         : Input features.
# y                         : Actual target labels.
# output                    : Directory where results will be saved.
# seed          = 500       : Random seed to make sampling and permutation reproducible.
# max_rows      = 250       : Maximum number of observations used for calculating feature importance.
# repeats       = 2         : Number of times each feature is randomly shuffled.

def feature_importance(model, X, y, output, seed = 500, max_rows = 250, repeats = 2):
    # Selecting observations.
    # Permutation importance can be computationally expensive. Sampling reduces the computational cost.
    
    # X.sample()            : Randomly selects rows from the dataset.
    # min(max_rows, len(X)) : Selects the smaller of 250 or the total number of available observations.
    # random_state = seed   : Ensures that the same observations are selected when the function is 
    #                         executed again with the same data and seed.

    Xs                      = X.sample(min(max_rows, len(X)), random_state = seed)

    # Selects the corresponding target labels for the sampled observations.
    # This ensures that the sampled features and target labels remain correctly aligned.

    # Xs.index contains the indices of the selected rows.
    # y.loc[Xs.index] retrieves the target labels belonging to those same rows.
    ys                      = y.loc[Xs.index]

    # Calculating permutation importance.
    # It calculates how much the model's predictive performance decreases when individual features are randomly shuffled.
    result                  = permutation_importance(model,                                 # The trained machine learning model being evaluated.
                                                     Xs,                                    # The sampled input features used for the calculation.
                                                     ys,                                    # The actual target labels corresponding to the sampled observations.
                                                     
                                                     # The importance of each feature is determined by measuring how much AP decreases after that feature is shuffled.
                                                     
                                                     # A large decrease in Average Precision indicates that the feature is important to the model.
                                                     # A small decrease indicates that the feature has relatively little impact.
                                                     # A negative decrease can indicate that shuffling the feature improved performance.

                                                     scoring        = "average_precision",  # Uses Average Precision (AP) as the performance metric.
                                                     
                                                     n_repeats      = repeats,              # Specifies how many times each feature is randomly shuffled.
                                                     random_state   = seed,                 # Controls the random permutations.

                                                     # Avoids parallel processing and can make execution more predictable, although it may be slower.
                                                     n_jobs         = 1)                    # Uses one CPU process for the computation.

    # Extracting feature importance values.
    # result.importances_mean   : Contains the mean performance decrease for each feature across all permutation repetitions.
    # index     = X.columns     : Assigns the original feature names as the Series index.
    # name      = "AP decrease" : Names the Series AP decrease.
    importance              = pd.Series(result.importances_mean, index = X.columns, name = "AP decrease")
    
    # Sorting feature importance.
    # ascending = False         : Places the highest importance values at the top.
    importance              = importance.sort_values(ascending = False)

    # Saving feature importance results.
    # header    = True          : Includes the column name.
    importance.to_csv(Path(output) / "feature_importance.csv", header = True)

    # Displaying the top 12 features.
    # importance.head(12)       : Selects the first 12 features from the sorted Series.
    # .round(4)                 : Rounds importance values to four decimal places.
    # .to_string()              : Converts the results into readable text.
    # print()                   : Displays the results in the console.
    print("\nTop permutation importances (decrease in average precision):\n", importance.head(12).round(4).to_string())

    # Creating the feature importance plot.
    # importance.head(15)       : Selects the 15 most important features.
    # .sort_values()            : Sorts them in ascending order for plotting.
    # .plot.barh()              : Creates a horizontal bar chart.
    # figsize   = (9, 6)        : Sets the plot dimensions to 9 inches wide and 6 inches high.
    
    importance.head(15).sort_values().plot.barh(figsize = (9, 6))
    
    plt.xlabel("Decrease in average precision when permuted")                               # Sets the X-axis label.
    plt.title("Held-out permutation feature importance")                                    # Sets the title of the feature importance plot.
    plt.tight_layout(); plt.savefig(Path(output) / "feature_importance.png", dpi = 160)
    plt.close()

# ------------------------------------------------------------------------------------------- #