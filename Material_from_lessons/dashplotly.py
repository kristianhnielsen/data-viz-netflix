import dash
from dash import dcc, html, Input, Output, State, ctx
import plotly.express as px
import pandas as pd


df = px.data.gapminder()
df = df[df["year"] >= 1952]
pd.set_option("display.max_columns", None)
print(df.head())


# Colors for each continent
continent_colors = {
    "Asia": "#1f77b4",
    "Europe": "#ff7f0e",
    "Africa": "#2ca02c",
    "Americas": "#d62728",
    "Oceania": "#9467bd",
}

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.H1("Gapminder – GDP vs Life Expectancy"),
        dcc.Graph(id="scatter-plot", config={"displayModeBar": False}),
        html.Div(
            id="bar-chart-container",
            children=dcc.Graph(id="bar-chart", config={"displayModeBar": False}),
        ),
        dcc.Slider(
            id="year-slider",
            min=df["year"].min(),
            max=df["year"].max(),
            step=None,
            value=df["year"].min(),
            marks={str(year): str(year) for year in df["year"].unique()},
        ),
        html.Button("Reset", id="reset-button", n_clicks=0),
        html.Div(id="stored-continent", style={"display": "none"}),  # hidden div
    ]
)


@app.callback(
    [
        Output("scatter-plot", "figure"),
        Output("bar-chart", "figure"),
        Output("stored-continent", "children"),
    ],
    [
        Input("year-slider", "value"),
        Input("bar-chart", "clickData"),
        Input("reset-button", "n_clicks"),
        Input("scatter-plot", "clickData"),
    ],
    [State("stored-continent", "children")],
)
def update_figures(
    selected_year, bar_click, reset_clicks, scatter_click, stored_continent
):
    dff = df[df["year"] == selected_year]
    trigger = ctx.triggered_id

    # --- RESET ---
    if trigger == "reset-button":
        stored_continent = None
        print(stored_continent)
        bar_click = None
        country_line_value = None
        clickData = None
        bar_click = None

    # --- BAR CLICK ---
    elif trigger == "bar-chart" and bar_click:
        clicked = bar_click["points"][0]["x"]
        stored_continent = clicked
        country_line_value = None

    # --- SCATTER CLICK ---
    elif trigger == "scatter-plot" and scatter_click:
        country = scatter_click["points"][0]["hovertext"]
        country_line_value = dff[dff["country"] == country]["lifeExp"].iloc[0]
    else:
        country_line_value = None

    # --- SCATTER FIGURE ---
    if stored_continent:
        scatter_dff = dff[dff["continent"] == stored_continent]
        scatter_title = stored_continent + " – " + str(selected_year)
    else:
        scatter_dff = dff
        scatter_title = (
            "Year: " + str(selected_year) + " – GDP per capita vs Life Expectancy"
        )

    scatter_fig = px.scatter(
        scatter_dff,
        x="gdpPercap",
        y="lifeExp",
        size="pop",
        color="continent",
        color_discrete_map=continent_colors,
        hover_name="country",
        log_x=True,
        size_max=60,
        title=scatter_title,
    )

    # --- BAR FIGURE ---
    bar_data = (
        dff.groupby("continent", as_index=False)
        .agg({"lifeExp": "mean", "gdpPercap": "mean"})
        .sort_values("gdpPercap", ascending=True)
    )
    bar_fig = px.bar(
        bar_data,
        x="continent",
        y="lifeExp",
        color="continent",
        color_discrete_map=continent_colors,
        title="Average life expectancy per continent – " + str(selected_year),
        labels={"continent": "Continent (sorted by avg GDP)"},
    )
    bar_fig.update_yaxes(range=[0, 85])
    bar_fig.update_layout(xaxis=dict(fixedrange=True), yaxis=dict(fixedrange=True))

    #  add line to bar-ch if sc.plot clicked
    if trigger == "scatter-plot" and scatter_click:
        continent_of_country = dff[dff["country"] == country]["continent"].iloc[
            0
        ]  # NY: farve følger kontinent
        bar_fig.add_hline(
            y=country_line_value,
            line_dash="dash",
            line_color=continent_colors[continent_of_country],  # ÆNDRET
            annotation_text=country + ": " + str(round(country_line_value, 1)),
            annotation_position="top left",
        )

    return scatter_fig, bar_fig, stored_continent


print(
    "run on 127.0.0.1:8003 - copy-past to your browser",
)

# run on local host: 127.0.0.1:8003 in your browser

if __name__ == "__main__":
    app.run(debug=True, port=8003)
