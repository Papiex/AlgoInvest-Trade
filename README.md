# AlgoInvest&Trade

AlgoInvest&Trade a financial company specializing in investment.
The company seeks to optimize its investment strategies using algorithms,
in order to generate more profits for its clients.

This project contains two algorithms, an optimized version and a brute force version

<li><a href="#requirements">Requirements</a></li>
<li><a href="#gitbash">Gitbash</a></li>
<li><a href="#installation-on-windows">Installation on Windows</a></li>
<li><a href="#installation-on-linux">Installation on Linux</a></li>
<li><a href="#installation-on-mac">Installation on Mac</a></li>
<li><a href="#uses">Uses</a></li>


## Requirements
```bash
Python 3.9.0
```
## Gitbash
You have to clone the deposit with this command on gitbash :
```
git clone https://github.com/Papiex/LITReview-Web-Application
```

## Installation on Windows
__1- You need to create virtual env with this command :__

*The virtual env is installed in the directory where you are (the path) with your terminal*

- ```python -m venv env```

__2- Now you have to activate your virtual env, the default path is :__
- if you use PowerShell :
``` env/Scripts/activate.ps1```
- if you use CMD or terminal that supports __.bat__ :
``` env/Scripts/activate.bat```

## Installation on Linux
__1- You need to create virtual env with this command :__

*The virtual env is installed in the directory where you are (the path) with your terminal*

- ```python3 -m venv env```

__2- Now you have to activate your virtual env, the command is :__
``` source env/bin/activate```

## Installation on Mac
__1- You need to create virtual env with this command :__

*The virtual env is installed in the directory where you are (the path) with your terminal*

- ```python3 -m venv env```

__2- Now you have to activate your virtual env, the command is :__
``` source env/bin/activate```

## Libraries
__This program need some libraries, for installing them, use this command (in your virtual env) :__

*View requirements.txt to know which library/version is used*

- ```pip3 install -r requirements.txt``` | Windows : ```pip install -r requirements.txt```

## Uses
You can run the brute force or optimized algorithm by running this command,
You can also add the CSV file from which the algorithm will take the data by adding the file as an argument.
- ```py optimized.py csv_file.csv```
  or
- ```py bruteforce.py csv_file.csv```

This project contains three datasets in folder "datasets":
- dataset_test.csv
- dataset1.csv
- dataset2.csv
