# ------------------------------------------------------------------------------------------- #
# Course    :   AI 500 Computational Tutorial
# Topic     :   22 - Transformations of numerical features
#
# Purpose   :   This code demonstrates log transformation of numerical features to examine how 
#               it affects the distribution of data. It compares four numerical variables before 
#               and after applying np.log1p(). It calculates their skewness and median to help 
#               determine whether the log transformation makes the data distribution less skewed.
#
# Run       :   python .\topic_22_transformations_of_numerical_features.py
#
# Date      :   October 24, 2026
# ------------------------------------------------------------------------------------------- #

import numpy                                as np
import pandas                               as pd

from scipy.stats                            import skew
from tutorial_common                        import load_data, section

# ------------------------------------------------------------------------------------------- #
def run():
    
    section("TOPIC 22 — Transformations of numerical features")
    
    df                      = load_data(sample = 100000)
    cols                    = ["healthcare_cost_usd", "glucose_mg_dl", "wbc_10e9_l", "lactate_mmol_l"]

    rows                    = []
    for c in cols:
        x                   = df[c].dropna()                    # .dropna() removes missing values (NaN). The remaining values are stored in x.
        
        # Apply the log transformation.
        # It is often useful for reducing right skewness, especially when data contain a few very large values.
        logx                = np.log1p(x)                       # np.log1p(x) calculates log(1 + x).

        rows.append({"variable"         : c,                    # Stores the column name.
                     "raw_skew"         : skew(x),              # Calculates skewness before transformation.
                     "log1p_skew"       : skew(logx),           # Calculates skewness after transformation.
                     "raw_median"       : x.median(),           # Calculates the original median.
                     "log1p_median"     : np.median(logx),})    # Calculates the median after transformation.

    # The transformation appears most effective for healthcare cost, followed by glucose and WBC. 
    # Lactate improves too, but some right-skewness remains.
    
    # Practical recommendation: If your goal is to prepare these features for machine learning, 
    # consider using log1p for variables with strong right-skewness, especially healthcare cost. 
    # Evaluate the effect on your chosen model rather than assuming every feature must be transformed.
    print(pd.DataFrame(rows).round(3))

# ------------------------------------------------------------------------------------------- #
if __name__ == '__main__':
    run()

# ------------------------------------------------------------------------------------------- #