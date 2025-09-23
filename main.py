from dash import Dash, html, dcc, callback, Output, Input
import pandas as pd
from components import data_table, graph
from static import heading
from data import netflix


def main():
    # data import and preprocessing

    config = netflix.NetflixDataConfig(
        netflix_titles_path="data/netflix_titles.csv", omdb_path="data/omdb_data.csv"
    )

    preprocessor = netflix.NetflixDataPreprocessor()

    netflix_data = netflix.NetflixData(config=config, preprocessor=preprocessor)
    data = netflix_data.data

    # app setup
    app = Dash(__name__)
    app.title = "Netflix in Numbers"

    # app layout
    from static import theme

    t = theme.THEME

    app.layout = html.Div(
        [
            heading.render(),
            html.Div(
                children=[
                    html.Div(data_table.render(app, data=data), style={
                        "padding": "10px",
                        "overflow": "auto",
                        "height": "calc(100vh - 64px)",
                        "backgroundColor": t["panel_bg"],
                    }),
                    html.Div(graph.render(app, data=data), style={
                        "padding": "10px",
                        "overflow": "auto",
                        "height": "calc(100vh - 64px)",
                        "backgroundColor": t["card_bg"],
                    }),
                ],
                style={
                    "display": "grid",
                    "gridTemplateColumns": "40% 60%",
                    "gap": "12px",
                    "padding": "10px 20px",
                    "backgroundColor": t["background"],
                },
            ),
        ],
        style={"margin": "0", "padding": "0", "boxSizing": "border-box", "backgroundColor": t["background"]},
    )

    app.run(debug=True)


if __name__ == "__main__":
    main()
