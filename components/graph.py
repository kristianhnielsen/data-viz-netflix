from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
from static import theme


def render(app: Dash, data: pd.DataFrame):
    df = data
    t = theme.THEME

    @callback(Output("graph-content", "figure"), Input("dropdown-selection", "value"))
    def update_graph(value):
        filtered_df = df[df["country_primary"] == value]
        fig = px.histogram(
            filtered_df,
            x="release_year",
            title=f"Movies in {value} by Year",
            labels={"release_year": "Release Year", "count": "Number of Movies"},
        )
        fig.update_layout(
            plot_bgcolor=t["card_bg"],
            paper_bgcolor=t["panel_bg"],
        )
        return fig

    return html.Div(
        [
            html.Div(
                html.H2("Movies by Year", style={"margin": "0"}),
                style={
                    "display": "flex",
                    "justifyContent": "space-between",
                    "alignItems": "center",
                },
            ),
            dcc.Dropdown(
                df["country_primary"].dropna().unique().tolist(),
                "Canada",
                id="dropdown-selection",
                style={"marginTop": "8px"},
            ),
            dcc.Graph(
                id="graph-content",
                style={"height": "calc(100vh - 160px)", "marginTop": "8px"},
            ),
        ],
        style={
            "padding": "20px",
            "backgroundColor": t["panel_bg"],
            "height": "100%",
            "boxSizing": "border-box",
        },
    )
