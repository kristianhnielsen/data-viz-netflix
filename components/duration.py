# Movie Duration vs Year
from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
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
            )
        fig.update_layout(
            plot_bgcolor=t["card_bg"],
            paper_bgcolor=t["card_bg"],
        )
        return fig

    return html.Div(
        [
            html.Div(
                html.H2("Movie Duration vs Year", style={"margin": "0"}),
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
            dcc.Graph(
                id="duration-graph",
                style={"height": "calc(100vh - 160px)", "marginTop": "8px"},
            ),
        ],
        style={
            "padding": "20px",
            "backgroundColor": t["card_bg"],
            "height": "100%",
            "boxSizing": "border-box",
        },
    )
