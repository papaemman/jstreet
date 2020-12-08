# Load modules
import numpy as np
import pandas as pd
import joblib

from src.dataset import load_dataset
from src.preprocessing import data_preprocessing
from src.feature_engineering import feature_engineering


## 1. Load data
df_train = load_dataset(path = "data/raw", train_df=True)
df_test = load_dataset(path = "data/raw", train_df=False)

## 2. Preprocessing
# - NAs
# - Scaling

df_train = data_preprocessing(df_train)

## 3. Fatures creation
df = feature_engineering(df)


df.shape
df.head()
df.dtypes
df.isna().sum()

## 4. Categorical encoding
from src.categorical import CategoricalFeatures

categorical_columns = df.columns[df.dtypes == "object"].to_list()

cat_feats = CategoricalFeatures(df, 
                                categorical_features=categorical_columns, 
                                encoding_type="label",
                                handle_na=False)

df = cat_feats.fit_transform()

joblib.dump(cat_feats, filename="cat_features.pkl")


df_test = cat_feats.transform(df_test)


## 4. Create Folds for Cross Validation (Create a new kfold column)
from src.cross_validation import CrossValidation
cv = CrossValidation(df,
                     shuffle=True, target_cols=["compliance"], 
                     problem_type="binary_classification")

df_split = cv.split()
print(df_split.head())
print(df_split.kfold.value_counts())




## 5. Train and Evaluate models

from src.dispatcher import MODELS
from src.metrics import ClassificationMetrics


FOLD_MAPPPING = {
    0: [1, 2, 3, 4],
    1: [0, 2, 3, 4],
    2: [0, 1, 3, 4],
    3: [0, 1, 2, 4],
    4: [0, 1, 2, 3]
}

# Πρώτα διαλέγω τα data για αυτό το fold
# Μετά κάνω το categorical encoding 
# Μετά χωρίζω X_train, y_train, X_val, y_val και πετάω τα columns που δεν χρειάζονται

df.shape
df.head()
df.nunique()
df.columns

columns_to_drop_from_training = ["ticket_id", "compliance_detail", "kfold"]

target = ["compliance"]


for MODEL in MODELS:

    # MODEL = "randomforest"
    print(MODEL)

    # Create data frame to store evaluation metrics for this model
    metrics_df = pd.DataFrame(data=np.empty(shape=(5,2)), index = range(0,5), columns=["accuracy", "auc"])
    metrics_df

    for FOLD in range(5): #0,1,2,3,4

        # FOLD=0
        print(FOLD)
        
        train_df = df[df.kfold.isin(FOLD_MAPPPING.get(FOLD))].reset_index(drop=True)
        valid_df = df[df.kfold==FOLD].reset_index(drop=True)

        ytrain = train_df[target].values
        yvalid = valid_df[target].values

        train_df = train_df.drop(columns_to_drop_from_training+target, axis=1)
        valid_df = valid_df.drop(columns_to_drop_from_training+target, axis=1)

        valid_df = valid_df[train_df.columns]
        

        # Training
        clf = MODELS[MODEL]
        clf.fit(train_df, ytrain)

        # Evaluation
        classification_metrics = ClassificationMetrics()
       
        preds = clf.predict(valid_df)
        accuracy_score = classification_metrics(metric="accuracy", y_true = yvalid, y_pred=preds)

        preds_proba = clf.predict_proba(valid_df)[:, 1]
        auc_score = classification_metrics(metric="auc", y_true = yvalid, y_pred=preds, y_proba = preds_proba)

        # Save metrics
        metrics_df.loc[FOLD,["accuracy","auc"]] = [accuracy_score, auc_score]

        # Save model
        # joblib.dump(label_encoders, f"models/{MODEL}_{FOLD}_label_encoder.pkl")
        # joblib.dump(clf, f"models/{MODEL}_{FOLD}.pkl")
        # joblib.dump(train_df.columns, f"models/{MODEL}_{FOLD}_columns.pkl")

        
    # Save metrics_df for this model
    metrics_df.to_csv("models/"+MODEL+"_cv.csv", index=False)

####

FOLD_MAPPPING = {
    0: [1, 2, 3, 4],
    1: [0, 2, 3, 4],
    2: [0, 1, 3, 4],
    3: [0, 1, 2, 4],
    4: [0, 1, 2, 3]
}

if __name__ == "__main__":
    df = pd.read_csv(TRAINING_DATA)
    df_test = pd.read_csv(TEST_DATA)
    train_df = df[df.kfold.isin(FOLD_MAPPPING.get(FOLD))].reset_index(drop=True)
    valid_df = df[df.kfold==FOLD].reset_index(drop=True)

    ytrain = train_df.target.values
    yvalid = valid_df.target.values

    train_df = train_df.drop(["id", "target", "kfold"], axis=1)
    valid_df = valid_df.drop(["id", "target", "kfold"], axis=1)

    valid_df = valid_df[train_df.columns]

    label_encoders = {}
    for c in train_df.columns:
        lbl = preprocessing.LabelEncoder()
        train_df.loc[:, c] = train_df.loc[:, c].astype(str).fillna("NONE")
        valid_df.loc[:, c] = valid_df.loc[:, c].astype(str).fillna("NONE")
        df_test.loc[:, c] = df_test.loc[:, c].astype(str).fillna("NONE")
        lbl.fit(train_df[c].values.tolist() + 
                valid_df[c].values.tolist() + 
                df_test[c].values.tolist())
        train_df.loc[:, c] = lbl.transform(train_df[c].values.tolist())
        valid_df.loc[:, c] = lbl.transform(valid_df[c].values.tolist())
        label_encoders[c] = lbl
    
    # data is ready to train
    clf = dispatcher.MODELS[MODEL]
    clf.fit(train_df, ytrain)
    preds = clf.predict_proba(valid_df)[:, 1]
    print(metrics.roc_auc_score(yvalid, preds))

    joblib.dump(label_encoders, f"models/{MODEL}_{FOLD}_label_encoder.pkl")
    joblib.dump(clf, f"models/{MODEL}_{FOLD}.pkl")
    joblib.dump(train_df.columns, f"models/{MODEL}_{FOLD}_columns.pkl")