
def create_targets(df, type:"string"):
    
    """
    
    Parameters
    ----------
    df: pd.DateFrame
        The training data frame
    type: string
        The type of targets to be constructed
        - 'boolean'
        - 'return', 'return_1', 'return_2', 'return_3', 'return_4'
        - 

    Returns
    -------
    pd.DataFrame
       the train_df with one additional column named `target` + type
       and without original columns for target
    
    """

    # --- Write function helpers ----
    # import pandas as pd
    # df = load_dataset()
    # df.head()


    if type == "binary":
        # Binary target (resp>0)
        df["target_binary"] = (df["resp"]>0).astype(int)
    
    elif type == "return":
        # resp 
        df["target_return"] = df["resp"]
    
    elif type == "return_1":
        # resp_1 
        df["target_return_1"] = df["resp_1"]

    elif type == "return_2":
        # resp_2
        df["target_return_2"] = df["resp_2"]
    
    elif type == "return_3":
        # resp_3
        df["target_return_3"] = df["resp_3"]

    elif type == "return_4":
        # resp_4
        df["target_return_4"] = df["resp_4"]
    
    else:
        raise Exception("This type isn't implemented")
    
    ## Drop unnecessary columns
    df.drop(["resp", "resp_1", "resp_2", "resp_3", "resp_4"], axis=1, inplace=True)

    return df



if __name__ == "__main__":


    import pandas as pd
    from dataset import load_dataset

    print("Loading dataset...")
    df = load_dataset()

    print("Creating targets...")
    df = create_targets(df, type = "binary")
    
    print(df.head())
    print(df.shape)