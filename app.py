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
        html.H2('Grafica de la Huaste'),
        dcc.Input(type='text', value='Buscar...', id='search-bar'),
        html.H3('Indicadores de la Huaste'),
        dcc.Graph(id='graph-huaste')
    ])
    

])

""" @app.route('/')
def index():
    req_huaste = requests.get(routes['huaste'])
    api_huaste = pd.read_json(req_huaste.json())
    js = api_huaste.to_json()
    return "<p>You are in Index</p>" """

@app.callback(
    Output('graph-huaste', 'figure'),
    Input('search-bar', 'value')
)
def actualizar_grafica():
    try:
        huaste= from_api('huaste')
        figure = px.scatter(huaste,
        x = "Area",
        y = "Grade",
        hover_data = ['Name', 'Style']
        )
    except Exception:
      print('An exception occurred')


    
    return figure


def from_api(name:str):
    request = requests.get(routes[name])
    zona = pd.read_json(request.json())
    return zona

if __name__ == '__main__':
    app.run_server(debug=True)# , port=os.getenv("PORT", default=5000))
