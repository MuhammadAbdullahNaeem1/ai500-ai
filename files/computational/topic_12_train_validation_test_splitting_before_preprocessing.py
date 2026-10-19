# ------------------------------------------------------------------------------------------- #
# Course    :   AI 500 Computational Tutorial
# Topic     :   12 - Train-validation-test splitting before preprocessing
#
# Purpose   :   The purpose of this code is to divide a dataset into training, validation, and 
#               test sets before performing any preprocessing. It uses stratified splitting to 
#               maintain a similar proportion of the target variable, deterioration_within_12h, 
#               in all three sets. 
#               Training set (60%)  : Used to train the machine learning model. 
#               Validation set (20%): Used to tune model parameters and compare models. 
#               Test set (20%)      : Used for the final, unbiased evaluation of model performance. 
#               The main goal is to prevent data leakage and ensure that the model is evaluated 
#               fairly on unseen data.
#
# Run       :   python .\topic_12_train_validation_test_splitting_before_preprocessing.py
#
# Date      :   October 17, 2026
# ------------------------------------------------------------------------------------------- #

from sklearn.model_selection            import train_test_split
from tutorial_common                    import load_data, section

# ------------------------------------------------------------------------------------------- #
def run():

    section("TOPIC 12 — Split before preprocessing")
    df                      = load_data()

    # Split the data into training/validation and test sets.

    # train_val: Receives 80% of the data, which will later be divided into training and validation sets.
    # test: Receives 20% of the data, reserved for final evaluation.
    # test_size = 0.20: Specifies that 20% of the dataset goes into the test set.

    # stratify = df["deterioration_within_12h"]: Maintains approximately the same proportion of 
    # positive and negative target values in both sets.
    
    # random_state = 500: Makes the split reproducible, so the same split can be obtained 
    # when the data and environment remain unchanged.
    train_val, test         = train_test_split(df, 
                                               test_size    = 0.20, 
                                               stratify     = df["deterioration_within_12h"], 
                                               random_state = 500)

    # Split the remaining data into training and validation sets.
    
    # train: Receives 75% of train_val.
    # val: Receives 25% of train_val.
    # test_size = 0.25: Specifies that 25% of the remaining data becomes the validation set.
    
    # stratify = train_val["deterioration_within_12h"]: Maintains approximately the same 
    # target-class proportions in the training and validation sets.

    # random_state = 500: Makes this split reproducible.
    train, val              = train_test_split(train_val, 
                                               test_size    = 0.25,
                                               stratify     = train_val["deterioration_within_12h"], 
                                               random_state = 500)

    # Print the dataset sizes
    print("Train / validation / test sizes:", len(train), len(val), len(test))

    # Print the target prevalence
    print("Target prevalence:",
          round(train["deterioration_within_12h"].mean(), 4),
          round(val["deterioration_within_12h"].mean()  , 4),
          round(test["deterioration_within_12h"].mean() , 4))

    print("\n [VERY IMPORTANT] Do NOT calculate imputation medians, scaling parameters, vocabularies, "
          "feature selection, PCA, or resampling statistics using validation/test data.")

# ------------------------------------------------------------------------------------------- #
if __name__ == '__main__':
    run()

# ------------------------------------------------------------------------------------------- #