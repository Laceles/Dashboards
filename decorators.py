# modificando as funções
import pandas as pd


def garantias_func(x: list, df: pd.DataFrame):
    valuex = list(df["garantias"].unique()) if "Todos" in x else x
    return valuex


def historia_func(x: list, df: pd.DataFrame):
    valuex = list(df["historia"].unique()) if "Todos" in x else x
    return valuex


def renda_func(x: list, df: pd.DataFrame):
    valuex = list(df["renda"].unique()) if "Todos" in x else x
    return valuex


def df_filtered(value_1, value_2, value_3, df: pd.DataFrame):
    garantias = garantias_func(value_1, df)
    historia = historia_func(value_2, df)
    renda = renda_func(value_3, df)
    df_filtered = df.loc[
        (df["garantias"].isin(garantias))
        & (df["historia"].isin(historia))
        & (df["renda"].isin(renda))
    ]
    return df_filtered
