from dash import Dash, html, dash_table, dcc
import pandas as pd


def render(app: Dash, data: pd.DataFrame):
    columns_for_table = ["title",  "director", "Country"]
    table = dash_table.DataTable(
        id="data-table",
        columns=[{"name": i, "id": i} for i in columns_for_table],
        data=data[columns_for_table].to_dict("records"),  # type: ignore
        page_size=10,
        style_table={"overflowX": "auto"},
        style_cell={
            "textAlign": "left",
            "backgroundColor": "#715A5A",
            "color": "#D3DAD9",
        },
        style_header={"backgroundColor": "#44444E", "fontWeight": "bold"},
        filter_action="native",
    )

    return html.Div(
        children=[
            html.H2("Data Overview", style={"color": "#D3DAD9", "marginTop": "0"}),
            html.Div(table, style={"height": "100%"}),
        ],
        style={"color": "#D3DAD9", "padding": "6px"},
    )
