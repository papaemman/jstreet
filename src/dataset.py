

def load_dataset(path = "data/raw", dataset = "train"):
    """
    Load and merge all availables dataset
    
    :param: path: string (data path)
    :param: dataset: string ["train", "test", "train-test"]

    :return: pandas.DataFrame
    """

    import pandas as pd

    ## Load main dataset
    if dataset=="train":
        df = pd.read_csv(path+"/train.csv", encoding='mac_roman', low_memory=False)

    elif dataset=="test": 
        df = pd.read_csv(path+"/test.csv", encoding='mac_roman', low_memory=False)

    elif dataset=="train-test":
        # Load train and test datasets and keep only common columns
        df1 = pd.read_csv(path+"/train.csv", encoding='mac_roman', low_memory=False)
        df1["train"] = 1
        
        df2 = pd.read_csv(path+"/test.csv", encoding='mac_roman', low_memory=False)
        df2["compliance"] = -1
        df2["train"] = 0

        df1 = df1[df2.columns]
        df = pd.concat([df1,df2], axis = 0)
        del df1, df2

    else:
        raise Exception(":param:dataset must be specified and can be one of ['train', 'test', 'train-test']")


    ## Load additional datasets
    latlons_df = pd.read_csv(path+"/latlons.csv", encoding='mac_roman')
    addresses_df = pd.read_csv(path+"/addresses.csv", encoding='mac_roman')

    ## Merge additional datasets between them and with main dataset
    addresses_latlons_df = addresses_df.merge(latlons_df, on="address")
    del addresses_df, latlons_df

    df = df.merge(addresses_latlons_df, on="ticket_id")

    return df



if __name__ == "__main__":

    import pandas as pd
    df = load_dataset(path="../data/raw", train_df="test")
    print(df.head())
    print(df.shape)