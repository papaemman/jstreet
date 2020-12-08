import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer


def data_preprocessing(df) -> pd.DataFrame:

    """
    Preprocessing of the train df

    - NA imputations
    - Drop rows with weight==0
    - Scaling
    - Categorical encoding

    """
    
    FEATURES = ["feature_" + str(i) for i in range(0,129)]
    df[FEATURES].isna().sum()
    
    ## ------ NA imputation for numericals --------

    numerical_imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
    df[FEATURES] = numerical_imputer.fit_transform(df[FEATURES])
    
    print("Statistics of Simple imputer with mean", numerical_imputer.statistics_)

    # Drop rows with weight==0
    df = df[df["weight"] != 0]


    return df



if __name__ == "__main__":

    import pandas as pd
    from src.dataset import load_dataset
    df = load_dataset(path="data/raw")
    print(df.head())