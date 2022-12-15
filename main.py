from flask import Flask, jsonify
import os
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import requests


app = Dash(__name__)

stylesheets = ['https://nl-climbing.deta.dev/static/style.css']
routes = {
    'huaste': 'https://nl-climbing.deta.dev/api/huaste/',
    'salto': 'https://nl-climbing.deta.dev/api/salto/',
    'epc': 'https://nl-climbing.deta.dev/api/epc/'
}

app.layout = html.Div(children=[
    html.Header(children=[
        html.H1('Dash para nlC')
    ]),
    html.Main(children=[
        dcc.Graph(id='graph-huaste')
    ])
    

])

""" @app.route('/')
def index():
    req_huaste = requests.get(routes['huaste'])
    api_huaste = pd.read_json(req_huaste.json())
    return api_huaste.to_json() """

@app.callback(
    Output('graph-huaste', 'figure')
)
def actualizar_grafica():
    huaste= from_api('huaste')
    figure = px.scatter(huaste,
        x = "Area",
        y = "Grade",
        hover_data = ['Name', 'Style'],

    )
    return figure


def from_api(name:str):
    request = requests.get(routes[name])
    zona = pd.read_json(request.json())
    return zona
if __name__ == '__main__':
    app.run_server(debug=True)# , port=os.getenv("PORT", default=5000))
