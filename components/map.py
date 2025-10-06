from dash import Dash, html, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
from static import theme


def render(app: Dash, data: pd.DataFrame):
    t = theme.THEME

    # Clean and prepare country data
    def clean_country_data(data: pd.DataFrame) -> pd.DataFrame:
        # Drop NaN values and split multi-country entries
        country_series = data["country_primary"].dropna()

        # Split comma-separated countries and explode
        country_list = []
        for countries_str in country_series:
            # Split by comma and clean each country name
            countries = [country.strip() for country in str(countries_str).split(",")]
            country_list.extend(countries)

        # Create DataFrame from the expanded list
        expanded_countries = pd.DataFrame({"country": country_list})

        # Count titles by country (country mapping now handled in preprocessor)
        country_counts = expanded_countries["country"].value_counts().reset_index()
        country_counts.columns = ["country", "title_count"]

        return country_counts

    country_data = clean_country_data(data)

    # Filter out very small counts to focus on main countries and ensure better color scaling
    country_data = country_data[country_data["title_count"] >= 5]

    fig = px.choropleth(
        country_data,
        locations="country",
        locationmode="country names",
        color="title_count",
        color_continuous_scale="Viridis",
        range_color=[
            country_data["title_count"].min(),
            country_data["title_count"].max(),
        ],
        title="Netflix Content Distribution by Country",
        hover_name="country",
        hover_data={"title_count": True},
        labels={"title_count": "Number of Titles"},
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
            # titleside="right",
            tickmode="linear",
            tick0=country_data["title_count"].min(),
            dtick=(
                country_data["title_count"].max() - country_data["title_count"].min()
            )
            / 5,
        ),
    )

    return html.Div(
        [
            html.Div(
                html.H2(
                    "Netflix Content by Country",
                    style={"margin": "0"},
                ),
                style={
                    "display": "flex",
                    "justifyContent": "space-between",
                    "alignItems": "center",
                },
            ),
            dcc.Graph(figure=fig),
        ]
    )
