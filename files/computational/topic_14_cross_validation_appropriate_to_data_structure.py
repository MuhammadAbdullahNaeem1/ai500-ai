# ------------------------------------------------------------------------------------------- #
# Course    :   AI 500 Computational Tutorial
# Topic     :   14 - Cross-validation appropriate to data structure
#
# Purpose   :   The purpose of this code is to compare four cross-validation strategies for a 
#               patient deterioration prediction dataset and examine how each strategy splits 
#               the data into training and testing sets. It compares: 
#               KFold               - splits data into folds randomly. 
#               StratifiedKFold     - preserves the proportion of each target class. 
#               GroupKFold          - keeps each patient's records in either training or testing, 
#                                     not both. 
#               TimeSeriesSplit     - splits data according to time order. 
#               The code prints the training size, testing size, and number of patients shared 
#               between the two sets for the first two folds of each strategy. 
#               This helps identify potential data leakage, especially when multiple records 
#               belong to the same patient.
#
# Run       :   python .\topic_14_cross_validation_appropriate_to_data_structure.py
#
# Date      :   October 17, 2026
# ------------------------------------------------------------------------------------------- #

from sklearn.model_selection                    import (KFold, StratifiedKFold, 
                                                        GroupKFold, TimeSeriesSplit)

from tutorial_common                            import load_data, section

# ------------------------------------------------------------------------------------------- #
def run():

    section("TOPIC 14 — Cross-validation appropriate to data structure")

    # load_data(sample=30000) loads a sample of 30,000 records.
    # .sort_values("admission_timestamp") sorts the records by admission time, from earliest to latest by default.
    # .reset_index(drop=True) resets the DataFrame index to 0, 1, 2, ... and discards the old index.

    # Note: Sorting makes the dataset chronological, which is important when demonstrating time-based cross-validation.
    df              = load_data(sample =30000).sort_values("admission_timestamp").reset_index(drop = True)

    # Extract the target variable.
    # 1 - the patient deteriorated within 12 hours.
    # 2 - the patient did not deteriorate within 12 hours.
    y               = df["deterioration_within_12h"].to_numpy()

    # Extract patient identifiers.
    groups          = df["patient_id"].to_numpy()

    # Define the four cross-validation strategies.
    
    # KFold(5, ...) Divides the dataset into five folds. Each fold is used as the test set once.
    # StratifiedKFold(5, ...) Creates five folds while approximately preserving the target-class proportions in each fold.
    # GroupKFold(5) Creates five folds while keeping each patient's records together.
    # TimeSeriesSplit(5) Creates five sequential splits, using earlier records for training and later records for testing.
    splitters       = {"KFold"              : KFold(5, shuffle = True, random_state = 500),
                       "StratifiedKFold"    : StratifiedKFold(5, shuffle = True, random_state = 500),

                       # Standard GroupKFold(5) does not use the shuffle or random_state arguments here.
                       # Patient identifiers will be supplied later when generating the splits.
                       "GroupKFold(patient)": GroupKFold(5),
                       
                       # five sequential splits.
                       # Training data comes before the corresponding test data in the ordered dataset.
                       # It does not randomly shuffle the records.
                       "TimeSeriesSplit"    : TimeSeriesSplit(5),}

    # Loop through the strategies
    # .items() returns each dictionary key and its corresponding value. 
    # name stores the strategy's name. name stores the strategy's name.
    for name, cv in splitters.items():
        print(f"\n{name}")
        
        if name.startswith("Group"):
            print("What groups look like", groups)
            splits      = cv.split(df, y, groups)

        elif name.startswith("Stratified"):
            splits      = cv.split(df, y)

        else:
            splits      = cv.split(df)

        # Iterate through the folds.

        # splits provides pairs of training and testing indices. 
        # enumerate(splits, 1) numbers the folds starting from 1. 
        # fold stores the fold number. 
        # tr stores the training indices. 
        # te stores the testing indices.
        # For example: fold = 1,  tr = [0, 1, 2, ...], and te = [100, 101, 102, ...].
        for fold, (tr, te) in enumerate(splits, 1):
            
            # Calculate patient overlap.
            # df.iloc[tr]["patient_id"] retrieves the patient IDs in the training set.
            # df.iloc[te]["patient_id"] retrieves the patient IDs in the testing set.
            # set(...) converts each collection into a set of unique patient IDs.
            # & finds the intersection i.e., the patients appearing in both sets.
            # len(...) counts the number of shared patients.
            overlap     = len(set(df.iloc[tr]["patient_id"]) & set(df.iloc[te]["patient_id"]))

            # Print the fold statistics.
            print(f" fold {fold}: train = {len(tr):5d}, test = {len(te):5d}, patient overlap = {overlap}")
            # if fold == 2:
            #     break

    # Learning outcomes.
    print("\n [VERY IMPORTANT]: ")
    print("Use GroupKFold when you want to know whether your model can predict " \
          "deterioration for patients whose records were not used during training.")
    
    print("Use TimeSeriesSplit when your main objective is to predict future events " \
          "using past hospital data, simulating deployment over time.")

    print("If the objective is both future prediction and generalization to unseen patients, " \
          "use a custom split that respects chronology and patient separation.\n")
    
# ------------------------------------------------------------------------------------------- #
if __name__ == '__main__':
    run()

# ------------------------------------------------------------------------------------------- #