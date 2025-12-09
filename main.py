from dash import Dash, html
from components import (
    explore_by_time,
    explore_by_country,
    ratings_comparison,
    genre_analysis,
)
from static import heading, navigation
from data import netflix

# app setup
app = Dash(__name__)
app.title = "Netflix in Numbers - Interactive Data Visualization"
server = app.server


def main():
    # data import and preprocessing
    config = netflix.NetflixDataConfig(
        netflix_titles_path="data/netflix_titles.csv", omdb_path="data/omdb_data.csv"
    )

    preprocessor = netflix.NetflixDataPreprocessor()

    netflix_data = netflix.NetflixData(config=config, preprocessor=preprocessor)
    data = netflix_data.data

    # app layout
    from static import theme

    t = theme.THEME

    app.layout = html.Div(
        [
            heading.render(),
            navigation.render(),
            # Temporal Analysis Section
            html.Div(
                id="temporal-analysis", children=[explore_by_time.render(app, data)]
            ),
            # Geographic Analysis Section
            html.Div(
                id="country-analysis", children=[explore_by_country.render(app, data)]
            ),
            # Ratings Comparison Section
            html.Div(
                id="ratings-analysis", children=[ratings_comparison.render(app, data)]
            ),
            # Genre Analysis Section
            html.Div(id="genre-analysis", children=[genre_analysis.render(app, data)]),
            # Footer
            html.Div(
                [
                    html.P(
                        "© 2024 Netflix Data Visualization Project | DSK808 Course",
                        style={
                            "textAlign": "center",
                            "margin": "20px 0",
                            "color": t["text_secondary"],
                        },
                    )
                ],
                style={
                    "backgroundColor": t["background"],
                    "padding": "20px 0",
                    "marginTop": "40px",
                },
            ),
        ],
        style={
            "margin": "0",
            "padding": "0",
            "boxSizing": "border-box",
            "backgroundColor": t["background"],
            "minHeight": "100vh",
            "fontFamily": "'Helvetica Neue', Arial, sans-serif",
        },
    )

    app.run(debug=True)


if __name__ == "__main__":
    main()
