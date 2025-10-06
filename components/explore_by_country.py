from dash import Dash, html, dcc, Output, Input, callback
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


def render(app: Dash, data: pd.DataFrame) -> html.Div:

    # Filter out very small counts to focus on main countries and ensure better color scaling
    country_data = data["country_primary"].value_counts().reset_index(name="count")

    fig = px.choropleth(
        country_data,
        locations="country_primary",
        locationmode="country names",
        color="count",
        color_continuous_scale="Viridis",
        labels={"count": "Number of Titles"},
    )

    # Update layout for better appearance
    fig.update_layout(
        title_font_size=16,
        title_x=0.5,
        geo=dict(
            showframe=False, showcoastlines=True, projection_type="equirectangular"
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
        Input("country-map", "clickData"),
    )
    def update_histogram(click_data: dict | None) -> go.Figure:
        # Default to United States if no country is clicked
        selected_country = "United States"

        if click_data and "points" in click_data:
            selected_country = click_data["points"][0]["location"]

        # Filter data for selected country
        country_df = data[
            (data["country_primary"] == selected_country) & (data["release_year"] > 0)
        ]

        # Create histogram of release years
        fig = px.histogram(
            country_df,
            x="release_year",
            nbins=30,
            title=f"Release Year Distribution - {selected_country}",
            labels={"release_year": "Release Year", "count": "Number of Titles"},
            color_discrete_sequence=["#636EFA"],
        )

        fig.update_layout(
            title_font_size=16,
            title_x=0.5,
            xaxis_title="Release Year",
            yaxis_title="Number of Titles",
            showlegend=False,
        )

        return fig

    return html.Div(
        [
            html.H2(
                "Netflix Content by Country",
            ),
            dcc.Graph(id="country-map", figure=fig),
            html.H2(
                "Content Release Timeline",
                style={"marginTop": "40px"},
            ),
            dcc.Graph(id="country-histogram"),
        ]
    )
