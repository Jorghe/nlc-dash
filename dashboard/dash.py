from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import plotly.express as px

def initialize_dash(server):    
    dash_app = Dash(server=server, routes_pathname_prefix='/dashapp/')
    dash_app.layout = html.Div(children=[
        html.Header(children=[
            html.H1('Dash para nlC')
        ]),
        html.Main(children=[
            html.H2('Grafica de la Huaste'),
            dcc.Input(type='text', value='Buscar...', id='search-bar'),
            html.H3('Indicadores de la Huaste'),
        # dcc.Graph(id='graph-huaste')
        ])
    ])
    return dash_app.server
    
"""@app.callback(
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
    """
