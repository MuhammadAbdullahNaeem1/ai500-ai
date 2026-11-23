# ------------------------------------------------------------------------------------------- #
# Course    :   AI 500 Computational Tutorial
# Topic     :   Machine Learning Model Prediction on New CSV Data
#
# Purpose   :   This code loads a previously trained machine learning model, reads new 
#               patient/encounter data from a CSV file, generates the required features, and 
#               predicts the class and corresponding decision scores. It then saves the 
#               predictions into a new CSV file.
#
# Date      :   November 13, 2026
# ------------------------------------------------------------------------------------------- #

"""Apply a previously saved model to new encounter rows."""
import argparse, joblib

import pandas                       as pd

from pathlib                        import Path

from data                           import make_features
from evaluation                     import decision_scores

# ------------------------------------------------------------------------------------------- #
# Defining the Main Prediction Function.

# model_path: Location of the previously trained model.
# input_csv : Location of the new input dataset.
# output_csv: Location where the prediction results will be saved.

def run(model_path, input_csv, output_csv):
    # Loads the previously trained machine learning model from the specified file.
    # The loaded model can now be used to make predictions on new data.
    # This avoids training the model again every time predictions are required.
    model                   = joblib.load(model_path)

    # Reads the input CSV file using Pandas.
    # low_memory = False instructs Pandas to read the file without processing it in smaller 
    # chunks for automatic data-type inference. This can help avoid inconsistent column-type warnings.
    df                      = pd.read_csv(input_csv, low_memory = False)

    # Converts the raw dataset into the required feature representation.
    # These features will be provided to the trained model for prediction.
    X                       = make_features(df)

    # Preparing the Output DataFrame.
    # Retains the patient and encounter identifiers (when available) so that each 
    # prediction can be associated with its corresponding record.

    # ("encounter_id", "patient_id"): Specifies the two identifiers to retain from the original dataset.
    # df[[...]]                     : Selects the available identifier columns.
    # .copy()                       : Creates an independent copy rather than modifying the original DataFrame.
    out                     = df[[c for c in ("encounter_id", "patient_id") if c in df]].copy()
    
    # model.predict(X) generates the predicted class labels.
    # These predictions are stored in a new column named predicted_class.
    out["predicted_class"]  = model.predict(X)

    # Passes the trained model and processed features to calculate decision scores.
    # Stores the resulting values in a new column called score.
    # [Very Important] For SVMs, these scores generally represent decision margins rather than probabilities.
    out["score"]            = decision_scores(model, X)

    # Saving the Prediction Results.
    # output_csv specifies the destination and filename.
    # index = False prevents Pandas from adding an extra index column to the output file.
    out.to_csv(output_csv, index = False)

    # Displays a confirmation message after saving the predictions.
    # len(out) calculates the total number of prediction records.
    # :, formats the number with thousands separators.
    # {output_csv} displays the output file location.
    print(f"Wrote {len(out):,} predictions to {output_csv}")   

# ------------------------------------------------------------------------------------------- #
if __name__ == "__main__":
    # Creates an argument parser.
    # The description explains that the script is used to generate predictions on a new CSV dataset.
    parser                  = argparse.ArgumentParser(description = "Predict on a new CSV")

    # Defines a command-line argument called --model.
    # Specifies the path of the trained model file. required = True means the user must provide this argument.
    parser.add_argument("--model"   , required  = True)
    
    # Defines the --csv argument.
    # Specifies the input CSV file containing new data. It is also required.
    parser.add_argument("--csv"     , required  = True)

    # Defines the --output argument.
    # Specifies the filename for saving predictions.
    # If the user does not provide an output filename, the default is new_predictions.csv.
    parser.add_argument("--output"  , default   = "new_predictions.csv")

    # Reads the arguments supplied by the user through the command line.
    # a.model contains the model file path.
    # a.csv contains the input CSV path.
    # a.output contains the output CSV path.
    a                       = parser.parse_args()

    # Passes the three command-line arguments to a run() function. Executes the complete prediction process.
    run(a.model, a.csv, a.output)

# ------------------------------------------------------------------------------------------- #