from dash import Dash, html, dcc, callback, Output, Input
import pandas as pd
from components import data_table, graph, map, duration
from static import heading
from data import netflix
from components import explore_by_country


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
            duration.render(app, data),
        ],
        style={
            "margin": "0",
            "padding": "0",
            "boxSizing": "border-box",
            "backgroundColor": t["background"],
        },
    )

    app.run(debug=True)


if __name__ == "__main__":
    main()
