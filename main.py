from dash import Dash, html, dcc, callback, Output, Input
import pandas as pd
from components import data_table
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
    app.layout = [
        heading.render(),
        html.Div(
            children=[
                data_table.render(app, data=data),
            ],
            style={
                "textAlign": "center",
                "backgroundColor": "#44444E",
                "padding": "10px",
            },
        ),
    ]

    app.run(debug=True)


if __name__ == "__main__":
    main()
