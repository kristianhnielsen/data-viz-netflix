from dash import Dash, html
from components import explore_by_time, explore_by_country
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
            explore_by_time.render(app, data),
            explore_by_country.render(app, data),
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
