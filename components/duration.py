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

    @callback(
        Output("content-calendar-heatmap", "figure"),
        Input("content-type-dropdown", "value"),
    )
    def update_content_calendar(content_type):
        # Filter by content type if specified
        if content_type == "All":
            filtered_df = df
        else:
            filtered_df = df[df["type"] == content_type]

        # Check if date_added column exists in the dataset
        if "date_added" in filtered_df.columns:
            filtered_df = filtered_df.copy()
            # date_added should already be processed in the data preprocessing

            # Remove rows with invalid dates
            filtered_df = filtered_df.dropna(subset=["date_added"])

            if filtered_df.empty:
                # Create empty figure if no valid dates
                fig = go.Figure()
                fig.update_layout(
                    title="Content Addition Calendar - No Valid Date Data",
                    plot_bgcolor=t["card_bg"],
                    paper_bgcolor=t["card_bg"],
                    height=500,
                )
                fig.add_annotation(
                    text="No valid dates found in dataset",
                    xref="paper",
                    yref="paper",
                    x=0.5,
                    y=0.5,
                    xanchor="center",
                    yanchor="middle",
                    showarrow=False,
                    font=dict(size=16),
                )
                return fig

            # Extract month and day
            filtered_df["month"] = filtered_df["date_added"].dt.month
            filtered_df["day"] = filtered_df["date_added"].dt.day

            # Create a pivot table for the heatmap
            # Count content additions by month and day
            heatmap_data = (
                filtered_df.groupby(["month", "day"]).size().reset_index(name="count")
            )

            # Create a complete grid for all months and days
            months = range(1, 13)
            days = range(1, 32)

            # Create a complete grid with valid dates only
            full_grid = []
            for month in months:
                for day in days:
                    # Skip invalid dates (like Feb 30, Apr 31, etc.)
                    try:
                        pd.Timestamp(year=2024, month=month, day=day)
                        full_grid.append({"month": month, "day": day})
                    except ValueError:
                        continue

            full_grid_df = pd.DataFrame(full_grid)

            # Merge with actual data
            heatmap_pivot = full_grid_df.merge(
                heatmap_data, on=["month", "day"], how="left"
            ).fillna(0)

            # Create pivot table for plotly
            pivot_table = heatmap_pivot.pivot(
                index="day", columns="month", values="count"
            ).fillna(0)

            # Month names for better readability
            month_names = [
                "Jan",
                "Feb",
                "Mar",
                "Apr",
                "May",
                "Jun",
                "Jul",
                "Aug",
                "Sep",
                "Oct",
                "Nov",
                "Dec",
            ]

            fig = go.Figure(
                data=go.Heatmap(
                    z=pivot_table.values,
                    x=month_names,
                    y=list(range(1, 32)),
                    colorscale="Blues",
                    hoverongaps=False,
                    hovertemplate=(
                        "<b>%{x} %{y}</b><br>"
                        + "Content Added: %{z}<br>"
                        + "<extra></extra>"
                    ),
                    colorbar=dict(
                        title="Content Count",
                    ),
                )
            )

            fig.update_layout(
                title={
                    "text": f"Netflix Content Addition Calendar - {content_type}",
                    "x": 0.5,
                    "xanchor": "center",
                    "font": {"size": 16},
                },
                xaxis_title="Month",
                yaxis_title="Day of Month",
                yaxis=dict(
                    dtick=1,
                    range=[0.5, 31.5],
                    autorange="reversed",  # Day 1 at top
                ),
                plot_bgcolor=t["card_bg"],
                paper_bgcolor=t["card_bg"],
                height=500,
                font=dict(size=11),
                margin=dict(t=60, b=60, l=60, r=100),
            )

        else:
            # Create empty figure if no date_added column
            fig = go.Figure()
            fig.update_layout(
                title="Content Addition Calendar - No Date Data Available",
                plot_bgcolor=t["card_bg"],
                paper_bgcolor=t["card_bg"],
                height=500,
            )
            fig.add_annotation(
                text="No date_added column found in dataset",
                xref="paper",
                yref="paper",
                x=0.5,
                y=0.5,
                xanchor="center",
                yanchor="middle",
                showarrow=False,
                font=dict(size=16),
            )

        return fig

    return html.Div(
        [
            html.Div(
                html.H2(
                    "Netflix Analytics: Duration, Trends, Ratings, Evolution & Calendar",
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
            html.Div(
                [
                    html.Div(
                        [
                            html.H3(
                                "Content Addition Calendar",
                                style={"margin": "0 0 10px 0"},
                            ),
                            html.Div(
                                [
                                    html.Label(
                                        "Content Type:",
                                        style={
                                            "marginRight": "10px",
                                            "fontWeight": "bold",
                                        },
                                    ),
                                    dcc.Dropdown(
                                        id="content-type-dropdown",
                                        options=[
                                            {"label": "All Content", "value": "All"},
                                            {"label": "Movies", "value": "Movie"},
                                            {"label": "TV Shows", "value": "TV Show"},
                                        ],
                                        value="All",
                                        style={"width": "150px"},
                                    ),
                                ],
                                style={
                                    "display": "flex",
                                    "alignItems": "center",
                                    "marginBottom": "10px",
                                },
                            ),
                            dcc.Graph(
                                id="content-calendar-heatmap", style={"height": "500px"}
                            ),
                        ],
                        style={
                            "width": "100%",
                            "display": "inline-block",
                        },
                    ),
                ],
                style={"marginTop": "20px"},
            ),
        ],
        style={
            "padding": "20px",
            "backgroundColor": t["card_bg"],
            "height": "100%",
            "boxSizing": "border-box",
        },
    )
