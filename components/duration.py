# Movie Duration vs Year
from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from static import theme


def render(app: Dash, data: pd.DataFrame):
    df = data
    t = theme.THEME

    @callback(Output("duration-graph", "figure"), Input("year-slider", "value"))
    def update_duration_graph(year_range):
        # Filter by year range and only include movies (since we want duration in minutes)
        filtered_df = df[
            (df["release_year"] >= year_range[0])
            & (df["release_year"] <= year_range[1])
            & (df["type"] == "Movie")  # Only movies have meaningful duration in minutes
        ]

        # Extract numeric duration from runtime column if it exists
        if "runtime" in filtered_df.columns:
            # Extract minutes from runtime strings like "90 min"
            filtered_df = filtered_df.copy()
            filtered_df["duration_minutes"] = (
                filtered_df["runtime"].str.extract(r"(\d+)").astype(float)
            )

            # Remove rows where duration couldn't be extracted
            filtered_df = filtered_df.dropna(subset=["duration_minutes"])
        else:
            # Fallback if runtime column doesn't exist
            filtered_df = pd.DataFrame()

        if filtered_df.empty:
            # Create empty figure if no data
            fig = px.scatter(
                title=f"Movie Duration from {year_range[0]} to {year_range[1]} (No Data Available)",
                labels={"x": "Release Year", "y": "Duration (minutes)"},
            )
        else:
            fig = px.scatter(
                filtered_df,
                x="release_year",
                y="duration_minutes",
                title=f"Movie Duration from {year_range[0]} to {year_range[1]}",
                labels={
                    "release_year": "Release Year",
                    "duration_minutes": "Duration (minutes)",
                },
                hover_data={
                    "title": True,  # Show movie title on hover
                    "release_year": True,  # Show release year
                    "duration_minutes": True,  # Show duration
                    "rating": True,  # Show rating if available
                },
            )

            # Customize hover template for better readability
            fig.update_traces(
                hovertemplate="<b>%{customdata[0]}</b><br>"  # Movie title
                + "Release Year: %{x}<br>"
                + "Duration: %{y} minutes<br>"
                + "Rating: %{customdata[3]}<br>"
                + "<extra></extra>"  # Remove trace box
            )
        fig.update_layout(
            plot_bgcolor=t["card_bg"],
            paper_bgcolor=t["card_bg"],
        )
        return fig

    @callback(
        Output("movies-per-year-histogram", "figure"), Input("year-slider", "value")
    )
    def update_movies_per_year_histogram(year_range):
        # Filter by year range and only include movies
        filtered_df = df[
            (df["release_year"] >= year_range[0])
            & (df["release_year"] <= year_range[1])
            & (df["type"] == "Movie")
        ]

        if filtered_df.empty:
            # Create empty figure if no data
            fig = go.Figure()
            fig.update_layout(
                title=f"Movies Released Per Year ({year_range[0]} - {year_range[1]}) - No Data Available",
                xaxis_title="Release Year",
                yaxis_title="Number of Movies",
                plot_bgcolor=t["card_bg"],
                paper_bgcolor=t["card_bg"],
            )
        else:
            # Count movies per year
            movies_per_year = filtered_df["release_year"].value_counts().sort_index()

            fig = go.Figure(
                data=[
                    go.Bar(
                        x=movies_per_year.index,
                        y=movies_per_year.values,
                        name="Movies Released",
                        hovertemplate="<b>Year: %{x}</b><br>"
                        + "Movies Released: %{y}<br>"
                        + "<extra></extra>",
                    )
                ]
            )

            fig.update_layout(
                title=f"Movies Released Per Year ({year_range[0]} - {year_range[1]})",
                xaxis_title="Release Year",
                yaxis_title="Number of Movies",
                plot_bgcolor=t["card_bg"],
                paper_bgcolor=t["card_bg"],
                showlegend=False,
            )

        return fig

    @callback(
        Output("rating-distribution-chart", "figure"), Input("year-slider", "value")
    )
    def update_rating_distribution(year_range):
        # Filter by year range and only include movies
        filtered_df = df[
            (df["release_year"] >= year_range[0])
            & (df["release_year"] <= year_range[1])
            & (df["type"] == "Movie")
        ]

        if filtered_df.empty:
            # Create empty figure if no data
            fig = go.Figure()
            fig.update_layout(
                title=f"Movie Rating Distribution ({year_range[0]} - {year_range[1]}) - No Data Available",
                plot_bgcolor=t["card_bg"],
                paper_bgcolor=t["card_bg"],
            )
        else:
            # Count ratings, handling missing values
            rating_counts = filtered_df["rating"].fillna("Not Rated").value_counts()

            # Group smaller values into "Other" category
            # Keep top 6 ratings, group the rest as "Other"
            top_ratings = rating_counts.head(6)
            other_count = rating_counts.iloc[6:].sum() if len(rating_counts) > 6 else 0

            if other_count > 0:
                # Add "Other" category
                final_ratings = top_ratings.copy()
                final_ratings["Other"] = other_count
            else:
                final_ratings = top_ratings

            # Create pie chart for rating distribution
            fig = go.Figure(
                data=[
                    go.Pie(
                        labels=final_ratings.index,
                        values=final_ratings.values,
                        hovertemplate="<b>%{label}</b><br>"
                        + "Count: %{value}<br>"
                        + "Percentage: %{percent}<br>"
                        + "<extra></extra>",
                        textinfo="label+percent",
                        textposition="auto",
                        textfont=dict(size=14),  # Larger text
                        hole=0.3,  # Create a donut chart for better aesthetics
                    )
                ]
            )

            fig.update_layout(
                title={
                    "text": f"Movie Rating Distribution ({year_range[0]} - {year_range[1]})",
                    "x": 0.5,  # Center the title
                    "xanchor": "center",
                    "font": {"size": 18},  # Larger title
                },
                plot_bgcolor=t["card_bg"],
                paper_bgcolor=t["card_bg"],
                showlegend=True,
                legend=dict(
                    orientation="h",  # Horizontal legend
                    yanchor="top",
                    y=-0.1,  # Position below the chart
                    xanchor="center",
                    x=0.5,
                    font=dict(size=12),  # Larger legend text
                ),
                font=dict(size=12),
                margin=dict(t=80, b=100, l=50, r=50),  # Adjust margins
            )

        return fig

    return html.Div(
        [
            html.Div(
                html.H2(
                    "Netflix Content Analytics: Duration, Trends, Ratings & Evolution",
                    style={"margin": "0"},
                ),
                style={
                    "display": "flex",
                    "justifyContent": "space-between",
                    "alignItems": "center",
                },
            ),
            dcc.RangeSlider(
                id="year-slider",
                min=int(1940),
                max=int(2025),
                value=[int(df["release_year"].min()), int(df["release_year"].max())],
                marks={
                    str(year): str(year)
                    for year in range(
                        int(df["release_year"].min()),
                        int(df["release_year"].max()) + 1,
                        5,
                    )
                },
                step=1,
            ),
            html.Div(
                [
                    html.Div(
                        [
                            dcc.Graph(
                                id="duration-graph",
                                style={"height": "400px", "marginTop": "8px"},
                            ),
                        ],
                        style={
                            "width": "50%",
                            "display": "inline-block",
                            "verticalAlign": "top",
                        },
                    ),
                    html.Div(
                        [
                            dcc.Graph(
                                id="movies-per-year-histogram",
                                style={"height": "400px", "marginTop": "8px"},
                            ),
                        ],
                        style={
                            "width": "50%",
                            "display": "inline-block",
                            "verticalAlign": "top",
                        },
                    ),
                ],
                style={"marginBottom": "20px"},
            ),
            html.Div(
                [
                    html.Div(
                        [
                            dcc.Graph(
                                id="rating-distribution-chart",
                                style={
                                    "height": "600px",
                                    "marginTop": "8px",
                                },  # Increased height
                            ),
                        ],
                        style={
                            "width": "100%",
                            "display": "inline-block",
                        },
                    ),
                ],
            ),
        ],
        style={
            "padding": "20px",
            "backgroundColor": t["card_bg"],
            "height": "100%",
            "boxSizing": "border-box",
        },
    )
