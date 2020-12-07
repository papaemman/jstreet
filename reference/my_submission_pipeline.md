# My Submission pipeline

---

## tl;dr

1. Upload the new model 
```
$ kaggle datasets version -p models -m "Add new xgboost model v0"
```


2. Attach new dataset and Run the pre-trained model submission pipeline notebook


---

## Submission Pipeline

**How can I submit a solution?**  
Submission must be done through Kaggle Notebooks and not using kaggle API.

<br>

**Process**

--> From Docker container running on remote server:

1. Create a notebook in `working/` directory with a new solution which I want to submit.

2. Make sure it runs smoothly trying `"Kernel -> Restart + Run all"` and ensure that there is a new `submission.csv` file with **correct format** in the `/working` directory.

3. From Jupyter go to File -> Downlad as Python (.py) and save script.


--> Kaggle website

4. Go to jane street's market prediction kaggle competition webpage and create a new Notebook (based on correct Docker images)

5. Paste the Python(.py) file's code inside the cell at the new Kaggle kernel.

- Make sure that the python code will not try to access any path that will not excist in kaggle environment.
- Make sure that there are tests about modules' verions

6. Save Notebook  (save Version -> Save & Run all (commit))

`Kaggle Notebook Settings`
- External Data source
- CPU or GPU, not TPU available
- No internet

I can close the browser now. The run will be continued in kaggle's servers


7. After notebook's succesful run, go to submission page and select this notebook for submission
https://www.kaggle.com/c/jane-street-market-prediction/submissions

<br>

---

<br>

## Submissions using pre-trained models

**I can use external data and pre-trained models can be used for this competition.**

**Detailed Steps to make submission using a pre-trained model**

* Trained the model in the remote machine
* Save the model as pickle (using joblib)
* Upload the trained model to kaggle as dataset, using the kaggle API
* Attach the dataset that contains the pre-trained model to kaggle kernel
* Use the model for inference


**How to Create a New Dataset using the kaggle API**

```
# Create a folder containing the files you want to upload
$ cd models

# Run 
$ kaggle datasets init -p models
to generate a metadata file

# Add your dataset’s metadata to the generated file, datapackage.json

# Run 
$ kaggle datasets create -p models
to create the dataset
```


**Create a New Dataset Version**
If you’d like to upload a new version of an existing dataset, follow these steps:

```
Run 
$ kaggle datasets version -p models -m "Add new xgboost model v0"
```

**SOS Notes:** (Maybe) I have to make public the dataset (pre-trained models) in order to be able to use in the competition's notebook.
https://www.kaggle.com/papaemman/models


<br>

**DESCRIPTION**

So, I can train a Machine Learnin model in offline in remote server (using a lot of cores, RAM and time), upload it as a dataset to kaggle, attach this dataset to kernel and use the kernel exclusively to perform inference based on pre-trained model and test data.

In Submission Notebook (~5 hours), I will only
- load the trained ml model
- preprocessing of test data
- make predictions
