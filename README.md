
#### Setting up Flask: (the pwd should be in the current folder)
1) Install python 
2) Create a virtual enviornment :
    `$ python3 -m venv ./venv`
3) Activate the virtual enviornment :
    `$ source venv/bin/activate`
4) Install flask using pip
    `$ pip install flask`

 To ensure you've installed flask correctly run :
    `$ python -c "import flask;print(flask.__version__)"`

#### Running the project :
 
 Setting some flask variables:

 `$ export FLASK_APP=main`

 `$ export FLASK_ENV=development`

 Running the server on port 8080 :

 `$ flask run --port=8080`

(Let the server running and switch to another terminal to make http requests to the server)

#### Testing the calls :


I have set dummy_data as in the main.py file : 

`dummy_data={ '200489':469 , '190007':200, '180000':461 , '1':123 , '200269':540}`


I used curl to make a POST request :

        a) The Roll Number DOES NOT exist in the dummy_data

        `$ curl --data '{"rollno":"200369"}' --header 'Content-Type: application/json' http://localhost:8080/coins`

        Output:

         {
          "coins": "null"
         }

        a) The Roll Number exists in the dummy_data

        `$ curl --data '{"rollno":"200269"}' --header 'Content-Type: application/json' http://localhost:8080/coins`

        Output:

        {
         "coins": 540
        }




