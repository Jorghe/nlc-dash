from flask import Flask, jsonify, render_template
import os
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import requests
from jinja2 import TemplatesNotFound, Template
# Initialize app and load templates and static folder
app = Flask(__name__)

@app.route('/')
def index():
    try:
        #print(app.instance_path)
        return render_template('index.html')
        # return Template()
    except TemplatesNotFound:
        return jsonify({404: "Error in rendering template"})
    except:
        return jsonify({404: "Unknown error"})

@app.route("/dash/")
def my_dash_app():
    # req_huaste = requests.get(routes['huaste'])
    # api_huaste = pd.read_json(req_huaste.json())
    # js = api_huaste.to_json()

    return 'Server working'# app.index()

def from_api(name:str):
    routes = {
    'huaste': 'https://nl-climbing.deta.dev/api/huaste/',
    'salto': 'https://nl-climbing.deta.dev/api/salto/',
    'epc': 'https://nl-climbing.deta.dev/api/epc/'
    }
    request = requests.get(routes[name])
    zona = pd.read_json(request.json())
    return zona

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
