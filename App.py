from flask import Flask, request

import json
from Backend import *
app = Flask(__name__)
@app.route('/getData/'+ID+'=<int:number>/', methods=['GET'])
def GetData(number):
    res = process_Get_Data (number)
    print ('*****')
    print (res)
    response = app.response_class(
        response=json.dumps(res [1]),
        status=res [0] ,
        mimetype='application/json'
    )
    return response

@app.route('/Update/', methods=['POST'])
def UpdateData():
    request_data = request.get_json()
    res = process_Post_Data (request_data)
    print ('######')
    print (res)
    response = app.response_class(
        response=json.dumps(res [1]),
        status=res [0] ,
        mimetype='application/json'
    )
    return response







@app.route('/Takeinputs/', methods=['PUT'])
def ProcessPUT():
    request_data = request.get_json()
    
    print (request_data)
    res = process_Put_Data (request_data)
    response = app.response_class(
        response=json.dumps(res [1]),
        status=res [0] ,
        mimetype='application/json'
    )
    return response
@app.route('/DeleteValues/', methods=['DELETE'])
def ProcessDEL():
    request_data = request.get_json()
    
    print (request_data)
    res = process_Del_Data (request_data)
    response = app.response_class(
        response=json.dumps(res [1]),
        status=res [0] ,
        mimetype='application/json'
    )
    return response
    
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)