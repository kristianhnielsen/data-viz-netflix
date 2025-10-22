from dash import Dash, html, dcc, Output, Input, callback
import pandas as pd
import plotly.express as px

from static import theme


def render(app: Dash, data: pd.DataFrame) -> html.Div:
    t = theme.THEME
    netflix_continuous = [t["background"], t["panel_bg"]]
    # Filter out very small counts to focus on main countries and ensure better color scaling
    country_data = data["country_primary"].value_counts().reset_index(name="count")

    fig = px.choropleth(
        country_data,
        locations="country_primary",
        locationmode="country names",
        color="count",
        color_continuous_scale=netflix_continuous,
        labels={"count": "Number of Titles"},
        range_color=(
            country_data["count"].quantile(0.1),
            country_data["count"].quantile(0.975),
        ),
    )

    # Update layout for better appearance
    fig.update_layout(
        title_font_size=16,
        title_x=0.5,
        geo=dict(
            showframe=True,
            framecolor="black",
            framewidth=4,
            showcoastlines=True,
            projection_type="equirectangular",
        ),
        coloraxis_colorbar=dict(
            title="Number of Titles",
            tickmode="linear",
            tick0=country_data["count"].min(),
            dtick=(country_data["count"].max() - country_data["count"].min()) / 5,
        ),
    )

    @callback(
        Output("country-histogram", "figure"),
        Output("country-genre-heatmap", "figure"),
        Input("country-map", "clickData"),
    )
    def update_charts(click_data: dict | None):
        # Default to United States if no country is clicked
        selected_country = "United States"

        if click_data and "points" in click_data:
            selected_country = click_data["points"][0]["location"]

        # Filter data for selected country
        country_df = data[
            (data["country_primary"] == selected_country) & (data["release_year"] > 0)
        ]

        # Create histogram data with bins and use bar chart with continuous color
        hist_data = country_df["release_year"].value_counts().sort_index().reset_index()
        hist_data.columns = ["release_year", "count"]

        hist_fig = px.bar(
            hist_data,
            x="release_year",
            y="count",
            title=f"Release Year Distribution - {selected_country}",
            labels={"release_year": "Release Year", "count": "Number of Titles"},
            color="release_year",
            color_continuous_scale=netflix_continuous,
        )

        hist_fig.update_layout(
            title_font_size=16,
            title_x=0.5,
            xaxis_title="Release Year",
            yaxis_title="Number of Titles",
            showlegend=False,
            coloraxis_showscale=False,  # Hide the colorbar since year is already on x-axis
        )

        # Create heatmap of genres over time
        # Split genres and create a row for each genre
        genre_data = []
        for _, row in country_df.iterrows():
            if pd.notna(row["genre"]):
                genres = [g.strip() for g in row["genre"].split(",")]
                for genre in genres:
                    genre_data.append(
                        {
                            "release_year": row["release_year"],
                            "genre": genre,
                        }
                    )

        if genre_data:
            genre_df = pd.DataFrame(genre_data)

            # Group by year and genre to count titles
            heatmap_data = (
                genre_df.groupby(["release_year", "genre"])
                .size()
                .reset_index(name="count")
            )

            # Pivot for heatmap
            pivot_data = heatmap_data.pivot(
                index="genre", columns="release_year", values="count"
            ).fillna(0)

            heatmap_fig = px.imshow(
                pivot_data,
                labels=dict(x="Release Year", y="Genre", color="Count"),
                title=f"Genre Distribution Over Time - {selected_country}",
                color_continuous_scale=netflix_continuous,
                aspect="auto",
            )

            heatmap_fig.update_layout(
                title_font_size=16,
                title_x=0.5,
                xaxis_title="Release Year",
                yaxis_title="Genre",
            )
        else:
            # Empty heatmap if no data
            heatmap_fig = px.imshow(
                [[0]],
                title=f"No Genre Data Available - {selected_country}",
            )

        return hist_fig, heatmap_fig

    return html.Div(
        [
            html.H2(
                "Netflix Content by Country",
                style={
                    "color": t["header_bg"],
                    "marginTop": "40px",
                },
            ),
            dcc.Graph(id="country-map", figure=fig, style={"height": "600px"}),
            html.Div(
                [
                    html.Div(
                        [
                            html.H3(
                                "Content Release Timeline",
                                style={"color": t["header_bg"], "marginTop": "40px"},
                            ),
                            dcc.Graph(
                                id="country-histogram", style={"height": "500px"}
                            ),
                        ]
                    ),
                    html.Div(
                        [
                            html.H3(
                                "Genre Popularity Over Time",
                                style={"marginTop": "40px", "color": t["header_bg"]},
                            ),
                            dcc.Graph(
                                id="country-genre-heatmap", style={"height": "500px"}
                            ),
                        ]
                    ),
                ],
                style={
                    "display": "grid",
                    "gridTemplateColumns": "1fr 1fr",
                    "gap": "20px",
                },
            ),
        ]
    )
