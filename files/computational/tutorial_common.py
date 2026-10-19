# ------------------------------------------------------------ #
from pathlib                    import Path     # class that makes paths easier to create, inspect, and manipulate.

import warnings                                 # lets you control warning messages produced by your program and its libraries.

import numpy                    as np           # Imports NumPy, a library for numerical calculations, and gives it the short name np.
import pandas                   as pd           # Imports Pandas and gives it the alias pd.
import matplotlib.pyplot        as plt          # Imports Matplotlib's plotting interface as plt.

# ------------------------------------------------------------ #
RANDOM_STATE        = 500                                           # Fixed random seed for reproducible results.

PACKAGE_ROOT        = Path(__file__).resolve().parent               # determines the directory containing the Python file.

DATASET_PATH        = PACKAGE_ROOT / "AI500_synthetic_multihospital_clinical_dataset.csv"

# ------------------------------------------------------------ #
def dataset_path(datapath):
    
    if datapath.exists(): return datapath

    raise FileNotFoundError("Dataset not found. Put AI500_synthetic_multihospital_clinical_dataset.csv "
                            "in the package root or update DEFAULT_CANDIDATES in tutorial_common.py.")

# ------------------------------------------------------------ #
# Read the CSV file, optionally converts timestamp columns into 
# datetime values, and optionally selects a random sample of rows.

def load_data(nrows = None, sample = None, parse_dates = True, random_state = RANDOM_STATE):

    # Creates a list of column names that should represent dates and times.
    date_cols       = ["admission_timestamp",                   # When the patient was admitted.
                       "prediction_timestamp",                  # When a prediction was generated.
                       "vitals_recorded_timestamp",             # When vital signs were recorded.
                       "data_arrival_timestamp",                # When the data arrived in the system.
                       "lab_result_available_timestamp",]       # When a laboratory result became available.

    # Reads a CSV file into a Pandas DataFrame.

    # low_memory = False tells Pandas to use more memory to read the CSV file 
    # in a way that helps it determine the correct data types for each column.

    # pd.to_datetime() is a Pandas function that converts values into a 
    # date and time format so you can work with them easily.

    df              = pd.read_csv(dataset_path(DATASET_PATH), nrows = nrows, low_memory = False)    
    
    if parse_dates:                                                 # Checks whether timestamp conversion is enabled.
        for c in date_cols:                                         # Loops through each timestamp column name.
            if c in df.columns:                                     # Checks whether the current column exists in the DataFrame.
                df[c] = pd.to_datetime(df[c], errors = "coerce")    # Converts the values in column c into Pandas datetime values.
                                                                    # errors = "coerce" converts invalid or unparseable values into NaT (Not a Time).
    
    if sample is not None and len(df) > sample:                                     # Deciding whether to sample.
        df          = df.sample(sample, random_state = random_state).copy()         # Selecting a random sample.
                                                                                    # .copy() creates a separate DataFrame containing the selected rows.
        # The original DataFrame is no longer accessible through the variable df (unless you saved it in another variable).                                    
    
    return df

# ------------------------------------------------------------ #
# Cleaning categorical variables.

def clean_basic_categories(df):
    # Copies the input DataFrame into out, so the function can add 
    # new columns without directly modifying the original DataFrame.

    out             = df.copy()

    if "sex_raw" in out:                                                                    # Checks whether the DataFrame contains a column named sex_raw.
        out["sex_clean"]        = (out["sex_raw"].astype("string").str.strip().str.lower()
                                   .replace({"f":"female", "m":"male", "u":"unknown"}))
        
    if "smoking_status_raw" in out:                                                         # Checks whether the DataFrame contains the original smoking-status column.
        out["smoking_clean"]    = (out["smoking_status_raw"].astype("string").str.strip().str.lower()
                                   .replace({"n":"never", "fmr":"former", "c":"current"}))
        
    return out

# ------------------------------------------------------------ #
# Converting weight into kilograms.

def convert_weight_to_kg(df):
    out                 = df.copy()

    # Converting weight values to numbers.
    w                   = pd.to_numeric(out["weight_value"], errors = "coerce")             # errors = "coerce" converts invalid values to NaN.
    unit                = out["weight_unit"].astype("string").str.lower()                   # Standardizing the unit text.
    out["weight_kg"]    = np.where(unit.eq("lb").fillna(False), w / 2.2046226218, w)        # np.where(condition, value_if_true, value_if_false).

    # out["weight_kg"]    = np.where( unit.eq("lb").fillna(False), w / 2.2046226218, 
    #                                 np.where(unit.eq("kg").fillna(False), w, np.nan) )

    return out

# ------------------------------------------------------------ #
# Creating a path for output files.

def safe_output_path(filename):
    outdir              = PACKAGE_ROOT / "outputs"

    # This creates the outputs directory if it doesn't already exist.
    outdir.mkdir(exist_ok = True)                       # exist_ok = True means Python won't raise an error if that directory already exists.

    return outdir / filename

# ------------------------------------------------------------ #
# This savefig() function saves a Matplotlib plot as an image file, 
# stores it in your project's outputs folder, and then closes the 
# plot to free up resources.

def savefig(filename):
    path                = safe_output_path(filename)

    # Adjusts the spacing between plot elements so that titles, 
    # axis labels, and tick labels are less likely to overlap or get cut off.

    plt.tight_layout()

    # plt.savefig(path) saves the current Matplotlib figure to the specified path.
    
    # dpi = 150 sets the resolution to 150 dots per inch. 
    # This is generally suitable for reports and presentations.
    
    # bbox_inches = "tight" trims unnecessary whitespace around the 
    # figure while keeping its contents within the saved image.

    plt.savefig(path, dpi = 150, bbox_inches = "tight")
    plt.close()                                                 # Closes the current Matplotlib figure.
    
    print(f"Saved figure: {path}")                              # Prints a confirmation message showing where the image was saved.

# ------------------------------------------------------------ #
def section(title):
    print("\n" + "="*88)
    print(title)
    print("="*88)

# ------------------------------------------------------------ #
# prevalence() function calculates the proportion of 
# positive cases in a dataset while ignoring missing values (NaN).

def prevalence(y):                                              # The prevalence is the proportion of patients who have the disease.
    s               = pd.Series(y).dropna()                     # Converts y into a Pandas Series, which is a one-dimensional data structure.
    
    return float(s.mean()) if len(s) else np.nan

# ------------------------------------------------------------ #
# report_shape() prints the number of rows and columns in a 
# Pandas DataFrame in a readable format.

def report_shape(df, label = "Data"):
    print(f"{label}: {df.shape[0]:,} rows x {df.shape[1]} columns")     # An f-string allows Python to insert variable values directly into a string.
                                                                        # Inserts the row count with thousands separators.

# ------------------------------------------------------------ #
# require_columns() checks whether a DataFrame contains all the required columns.
# Suppresses FutureWarning messages so they don't appear in the output.

def require_columns(df, cols):
    # This is a list comprehension. It builds a list containing the 
    # required column names that are absent from the DataFrame.

    missing = [c for c in cols if c not in df.columns]
    
    if missing:
        raise KeyError(f"Missing required columns: {missing}")

# A FutureWarning indicates that some code uses behavior that may 
# change in a future version of a library.

# warnings.filterwarnings() configures how Python handles warnings.
# "ignore" do not display matching warnings.
# category = FutureWarning apply this rule only to FutureWarning messages.

warnings.filterwarnings("ignore", category = FutureWarning)

# ------------------------------------------------------------ #