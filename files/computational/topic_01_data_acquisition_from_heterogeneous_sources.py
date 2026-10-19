# ------------------------------------------------------------------------------------------- #
# Course    :   AI 500 Computational Tutorial
# Topic     :   1 - Data acquisition from heterogeneous sources
#
# Purpose   :   - Load data from a CSV-like source into a Pandas DataFrame.
#               - Convert selected data into JSON to simulate the response from a public API.
#               - Inspect the source data to understand its columns and structure.
#
# Install   :   conda create -n AI500 python=3.12 
#               conda install conda-forge::pandas
#
# Run       :   python .\topic_01_data_acquisition_from_heterogeneous_sources.py
#
# Date      :   October 10, 2026
# ------------------------------------------------------------------------------------------- #

import json                                                                 # JSON stands for JavaScript Object Notation. 
                                                                            # It is a lightweight, text-based data format used to 
                                                                            # store and exchange information.

import pandas                   as pd                                       # Pandas is a Python library used for working with tabular data.

from io                         import StringIO                             # StringIO lets you treat a string as if it were a file.
from pprint                     import pprint                               # Print the records in a readable format.
from tutorial_common            import load_data, report_shape, section

# ------------------------------------------------------------------------------------------- #
def run():
    """
    Demonstrate CSV + JSON style ingestion and safe source inspection.
    """

    # Print a section heading.
    # Heterogeneous sources are sources that differ in format or structure, 
    # such as: CSV files JSON API responses SQL databases Excel spreadsheets

    section("TOPIC 01 - Data acquisition from heterogeneous sources")

    df                  = load_data(nrows = 20000)
    report_shape(df, "CSV extract")                                             # "CSV extract" is a label describing the data source.

    # A realistic public-API response is usually JSON. Here we convert a local
    # hospital sample to JSON so the exercise remains reproducible and offline.

    # In Pandas, df.loc[rows, columns] is used to select rows and columns from a DataFrame using their labels.
    # The column names must exist in df, or Pandas will raise a KeyError.

    # api_like = ( ... ) parentheses allow a long expression to be split across multiple lines for readability.                   

    api_like            = (df.loc[df["hospital_id"].eq("H01"),                  # selects the hospital_id column from df. eq() method means equals.             
                                  ["encounter_id",                              # identifies the encounter.
                                   "hospital_id",                               # identifies the hospital.
                                   "admission_timestamp",                       # records the admission time.
                                   "heart_rate_bpm",                            # records heart rate in beats per minute.
                                   "deterioration_within_12h"]].head(200))      # indicates whether deterioration occurred within 12 hours, according to the dataset's definition.
                                                                                # selects the first 200 rows of the filtered result.
    
    # orient = "records" represent each row as a JSON object and combine the objects into a list.
    # date_format = "iso" formats datetime values using the ISO 8601 date/time representation. E.g., 2026-10-10T08:30:00
    # payload is a string containing JSON text.

    # This process of converting a Python object or DataFrame into JSON text is called serialization.

    payload             = api_like.to_json(orient = "records", date_format = "iso")
    print(type(payload))

    records             = json.loads(payload)                                   # Convert JSON text back into Python objects.
                                                                                # .loads() means "load from a string".
    api_df              = pd.DataFrame(records)                                 # Converts the list of dictionaries into a Pandas DataFrame.
                                                                                # Dictionary keys become column names, and dictionary values become row values.
    report_shape(api_df, "API-like JSON response")

    print("\nSource-level checks:")
    print("CSV columns:", list(df.columns[:8]), "...")                          # Prints the first eight column names from the existing CSV DataFrame, df.
                                                                                # The ellipsis indicates that additional columns may exist.
    print("JSON keys:", list(records[0].keys()))                                # Displays the keys of the first dictionary in records.
    pprint(records) 

# ------------------------------------------------------------------------------------------- #
if __name__ == '__main__':
    run()

# ------------------------------------------------------------------------------------------- #