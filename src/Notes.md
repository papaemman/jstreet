# How to write and run code inside each script

1. Open the script and write code for the fucntion
2. Write code to test the function into `if __name__ == "__main__"`
3. Open terminal and run the script with python

```
$ cd src/
$ python script.py
```

## Detailed steps 

### 0. src/`__init__.py`


<br>

### 1. src/`dataset.py`

* load_dataset() : Load training dataset

<br>


### 2. src/`targets.py`

* create_targets(train_df, type:"string") : Create different types of targets based on resp_{_, 1,2,3,4} columns

<br>


### 3.  src/`preprocessing`

<br>


### 4. src/`feature_engineering`

<br>


### 5. src/`cross_validation`

* class: **CrossValidation**   
methods: split for holdout_nbofdays and ts.3fold.cv_nb_of_days

<br>

### 6. src/`train.py`

Train a ML model to the full training dataset

<br>


### 6. src/`predict`


<br>


### 6. src/`experiment_id` + src/`dispatcher`

Experimentation. Complete end-to-end ML pipeline.

* load dataset
* create targets
* data preprocessing
* feature engineering
* train - test split
* train model using dispatcher
* make predictions 
* evaluate predictions
* track experiment configuration and results

<br>



### 7. src/`metrics`

* class: **ClassificationMetrics:** Most important classification metrics

* class: **RegressionMetrics:** Most important regression metrics

* function: **utility_score():** Competitions evaluation metric (utility score)

<br>





