# User Authentication
## Prerequisites:

You will need the following programmes properly installed on your computer.

* [Python](https://www.python.org/) 3.5+
* Virtual Environment

To install virtual environment on your system use:

```bash
pip install virtualenv

or

pip3 install virtualenv #if using linux(for python 3 and above)
```

## Installation and Running :

```bash
git clone https://github.com/ongraphpythondev/userLogin

cd userLogin

virtualenv venv 
      or 
virtualenv venv -p python3 #if using linux(for python 3 and above)

venv\Scripts\activate # for windows
      or
source venv/bin/activate # for linux

# install required packages for the project to run
pip install -r requirements.txt 

python manage.py runserver
```
