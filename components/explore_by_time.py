from dash import Dash, html, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
from static import theme


def get_colors_from_scale(scale_data: str | list, num_colors: int) -> list:
    """
    Extract colors from a Plotly colorscale or use categorical colors.

    Args:
        scale_data: Either a Plotly colorscale name (str) or a list of colors
        num_colors: Number of colors to extract

    Returns:
        List of color strings
    """
    import plotly.colors as pc

    # If it's already a list of colors (categorical), return subset
    if isinstance(scale_data, list):
        # If first item is a list (sequential scale format), extract from it
        if scale_data and isinstance(scale_data[0], list):
            colorscale = scale_data
            colors = []
            for i in range(num_colors):
                ratio = i / (num_colors - 1) if num_colors > 1 else 0
                closest_idx = min(
                    range(len(colorscale)), key=lambda j: abs(colorscale[j][0] - ratio)
                )
                colors.append(colorscale[closest_idx][1])
            return colors
        else:
            # It's a categorical color list, cycle through if needed
            return [scale_data[i % len(scale_data)] for i in range(num_colors)]

    # It's a named Plotly colorscale string
    colorscale = pc.get_colorscale(scale_data)
    colors = []
    for i in range(num_colors):
        ratio = i / (num_colors - 1) if num_colors > 1 else 0
        closest_idx = min(
            range(len(colorscale)), key=lambda j: abs(colorscale[j][0] - ratio)
        )
        colors.append(colorscale[closest_idx][1])

    return colors


def render(app: Dash, data: pd.DataFrame) -> html.Div:
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
            runtime_series = pd.Series(filtered_df["runtime"])
            filtered_df["duration_minutes"] = (
                pd.to_numeric(runtime_series.str.extract(r"(\d+)")[0], errors="coerce")
            )

            # Remove rows where duration couldn't be extracted
            filtered_df = filtered_df[pd.notna(filtered_df["duration_minutes"])]
        else:
            # Fallback if runtime column doesn't exist
            filtered_df = pd.DataFrame()

        if len(filtered_df) == 0:
            # Create empty figure if no data
            fig = px.scatter(
                title=f"Movie Duration from {year_range[0]} to {year_range[1]} (No Data Available)",
                labels={"x": "Release Year", "y": "Duration (minutes)"},
            )
            fig.update_layout(
                plot_bgcolor=t["card_bg"],
                paper_bgcolor=t["card_bg"],
                title_font_size=16,
                title_x=0.5,
                xaxis_title="Release Year",
                yaxis_title="Duration (minutes)",
                font=dict(color=t["text_primary"]),
                xaxis=dict(gridcolor=t["grid_color"], zerolinecolor=t["grid_color"]),
                yaxis=dict(gridcolor=t["grid_color"], zerolinecolor=t["grid_color"])
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

            # Apply theme color to markers
            fig.update_traces(
                marker=dict(color=t["plot_color"]),
                hovertemplate="<b>%{customdata[0]}</b><br>"  # Movie title
                + "Release Year: %{x}<br>"
                + "Duration: %{y} minutes<br>"
                + "Rating: %{customdata[3]}<br>"
                + "<extra></extra>",  # Remove trace box
            )

            fig.update_layout(
                plot_bgcolor=t["card_bg"],
                paper_bgcolor=t["card_bg"],
                title_font_size=16,
                title_x=0.5,
                font=dict(color=t["text_primary"]),
                xaxis=dict(gridcolor=t["grid_color"], zerolinecolor=t["grid_color"]),
                yaxis=dict(gridcolor=t["grid_color"], zerolinecolor=t["grid_color"])
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

        if len(filtered_df) == 0:
            # Create empty figure if no data
            fig = px.bar(
                title=f"Movies Released Per Year ({year_range[0]} - {year_range[1]}) - No Data Available",
                labels={"x": "Release Year", "y": "Number of Movies"},
            )
            fig.update_traces(marker=dict(color=t["plot_color"]))
            fig.update_layout(
                plot_bgcolor=t["card_bg"],
                paper_bgcolor=t["card_bg"],
                title_font_size=16,
                title_x=0.5,
                font=dict(color=t["text_primary"]),
                xaxis=dict(gridcolor=t["grid_color"], zerolinecolor=t["grid_color"]),
                yaxis=dict(gridcolor=t["grid_color"], zerolinecolor=t["grid_color"])
            )
        else:
            # Count movies per year
            movies_per_year = pd.Series(filtered_df["release_year"]).value_counts().sort_index()
            movies_df = movies_per_year.reset_index()
            movies_df.columns = ["release_year", "count"]

            fig = px.bar(
                movies_df,
                x="release_year",
                y="count",
                title=f"Movies Released Per Year ({year_range[0]} - {year_range[1]})",
                labels={"release_year": "Release Year", "count": "Number of Movies"},
            )

            fig.update_traces(
                marker=dict(color=t["plot_color"]),
                hovertemplate="<b>Year: %{x}</b><br>"
                + "Movies Released: %{y}<br>"
                + "<extra></extra>",
            )

            fig.update_layout(
                plot_bgcolor=t["card_bg"],
                paper_bgcolor=t["card_bg"],
                showlegend=False,
                title_font_size=16,
                title_x=0.5,
                xaxis_title="Release Year",
                yaxis_title="Number of Movies",
                font=dict(color=t["text_primary"]),
                xaxis=dict(gridcolor=t["grid_color"], zerolinecolor=t["grid_color"]),
                yaxis=dict(gridcolor=t["grid_color"], zerolinecolor=t["grid_color"])
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

        if len(filtered_df) == 0:
            # Create empty figure if no data
            fig = px.pie(
                title=f"Movie Rating Distribution ({year_range[0]} - {year_range[1]}) - No Data Available",
            )
            fig.update_layout(
                plot_bgcolor=t["card_bg"],
                paper_bgcolor=t["card_bg"],
                title_font_size=16,
                title_x=0.5,
                font=dict(color=t["text_primary"]),
                xaxis=dict(gridcolor=t["grid_color"], zerolinecolor=t["grid_color"]),
                yaxis=dict(gridcolor=t["grid_color"], zerolinecolor=t["grid_color"])
            )
        else:
            # Count ratings, handling missing values
            rating_counts = pd.Series(filtered_df["rating"]).fillna("Not Rated").value_counts()

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
            rating_df = final_ratings.reset_index()
            rating_df.columns = ["rating", "count"]

            fig = px.pie(
                rating_df,
                values="count",
                names="rating",
                title=f"Movie Rating Distribution ({year_range[0]} - {year_range[1]})",
                hole=0.3,  # Create a donut chart for better aesthetics
                color_discrete_sequence=t[
                    "categorical_colors"
                ],  # Use colorblind-safe categorical colors
            )

            fig.update_traces(
                hovertemplate="<b>%{label}</b><br>"
                + "Count: %{value}<br>"
                + "Percentage: %{percent}<br>"
                + "<extra></extra>",
                textinfo="label+percent",
                textposition="auto",
                textfont=dict(size=14),
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
            html.H2(
                "📈 Content Trends",
                style={
                    "color": t["text_primary"],
                    "marginBottom": "24px",
                    "fontWeight": "300"
                },
            ),
            
            # Year Range Filter
            html.Div([
                html.Label("Time Period", style={"color": t["text_secondary"], "marginBottom": "12px", "display": "block", "fontSize": "14px"}),
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
                            10,
                        )
                    },
                    step=1,
                ),
            ], style={"marginBottom": "32px", "padding": "24px", "backgroundColor": t["surface"], "borderRadius": t["border_radius"], "border": f"1px solid {t['surface_border']}"}),
            
            # Charts Grid
            html.Div(
                [
                    html.Div(
                        [dcc.Graph(id="rating-distribution-chart", style={"height": "350px"})],
                        style={"backgroundColor": t["surface"], "borderRadius": t["border_radius"], "padding": "16px", "border": f"1px solid {t['surface_border']}"}
                    ),
                    html.Div(
                        [dcc.Graph(id="movies-per-year-histogram", style={"height": "350px"})],
                        style={"backgroundColor": t["surface"], "borderRadius": t["border_radius"], "padding": "16px", "border": f"1px solid {t['surface_border']}", "marginLeft": "16px"}
                    ),
                ],
                style={"display": "grid", "gridTemplateColumns": "1fr 1fr", "gap": "0", "marginBottom": "24px"}
            ),
            
            # Duration Analysis
            html.Div([
                dcc.Graph(id="duration-graph", style={"height": "500px"})
            ], style={"backgroundColor": t["surface"], "borderRadius": t["border_radius"], "padding": "24px", "border": f"1px solid {t['surface_border']}"})
        ],
        style={"padding": "40px 24px"}
    )
