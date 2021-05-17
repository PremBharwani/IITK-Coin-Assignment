from logging import log
from flask import Flask,request,jsonify
from flask.wrappers import Request

app =  Flask(__name__)

#Below is the dummy data
dummy_data={ '200489':469 , '190007':200, '180000':461 , '1':123 , '200269':540}

#Defining the /coins endpoint
@app.route('/coins', methods=['POST'])
def coins_method():

    # Extracting the json data from the http request 
    input_json = request.get_json(force=True)
    rollno = input_json["rollno"]

    # Checking if the rollno exists in records
    if rollno in dummy_data:
        #If the rollno is found in dummy data we return the number of coins as JSON
        app.logger.info("\n*******\nRoll number {} is found in the dummy data\n*******\n".format(rollno))
        dictToReturnIfFound = {'coins':dummy_data[rollno]}
        return jsonify(dictToReturnIfFound)
    #If the rollno was not found , we will output coins value to be null
    app.logger.info("\n*******\nRoll number {} NOT found in the dummy data\n*******\n".format(rollno))
    dictToReturn = {'coins':'null'}
    return jsonify(dictToReturn)
    

if __name__=="__main__":
    app.run(debug=True)
    
    

