from dash import Dash, html, dash_table, dcc
import pandas as pd
from static import theme


def render(app: Dash, data: pd.DataFrame):
    t = theme.THEME

    columns_for_table = ["title",  "director", "Country"]
    table = dash_table.DataTable(
        id="data-table",
        columns=[{"name": i, "id": i} for i in columns_for_table],
        data=data[columns_for_table].to_dict("records"),  # type: ignore
        page_size=10,
        style_table={"overflowX": "auto", "height": "calc(100vh - 160px)"},
        style_cell={
            "textAlign": "left",
            "backgroundColor": t["card_bg"],
            "color": t["text"],
        },
        style_header={"backgroundColor": t["panel_bg"], "fontWeight": "bold", "color": t["muted_text"]},
        filter_action="native",
    )

    return html.Div(
        children=[
            html.H2("Data Overview", style={"color": t["text"], "marginTop": "0"}),
            html.Div(table, style={"height": "100%"}),
        ],
        style={"color": t["text"], "padding": "6px"},
    )
