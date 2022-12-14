from flask import Flask, jsonify
import os
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd


app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
