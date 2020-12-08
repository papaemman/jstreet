from sklearn import metrics as skmetrics


def utility(valid_df, submission_df):
    """
    Fast imlementation of the evaluation metric (utility score)
    
    Arguments
    ------------
    
    valid_df   : validation data frame with columns ts_id, date, weight, resp
    submission : ts_id, action 
    
    
    Return
    ---------
    - utility score 
    - t (annualized sharpe ratio)
    - Σpi (total profit)
    - pi (profit per day)
    
    
    """
    
    # From valid df keep only usefull columns and merge submission file to it
    valid_df = valid_df[["ts_id", "date", "weight", "resp"]].merge(submission_df, on="ts_id", how="left")
    
    # Calulate profit for specific ts_id wrt action (trade)
    valid_df["profit"] = valid_df["weight"] * valid_df["resp"] * valid_df["action"]
    
    
    # Calculate Profit per date (pi) - return this
    profit_df = (valid_df
                 .groupby("date")
                 .agg({"profit": ["sum"]}))

    profit_df.columns = ["_".join(x) for x in profit_df.columns.ravel()]
    profit_df.reset_index(inplace=True)
    
    # Calculate total profits (Σpi)
    a = sum(profit_df["profit_sum"]) 

    
    # Calculate std of profits per day (sqrt(Σpi^2))
    b = np.sqrt(sum(profit_df["profit_sum"]**2))

    # Count total number of days (|i|)
    i = profit_df["date"].nunique()
    

    # Calculate t
    t = (a/b) * np.sqrt(250/i)
    

    # Calculate utility score
    utility_score = min(max(t,0),6)*a
    
    results = {"utility_score": utility_score,
               "total_nb_of_days": i,
               "t": t,
               "a": a,
               "b": b,
               "profit_df":profit_df,
               "details": "a = Σpi | b = sqrt(Σpi^2) | profit_df: total profit per day"}

    return results


class ClassificationMetrics:
    def __init__(self):
        self.metrics = {
            "accuracy": self._accuracy,
            "f1": self._f1,
            "precision": self._precision,
            "recall": self._recall,
            "auc": self._auc,
            "logloss": self._logloss
        }
    
    def __call__(self, metric, y_true, y_pred, y_proba=None):
        if metric not in self.metrics:
            raise Exception("Metric not implemented")
        if metric == "auc":
            if y_proba is not None:
                return self._auc(y_true=y_true, y_pred=y_proba)
            else:
                raise Exception("y_proba cannot be None for AUC")
        elif metric == "logloss":
            if y_proba is not None:
                return self._logloss(y_true=y_true, y_pred=y_proba)
            else:
                raise Exception("y_proba cannot be None for logloss")
        else:
            return self.metrics[metric](y_true=y_true, y_pred=y_pred)

    @staticmethod
    def _auc(y_true, y_pred):
        return skmetrics.roc_auc_score(y_true=y_true, y_score=y_pred)

    @staticmethod
    def _accuracy(y_true, y_pred):
        return skmetrics.accuracy_score(y_true=y_true, y_pred=y_pred)
    
    @staticmethod
    def _f1(y_true, y_pred):
        return skmetrics.f1_score(y_true=y_true, y_pred=y_pred)
    
    @staticmethod
    def _recall(y_true, y_pred):
        return skmetrics.recall_score(y_true=y_true, y_pred=y_pred)
    
    @staticmethod
    def _precision(y_true, y_pred):
        return skmetrics.precision_score(y_true=y_true, y_pred=y_pred)
    
    @staticmethod
    def _logloss(y_true, y_pred):
        return skmetrics.log_loss(y_true=y_true, y_pred=y_pred)



class RegressionMetrics:
   pass

