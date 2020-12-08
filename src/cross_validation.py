import pandas as pd
from sklearn import model_selection

"""
This is a time series dataset, so I have to do a time-series CV
based on date column.

There are 500 days in train dataset


-- holdout_nbofdays       : Holdout the last nbofdays as validation dataset

    train days     +    valid days
 (500 - nbofdays)        nbofdays


-- ts.3fold.cv_nbofdays  : Create 3 fold time series CV. 

    train days        +  valid_days_1    +  valid_days_2  +  valid_days_3   
 (500 - 3*nbofdays)       nbofdays           nbofdays          nbofdays 

fold 1: train_days                                 -- valid_days_1
fold 2: train_days + valid_days_1                  -- valid_days_2
fold 3: train_days + valid_days_1 + valid_days_2   -- valid_days_3

"""


class CrossValidation:
    
    def __init__(self, df, time_col, problem_type = "holdout_50", random_state=42):
        self.dataframe = df
        self.time_col = time_col
        self.problem_type = problem_type
        self.random_state = random_state        
        self.dataframe["kfold"] = -1
        self.unique_dates = self.dataframe[self.time_col].unique()
    
    
    def split(self):
        
        if self.problem_type.startswith("holdout_"):

            self.holdout_days = int(self.problem_type.split("_")[1])
            days_to_keep = self.unique_dates[:-self.holdout_days ]

            self.dataframe.loc[self.dataframe[self.time_col].isin(days_to_keep), "kfold"] = 0
            self.dataframe.loc[~self.dataframe[self.time_col].isin(days_to_keep), "kfold"] = 1

        elif self.problem_type.startswith("ts.3fold.cv_"):

            self.holdout_days  = int(self.problem_type.split("_")[1])
            days_train = self.unique_dates[:-3*(self.holdout_days )]
            days_valid_1 = self.unique_dates[-3*(self.holdout_days):-2*(self.holdout_days )]
            days_valid_2 = self.unique_dates[-2*(self.holdout_days):-1*(self.holdout_days )]
            days_valid_3 = self.unique_dates[-1*(self.holdout_days):]

            self.dataframe.loc[self.dataframe[self.time_col].isin(days_train), "kfold"] = 0
            self.dataframe.loc[self.dataframe[self.time_col].isin(days_valid_1), "kfold"] = 1
            self.dataframe.loc[self.dataframe[self.time_col].isin(days_valid_2), "kfold"] = 2
            self.dataframe.loc[self.dataframe[self.time_col].isin(days_valid_3), "kfold"] = 3

        else:
            raise Exception("Problem type not understood!")

        return self.dataframe


if __name__ == "__main__":

    from src.dataset import load_dataset

    print("Loading dataset...")
    df = load_dataset()

    from src.targets import create_targets

    print("Creating targets...")
    df = create_targets(df, type = "binary")
    
    print(df.head())
    print(df.shape)
    
    # Cross validation (initiate class)
    
    # cv = CrossValidation(df, time_col = "date", problem_type="holdout_50")
    cv = CrossValidation(df, time_col = "date", problem_type = "ts.3fold.cv_50")

    # Create kfold column
    df = cv.split()

    print(df.head())
    print(df["kfold"].value_counts())
    print(df.groupby("kfold").agg({"date":"nunique"}))