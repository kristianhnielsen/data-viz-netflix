from dash import Dash, html, dcc, Output, Input, callback
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from static import theme


def render(app: Dash, data: pd.DataFrame) -> html.Div:
    t = theme.THEME

    # Filter data to only include rows with both IMDb and Metascore ratings
    ratings_data: pd.DataFrame = data.dropna(subset=["imdb_rating", "metascore"]).copy()

    # Convert ratings to numeric if they aren't already
    ratings_data["imdb_rating"] = pd.to_numeric(
        ratings_data["imdb_rating"], errors="coerce"
    )
    ratings_data["metascore"] = pd.to_numeric(
        ratings_data["metascore"], errors="coerce"
    )
    ratings_data = ratings_data.dropna(subset=["imdb_rating", "metascore"])

    # Clean imdb_votes column - remove commas and convert to numeric
    if "imdb_votes" in ratings_data.columns:
        ratings_data["imdb_votes"] = (
            ratings_data["imdb_votes"]
            .astype(str)
            .str.replace(",", "", regex=False)
            .replace("nan", "0")
        )
        ratings_data["imdb_votes"] = pd.to_numeric(
            ratings_data["imdb_votes"], errors="coerce"
        )
        ratings_data["imdb_votes"] = ratings_data["imdb_votes"].fillna(0)

    # Extract primary genre from genre column (handle comma-separated genres)
    ratings_data["primary_genre"] = (
        ratings_data["genre"].str.split(",").str[0].str.strip()
    )

    # Get unique genres for filter dropdown
    genres: list[str] = sorted(ratings_data["primary_genre"].dropna().unique())

    @callback(
        Output("ratings-scatter", "figure"),
        Output("genre-boxplot", "figure"),
        Input("genre-filter", "value"),
        Input("type-filter", "value"),
    )
    def update_ratings_charts(
        selected_genres: list[str] | None,
        selected_types: list[str] | None,
    ):
        # Filter data based on selections
        filtered_data = ratings_data.copy()

        # Filter by genre
        if selected_genres:
            filtered_data = filtered_data.loc[
                filtered_data["primary_genre"].isin(selected_genres)
            ]

        # Filter by type (Movie/TV Show)
        if selected_types:
            filtered_data = filtered_data.loc[
                filtered_data["type"].isin(selected_types)
            ]

        # Create scatter plot: IMDb vs Metascore
        if len(filtered_data) > 0:
            scatter_fig = px.scatter(
                filtered_data,
                x="imdb_rating",
                y="metascore",
                color="primary_genre",
                size="imdb_votes" if "imdb_votes" in filtered_data.columns else None,
                hover_data=["title", "type", "release_year"],
                title="IMDb Rating vs Metascore Comparison",
                labels={
                    "imdb_rating": "IMDb Rating",
                    "metascore": "Metascore",
                    "primary_genre": "Genre",
                    "imdb_votes": "Votes",
                    "title": "Title",
                    "type": "Type",
                    "release_year": "Year",
                },
                color_discrete_sequence=t["categorical_colors"],
            )

            scatter_fig.update_traces(
                hovertemplate="<b>%{customdata[0]}</b><br>"
                + "Genre: %{fullData.name}<br>"
                + "IMDb Rating: %{x}<br>"
                + "Metascore: %{y}<br>"
                + "Type: %{customdata[1]}<br>"
                + "Year: %{customdata[2]}"
                + (
                    "<br>Votes: %{marker.size}"
                    if "imdb_votes" in filtered_data.columns
                    else ""
                )
                + "<extra></extra>"
            )

            # Add reference lines
            scatter_fig.add_hline(
                y=50,
                line_dash="dash",
                line_color="gray",
                annotation_text="Average Metascore",
            )
            scatter_fig.add_vline(
                x=6.5,
                line_dash="dash",
                line_color="gray",
                annotation_text="Average IMDb",
            )

            scatter_fig.update_layout(
                plot_bgcolor=t["card_bg"],
                paper_bgcolor=t["card_bg"],
                title_font_size=16,
                title_x=0.5,
                font=dict(color=t["text_primary"]),
                xaxis=dict(gridcolor=t["grid_color"], zerolinecolor=t["grid_color"]),
                yaxis=dict(gridcolor=t["grid_color"], zerolinecolor=t["grid_color"]),
            )

            # Create box plot: Rating distribution by genre
            boxplot_fig = go.Figure()

            # Add IMDb rating box plot
            boxplot_fig.add_trace(
                go.Box(
                    y=filtered_data["imdb_rating"],
                    x=filtered_data["primary_genre"],
                    name="IMDb Rating",
                    marker_color=t["plot_color"],
                    hovertemplate="Genre: %{x}<br>Rating: %{y}<extra></extra>",
                )
            )

            boxplot_fig.update_layout(
                title="Rating Distribution by Genre",
                xaxis_title="Genre",
                yaxis_title="IMDb Rating",
                plot_bgcolor=t["card_bg"],
                paper_bgcolor=t["card_bg"],
                title_font_size=16,
                title_x=0.5,
                xaxis_tickangle=-45,
                font=dict(color=t["text_primary"]),
                xaxis=dict(gridcolor=t["grid_color"], zerolinecolor=t["grid_color"]),
                yaxis=dict(gridcolor=t["grid_color"], zerolinecolor=t["grid_color"]),
            )

        else:
            # Empty figures if no data
            scatter_fig = px.scatter(title="No data available for selected filters")
            scatter_fig.update_layout(
                plot_bgcolor=t["card_bg"],
                paper_bgcolor=t["card_bg"],
                title_font_size=16,
                title_x=0.5,
                font=dict(color=t["text_primary"]),
                xaxis=dict(gridcolor=t["grid_color"], zerolinecolor=t["grid_color"]),
                yaxis=dict(gridcolor=t["grid_color"], zerolinecolor=t["grid_color"]),
            )

            boxplot_fig = go.Figure()
            boxplot_fig.update_layout(
                title="No data available for selected filters",
                plot_bgcolor=t["card_bg"],
                paper_bgcolor=t["card_bg"],
                title_font_size=16,
                title_x=0.5,
            )

        return scatter_fig, boxplot_fig

    return html.Div(
        [
            html.H2(
                "Ratings",
                style={
                    "color": t["text_primary"],
                    "marginBottom": "24px",
                    "fontWeight": "300",
                },
            ),
            # Filters section
            html.Div(
                [
                    html.Div(
                        [
                            html.Label(
                                "Genre",
                                style={
                                    "color": t["text_secondary"],
                                    "marginBottom": "8px",
                                    "display": "block",
                                    "fontSize": "14px",
                                },
                            ),
                            dcc.Dropdown(
                                id="genre-filter",
                                options=[
                                    {"label": genre, "value": genre} for genre in genres
                                ],
                                value=(
                                    genres[:5] if len(genres) > 5 else genres
                                ),  # Default to first 5 genres
                                multi=True,
                                placeholder="Select genres...",
                            ),
                        ],
                        style={
                            "width": "48%",
                            "display": "inline-block",
                            "marginRight": "2%",
                        },
                    ),
                    html.Div(
                        [
                            html.Label(
                                "Type",
                                style={
                                    "color": t["text_secondary"],
                                    "marginBottom": "8px",
                                    "display": "block",
                                    "fontSize": "14px",
                                },
                            ),
                            dcc.Dropdown(
                                id="type-filter",
                                options=[
                                    {"label": "Movie", "value": "Movie"},
                                    {"label": "TV Show", "value": "TV Show"},
                                ],
                                value=["Movie", "TV Show"],
                                multi=True,
                                placeholder="Select content type...",
                            ),
                        ],
                        style={
                            "width": "48%",
                            "display": "inline-block",
                        },
                    ),
                ],
                style={
                    "marginBottom": "32px",
                    "padding": "24px",
                    "backgroundColor": t["surface"],
                    "borderRadius": t["border_radius"],
                    "border": f"1px solid {t['surface_border']}",
                },
            ),
            # Charts section
            html.Div(
                [
                    html.Div(
                        [dcc.Graph(id="ratings-scatter", style={"height": "500px"})],
                        style={
                            "backgroundColor": t["surface"],
                            "borderRadius": t["border_radius"],
                            "padding": "16px",
                            "border": f"1px solid {t['surface_border']}",
                            "display": "inline-block",
                            "verticalAlign": "top",
                            "marginRight": "2%",
                        },
                    ),
                    html.Div(
                        [dcc.Graph(id="genre-boxplot", style={"height": "500px"})],
                        style={
                            "backgroundColor": t["surface"],
                            "borderRadius": t["border_radius"],
                            "padding": "16px",
                            "border": f"1px solid {t['surface_border']}",
                            "display": "inline-block",
                            "verticalAlign": "top",
                        },
                    ),
                ],
                style={"display": "grid", "gridTemplateColumns": "1fr 1fr", "gap": "0"},
            ),
        ],
        style={"padding": "40px 24px"},
    )
