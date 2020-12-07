# ABOUT EVALUATION AND SUBMISSION PROCESS

<br>

## Competition Guidelines

[Code requirements](https://www.kaggle.com/c/jane-street-market-prediction/overview/code-requirements)

> This is a Code Competition.    
> Submissions to this competition must be made through Notebooks.    
For this competition, training is not required in Notebooks.    
> In order for to be eligible for submission, the following 
conditions must be met:    
> 
> **Training Phase**
> * Your notebook must use the time-series module to make predictions
> * CPU Notebook <= 5 hours run-time
> * GPU Notebook <= 5 hours run-time
> * TPU Notebooks are not supported
> * Freely & publicly available external data is allowed, including pre-trained models
>
> **Forecasting Phase**   
> Because the size of the test set will change during the live forecasting phase, the time limits will be adjusted in proportion to the test set size, with a 10% added time allowance. As a hypothetical example, if there are 1,000,000 test rows and a 5 hour runtime limit during the training phase and the forecasting phase has 2,000,000 rows, your notebook will be allowed 10 hours + 10% = 11 hours during the forecasting phase.

Please see the [Code Competition FAQ](https://www.kaggle.com/docs/competitions#kernels-only-FAQ) for more information on how to submit.

<br>

---

## Prediction using time series API (janestreet module)

**Use the following snippet of code for prediction**

```
import janestreet
env = janestreet.make_env() # initialize the environment
iter_test = env.iter_test() # an iterator which loops over the test set

for (test_df, sample_prediction_df) in iter_test:
    sample_prediction_df.action = 0 # make your 0/1 prediction here
    env.predict(sample_prediction_df)

```

>In this competition, we will privately re-run your selected Notebook Version with a hidden test set substituted into the competition dataset. 
We then extract your chosen Output File from the re-run and use that to determine your score.

<br>

---

## Final Submission

> You may select up to 2 submissions to be used to count towards your final leaderboard score. If 2 submissions are not selected, they will be automatically chosen based on your best submission scores on the public leaderboard. In the event that automatic selection is not suitable, manual selection instructions will be provided in the competition rules or by official forum announcement.    
> Your final score may not be based on the same exact subset of data as the public leaderboard, but rather a different private data subset of your full submission — your public score is only a rough indication of what your final score is.   
You should thus choose submissions that will most likely be best overall, and not necessarily on the public subset.

<br>

---

<br>


## Common Errors 

[Code competition debugging](https://www.kaggle.com/code-competition-debugging)


**1. Cannot submit**  

Your Notebook cannot use internet access in this competition. Please disable internet in the Notebook editor and save a new version.


**2. Notebook Timeout**

Your submission notebook exceeded the allowed runtime.
Review the competition's Code Requirements page for the time limits. Note that the hidden dataset can be larger/smaller/different than the public dataset.

**3. Submission Scoring Error**

Your notebook generated a submission file with incorrect format. 
Some examples causing this are: 
- wrong number of rows or columns,
- empty values,
- an incorrect data type for a value,
- or invalid submission values from what is expected.

This can be happened due the presense of NAs, different versions of packages etc.
