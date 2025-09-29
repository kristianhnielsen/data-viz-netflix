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
    sns.barplot(x=country_val_counts.index, y=country_val_counts.values)
    plt.title(
        f"Top {top_x_countries.value} Countries by Number of Titles on Netflix"
    )
    plt.xlabel("Country")
    plt.ylabel("Number of Titles")
    plt.xticks(rotation=65)
    plt.show()
    return


if __name__ == "__main__":
    app.run()
