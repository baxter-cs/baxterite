Baxterite CLI Prototype
=======================

## Steps to run

#### 1. 

##### Install Python 3.6 & virtualenv

If on Ubuntu 16.04:

```
sudo add-apt-repository ppa:jonathonf/python-3.6
sudo apt-get update
sudo apt-get install python3.6 virtualenv;
```

If on Ubuntu 16.10:
```
sudo apt install python3.6 virtualenv;
```

#### 2.

Assuming you're in the `cli` folder where this readme is located, then.

```
virtualenv -p python3.6 .venv
source .venv/bin/activate
pip install requirements.txt;
```

Now you have all the requirements to run this.
