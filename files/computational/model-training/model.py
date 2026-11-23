# ------------------------------------------------------------------------------------------- #
# Course    :   AI 500 Computational Tutorial
# Topic     :   Machine Learning Classification Pipeline with Data Preprocessing
#
# Purpose   :   This code builds a reusable machine learning pipeline that handles missing 
#               values, scales numerical features, encodes categorical features, and trains 
#               one of three classification algorithms: Linear SVM, RBF SVM, or Random Forest. 
#               It ensures that preprocessing and classification are performed together in a 
#               consistent workflow.
#
# Install   :   pip install pandas scikit-learn
#
# Date      :   November 13, 2026
# ------------------------------------------------------------------------------------------- #

# Imports NUMERIC and CATEGORICAL from a module named data.
# NUMERIC contains the names of numerical columns (e.g., age, salary, income).
# CATEGORICAL contains the names of categorical columns (e.g., gender, city, occupation).
# These variables help identify which preprocessing operations should be applied to each type of feature.
from data                               import NUMERIC, CATEGORICAL

from sklearn.impute                     import SimpleImputer                        # handles missing values in datasets.
from sklearn.preprocessing              import OneHotEncoder, StandardScaler        # OneHotEncoder: Converts categorical values into numerical binary columns.
                                                                                    # StandardScaler: Standardizes numerical features so they have approximately zero mean and unit variance.

# ColumnTransformer allows different preprocessing operations to be applied to different groups of columns.
# For example, numerical columns can be scaled while categorical columns are encoded.
from sklearn.compose                    import ColumnTransformer

# Pipeline combines multiple machine learning operations into a single sequential workflow.
# Each step passes its output to the next step automatically.
from sklearn.pipeline                   import Pipeline

# LinearSVC : Uses a linear decision boundary to classify data.
# RBF       : Handles nonlinear classification problems.
from sklearn.svm                        import LinearSVC, SVC

# Random Forest combines multiple decision trees to produce a final classification prediction.
from sklearn.ensemble                   import RandomForestClassifier

# ------------------------------------------------------------------------------------------- #
# Defining available classifier choices.
# Creates a tuple containing the names of the three supported classification algorithms.
CHOICES                     = ("svm-linear", "svm-rbf", "random-forest")

# ------------------------------------------------------------------------------------------- #
# Defining the pipeline function.
# choice    : Specifies which classifier to use.
# seed = 500: Sets a default random seed for reproducibility where supported.
def build_pipeline(choice, seed = 500):
    # Creating the numerical preprocessing pipeline.
    
    # add_indicator = True creates additional binary features indicating which values were originally missing.
    # Standardizes numerical features. 
    # This is particularly useful for SVM models because they are sensitive to differences in feature scales.
    numerical               = Pipeline([("impute"   , SimpleImputer(strategy        = "median", add_indicator = True)),
                                        ("scale"    , StandardScaler())])

    # Creating the categorical preprocessing pipeline.

    # Replaces missing values with the most frequently occurring value (mode) in each column.
    # Converts categorical values into binary numerical columns.
    # handle_unknown = "ignore" prevents errors when the model encounters a category that was not present during training.
    categorical             = Pipeline([("impute"   , SimpleImputer(strategy        = "most_frequent")),
                                        ("encode"   , OneHotEncoder(handle_unknown  = "ignore"))])

    # Combining numerical and categorical preprocessing. This combines both preprocessing pipelines into one object.
    # ColumnTransformer determines which transformation should be applied to each group of columns.
    preprocess              = ColumnTransformer([("numeric"     , numerical     , NUMERIC),
                                                 ("categorical" , categorical   , CATEGORICAL)])

    # Selecting the Linear SVM classifier. Linear SVM attempts to separate classes using a linear decision 
    # boundary (a straight line in 2D or a hyperplane in higher dimensions).
    if choice == "svm-linear":
        # C             = 1.0       : Controls regularization. Smaller values allow more regularization, 
        #                             while larger values penalize classification errors more strongly.
        # class_weight  = "balanced": Automatically adjusts class weights inversely according to class frequencies. 
        #                             Useful for imbalanced datasets.
        # dual          = False     : Uses the primal optimization formulation instead of the dual formulation.
        # max_iter      = 5000      : Allows up to 5,000 iterations for model optimization.
        # random_state  = seed      : Sets the random seed where applicable.

        classifier          = LinearSVC(C               = 1.0, 
                                        class_weight    = "balanced", 
                                        dual            = False,
                                        max_iter        = 5000, 
                                        random_state    = seed)
    
    # SVM model using the Radial Basis Function (RBF) kernel.
    # RBF SVM can identify complex, nonlinear relationships between features and classes.
    # Unlike Linear SVM, it can create curved decision boundaries.
    elif choice == "svm-rbf":
        # C             = 1.0       : Controls the regularization strength and penalty for classification errors.
        # kernel        = "rbf"     : Uses the Radial Basis Function kernel to learn nonlinear decision boundaries.
        # gamma         = "scale"   : Automatically calculates gamma based on the number of features and their variance.
        # class_weight  = "balanced": Adjusts class weights to account for imbalanced class distributions.

        classifier          = SVC(C             = 1.0, 
                                  kernel        = "rbf", 
                                  gamma         = "scale", 
                                  class_weight  = "balanced")

    # Selecting the Random Forest classifier.
    # Random Forest combines predictions from multiple decision trees to produce a final classification result.
    # It can capture nonlinear relationships and feature interactions without requiring feature scaling.
    elif choice == "random-forest":
        # n_estimators      = 150                   : Builds 150 decision trees in the forest.
        # min_samples_leaf  = 3                     : Requires at least 3 training samples in each leaf node.
        # class_weight      = "balanced_subsample"  : Adjusts class weights separately for each bootstrap sample used to train a tree.
        # n_jobs            = -1                    : Uses all available CPU cores to speed up training.
        # random_state      = seed                  : Sets a random seed to improve reproducibility.

        classifier          = RandomForestClassifier(n_estimators       = 150, 
                                                     min_samples_leaf   = 3,
                                                     class_weight       = "balanced_subsample", 
                                                     n_jobs             = -1,
                                                     random_state       = seed)
    
    # Handling invalid classifier choices.
    else:
        # raise ValueError generates an error and stops execution.
        # The f-string displays the invalid classifier name and the available choices.
        raise ValueError(f"Unknown classifier: {choice}. Choose from {CHOICES}.")

    # Returning the complete machine learning pipeline. 
    # It combines preprocessing and classification into one complete pipeline.

    # ("preprocess", preprocess): First, handles missing values, scaling, and categorical encoding.
    # ("classifier", classifier): Then, passes the processed data to the selected classification algorithm.
    return Pipeline([("preprocess", preprocess), 
                     ("classifier", classifier)])

# ------------------------------------------------------------------------------------------- #