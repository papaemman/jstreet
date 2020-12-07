<center>
<img src="../assets/docker-logo.png">
</center>

# Kaggle's specific docker container 

## Python version

`Python 3.7.6`

<br>

## Modules' versions

[requirements_true.txt](./requirements_true.txt)


<br>

## Directory structure

**root directory of the docker container**

```
$ cd /
$ tree

.
├── bin
├── boot
├── dev
├── entrypoint.sh
├── etc
├── home
├── kaggle
├── lib
├── lib64
├── media
├── mnt
├── opt
├── proc
├── root
├── run
├── run_jupyter.sh
├── sbin
├── src
├── srv
├── sys
├── tmp
├── usr
└── var
```

<br>

**/kaggle/ directory structure**

```
$ cd /kaggle
$ tree
.
├── input
│   └── jane-street-market-prediction
│       ├── example_sample_submission.csv
│       ├── example_test.csv
│       ├── features.csv
│       ├── janestreet
│       │   ├── __init__.py
│       │   └── competition.cpython-37m-x86_64-linux-gnu.so
│       └── train.csv
├── lib
│   └── kaggle
│       └── gcp.py
│
├── working
│   ├── __notebook_source__.ipynb
│   └── notebook_for_submission.ipynb
│
├── datasets
│
├── notebooks
│
└── src
```

/kaggle directory contains 

- the competition's datasets and any other input dataset in the `/input` directory
- output datasets in the `/kaggle/working` directory
- current running notebook in `/kaggle/working` directory


<br>

```
cd $ /home  
tree
.
```

/home is empty


















