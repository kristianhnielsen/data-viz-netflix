import marimo

__generated_with = "0.16.0"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(
        r"""
    # Exploratory Data Analysis
    In this script we can do EDA and preview data transformations needed for visualization in the Dash app
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Import libraries and data""")
    return


@app.cell
def _(plt, sns):
    # Palette
    sns.palplot(['#221f1f', '#b20710', '#e50914','#f5f5f1'])

    plt.title("Netflix brand palette ",loc='left',fontfamily='serif',fontsize=15,y=1.2)
    plt.show()
    return


@app.cell
def _(sns):
    # Create a theme for the plots using the color scheme above
    sns.set_theme(
        style="whitegrid",
        rc={
            "axes.facecolor": "#f5f5f1",
            "figure.facecolor": "#f5f5f1",
            "axes.edgecolor": "#221f1f",
            "grid.color": "#e50914",
            "text.color": "#221f1f",
            "xtick.color": "#221f1f",
            "ytick.color": "#221f1f",
            "axes.titleweight": "bold",
            "axes.titlepad": 15,
            "axes.titlesize": 16,
            "axes.labelsize": 14,
            "axes.labelweight": "bold",
            "legend.fontsize": 12,
            "legend.title_fontsize": 14,
        },
    )
    return


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    import numpy as np
    import seaborn as sns
    import matplotlib.pyplot as plt
    return mo, plt, sns


@app.cell
def _():
    from data import netflix

    config = netflix.NetflixDataConfig(
        netflix_titles_path="data/netflix_titles.csv",
        omdb_path="data/omdb_data.csv",
    )
    preprocessor = netflix.NetflixDataPreprocessor()

    netflix_data = netflix.NetflixData(
        config=config, preprocessor=preprocessor
    ).data
    netflix_data.head()
    return (netflix_data,)


@app.cell
def _(mo):
    mo.md(r"""# Top (primary) countries""")
    return


@app.cell
def _(mo):
    top_x_countries = mo.ui.slider(1, 40, value=10)
    mo.md(f"How many countries to show: {top_x_countries}")
    return (top_x_countries,)


@app.cell
def _(netflix_data, plt, sns, top_x_countries):
    country_val_counts = netflix_data.value_counts("country_primary")[
        : top_x_countries.value
    ]


    # Plotting top X countries
    plt.figure(figsize=(5, 3))
    sns.barplot(x=country_val_counts.index, y=country_val_counts.values, palette="Reds_r")
    plt.title(
        f"Top {top_x_countries.value} Countries by Number of Titles on Netflix"
    )
    plt.xlabel("Country")
    plt.ylabel("Number of Titles")
    plt.xticks(rotation=65)
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# What to plot?""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Ideas for different visualization:

     - Distribution of movie ratings (e.g., G, PG, PG-13, R)
     - Number of titles added per year
     - Distribution of movie durations
     - Top genres by number of titles
     - Top directors by number of titles
     - Correlation between movie duration and release year
     - Number of titles by country
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    How to visualize the above?

    - Bar charts for categorical distributions (e.g., ratings, genres, directors, countries)
    - Line charts for trends over time (e.g., titles added per year)
    - Histograms for numerical distributions (e.g., movie durations)
    - Scatter plots for correlations (e.g., movie duration vs. release year)
    - Pie charts for proportions (e.g., genre distribution)
    - Heatmaps for correlations between multiple variables
    - Box plots for numerical distributions (e.g., movie durations by rating)
    - Map visualizations for geographical distributions (e.g., titles by country)
    """
    )
    return


if __name__ == "__main__":
    app.run()
