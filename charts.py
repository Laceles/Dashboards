import pandas as pd
import plotly.express as px
import plotly.graph_objs as go

df = pd.read_csv("risco_credito_regras.csv")

#Category columns list
garantias = list(df["garantias"].unique())
historia = list(df["historia"].unique())
renda = list(df["renda"].unique())
risco = list(df["risco"].unique())
divida = list(df["divida"].unique())

#Options list
garantias.append("Todos")
historia.append("Todos")
renda.append("Todos")
risco.append("Todos")
divida.append("Todos")

# Bar chart
divida_names = list(df['divida'].unique())
divida_count = list(df['divida'].value_counts().values)
bar_data = go.Bar(x=divida_names, y=divida_count)

#Pizza chart
historia_names = list(df['historia'].unique())
historia_count = list(df['historia'].value_counts().values)
pie_data = go.Pie(labels=divida_names, values=divida_count)
