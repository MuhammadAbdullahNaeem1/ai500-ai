# ------------------------------------------------------------------------------------------- #
# Course    :   AI 500 Computational Tutorial
# Topic     :   11 - Class imbalance
#
# Purpose   :   This code demonstrates class imbalance in a dataset used to predict whether a 
#               patient will experience deterioration within 12 hours. It first examines the 
#               distribution of the target variable, evaluates a simple majority-class baseline 
#               model, and then applies two techniques to balance the classes: 
#               Random Oversampling and SMOTE. The main goal is to show why accuracy alone can 
#               be misleading when one class is much more common than the other, and how 
#               resampling can help address this problem.
#
# Install   :   conda install conda-forge::imbalanced-learn
#
# Run       :   python .\topic_11_class_imbalance.py
#
# Date      :   October 17, 2026
# ------------------------------------------------------------------------------------------- #

from sklearn.dummy                      import DummyClassifier
from sklearn.metrics                    import (accuracy_score, balanced_accuracy_score, 
                                                precision_score, recall_score, f1_score)
from imblearn.over_sampling             import RandomOverSampler, SMOTE                 # Python module to balance data set using under- and over-sampling

from tutorial_common                    import load_data, section

# ------------------------------------------------------------------------------------------- #
def run():
    
    section("TOPIC 11 — Class imbalance")

    # sample = 80_000 requests a sample of 80,000 records.
    df              = load_data(sample = 80000)

    # Select the target variable.
    y               = df["deterioration_within_12h"]
    print("Target prevalence:")
    print(y.value_counts(normalize = True).rename("proportion").round(4))       # value_counts(normalize=True) calculates the proportion 
                                                                                # of each target class rather than its raw count.
                                                                                # rename("proportion") labels the resulting series proportion.

    # Select the input features
    # .fillna(0) replaces missing values with zero.
    
    # [Becareful] Zero may not be a medically meaningful replacement for missing measurements. 
    # In a real clinical model, consider imputation methods such as median imputation and 
    # preserve missingness information where appropriate.
    X               = df[["age_years","heart_rate_bpm","respiratory_rate_bpm",
                          "oxygen_saturation_pct","systolic_bp_mmHg"]].fillna(0)

    # Create a majority-class baseline model
    # DummyClassifier creates a simple model that does not learn meaningful relationships 
    # between the features and the outcome.

    # strategy = "most_frequent" tells it to always predict the most common class in y.
    # .fit(X, y) fits the classifier and identifies the majority class.
    dummy           = DummyClassifier(strategy = "most_frequent").fit(X, y)
    pred            = dummy.predict(X)          # Uses the fitted classifier to generate predictions.
                                                # Because this is a majority-class classifier, every prediction will be the same class.

    print("\nMajority-class baseline:")
    print("accuracy ="          , round(accuracy_score(y, pred), 4))                    # proportion of predictions that are correct.
    
    # average recall across the classes. Unlike ordinary accuracy, it gives 
    # equal importance to each class.
    print("balanced accuracy =" , round(balanced_accuracy_score(y, pred), 4))

    # Measures the proportion of actual positive cases correctly identified.
    # Because the baseline never predicts the positive class, its 
    # positive-class recall is 0.0 if positive cases exist.
    print("recall positive ="   , round(recall_score(y, pred, zero_division = 0), 4))                                                                                   

    # Calculates the F1 score for the positive class. 
    # The F1 score is the harmonic mean of precision and recall.
    # It is useful when both false positives and false negatives matter.
    print("F1 positive ="       , round(f1_score(y, pred, zero_division = 0), 4))

    # Apply Random Oversampling. 
    # Random oversampling balances the classes by randomly duplicating examples from the minority class.
    ros             = RandomOverSampler(random_state = 500)         # Creates a RandomOverSampler object.
    
    # Xr contains the resampled input features.
    # yr contains the corresponding resampled target labels.
    Xr, yr          = ros.fit_resample(X, y)                        # learns the class distribution and resamples the dataset.
    print("\nRandomOverSampler class counts:", yr.value_counts().to_dict())

    # Apply SMOTE (Synthetic Minority Over-sampling Technique).
    # Instead of simply duplicating minority-class records, 
    # it generates synthetic minority-class examples by interpolating between 
    # existing minority-class neighbors.
    # The minority class must have enough samples for k_neighbors = 5 setting.
    sm              = SMOTE(random_state = 500, k_neighbors = 5)                # Creates a SMOTE sampler.
    
    # Xs contains the resampled features, including synthetic examples.
    # ys contains the corresponding target labels.
    Xs, ys          = sm.fit_resample(X, y)                                     # Applies SMOTE to the input features and target.
    print("SMOTE class counts:", ys.value_counts().to_dict())
    
    print("VERY IMPORTANT: resample TRAINING data only.")

# ------------------------------------------------------------------------------------------- #
if __name__ == '__main__':
    run()

# ------------------------------------------------------------------------------------------- #