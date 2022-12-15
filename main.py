from flask import Flask, jsonify, render_template
import os
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import requests

app = Flask(__name__)
# app = Dash(__name__, server=server, url_base_pathname='/dash')

stylesheets = ['https://nl-climbing.deta.dev/static/style.css']
routes = {
    'huaste': 'https://nl-climbing.deta.dev/api/huaste/',
    'salto': 'https://nl-climbing.deta.dev/api/salto/',
    'epc': 'https://nl-climbing.deta.dev/api/epc/'
}
@app.route('/')
def index():
    return render_template('index.html')

@app.route("/dash/")
def my_dash_app():
    # req_huaste = requests.get(routes['huaste'])
    # api_huaste = pd.read_json(req_huaste.json())
    # js = api_huaste.to_json()

    return 'Server working'# app.index()

def from_api(name:str):
    request = requests.get(routes[name])
    zona = pd.read_json(request.json())
    return zona

if __name__ == '__main__':
    app.run(debug=True)# , port=os.getenv("PORT", default=5000))
