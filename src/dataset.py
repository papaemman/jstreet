
def load_dataset():
    
    """
    Load trainind dataset
    
    :return: pandas.DataFrame
    """
    import pandas as pd
    df = pd.read_csv("input/jane-street-market-prediction/train.csv")
    return df



if __name__ == "__main__":

    import pandas as pd
    df = load_dataset()
    print(df.head())
    print(df.shape)