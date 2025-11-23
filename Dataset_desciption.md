# Dataset description

This dataset combines the [Netflix Movies and TV shows dataset](https://www.kaggle.com/datasets/shivamb/netflix-shows) with enriched metadata from [OMDB API](https://www.omdbapi.com/).

The combined dataset contains approx. 8800 titles (70% movies, 30% TV shows) spanning from 1903 to 2025. The OMDB enrichment adds critical insights including IMDb ratings, Metascores for quality comparison, for analysis of critic vs. user score correlations, content quality trends, and production patterns across countries and genres.

# Research Questions

## How do critic scores (Metascore) compare to user scores (IMDb Rating) across different genres?

- **Task**: Compare and correlate different rating systems
- **Approach**: Interactive scatter plots with genre filtering
- **Insights**: Identify genres where critics and audiences agree/disagree

## What are the content production trends by country and genre over time?

- **Task**: Discover temporal and geographic patterns
- **Approach**: Choropleth maps, timelines, and heatmaps
- **Insights**: Understand Netflix's content strategy evolution

## How can users find highly-rated content based on their preferences?

- **Task**: Enable content discovery and filtering
- **Approach**: Multi-criteria filtering with visual feedback
- **Insights**: Personalized content recommendations

# Tasks

## Kristian:

- Get OMDB data
- Merge, clean, and preprocess data for use
- Explore by countries
- Genre analysis

## Lasse:

- Initial layout
- Explore by time
- Ratings comparison

# Design

## Considerations

### Layout

We want to keep the research questions as individual components for better seperation of concerns, and workload management within the group.

Each component would have a control-component which will be the primary filter for the visualizations in the rest of the component e.g. dropdown selection or chloropleth that would filter based on the chosen country. The other visualizations in the component should encourage and allow for more in-depth exploration within the boundaries of the component topic.

### Colors

Color-wise we should as a starting point use the Netflix red and black for the page. However only using Netflix brand colors (red and black), is not an option for many types visualizations.

When making plots for multivariate data, use Dash/Plotly built-in color schemes for accessibility and visible clarity.

## Sketches
