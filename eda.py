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
    return mo, np, pd, plt, sns


@app.cell
def _(pd):
    netflix_data = pd.read_csv(r"data\netflix_titles.csv")
    return (netflix_data,)


@app.cell
def _(netflix_data):
    netflix_data.columns
    return


@app.cell
def _(mo):
    mo.md(r"""## Missing Values""")
    return


@app.cell
def _(netflix_data):
    netflix_data.isnull().sum()
    return


@app.cell
def _(netflix_data, np):
    # add No Data where cast and director is NA
    netflix_data['cast'] = netflix_data['cast'].replace(np.nan, 'No Data')
    netflix_data['director'] = netflix_data['director'].replace(np.nan, 'No Data')
    netflix_data.isnull().sum()
    return


@app.cell
def _(mo):
    mo.md(r"""## Handle Datetimes""")
    return


@app.cell
def _(df, netflix_data):
    netflix_data["date_added"] = netflix_data.to_datetime(df['date_added'])

    netflix_data['month_added'] = netflix_data['date_added'].dt.month
    netflix_data['month_name_added'] = netflix_data['date_added'].dt.month_name()
    netflix_data['year_added'] = netflix_data['date_added'].dt.year
    return


@app.cell
def _(mo):
    mo.md(r"""# Top countries""")
    return


@app.cell
def _(netflix_data):
    country_val_counts = netflix_data.value_counts("country")
    first_10_countries = country_val_counts[:20]
    return country_val_counts, first_10_countries


@app.cell
def _(first_10_countries, plt, sns):
    # Plotting top 10 countries
    plt.figure(figsize=(10, 6))
    sns.barplot(x=first_10_countries.index, y=first_10_countries.values)
    plt.title("Top 10 Countries by Number of Titles on Netflix")
    plt.xlabel("Country")
    plt.ylabel("Number of Titles")
    plt.xticks(rotation=65)
    plt.show()
    return


@app.cell
def _(country_val_counts):
    country_val_counts[:10]
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
