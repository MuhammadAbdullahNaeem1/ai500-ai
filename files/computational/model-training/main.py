# ------------------------------------------------------------------------------------------- #
# Course    :   AI 500 Computational Tutorial
# Topic     :   Clinical Deterioration Prediction Using Machine Learning
#
# Purpose   :   This code trains and evaluates a machine learning classifier (Linear SVM, 
#               RBF SVM, or Random Forest) to predict clinical deterioration using patient data. 
#               It saves the trained model, evaluation results, feature importance, and 
#               test-set predictions for further analysis.
#
# Install   :   pip install pandas numpy scikit-learn joblib matplotlib seaborn
#
# Run       :   python main.py --classifier svm-linear --importance-csv "results\svm-linear\feature_importance.csv" --boundary-top-k 5      
#               python main.py --classifier svm-rbf --importance-csv "results\svm-rbf\feature_importance.csv" --boundary-top-k 5      
#               python main.py --classifier random-forest --importance-csv "results\random-forest\feature_importance.csv" --boundary-top-k 5      
#
# Date      :   November 13, 2026
# ------------------------------------------------------------------------------------------- #

# argparse  : Allows the user to provide input arguments when running the Python program from the command line.
# joblib    : Used to save the trained machine learning model to a file so it can be reused later without retraining.
import argparse, joblib

import pandas                               as pd                                           # Pandas library for handling and processing tabular data.

from pathlib                                import Path                                     # Path to manage file and directory paths.

# Imports functions and variables from the custom data.py file.
# TARGET        : Specifies the target column that the model needs to predict.
# load_csv      : Loads the dataset from a CSV file.
# make_features : Extracts and prepares input features for machine learning.
# grouped_split : Divides the dataset into training and testing sets while keeping patient groups separate.
from data                                   import TARGET, load_csv, make_features, grouped_split

# Imports components from the custom model.py file.
# CHOICES       : Contains the available classifier options, such as Linear SVM, RBF SVM, and Random Forest.
# build_pipeline: Creates the machine learning pipeline for the selected classifier.
from model                                  import CHOICES, build_pipeline

# Imports functions from evaluation.py.
# evaluate          : Evaluates the trained model using test data.
# feature_importance: Identifies which input features contribute most to the model's predictions.
# decision_scores   : Calculates the model's prediction scores.
from evaluation                             import evaluate, feature_importance, decision_scores

# Visualizing a Classification Decision Boundary Using PCA and Feature Importance.
from decision_boundary                      import plot_decision_boundary

# ------------------------------------------------------------------------------------------- #
def run(args):              # args contains the command-line arguments entered by the user.

    # Step # 1: Loads the CSV dataset using the load_csv() function.
    df                          = load_csv(args.csv)                        # args.csv specifies the dataset filename.
    
    # Step # 2: Split the Dataset. 
    
    # Divides the dataset into two subsets:
    # train : Used to train the machine learning model.
    # test  : Used to evaluate the trained model.
    # seed  = args.seed ensures reproducibility, meaning the same random split can be generated again.
    
    # grouped_split() keeps records belonging to the same patient in the same subset. 
    # This prevents patient data from appearing in both training and testing sets, reducing data leakage.
    train, test                 = grouped_split(df, seed = args.seed)

    # Step # 3: Limit SVM Training Data. 
    # [Important Note] This is only for the tutorial. SVM models, particularly RBF SVM, 
    # can require significant computational resources when trained on large datasets. 
    # Limiting the training rows reduces execution time.

    if args.classifier.startswith("svm") and len(train) > args.svm_max_rows:

        # [Very Important] The test dataset remains unchanged, so the model is still 
        # evaluated on the entire held-out test set.

        # n             = args.svm_max_rows specifies the maximum number of rows.
        # random_state  = args.seed ensures reproducibility.
        train                   = train.sample(n = args.svm_max_rows, random_state = args.seed)

        # Displays a message showing the number of training rows being used.
        # len(train) calculates the number of rows.
        # :, formats large numbers with commas.
        print(f"SVM training limited to {len(train):,} rows for classroom runtime.")

    # Step # 4: Preparing Features and Target Variables.
    
    # X_train: Contains the input features used to train the model.
    # y_train: Contains the actual target labels that the model needs to predict.   
    X_train, y_train            = make_features(train), train[TARGET]

    # X_test: Input features from the testing dataset.
    # y_test: Actual target labels used to compare against model predictions.
    X_test, y_test              = make_features(test), test[TARGET]

    # Displays important information about the dataset:
    # len(train)    : Number of training records.
    # len(test)     : Number of testing records.
    # y_test.mean() : Calculates the proportion of positive target labels.
    # .2% formats the positive rate as a percentage with two decimal places.

    print(f"Training: {len(train):,}; held-out test: {len(test):,}; " f"positive rate: {y_test.mean():.2%}")

    # Step # 5: Building and Training the Machine Learning Model.

    # Creates the machine learning pipeline using the selected classifier.
    # args.classifier specifies which algorithm to use.
    # seed = args.seed provides a random seed for reproducibility where applicable.

    # A pipeline may also include preprocessing steps, such as feature scaling, 
    # depending on how build_pipeline() is implemented.
    pipeline                    = build_pipeline(args.classifier, seed = args.seed)
    
    # Trains the selected machine learning model.
    # X_train provides the patient input features.
    # y_train provides the correct target labels.

    # During training, the algorithm learns patterns and relationships between 
    # patient characteristics and clinical deterioration.
    pipeline.fit(X_train, y_train)

    # Step # 5: Creating the Output Directory.

    # args.output specifies the main output directory.
    # args.classifier creates a separate subdirectory for the selected algorithm.
    out                         = Path(args.output) / args.classifier

    # parents   = True: Creates any missing parent directories.
    # exist_ok  = True: Prevents an error if the directory already exists.
    out.mkdir(parents = True, exist_ok = True)

    # Saving the Trained Model. The saved file is named model.joblib.
    # It can later be loaded using joblib.load() without training the model again.
    joblib.dump(pipeline, out / "model.joblib")

    # Step # 6: Evaluating Model Performance.

    # Evaluates the trained model using the testing dataset.
    # pipeline  : The trained machine learning model.
    # X_test    : Testing input features.
    # y_test    : Actual testing labels.
    # out       : Directory where evaluation results are saved.
    evaluate(pipeline, X_test, y_test, out)

    # Step # 7: Calculating Feature Importance and Visualize Decision Boundary.
    feature_importance(pipeline,                            # pipeline              : Trained machine learning pipeline.
                       X_test,                              # X_test                : Testing input features.
                       y_test,                              # y_test                : Actual testing labels.
                       out,                                 # out                   : Directory where feature importance results are saved.
                       seed     = args.seed,                # args.seed             : Ensures reproducibility.
                       max_rows = args.importance_rows)     # args.importance_rows  : Limits the number of rows used for feature importance analysis.

    if not args.skip_boundary:
        plot_decision_boundary(pipeline, 
                               X_train, y_train, 
                               X_test, y_test, 
                               out,
                               importance_csv   = args.importance_csv, 
                               top_k            = args.boundary_top_k,
                               max_rows         = args.boundary_train_rows, 
                               seed             = args.seed)    
    
    # Step # 8: Generating Test Predictions.

    # Creates a new DataFrame named predictions.
    # Copies three columns from the original testing dataset:
    # encounter_id  : Identifies the patient encounter.
    # patient_id    : Identifies the patient.
    # TARGET        : Contains the actual outcome.
    # .copy() creates an independent copy rather than modifying the original testing DataFrame.

    predictions                     = test[["encounter_id", "patient_id", TARGET]].copy()

    # Uses the trained model to predict the target class for each testing record.
    # Stores the predicted labels in a new column named predicted_class.
    predictions["predicted_class"]  = pipeline.predict(X_test)

    # Calculates a decision score for each testing record.
    # Stores the scores in a new column called score.
    # These scores indicate how strongly the model's decision function favors a particular class.
    predictions["score"]            = decision_scores(pipeline, X_test)

    # Saves all actual labels, predicted labels, patient IDs, encounter IDs, and scores into a CSV file.
    # The output file is named test_predictions.csv.
    # index = False prevents Pandas from adding an unnecessary index column.
    predictions.to_csv(out / "test_predictions.csv", index = False)

    # Step # 9: Displaying the Output Location.
    # Displays a message confirming where the output files have been saved.
    # out.resolve() returns the absolute path of the output directory.
    # \n adds a blank line before the message.
    print(f"\nSaved model, figures, metrics, and predictions to: {out.resolve()}")

    # Displays a reminder that SVM decision scores should not be interpreted as probabilities.
    print("Note: SVM scores are decision margins, NOT probabilities.")

# ------------------------------------------------------------------------------------------- #
# Defining the Main Function and Command-Line Arguments.
def main():
    # Creates an argument parser.
    # Allows users to configure the program through command-line arguments.
    # The description explains the purpose of the program.
    parser                          = argparse.ArgumentParser(description = "AI500 clinical deterioration classifier")

    # Adding Command-Line Arguments.

    # Defines the --csv argument. If the user does not provide a filename, the default dataset is used.  
    parser.add_argument("--csv"             , default   = "AI500_synthetic_multihospital_clinical_dataset.csv")

    # Defines the classifier selection argument.
    # choices = CHOICES restricts the user to the available classifiers.
    # The help parameter provides information about valid options.
    parser.add_argument("--classifier"      , choices   = CHOICES   , help      = "svm-linear, svm-rbf, or random-forest")

    # Defines the maximum number of training rows for SVM models.
    # type = int ensures the value is an integer.
    # The default value is 10,000. Helps control SVM computational costs.
    parser.add_argument("--svm-max-rows"    , type      = int       , default   = 10000, help = "Cap SVM training; kernel SVM scales poorly to 250k rows")
    
    # Defines the maximum number of rows used for feature importance analysis. The default is 250.
    parser.add_argument("--importance-rows" , type      = int       , default   = 250)
    
    # Defines the directory where model outputs will be saved.
    # The default directory is named results.
    parser.add_argument("--output"          , default   = "results")
    
    # Defines the random seed. The default value is 500. Helps make random operations reproducible.
    parser.add_argument("--seed"            , type      = int       , default   = 500)

    # Visualizing decision boundary.
    parser.add_argument("--boundary-top-k"      , type      = int                       , default   = 5     , help = "Top ranked numerical features used for PCA")
    parser.add_argument("--boundary-train-rows" , type      = int                       , default   = 4000  , help = "Training cap for auxiliary PCA classifier")
    parser.add_argument("--skip-boundary"       , action    = "store_true"              , help      = "Skip decision-boundary visualization")
    parser.add_argument("--importance-csv"      , default   = "feature_importance.csv"  , help      = "Existing feature-importance CSV (no recomputation)")

    # Parsing User Arguments.
    # Reads and processes the command-line arguments.
    # Stores the resulting values in the args object.
    args                            = parser.parse_args()

    # Asking the User to Select a Classifier.
    # Checks whether the user has provided a classifier through the command line.
    # If no classifier is selected, the program asks the user to choose one.
    if args.classifier is None:
        # Displays the available classifier options.
        print("Select a classifier: 1) Linear SVM  2) RBF SVM  3) Random Forest")

        # input() asks the user to enter 1, 2, or 3.
        # .strip() removes unnecessary spaces from the input.
        # zip() pairs the numbers with the classifier names in CHOICES.
        # dict() converts these pairs into a dictionary.
        # .get() retrieves the classifier corresponding to the user's selection.
        # The selected classifier is stored in args.classifier.
        args.classifier             = dict(zip(("1", "2", "3"), CHOICES)).get(input("Choice [1/2/3]: ").strip())

        # Checks whether the user's selection is invalid.
        # If no valid classifier was selected, the program displays an error and stops execution.
        if args.classifier is None: parser.error("Choose 1, 2 or 3.")

    # Running the Machine Learning Workflow.
    run(args)       # Calls the run() function. Passes all collected command-line arguments.

# ------------------------------------------------------------------------------------------- #
if __name__ == "__main__":
    
    main()

# ------------------------------------------------------------------------------------------- #