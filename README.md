I'll just mention how to setup the dependencies and frameworks :

#### Setting up Flask: (the pwd should be in the current folder)
1) Install python (lots of online tutorials available)
2) Create a virtual enviornment :
    `$ python3 -m venv ./venv`
3) Activate the virtual enviornment :
    `$ source venv/bin/activate`
4) Install flask using pip
    `$ pip install flask`

 To ensure you've installed flask correctly run :
    `$ python -c "import flask;print(flask.__version__)"`

#### Runnin the project :
 
 `$ export FLASK_APP=main`
 `$ export FLASK_ENV=development`
 `$ flask run`

