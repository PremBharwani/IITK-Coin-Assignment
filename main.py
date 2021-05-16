from flask import Flask,render_template,request
from flask.wrappers import Request

app =  Flask(__name__)

coins_students_initialise={ '1':469 , '2':200, '3':461 , '4':123 }
coins_dict={}

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/coins', methods=['POST'])
def coins_method():
    coins_dict={ '1':469 , '2':200, '3':461 , '4':123 }
    rollno=str(request.form.get("rollno"))
    dict_status=str(coins_dict)
    if str(rollno) in coins_dict:
        found_op=dict_status+"{} has {} coins".format(rollno,coins_dict[str(rollno)])
        return found_op        
    else:
        op=dict_status+"Roll Number {} is not present in the database".format(rollno)
        return op


    
    

if __name__=="__main__":
    app.run(debug=True)
    
    

