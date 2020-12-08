import pandas as pd

def feature_engineering(df: pd.DataFrame) -> pd.DataFrame:

    """
    Create new Features

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