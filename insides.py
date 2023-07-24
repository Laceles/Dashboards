import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import decorators as dc
import dash_table
import dash_bootstrap_components as dbc
from charts import bar_data, pie_data,garantias,historia,renda,risco,divida, df
from dark_mode import colors
import json



app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = html.Div(
        children=[
            html.H1(children="Filtragem de Valores", style={
            'textAlign': 'center',
            'color': "#4169E1"
        }),
            html.H2("Aplicando os gráficos de barras", style={
            'textAlign': 'center',
            'color': "#4169E1"
        }),
            dcc.Dropdown(
                id='dark_mode',
                options=[{'label': 'Light', 'value': 'Light'},
                         {'label': 'Dark', 'value': 'Dark'}],
                value='Light',
                style={
                'width': '100px',  # Define a largura do dropdown
                'color': 'blue',   # Define a cor do texto
                'font-size': '16px', # Define o tamanho da fonte
                'background-color': 'lightgrey',  # Define a cor de fundo
                'border': '2px solid black',      # Define a borda
                'border-radius': '5px',          # Define o raio da borda
                'align-items': 'left'
                }),
            html.Div(
            children=[
                    html.H3("História",
                            style={
                            'color': '#4169E1',
                            'fontFamily': 'Arial'
                            }),
                    dcc.Dropdown(
                    id="filtro_historia",
                    options=historia,
                    value="Todos",
                    style={'font-family': 'arial', "font-size": "1.2em",
                    'marginBottom': 10, 'marginTop': 2, 'text-align': 'center',
                    'width': '200px'}
                ),
                    html.H3("Garantias",
                            style={
                            'color': '#4169E1',
                            'fontFamily': 'Arial'
                            }),
                    dcc.Dropdown(
                    id="filtro_garantias",
                    options=garantias,
                    value="Todos",
                    style={'font-family': 'arial', "font-size": "1.2em",
                    'marginBottom': 10, 'marginTop': 2, 'text-align': 'center',
                    'width': '200px'}
                ),
                    html.H3("Renda",
                            style={
                            'color': '#4169E1',
                            'fontFamily': 'Arial',
                            }),
                    dcc.Dropdown(
                    id="filtro_renda",
                    options=renda,
                    value="Todos",
                    style={'font-family': 'arial', "font-size": "1.2em",
                    'marginBottom': 10, 'marginTop': 2, 'text-align': 'center',
                    'width': '200px'}
                )
            ]
        ),
            html.Div(children=[
                dcc.Graph(
                    id='bar-chart',
                    config={"displayModeBar":False},
                     figure={
                        'data':[
                            bar_data
                            ],
                        'layout':{
                            'title': 'Gráficos de Barras',
                            'plot_bgcolor': '#000000',
                            'paper_bgcolor': '#121212'
                            }
                        },
                    style={"color":"white","width": "50%", "display": "inline-block",'backgroundColor': '#f0f0f0'}
                    ),
                dcc.Graph(
                    id='pizza-chart',
                    config={"displayModeBar":False},
                    figure={
                        'data':[
                            pie_data
                            ],
                        'layout':{
                            'title': 'Gráficos de Pizza',
                            'plot_bgcolor': 'white',
                            'paper_bgcolor': '#121212',
                            }
                        },
                    style={"color":"white","width": "50%", "display": "inline-block",'backgroundColor': '#121212'}
                )]),
            html.Div(
                        children=[
                            dbc.Row(
                                dbc.Col(
                                    html.Div(
                                    children =[
                                    html.H3("Tabela com Dados da Base de Dados",style={'textAlign':'center',"width": "50%",'color': "white"}),
                                    
                                    dash_table.DataTable(
                                    id='tabela-dados',
                                    columns=[{'name': col, 'id': col} for col in df.columns],
                                    data=df.to_dict('records'),
                                    style_table={
                                                'width': '50%',
                                                'margin': 'auto',
                                                'border': '2px solid black',
                                                'border-collapse': 'collapse',
                                                "width": "50%"
                                            },
                                    style_cell={'padding': '5px',
                                                'backgroundColor': 'Grey'},
                                    style_header={
                                                    'backgroundColor': 'Black',
                                                    'fontWeight': 'bold',
                                                    'color': 'White'
                                                },
                                    page_size=5,
                
                                        )   
                                    ]
                                    )
                                )
                            )
                        ]
                    )
    ],style={'backgroundColor': '#121212'}
)


@app.callback(
    Output("bar-chart", "figure"),
    [Input("filtro_garantias", "value"),
     Input("filtro_historia", "value"),
     Input("filtro_renda", "value")]
)
def chart_bar(filtro_garantias,filtro_historia,filtro_renda):
    df_filtered = dc.df_filtered(filtro_garantias,filtro_historia,filtro_renda, df)
    divida_names = list(df_filtered['divida'].unique())
    divida_count = list(df_filtered['divida'].value_counts().values)
    fig_bar = {"data":[{'x': divida_names, 'y': divida_count, 'type': 'bar'}],
               'layout':{
                            'title': 'Gráficos de Barras',
                            'plot_bgcolor': '#000000',
                            'paper_bgcolor': '#121212',
                            'font':{'color':'white'}
                            }}
    return fig_bar

@app.callback(
    Output("pizza-chart", "figure"),
    [Input("filtro_garantias", "value"),
     Input("filtro_historia", "value"),
     Input("filtro_renda", "value")]
)
def pizza_chart(filtro_garantias,filtro_historia,filtro_renda):
    df_filtered = dc.df_filtered(filtro_garantias,filtro_historia,filtro_renda, df)
    historia_names = list(df_filtered['historia'].unique())
    historia_count = list(df_filtered['historia'].value_counts().values)
    fig_pie = {"data":[{'values': historia_count, 'labels': historia_names, 'type': 'pie'}],
               'layout':{
                            'title': 'Gráficos de Barras',
                            'plot_bgcolor': '#000000',
                            'paper_bgcolor': '#121212',
                            'font':{'color':'white'}
                            }}
    return fig_pie

@app.callback(
    Output("tabela-dados", "data"),
    [Input("filtro_garantias", "value"),
     Input("filtro_historia", "value"),
     Input("filtro_renda", "value")]
)
def chart_table(filtro_garantias,filtro_historia,filtro_renda):
    df_filtered = dc.df_filtered(filtro_garantias,filtro_historia,filtro_renda, df)
    data=df_filtered.to_dict('records')
    return data

# App execution
if __name__ == "__main__":
    app.run_server(debug=True)