from sklearn import ensemble
from sklearn.linear_model import LinearRegression
import xgboost as xgb


MODELS = {

    "linear_regression": LinearRegression(n_jobs=-1),

    "randomforest_v1": ensemble.RandomForestClassifier(n_estimators=100, n_jobs=-1, verbose=2),
    "randomforest_v2": ensemble.RandomForestClassifier(n_estimators=200, n_jobs=-1, verbose=2),
    "randomforest_v3": ensemble.RandomForestClassifier(n_estimators=300, n_jobs=-1, verbose=2),

    "extratrees_v1": ensemble.ExtraTreesClassifier(n_estimators=100, n_jobs=-1, verbose=2),
    "extratrees_v2": ensemble.ExtraTreesClassifier(n_estimators=200, n_jobs=-1, verbose=2),
    "extratrees_v3": ensemble.ExtraTreesClassifier(n_estimators=300, n_jobs=-1, verbose=2),

    "xgboost_v1": xgb.XGBClassifier(n_estimators=100, reg_lambda=1, gamma=0, max_depth=3),
    "xgboost_v2": xgb.XGBClassifier(n_estimators=200, reg_lambda=1, gamma=0, max_depth=5),
}