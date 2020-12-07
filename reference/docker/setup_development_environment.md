# Compete in Kaggle using their Docker container


## Why docker?

1. Identical development environment with kaggle kernels
2. For code competitions this is crucial, because I have to ensure that the local develped solutio will run smoothly through Kaggle kernels.

<br>

**Links:**

Kaggle docker image for python: 
- https://github.com/Kaggle/docker-python


<br>

---

## Steps to setup kaggle docker container to a remote server

1. Connect to remote server via ssh

2. Install the docker community edition 
```
$ docker --version
$ docker ps
```

3. Download kaggle docker image for python. 
This docker image runs to kaggle notebooks too!

```
$ docker pull gcr.io/kaggle-images/python:latest
```

4. Create and Run a new docker container based on kaggle docker image

```
$ docker images

$ docker run -d --name jstreet-container -p 8888:8888 -p 5000:22 -v /home/panagiotis.medoid/jstreet_docker:/kaggle  gcr.io/kaggle-images/python
```

**Docker description**

```
Explain command

docker run   : create and runs a docker container based on a docker image


Explain flags

-d     : create and run docker container `detached` ie run in the background and don't withhold the terminal

--name : give a name to container

-p     : export a port from container to host (<port_from_host>:<port_inside_container>)
	 22   -> default openssh server port
	 8888 -> default jupyter-notebook port

-v     : mount a volume (directory) from container to host (<dir/on/host>:<dir/inside/the/container>) in order to have access in files inside docker container from host
```

**Make sure to:**

*  Define the correct directory structure inside the docker container, to identicaly match kaggle notebooks envirment. Use `/kaggle` directory for the project, not `/home`  or anything else.

* Expose required port to have access to container via ssh (22) and to have
access to jupyter notebooks running on container (8888)

<br>


5. Get into the docker container and install some more helper pacakges


**Get into the container**

```
$ docker inspect jstreet-container
$ docker exec -ti jstreet-container bash
```

**Install Ubuntu releated packages**

```
/# apt-get install htop
/# apt-get install nano
/# apt-get install tree
```

**Install python releated packages**

Be carefull here! Don't modify the version of any installed package,
because this will breake the submission process.
Install only jupyter releated packages.

```
$ pip install jupyter_nbextensions_configurator jupyter_contrib_nbextensions
$ jupyter contrib nbextension install --user
$ jupyter nbextensions_configurator enable --user
$ pip install ipywidgets
$ jupyter nbextension enable --py widgetsnbextension
```


6. Setup the kaggle API and download the dataset

- Save the `kaggle.json` token from Kaggle Account webapge into `~/.kaggle` directory inside the docker container.

- Create the appropriate data structure and download the dataset

```
$ cd /kaggle
$ mkdir input
$ cd input
$ kaggle competitions download -c jane-street-market-prediction
$ unzip *.zip
```

**The data structure must look like this**

```
$ cd /kaggle
$ tree

.
├── README.md
├── TODO
├── datasets
│   └── submission-files
├── input
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
├── models
├── notebooks
└── src
    ├── __init__.py
    ├── test.py
    └── utils.py
```
<br>

7. Update the `PYTHONPATH` environment variable in order to be able to use custom prebuild package provided by Kaggle (*janestreet*).

**Custom module** in `input/jane-street-market-prediction/janestreet/` directory. The module **competition.cpython-37m-x86_64-linux-gnu.so** is provided in compiled form to block kagglers for using test data in their predictions. It is compiled for x86, 64-bit, Linux GNU, so it can be only read from this type of machine.


```
$ cd /kaggle/input/
$ tree
.
└── jane-street-market-prediction
    ├── example_sample_submission.csv
    ├── example_test.csv
    ├── features.csv
    ├── janestreet
    │   ├── __init__.py
    │   ├── __pycache__
    │   │   └── __init__.cpython-37.pyc
    │   └── competition.cpython-37m-x86_64-linux-gnu.so
    └── train.csv
```

Add this line to `.bashrc` to run every time on start up:  
`export PYTHONPATH=$PYTHONPATH:/home/jstreet/input`

```
$ cd ~
$ nano .bashrc (and add the previous line!)
$ source .bashrc
```

Test if janestreet module is accessible from python

```
$ python
>>> import janestreet 
>>> (No error. DONE!)
```

----

## Local Development Environment (VSCode)

**Description of how can I connect and run VSCode from my local operating system, inside the container running on remote server.**


### Instructions

I have to create a **running `openssh` server inside docker container**, to connect straight insight docker, from my local machine. I will not connect to remote server, in which the container running, but instead I will connect straight inside to the docker container using openssh server.

In order to connect using the ssh, I need to set `passwordless ssh` authentication. For this I have to copy the `id_rsa.pub` key from my local machine into the `~./ssh/` directory, to `authorized_keys` file, into the running docker container.


### Detailed Steps:

I. Login to remote server and then into the docker container


```
# Connect to remote server
(local machine)$ ssh ...

# Connect to running docker container
(server)       $ docker ps
(server)       $ docker exec -ti jstreet-container bash


# Install and start ssh server
(running container) #> apt-get update && apt-get install -y openssh-server
(running container) #> mkdir /var/run/sshd
(running container) #> sed -ri 's/^#?PermitRootLogin\s+.*/PermitRootLogin without-password/' /etc/ssh/sshd_config
(running container) #> sed -ri 's/^#?UsePAM\s+.*/UsePAM no/' /etc/ssh/sshd_config
(running container) #> sed -ri 's/^#?PasswordAuthentication\s+.*/PasswordAuthentication no/' /etc/ssh/sshd_config
(running container) #> sed -ri 's/^#?ChallengeResponseAuthentication\s+.*/ChallengeResponseAuthentication no/' /etc/ssh/sshd_config
(running container) #> mkdir /root/.ssh
(running container) #> apt-get update && apt-get install -y locales
(running container) #> locale-gen en_US.UTF-8
(running container) #> apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Start the openssh server
#>/usr/sbin/sshd

```

II. Set ssh passwordless login

```
(local machine) $ cat ~/.ssh/id_rsa.pub (and COPY)

(container)     $ mkdir ~/.ssh
(container)     $ cd ~./ssh
(container)     $ nano authorized_keys (and copy the id_rsa.pub key, save and exit)
(container)     $ cat authorized_keys (check results)
```

III. Add the new ssh server to my config file

```
(local machine) $ nano /home/user7/.ssh/config
```

Paste the following text:

```
Host jstreet_container
  HostName 138.201.55.46
  User root
  Port 5000
```

* Don't forget to specify the port 5000, because this is the exported port of the **openssh server**, from inside the docker container to the host machine of the docker container `(-p 5000:22)`


IV. Test results

- Open local terminal and test if you can connect to running docker container.
This must connect the terminal inside the docker container

```
$ ssh jstreet_container
```
<br>


- Open **VSCode** and connect to jstreet_container from the **Remote Explorer** window.

<br>

---

## Local Development Environment (Jupyter Notebook)

**Description of how can I run a Jupyte Notebook from inside the docker container running on a remote server and and access it from my local web browser.**


- Make sure that the default port (8888) for Jupyter Notebook is been exported during docker container creation 

```<port in remote server>:<port inside docker container>```

**Detailed Steps**

1. Connect to remote server
2. Run docker container
3. Get into docker container 
4. Start jupyter notebook
5. Enable ssh tunneling from my local machine to remote server

<br>

```
(local machine) $ ssh ...

(remote server) $ docker ps
(remote server) $ docker exec -ti docker_container_name bash

(docker container) $ jupyter-notebook --no-browser --ip=0.0.0.0 --port=8888 --allow-root



Explain flags

--no-browser   : Don't ty to open browser for jupyter-notebook from inside docker

--ip=0.0.0.0   : Define specific IP because eitherwise running on localhost make it available only from inside the container.

--port=8888    : Specify the exported port

--allow-root   : allow connect as root user
```

**Enable ssh tunneling**

Open new terminal in local machine and create ssh tunneling

```
$ ssh -N -f -L localhost:8888:172.17.0.2:8888 panagiotis.medoid@tiger.ngsqintl.com
```

<br>

I have to find the IP address in which the docker container running

```
(local machine) $ ssh ...
(remote server) $ docker ps

(remote server)$ docker inspect jstreet-container (and find IP address) 
OR
(remote server) $ docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' jstreet-container
```







