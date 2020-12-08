from sklearn import ensemble
from sklearn.linear_model import LinearRegression, LogisticRegression
import xgboost as xgb
import lightgbm as lgb



## ------------------- MODELS ------------------- ##

# sklearn.ensemble.ExtraTreesClassifier
# sklearn.ensemble.RandomForestClassifier
# xgboost
# lightgbm


MODELS = {

    "linear_regression": LinearRegression(random_state=0, n_jobs=-1, verbose=2),

    "logistic_regression": LogisticRegression(random_state=0, n_jobs=-1, verbose=2),

    "randomforest": ensemble.RandomForestClassifier(random_state=0, n_jobs=-1, verbose=2),

    "extratrees": ensemble.ExtraTreesClassifier(random_state=0, n_jobs=-1, verbose=2),

    "xgboost": xgb.XGBClassifier(random_state=0, n_jobs=-1, verbose=2),
}



## ------------------- HYPER-PARAMETERS ------------------- ##

# sklearn.ensembles
sklearn_enselmbles_params = {
    "n_estimators":[100,200,300],
    "max_depth":[1,2,5,10],
    "criterion" : ["gini", "entropy"],
    "min_samples_split": [5,10, 100],
    "min_samples_leaf":[1,3,5,50]
}


# xgboost params
xgboost_params = {
    "n_estimators":[100,200,500],
    "reg_lambda": [1,0.1],
    "gamma": [0,0.1,1],
    "max_depth": [3,5,10]
}