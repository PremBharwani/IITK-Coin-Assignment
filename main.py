from logging import log
from flask import Flask,request,jsonify
from flask.wrappers import Request

app =  Flask(__name__)

dummy_data={ '1':469 , '2':200, '3':461 , '4':123 , '200269':540}

@app.route('/coins', methods=['POST'])
def coins_method():
    input_json = request.get_json(force=True)
    rollno = input_json["rollno"]
    if rollno in dummy_data:
        app.logger.info("Found {} coins balace ".format(rollno))
        dictToReturnIfFound = {'coins':dummy_data[rollno]}
        return jsonify(dictToReturnIfFound)
    dictToReturn = {'coins':'null'}
    return jsonify(dictToReturn)
    # coins_dict={ '1':469 , '2':200, '3':461 , '4':123 }
    # rollno=str(request.form.get("rollno"))
    # app.logger.info("Roll Number : "+rollno)
    # app.logger.info("req.form.items : "+str(request.form.items))
    # prem_dic=request.form
    # prem_json = request.get_json
    # prem_data = request.get_data
    # app.logger.info("Get json : "+str(prem_json))
    # app.logger.info("Get Data : "+str(prem_data))
    
    # # app.logger.info("Request form "+str(request.form))
    # return prem_dic
    


    
    

if __name__=="__main__":
    app.run(debug=True)
    
    

