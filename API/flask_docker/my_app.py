import pandas as pd

import flask
from flask import Flask, request, jsonify, session, app
import json

import mls

app = Flask(__name__)

def predict(name, json_df):
    model = mls.get_model(name, json_df)
    try:
    	return model.res.to_json()
    except Exception as erro:
        return f"error:{str(erro)} | erroH2O:{model.erro}"

@app.get("/")
def geting():
    try:    
        f = open ('path.json', "r")
        j = f.read()
        jl = json.loads(j)
        info = pd.read_csv(jl['modeldata'] + 'info.csv')
	
        if info.columns[0] == 'Unnamed: 0':
                info = info.drop(info.columns[0], axis=1)
        
        j_info = info.to_json()
        return j_info
    
    except Exception as erro:
        return {"error":str(erro)}
    return {"error": "Info file not found"}

@app.post("/")
def posting():
    js = jsonify(request.form).json
    try:
        name = js['name']
        json_df = js['json_df']
        
        pred = predict(name, json_df)
        
        return pred
    
    except Exception as erro:
        return {"error":str(erro)}
    return {"error": "Request must be JSON"}

if __name__ == "__main__":
    app.run(host='0.0.0.0', threaded=True, port=5000)
    
