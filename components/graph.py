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
            labels={"release_year": "Release Year", "count": "Number of Movies"},
        )

    return html.Div(
        [
            html.Div(html.H2("Movies by Year", style={"color": "#D3DAD9", "margin": "0"}), style={"display": "flex", "justifyContent": "space-between", "alignItems": "center"}),
            dcc.Dropdown(df.Country.unique(), "Canada", id="dropdown-selection", style={"marginTop": "8px"}),
            dcc.Graph(id="graph-content", style={"height": "calc(100vh - 160px)", "marginTop": "8px"}),
        ],
        style={"padding": "20px", "backgroundColor": "#2C2C2E", "height": "100%", "boxSizing": "border-box"},
    )
