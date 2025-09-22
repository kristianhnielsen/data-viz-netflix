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
def _():
    return


@app.cell
def _(pd):
    netflix_data = pd.read_csv("data/netflix_titles.csv")
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
def _():
    # netflix_data["date_added"] = netflix_data.to_datetime(df['date_added'])

    # netflix_data['month_added'] = netflix_data['date_added'].dt.month
    # netflix_data['month_name_added'] = netflix_data['date_added'].dt.month_name()
    # netflix_data['year_added'] = netflix_data['date_added'].dt.year
    return


@app.cell
def _(mo):
    mo.md(r"""## Handle multiple countries in one value""")
    return


@app.cell
def _(netflix_data):
    netflix_data[netflix_data['country'].str.contains(',', na=False)]
    return


@app.cell
def _(mo):
    mo.md(r"""### Split the countries up into primary and secondary (where secondary is any other countries listed, if any)""")
    return


@app.cell
def _(netflix_data):
    # First, let's create a list of countries for each row by splitting the string
    country_lists = netflix_data['country'].str.split(', ', expand=False)

    # Create the 'country_primary' column by taking the first item from each list
    netflix_data['country_primary'] = country_lists.str[0]

    # Create the 'country_secondary' column by taking all other items and joining them
    netflix_data['country_secondary'] = country_lists.str[1:].str.join(', ')
    return


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
    country_val_counts = netflix_data.value_counts("country_primary")[:top_x_countries.value]


    # Plotting top X countries
    plt.figure(figsize=(5, 3))
    sns.barplot(x=country_val_counts.index, y=country_val_counts.values)
    plt.title(f"Top {top_x_countries.value} Countries by Number of Titles on Netflix")
    plt.xlabel("Country")
    plt.ylabel("Number of Titles")
    plt.xticks(rotation=65)
    plt.show()
    return


@app.cell
def _():
    from data import netflix

    config = netflix.NetflixDataConfig(
            netflix_titles_path="data/netflix_titles.csv", omdb_path="data/omdb_data.csv"
        )
    preprocessor = netflix.NetflixDataPreprocessor()

    netflixData = netflix.NetflixData(config=config, preprocessor=preprocessor)
    data = netflixData.data
    data.head()

    return


if __name__ == "__main__":
    app.run()
