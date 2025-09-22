from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd


def render(app: Dash, data: pd.DataFrame):
    df = data

    @callback(Output("graph-content", "figure"), Input("dropdown-selection", "value"))
    def update_graph(value):
        filtered_df = df[df.Country == value]
        return px.histogram(
            filtered_df,
            x="release_year",
            title=f"Movies in {value} by Year",
        )

    return html.Div(
        [
            html.H1(children="Movies in ", style={"textAlign": "center"}),
            dcc.Dropdown(df.Country.unique(), "Canada", id="dropdown-selection"),
            dcc.Graph(id="graph-content"),
        ]
    )
