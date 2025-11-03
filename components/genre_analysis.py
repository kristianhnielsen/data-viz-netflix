from dash import Dash, html, dcc, Output, Input, callback
import pandas as pd
import plotly.express as px
from static import theme


def render(app: Dash, data: pd.DataFrame) -> html.Div:
    t = theme.THEME
    
    # Prepare genre data
    genre_data = data.copy()
    
    # Split genres and create a row for each genre
    genre_rows = []
    for _, row in genre_data.iterrows():
        if pd.notna(row['genre']) and isinstance(row['genre'], str):
            genres = [g.strip() for g in row['genre'].split(',')]
            for genre in genres:
                genre_rows.append({
                    'title': row['title'],
                    'type': row['type'],
                    'release_year': row['release_year'],
                    'rating': row['rating'],
                    'country_primary': row['country_primary'],
                    'imdb_rating': row.get('imdb_rating'),
                    'metascore': row.get('metascore'),
                    'genre': genre
                })
    
    genre_df = pd.DataFrame(genre_rows)
    
    # Get unique genres for dropdown
    unique_genres = sorted(genre_df['genre'].unique())
    
    @callback(
        Output("genre-treemap", "figure"),
        Output("genre-timeline", "figure"),
        Output("genre-country-heatmap", "figure"),
        Input("selected-genre", "value"),
        Input("content-type-filter", "value")
    )
    def update_genre_charts(selected_genre, content_type):
        # Filter data
        filtered_data = genre_df.copy()
        
        if selected_genre:
            filtered_data = filtered_data[filtered_data['genre'] == selected_genre]
        
        if content_type:
            filtered_data = filtered_data[filtered_data['type'].isin(content_type)]
        
        # 1. Genre Treemap (if no specific genre selected)
        if not selected_genre:
            genre_counts = genre_df['genre'].value_counts().reset_index()
            genre_counts.columns = ['genre', 'count']
            
            treemap_fig = px.treemap(
                genre_counts,
                path=['genre'],
                values='count',
                title="Content Distribution by Genre",
                color='count',
                color_continuous_scale=t["cont_scale"]
            )
            treemap_fig.update_layout(
                plot_bgcolor=t["card_bg"],
                paper_bgcolor=t["card_bg"],
                title_font_size=16,
                title_x=0.5
            )
        else:
            # Show content type breakdown for selected genre
            type_counts = filtered_data['type'].value_counts().reset_index()
            type_counts.columns = ['type', 'count']
            
            treemap_fig = px.pie(
                type_counts,
                values='count',
                names='type',
                title=f"Content Type Distribution for {selected_genre}",
                color_discrete_sequence=t["categorical_colors"]
            )
            treemap_fig.update_layout(
                plot_bgcolor=t["card_bg"],
                paper_bgcolor=t["card_bg"],
                title_font_size=16,
                title_x=0.5
            )
        
        # 2. Genre Timeline
        if len(filtered_data) > 0:
            timeline_data = filtered_data.groupby(['release_year', 'type']).size().reset_index(name='count')
            
            timeline_fig = px.bar(
                timeline_data,
                x='release_year',
                y='count',
                color='type',
                title=f"Content Release Timeline - {selected_genre or 'All Genres'}",
                labels={'release_year': 'Release Year', 'count': 'Number of Titles'},
                color_discrete_sequence=t["categorical_colors"]
            )
            timeline_fig.update_layout(
                plot_bgcolor=t["card_bg"],
                paper_bgcolor=t["card_bg"],
                title_font_size=16,
                title_x=0.5,
                xaxis_tickangle=-45
            )
        else:
            timeline_fig = px.bar(
                title="No timeline data available"
            )
            timeline_fig.update_layout(
                plot_bgcolor=t["card_bg"],
                paper_bgcolor=t["card_bg"]
            )
        
        # 3. Genre-Country Heatmap
        if len(filtered_data) > 0:
            heatmap_data = filtered_data.groupby(['country_primary', 'genre']).size().reset_index(name='count')
            
            # Get top countries for better visualization
            top_countries = filtered_data['country_primary'].value_counts().head(10).index
            heatmap_data = heatmap_data[heatmap_data['country_primary'].isin(top_countries)]
            
            heatmap_pivot = heatmap_data.pivot(
                index='country_primary', 
                columns='genre', 
                values='count'
            ).fillna(0)
            
            heatmap_fig = px.imshow(
                heatmap_pivot,
                title=f"Genre Production by Country - {selected_genre or 'All Genres'}",
                labels=dict(x="Genre", y="Country", color="Number of Titles"),
                color_continuous_scale=t["cont_scale"],
                aspect="auto"
            )
            heatmap_fig.update_layout(
                plot_bgcolor=t["card_bg"],
                paper_bgcolor=t["card_bg"],
                title_font_size=16,
                title_x=0.5,
                xaxis_tickangle=-45
            )
        else:
            heatmap_fig = px.imshow(
                [[0]],
                title="No heatmap data available"
            )
            heatmap_fig.update_layout(
                plot_bgcolor=t["card_bg"],
                paper_bgcolor=t["card_bg"]
            )
        
        return treemap_fig, timeline_fig, heatmap_fig
    
    return html.Div([
        html.H2(
            "Genre Analysis: Content Categories & Trends",
            style={"color": t["header_bg"], "marginTop": "40px"}
        ),
        
        # Controls
        html.Div([
            html.Div([
                html.Label("Select Genre:", style={"fontWeight": "bold"}),
                dcc.Dropdown(
                    id="selected-genre",
                    options=[{"label": "All Genres", "value": ""}] + 
                            [{"label": genre, "value": genre} for genre in unique_genres],
                    value="",
                    placeholder="Choose a genre or view all..."
                )
            ], style={"width": "40%", "display": "inline-block", "marginRight": "5%"}),
            
            html.Div([
                html.Label("Content Type:", style={"fontWeight": "bold"}),
                dcc.Dropdown(
                    id="content-type-filter",
                    options=[
                        {"label": "Movies", "value": "Movie"},
                        {"label": "TV Shows", "value": "TV Show"}
                    ],
                    value=["Movie", "TV Show"],
                    multi=True,
                    placeholder="Select content types..."
                )
            ], style={"width": "30%", "display": "inline-block"})
        ], style={"marginBottom": "30px", "padding": "20px", "backgroundColor": t["card_bg"]}),
        
        # Visualizations
        html.Div([
            html.Div([
                dcc.Graph(id="genre-treemap", style={"height": "500px"})
            ], style={"width": "50%", "display": "inline-block", "verticalAlign": "top"}),
            
            html.Div([
                dcc.Graph(id="genre-timeline", style={"height": "500px"})
            ], style={"width": "48%", "display": "inline-block", "verticalAlign": "top", "marginLeft": "2%"})
        ], style={"marginBottom": "30px"}),
        
        html.Div([
            dcc.Graph(id="genre-country-heatmap", style={"height": "600px"})
        ]),
        
        # Genre Insights
        html.Div([
            html.H3("Genre Insights:", style={"color": t["header_bg"]}),
            html.Div(id="genre-insights", children=[
                html.P("Select a genre to see specific insights and trends...")
            ])
        ], style={"marginTop": "30px", "padding": "20px", "backgroundColor": t["card_bg"]})
    ])
