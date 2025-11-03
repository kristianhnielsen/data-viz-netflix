this is the final project description for data visualization course:

Objective:

You will design and implement an interactive data visualization prototype based on a selected open dataset. The goal is to apply principles of interactive design, data analysis, and/or visual storytelling to a domain of their choice.

Project Theme:

Students may choose any dataset (e.g., finance, health, environment, education, etc.) and build a visualization tool that helps non-experts make informed decisions.

Requirements

1. Dataset Selection (What)

Use an open dataset from sources such as:

https://www.data.gov

https://data.europa.eu

https://www.kaggle.com/datasets

Justify the relevance and quality of the dataset.

2. Model Design (Why)

Define research questions (RQs) that guide your visualization goals.

3. Visualization Prototype (How)

Create comparative sketches of interactive views (e.g., treemap, heatmap, scatter plot, summary dashboard).

https://fds-design.github.io/

Each view should highlight a different aspect of the data (distribution, correlation, performance, risk).

Apply consistent color schemes and intuitive design elements for clarity.

4. User Interaction

Implement features such as brushing, filters, and visual queries for dynamic exploration.

Ensure accessibility and ease of use for non-expert users.

5. Documentation

Submit a short report (max 3 pages) including:

Introduction and motivation for the RQs

Design rationale

Background or related work

Data preprocessing steps

Visualization choices

Use cases

Conclusions

6. Submission Format

Upload:

GitHub repository link (code + snapshots)

Short video demo of your prototype

PDF report

Deadline: [To Be Defined]

Evaluation Criteria

Creativity and relevance of chosen domain

Clarity and effectiveness of visualizations

Interactivity and usability

Technical execution and documentation

I've reviewed the project description for your DSK808 course. This project integrates the core concepts from Professor Diehl's lectures and Camilla's exercise class.

The objective is to build an interactive dashboard, likely using Plotly and Dash as shown in your exercise class , by applying the "What, Why, How" model.

Here is a breakdown of the requirements based on your course materials:

Project Requirements

1. What? (Data Abstraction) This is your dataset selection. You need to find an open dataset and, as your lectures describe, identify its data and attribute types (e.g., table, network, quantitative, categorical). You must also justify its quality.

2. Why? (Task Abstraction) This is your model design. You must define research questions (RQs) that guide the project. This means abstracting a domain-specific problem into generic tasks , such as discovering correlations, identifying outliers, or summarizing distributions.

3. How? (Visual Encoding & Interaction) This is your prototype. You must:

Design: Choose appropriate marks (e.g., points, lines, areas) and channels (e.g., position, color, size) to encode your data. Your choices should be based on their effectiveness, as discussed in your lectures (e.g., using position for quantitative data).

Interact: Implement interactive methods like filtering or brushing to help the user perform the tasks you defined in your "Why?" step.

Color: Apply consistent and accessible color schemes , keeping principles like color blindness in mind.

4. Submission & Documentation You will submit a GitHub repository, a video demo, and a short 3-page report. This report must explain your design rationale, connecting your "What" (data) and "Why" (tasks) to your "How" (visualization choices).

The first step is selecting a dataset and defining your research questions.

Would you like me to help you brainstorm some project ideas or find a dataset for a specific domain you are interested in?

this is our data that we are working with for the final project.

Hello! I've loaded and analyzed your Netflix dataset. This is a great dataset that fits your DSK808 project perfectly.

Following the project structure from your course, here is an initial analysis based on the "What, Why, How" framework.

1. What? (Data Abstraction)
   Dataset: A table with 8,823 titles.

Attributes: A mix of:

Categorical: type (Movie/TV Show), director, country_primary, rating, genre.

Quantitative: metascore, imdb_rating, seasons.

Temporal: release_year, date_added.

Data Quality: As is common, it needs some cleaning. I've already converted runtime, imdb_votes, and date_added into usable formats for visualization.

2. Why? (Task Abstraction)
   Based on the available data, here are some sample Research Questions (RQs) you could explore:

RQ 4 (Compare): What are the top content-producing countries on Netflix?

RQ 5 (Correlation): Is there a relationship between critic scores (Metascore) and user scores (IMDb Rating)?

RQ 6 (Distribution): What does the distribution of movie runtimes look like?

3. How? (Visualization Prototypes)
   To help you get started, I've created three initial visualizations that address the RQs above. These could serve as the first "comparative sketches" for your interactive dashboard.

1. Top 10 Content-Producing Countries (Bar Chart) This chart addresses RQ 4 ("Compare"). It clearly shows the United States and India as the dominant producers of content in this dataset.

1. IMDb Rating vs. Metascore (Scatter Plot) This chart addresses RQ 5 ("Identify Correlation"). It plots user ratings against critic ratings. There appears to be a positive, though not perfect, correlation between the two. This is a great candidate for an interactive view where you could hover to see title details.

1. Distribution of Movie Runtimes (Histogram) This chart addresses RQ 6 ("Summarize Distribution"). It shows that the vast majority of movies on Netflix cluster around the 90-100 minute mark, with a long tail of shorter films.

These examples should give you a solid foundation for your project. Your next steps would be to refine your research questions and build these charts into an interactive dashboard using Plotly and Dash, adding features like filters (e.g., by release_year or genre) and brushing (e.g., selecting points on the scatter plot to see details).

give me some research questions and plots I can do for this project.

Here are three potential project ideas, each with specific research questions and plot suggestions, based on your processed_netflix_data.csv file and the DSK808 course requirements.

Project 1: The "What Should I Watch?" Dashboard
This idea directly addresses the "help non-experts make informed decisions" goal by focusing on finding and comparing content.

Why? (Task Abstraction):

RQ 1 (Search/Filter): How can a user find a highly-rated movie or show that matches their preferences for genre, runtime, and release year?

RQ 2 (Compare/Distribution): How does a specific title's rating and runtime compare to the average for its genre?

How? (Visualization & Interaction):

Plot 1: Rating vs. Popularity Scatter Plot

Type: Bubble Chart.

Encoding:

X-Axis: imdb_rating (quantitative).

Y-Axis: metascore (quantitative).

Size: imdb_votes_num (quantitative) to show popularity.

Color: type (Movie/TV Show) (categorical).

Plot 2: Genre Quality Dashboard

Type: Box Plots.

Encoding:

X-Axis: genre (categorical).

Y-Axis: imdb_rating (quantitative).

This plot summarizes the distribution for each genre, showing the median and identifying outliers.

Interaction (How):

Filters: Use dropdowns to filter by genre, type, and rating (e.g., 'PG-13', 'TV-MA'). Use a slider for release_year.

Brushing & Linking: Clicking a genre in the box plot (Plot 2) filters the scatter plot (Plot 1) to show only titles from that genre. Hovering over a bubble in Plot 1 reveals a tooltip with the title, director, and runtime.

Project 2: Netflix's Content Strategy Analyzer
This idea targets a "non-expert" like a business analyst or journalist interested in Netflix's content trends.

Why? (Task Abstraction):

RQ 1 (Trend): How has the type of content (Movie vs. TV Show) added to Netflix changed over time?

RQ 2 (Trend/Correlation): Has the average runtime of movies changed in recent years?

RQ 3 (Distribution): Where does Netflix source its content from, and how has this changed?

How? (Visualization & Interaction):

Plot 1: Content Added Over Time

Type: Stacked Bar Chart or 100% Stacked Area Chart.

Encoding:

X-Axis: year_added (temporal/ordinal).

Y-Axis: COUNT(title) (quantitative).

Color: type (Movie/TV Show) (categorical). This will show the shift from movies to TV shows.

Plot 2: Geographic Sourcing of Content

Type: Choropleth Map.

Encoding:

Geography: country_primary (categorical/spatial).

Color: COUNT(title) (quantitative). Use a sequential color scheme (e.g., light blue to dark blue).

Interaction (How):

Map as Filter: Clicking a country on the map (Plot 2) filters the bar chart (Plot 1) to show the content trend only for that country.

Slider: A range slider for year_added updates both charts to show data within that time window.

Project 3: A Deep Dive into Genres and Ratings
This idea focuses on comparing different categories and their internal properties, leveraging parallel coordinates for a multivariate view.

Why? (Task Abstraction):

RQ 1 (Compare/Correlation): What is the relationship between different rating systems (IMDb vs. Metascore) across different genres?

RQ 2 (Explore/Pattern-Finding): Are there "typical" profiles for titles within a specific genre (e.g., "Horror" vs. "Documentaries") based on their ratings, runtime, and release year?

How? (Visualization & Interaction):

Plot 1: Genre Profile Explorer

Type: Parallel Coordinates Plot.

Encoding:

Axes (quantitative): imdb_rating, metascore, runtime_min, release_year.

Lines (items): Each line is a movie or TV show.

Color: genre (categorical).

Plot 2: Rating Comparison

Type: Scatter Plot Matrix (SPLOM).

Encoding:

Grid: A grid of scatter plots comparing imdb_rating, metascore, and imdb_votes_num against each other.

Color: genre (categorical).

Interaction (How):

Brushing: The key interaction for parallel coordinates. Users can "brush" a range on one or more axes (e.g., select only imdb_rating > 8.0 and runtime_min < 100) to highlight the lines that fit those criteria.

Filtering: A dropdown to select and isolate one or more genre to make the plots less cluttered.

how to understand the final project? do I make 1 plot for 1 research question, or do I come up with fictional user journeys and make plots based on that, or?

That's a great question. You're trying to connect the "Why?" (Task Abstraction) with the "How?" (Visual Encoding).

The short answer is: It's a combination of both.

Your Research Questions (RQs) are your high-level goals. Your "user journeys" (which the project brief calls "Use Cases" ) are the stories of how a user achieves those goals using your plots and interactions.

You don't just make 1 plot for 1 RQ. You build an interactive system of plots and filters that work together to answer a family of RQs.

How to Think About It
Use the "Why" and "How" framework from your course:

Why? (The Task/RQ): This is the user's goal. It's what the non-expert wants to do.

Example RQ: "How can I find a high-quality movie that's similar to ones I already like?"

How? (The Tools/Prototype): These are your plots and interactions (filters, brushing) that help the user complete their task.

Example Tools: A scatter plot of ratings, a dropdown to filter by genre, and a hover-tool to show movie details.

The User Journey / Use Case (The Story): This is the story that connects the Why and the How. You must think about this to build a good prototype. It describes the steps a user takes to answer their RQ.

Practical Example
Let's use your Netflix data to walk through a use case.

1. The "Why?" (RQ): A user wants to find a new movie to watch. Their general question is: "What are the most popular and critically acclaimed comedy movies released since 2015?"

This single RQ combines several tasks:

Filter by type (Movie), genre (Comedy), and release_year (>2015).

Compare titles based on scores (imdb_rating, metascore).

Identify which of those are popular (imdb_votes).

Lookup the title of the movie they find.

2. The "How?" (Your Dashboard Design): You decide to make a dashboard with two main plots and several filters:

Filters:

Dropdown for genre (categorical).

Slider for release_year (quantitative).

Plot 1 (Scatter Plot):

X-Axis: imdb_rating (quantitative).

Y-Axis: metascore (quantitative).

Size: imdb_votes_num (quantitative).

Hover Tool: Shows title, director, and runtime.

Plot 2 (Bar Chart):

X-Axis: director (categorical).

Y-Axis: COUNT(title) (quantitative).

3. The User Journey / Use Case (The Story): Here is the fictional user journey you would describe in your report:

"A user arrives at the dashboard wanting to find a new comedy."

First, they use the genre filter and select "Comedy".

Next, they use the release_year slider to set the range from 2015 to 2025.

The Scatter Plot is now filtered. The user's task is to Explore. They visually scan the top-right quadrant (where both IMDb and Metascores are high). 4. They Identify a few large bubbles, indicating high popularity (lots of votes). 5. They hover over one of these bubbles, using the Lookup action to see the title: "Glass Onion".

Curious, they click on that bubble. This links to the bar chart, which updates to show other movies by that same director (Rian Johnson), allowing them to Discover new, related content.

Summary
So, to answer your question directly:

You start with RQs (the "Why"). These justify why you are building the tool.

You invent fictional user journeys (or "Use Cases") to imagine how a person would use your tool to answer those RQs.

This journey dictates what plots and interactions (the "How") you must build.

Your goal is not just a collection of plots. Your goal is a prototype that supports a user journey to answer a research question.
