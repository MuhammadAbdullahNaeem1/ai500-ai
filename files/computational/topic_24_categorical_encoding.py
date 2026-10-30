# ------------------------------------------------------------------------------------------- #
# Course    :   AI 500 Computational Tutorial
# Topic     :   24 - Categorical encoding
#
# Purpose   :   This code demonstrates three techniques for encoding categorical data so that 
#               machine-learning algorithms can work with it: 
#               - One-hot encoding: Converts categories such as hospital IDs, admission types, 
#                                   and insurance types into separate binary columns. 
#               - Ordinal encoding: Converts ordered categories, such as socioeconomic quintiles 
#                                   (1–5), into numerical values. 
#               - Frequency encoding: Replaces each preferred language with the proportion of 
#                                     records belonging to that language. 
#               The code loads a sample of data, applies these encoding methods, and prints 
#               example results to show how categorical values are transformed.
#
# Run       :   python .\topic_24_categorical_encoding.py
#
# Date      :   October 24, 2026
# ------------------------------------------------------------------------------------------- #

import pandas                                   as pd

from tutorial_common                            import load_data, section
from sklearn.preprocessing                      import OneHotEncoder, OrdinalEncoder

# ------------------------------------------------------------------------------------------- #
def run():  

    section("TOPIC 24 — Categorical encoding")
    
    df                  = load_data(sample = 20000)

    # Creates a list containing three categorical column names.
    # These columns will be converted using one-hot encoding.
    onehot_cols         = ["hospital_id", "admission_type", "insurance_type"]

    # Create the one-hot encoder.
    
    # handle_unknown = "ignore" means that if the encoder encounters a category it did not see 
    # during fitting, it will not raise an error. 
    # For that feature, the unknown category is represented by zeros.

    # sparse_output = False tells the encoder to return a regular, dense NumPy array rather than a sparse matrix.
    enc                 = OneHotEncoder(handle_unknown = "ignore", sparse_output = False)
    
    # Fit and transform the selected columns.
    # Learns the unique categories present in each selected column and 
    # converts each row into its one-hot encoded representation.
    Z                   = enc.fit_transform(df[onehot_cols])

    print("One-hot shape:"      , Z.shape)                              # Displays the dimensions of the encoded array.
    print("First encoded names:", enc.get_feature_names_out()[:12])     # Print the first 12 encoded feature names

    # Creates an OrdinalEncoder for the socioeconomic_quintile column.

    # categories = [[1, 2, 3, 4, 5]]: Specifies the allowed categories in their intended order. 
    # The outer list corresponds to one input column.
    # handle_unknown = "use_encoded_value": Tells the encoder how to handle a category not listed in categories.
    # unknown_value = -1: Assigns -1 to an unknown category.

    ord_enc             = OrdinalEncoder(categories     = [[1, 2, 3, 4, 5]],
                                         handle_unknown = "use_encoded_value",
                                         unknown_value  = -1)

    # Transform the socioeconomic column.
    # fit_transform() learns the specified categories and converts the values into numerical codes.
    socioeconomic       = ord_enc.fit_transform(df[["socioeconomic_quintile"]])

    # Print the first 10 ordinal values. socioeconomic[:10] selects the first 10 rows.
    # .ravel() flattens the two-dimensional array into a one-dimensional array for easier printing.
    print("\nOrdinal encoding first 10:", socioeconomic[:10].ravel())

    # Calculate frequency encoding.
    # Frequency encoding represents how common a category is; it does not represent an inherent order or importance.

    # df["preferred_language"] selects the preferred language column.
    # .value_counts(normalize = True) calculates the proportion of records belonging to each language.
    # .map(...) replaces each language in the original column with its corresponding proportion.

    freq                = df["preferred_language"].map(df["preferred_language"].value_counts(normalize = True))
    
    print("\nFrequency encoding example:")

    # Display the original languages alongside their frequencies.
    print(pd.DataFrame({"language":df["preferred_language"], "freq":freq}).head(10))

# ------------------------------------------------------------------------------------------- #
if __name__ == '__main__':
    run()

# ------------------------------------------------------------------------------------------- #