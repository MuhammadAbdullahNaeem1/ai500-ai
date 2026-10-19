# ------------------------------------------------------------------------------------------- #
# Course    :   AI 500 Computational Tutorial
# Topic     :   13 - Data-leakage demonstration
#
# Purpose   :   The purpose of this code is to demonstrate data leakage in a machine learning 
#               model by comparing two logistic regression models that predict whether a patient 
#               will deteriorate within the next 12 hours. 
#               Leakage-safe model: Uses only appropriate patient and admission features available 
#                                   for prediction. 
#               Leaked-feature model: Includes features such as ICU transfer and rapid response 
#                                     calls that may occur during the prediction period, giving the 
#                                     model access to future information. 
#               Both models are evaluated using ROC-AUC (Area Under the Receiver Operating 
#               Characteristic Curve). The leaked model may achieve a higher AUC, but that 
#               performance can be misleading because it relies on information that would 
#               not be available at prediction time.
#
# Run       :   python .\topic_13_data_leakage_demonstration.py
#
# Date      :   October 17, 2026
# ------------------------------------------------------------------------------------------- #

from sklearn.model_selection                    import train_test_split
from sklearn.compose                            import ColumnTransformer
from sklearn.preprocessing                      import OneHotEncoder, StandardScaler
from sklearn.impute                             import SimpleImputer
from sklearn.pipeline                           import Pipeline
from sklearn.linear_model                       import LogisticRegression
from sklearn.metrics                            import roc_auc_score

from tutorial_common                            import load_data, section

# ------------------------------------------------------------------------------------------- #
# This function trains a logistic regression model and returns its ROC-AUC score.
def fit_auc(cols, df, y):
    X                   = df[cols]

    # Splits the dataset into training and testing set.
    tr, te, ytr, yte    = train_test_split(X, y, test_size = .25, stratify = y, random_state = 500)

    # Creates a list called num containing the numerical features.
    # Excludes the three specified categorical columns.
    num                 = [c for c in cols if c not in ["admission_type", "hospital_id", "discharge_disposition"]]

    # Creates a list called cat containing categorical features.
    # These features represent categories or identifiers rather than continuous numerical measurements.
    cat                 = [c for c in cols if c in ["admission_type", "hospital_id", "discharge_disposition"]]

    # Data preprocessing via the ColumnTransformer
    # It applies the numerical preprocessing pipeline to the columns in num and the 
    # categorical preprocessing pipeline to the columns in cat, then combines the transformed features.

    # "num" for numerical features. 
    # Replaces missing numerical values with the median of the corresponding feature.
    # The median is calculated from the training data when the pipeline is fitted.
    # StandardScaler() is 0-mean, 1-variance normalization i.e., the z-score standardization.

    # "cat" for categorical features. 
    # Replaces missing categorical values with the most frequently occurring category in the training data.
    # OneHotEncoder() converts categorical values into numerical indicator columns.
    # handle_unknown = "ignore" prevents errors when a category appears in the test data but was not observed during training.
    prep    = ColumnTransformer([("num", Pipeline([("imp"  , SimpleImputer(strategy = "median")),
                                                   ("sc"   , StandardScaler())]), num),

                                 ("cat", Pipeline([("imp"   , SimpleImputer(strategy = "most_frequent")),
                                                   ("oh"    , OneHotEncoder(handle_unknown = "ignore"))]), cat)])

    # Creating and training the model.
    model   = Pipeline([("prep"   , prep),                                  # performs the preprocessing defined earlier
                        ("clf"    , LogisticRegression(max_iter = 1000))])  # the logistic regression classifier.
                                                                            # max_iter = 1000 allows up to 1,000 optimization iterations to help the model converge.
    
    # Trains the model using the training features (tr) and training labels (ytr).
    # Learns the imputation values, scaling parameters, encoding categories, and logistic regression coefficients.
    model.fit(tr, ytr)

    # model.predict_proba(te): Calculates the predicted probabilities for each class in the test set.
    # [:,1]: Selects the predicted probability of class 1, assumed here to represent deterioration within 12 hours.
    # roc_auc_score(yte, ...): Compares the predicted probabilities with the actual test labels and calculates the ROC-AUC score.
    # return: Sends the score back to the calling function.

    # AUC = 0.5: Performance equivalent to random ranking.
    # AUC = 0.7–0.8: Often considered acceptable discrimination.
    # AUC = 0.8–0.9: Often considered good discrimination.
    # AUC = 1.0: Perfect ranking on the evaluated dataset.
    return roc_auc_score(yte, model.predict_proba(te)[:,1])

# ------------------------------------------------------------------------------------------- #
def run():

    section("TOPIC 13 — Data-leakage demonstration")
    
    df              = load_data(sample = 100000)
    y               = df["deterioration_within_12h"]

    safe            = ["age_years","heart_rate_bpm","respiratory_rate_bpm",
                       "oxygen_saturation_pct","systolic_bp_mmHg","admission_type","hospital_id"]

    # The additional variables may contain information about events occurring after the prediction time.
    
    # rapid_response_called_next_12h: A rapid response call may directly reflect deterioration during the prediction period. 
    # icu_transfer_within_12h: An ICU transfer may be a consequence of the patient's deterioration. 
    # discharge_disposition: The final discharge destination may only be known later in the patient's stay. 
    # length_of_stay_days: The completed length of stay may not be known when the prediction is made.
    leaked          = safe + ["rapid_response_called_next_12h","icu_transfer_within_12h",
                              "discharge_disposition","length_of_stay_days"]

    print("Leakage-safe AUC:"   , round(fit_auc(safe, df, y), 3))
    print("Leaked-feature AUC:" , round(fit_auc(leaked, df, y), 3))
    
# ------------------------------------------------------------------------------------------- #
if __name__ == '__main__':
    run()

# ------------------------------------------------------------------------------------------- #