from flask import Flask, jsonify
import os
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import requests


app = Flask(__name__)

routes = {
    'huaste': 'https://nl-climbing.deta.dev/api/huaste/',
    'salto': 'https://nl-climbing.deta.dev/api/salto/',
    'epc': 'https://nl-climbing.deta.dev/api/epc/'
}

@app.route('/')
def index():
    req_huaste = requests.get(routes['huaste'])
    api_huaste = pd.read_json(req_huaste.json())
    return api_huaste.to_html()


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
