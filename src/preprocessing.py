import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

# TODO Write it as class

# fit_transform, transform
# - columns to drop
# - numerical_imputer, categorical_imputer
# 

def data_preprocessing(df: pd.DataFrame, train_df = True) -> pd.DataFrame:

    """
    Preprocessing of the raw datasets

    :param df: dataset in dataframe format
    :type df: pd.DataFrame

    :return: clean dataframe
    :rtype: pd.DataFrame
    """

    

    return df



if __name__ == "__main__":

    import pandas as pd
    from src.dataset import load_dataset
    df = load_dataset(path="data/raw")
    print(df.head())