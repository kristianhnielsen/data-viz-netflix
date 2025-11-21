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
    for index in range(len(genre_data)):
        row = genre_data.iloc[index]
        genre_value = row['genre']
        if pd.isna(genre_value) or not isinstance(genre_value, str):
            continue
        if len(genre_value.strip()) == 0:
            continue
            
        genres = [g.strip() for g in genre_value.split(',')]
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
    
    genre_df: pd.DataFrame = pd.DataFrame(genre_rows)
    
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
            filtered_data = filtered_data.loc[filtered_data['genre'] == selected_genre]
        
        if content_type:
            filtered_data = filtered_data.loc[filtered_data['type'].isin(content_type)]
        
        # 1. Genre Treemap (if no specific genre selected)
        if not selected_genre:
            genre_counts_series = genre_df['genre'].value_counts()
            genre_counts = genre_counts_series.reset_index()
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
                title_x=0.5,
                font=dict(color=t["text_primary"])
            )
        else:
            # Show content type breakdown for selected genre
            type_counts_series = filtered_data['type'].value_counts()
            type_counts = type_counts_series.reset_index()
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
                title_x=0.5,
                font=dict(color=t["text_primary"])
            )
            treemap_fig.update_layout(
                plot_bgcolor=t["card_bg"],
                paper_bgcolor=t["card_bg"],
                title_font_size=16,
                title_x=0.5,
                font=dict(color=t["text_primary"])
            )
        
        # 2. Genre Timeline
        if len(filtered_data) > 0:
            grouped_timeline = filtered_data.groupby(['release_year', 'type'], observed=True).size()
            timeline_data = grouped_timeline.reset_index()
            timeline_data = timeline_data.rename(columns={0: 'count'})
            
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
                xaxis_tickangle=-45,
                font=dict(color=t["text_primary"]),
                xaxis=dict(gridcolor=t["grid_color"], zerolinecolor=t["grid_color"]),
                yaxis=dict(gridcolor=t["grid_color"], zerolinecolor=t["grid_color"])
            )
        else:
            timeline_fig = px.bar(
                title="No timeline data available"
            )
            timeline_fig.update_layout(
                plot_bgcolor=t["card_bg"],
                paper_bgcolor=t["card_bg"],
                title_font_size=16,
                title_x=0.5,
                font=dict(color=t["text_primary"])
            )
        
        # 3. Genre-Country Heatmap
        if len(filtered_data) > 0:
            grouped_heatmap = filtered_data.groupby(['country_primary', 'genre'], observed=True).size()
            heatmap_data = grouped_heatmap.reset_index()
            heatmap_data = heatmap_data.rename(columns={0: 'count'})
            
            # Get top countries for better visualization
            top_countries = filtered_data['country_primary'].value_counts().head(10).index.tolist()
            heatmap_data = heatmap_data.loc[heatmap_data['country_primary'].isin(top_countries)]
            
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
                xaxis_tickangle=-45,
                font=dict(color=t["text_primary"]),
                xaxis=dict(gridcolor=t["grid_color"], zerolinecolor=t["grid_color"]),
                yaxis=dict(gridcolor=t["grid_color"], zerolinecolor=t["grid_color"])
            )
        else:
            heatmap_fig = px.imshow(
                [[0]],
                title="No heatmap data available"
            )
            heatmap_fig.update_layout(
                plot_bgcolor=t["card_bg"],
                paper_bgcolor=t["card_bg"],
                title_font_size=16,
                title_x=0.5,
                font=dict(color=t["text_primary"])
            )
        
        return treemap_fig, timeline_fig, heatmap_fig
    
    return html.Div([
        html.H2(
            "🎭 Genre Explorer",
            style={
                "color": t["text_primary"],
                "marginBottom": "24px",
                "fontWeight": "300"
            }
        ),
        
        # Controls
        html.Div([
            html.Div([
                html.Label("Genre", style={"color": t["text_secondary"], "fontSize": "14px", "marginBottom": "8px", "display": "block"}),
                dcc.Dropdown(
                    id="selected-genre",
                    options=[{"label": "All Genres", "value": ""}] + 
                            [{"label": str(genre), "value": str(genre)} for genre in unique_genres],  # type: ignore
                    value="",
                    placeholder="Choose a genre...",
                    style={
                        "backgroundColor": t["surface"],
                        "color": t["text_primary"],
                        "border": f"1px solid {t['surface_border']}"
                    }
                )
            ], style={"width": "48%", "display": "inline-block", "marginRight": "4%"}),
            
            html.Div([
                html.Label("Content Type", style={"color": t["text_secondary"], "fontSize": "14px", "marginBottom": "8px", "display": "block"}),
                dcc.Dropdown(
                    id="content-type-filter",
                    options=[
                        {"label": "Movies", "value": "Movie"},
                        {"label": "TV Shows", "value": "TV Show"}
                    ],  # type: ignore
                    value=["Movie", "TV Show"],
                    multi=True,
                    placeholder="Select types...",
                    style={
                        "backgroundColor": t["surface"],
                        "color": t["text_primary"],
                        "border": f"1px solid {t['surface_border']}"
                    }
                )
            ], style={"width": "48%", "display": "inline-block"})
        ], style={
            "marginBottom": "24px", 
            "padding": "20px", 
            "backgroundColor": t["surface"],
            "borderRadius": t["border_radius"],
            "border": f"1px solid {t['surface_border']}"
        }),
        
        # Visualizations Grid
        html.Div([
            html.Div([
                dcc.Graph(id="genre-treemap", style={"height": "450px", "backgroundColor": t["surface"], "borderRadius": t["border_radius"], "border": f"1px solid {t['surface_border']}"})
            ], style={"width": "48%", "display": "inline-block", "verticalAlign": "top", "marginRight": "4%"}),
            
            html.Div([
                dcc.Graph(id="genre-timeline", style={"height": "450px", "backgroundColor": t["surface"], "borderRadius": t["border_radius"], "border": f"1px solid {t['surface_border']}"})
            ], style={"width": "48%", "display": "inline-block", "verticalAlign": "top"})
        ], style={"marginBottom": "24px"}),
        
        html.Div([
            dcc.Graph(id="genre-country-heatmap", style={"height": "500px", "backgroundColor": t["surface"], "borderRadius": t["border_radius"], "border": f"1px solid {t['surface_border']}"})
        ], style={"marginBottom": "24px"})
    ], style={"padding": "40px 24px"})
