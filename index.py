import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import decorators as dc
import plotly.express as px
import charts as ch

app = dash.Dash(__name__)

html.Div(
            style={'display': 'flex'},
            children=[
                
                    dcc.Dropdown(
                    id="filtro_historia",
                    options=historia,
                    value="Todos",
                    # multi=True
                    title="História"
                        ),
                    
                dcc.Dropdown(
                    dcc.Dropdown(
                    id="filtro_garantias",
                    options=garantias,
                    value="Todos",
                    #multi=True
                        ),
                    title="Garantias"
                ),
                dcc.Dropdown(
                    dcc.Dropdown(
                    id="filtro_renda",
                    options=renda,
                    value="Todos",
                    #multi=True
                        ),
                    title="Renda"
                )
            ]
        )