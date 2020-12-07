<img src="./reference/assets/Jane-Street.jpg">

# Jane street market prediction, Kaggle competition

**Competition's Link:** https://www.kaggle.com/c/jane-street-market-prediction


<img src="./reference/assets/kaggle-logo.png">


## Project directory structure


```
.
├── README.md                                                : You are here
├── TODO                                                     : Ideas to try
├── datasets                                                 : Additional datasets, created datasets, submission files
│   └── submission-files
├── input                                                    : Competition's datasets
│   └── jane-street-market-prediction
│       ├── example_sample_submission.csv
│       ├── example_test.csv
│       ├── features.csv
│       ├── janestreet
│       │   ├── __init__.py
│       │   ├── __pycache__
│       │   │   └── __init__.cpython-37.pyc
│       │   └── competition.cpython-37m-x86_64-linux-gnu.so
│       └── train.csv
├── models                                                   : Saved trained models
│   ├── dataset-metadata.json 
│   └── xgboost_v0.joblib.dat
├── notebooks                                                : Notebooks
│   └── template_notebook.ipynb
├── reference                                                : Notes, Guides, Pictures
│   ├── Errors.txt
│   ├── Notes.txt
│   ├── Submission_process.txt
│   ├── Workflow.md
│   ├── assets
│   └── requirements_true.txt
├── requirements.txt                                         : Modules versions
├── run.sh                                                   : Bash script to run experiments
├── src                                                      : Python code for pipelines
│   ├── __init__.py
│   ├── cross_validation.py
│   ├── dataset.py
│   ├── dispatcher.py
│   ├── experiment.py
│   ├── feature_engineering.py
│   ├── metrics.py
│   ├── predict.py
│   ├── predict_using_api.py
│   ├── preprocessing.py
│   ├── test.py
│   └── utils.py
└── working                                                  : Kernels from Kaggle
```

---
<br>

### Python version

`Python 3.7.6`

<br>


### Activate Development Environment

```
$ source /opt/conda/bin/activate
$ conda activate base
```
<br>

### Download dataset using kaggle API

```
$ kaggle competitions download -c jane-street-market-prediction
```
<br>

**How to read datasets?**

```
train = pd.read_csv("../input/jane-street-market-prediction/train.csv")
```

---

<br>

## Common Errors and Solutions 
[Erros and Solutions](reference/Errors.txt)

<br>

---

## Submission Pipeline

[About evaluation and submission process](reference/Submission_process.md)

[My submission pipeline](reference/my_submission_pipeline.md)

<br>

---

<br>

## Setup Development Environment using docker

* [Setup Development environment using docker notes]("reference/docker/setup_development_environment.md")

* [Kaggle Docker container notes]("refernce/docker/kaggle_docker_container.md")


<br>

## tl;dr

**I. How to Connect **VSCode** to running docker container to remote server** 
* Open VScode and hit connect to jstreet-container


**II. Start Jupyter notebook from docker container running on remote server and conect from local web browser**

```
(local machine) $ ssh ...

(remote server) $ docker ps
(remote server) $ docker exec -ti jstreet-container bash

(docker container) $ jupyter-notebook --no-browser --ip=0.0.0.0 --port=8888 --allow-root

(local machine) $ ssh -N -f -L localhost:8888:172.17.0.2:8888 panagiotis.medoid@tiger.ngsqintl.com


Open Jupyter Notebook in `localhost:8888` from webrowser.
```