from dash import Dash, html, dcc, callback, Output, Input
import pandas as pd
from components import data_table
from static import heading


def main():
    # data preprocessing
    netflix_data = pd.read_csv(r"data\netflix_titles.csv")

    netflix_data["Top 3 cast"] = netflix_data["cast"].apply(
        lambda x: ", ".join(x.split(", ")[:3]) if pd.notnull(x) else x
    )

    # app setup
    app = Dash(__name__)
    app.title = "Netflix in Numbers"

    # app layout
    app.layout = [
        heading.render(),
        html.Div(
            children=[
                data_table.render(app, data=netflix_data),
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
