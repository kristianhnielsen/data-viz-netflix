from dash import html
from static import theme


def render() -> html.Div:
    t = theme.THEME
    
    return html.Div([
        html.H2(
            "📖 User Guide: How to Explore Netflix Data",
            style={"color": t["header_bg"], "marginTop": "40px"}
        ),
        
        # Research Questions Section
        html.Div([
            html.H3("🎯 Research Questions This Dashboard Answers", style={"color": t["header_bg"]}),
            html.Div([
                html.Div([
                    html.H4("RQ1: Compare", style={"color": t["plot_color"]}),
                    html.P("How do critic scores (Metascore) compare to user scores (IMDb Rating) across different genres?"),
                    html.Ul([
                        html.Li("Use the Ratings Analysis section to explore correlations"),
                        html.Li("Filter by genre to see which categories critics vs audiences prefer"),
                        html.Li("Look for outliers where critics and audiences disagree")
                    ])
                ], style={"marginBottom": "20px"}),
                
                html.Div([
                    html.H4("RQ2: Explore", style={"color": t["plot_color"]}),
                    html.P("What are the content production trends by country and genre over time?"),
                    html.Ul([
                        html.Li("Geographic Analysis shows content distribution by country"),
                        html.Li("Genre Analysis reveals trends in content categories"),
                        html.Li("Time Analysis displays release patterns over years")
                    ])
                ], style={"marginBottom": "20px"}),
                
                html.Div([
                    html.H4("RQ3: Discover", style={"color": t["plot_color"]}),
                    html.P("How can users find highly-rated content based on their preferences?"),
                    html.Ul([
                        html.Li("Use filters to narrow down by genre, type, and ratings"),
                        html.Li("Interactive scatter plots help identify quality content"),
                        html.Li("Country analysis helps discover international content")
                    ])
                ])
            ])
        ], style={"marginBottom": "30px", "padding": "20px", "backgroundColor": t["card_bg"]}),
        
        # How to Use Section
        html.Div([
            html.H3("🚀 How to Use This Dashboard", style={"color": t["header_bg"]}),
            html.Div([
                html.H4("Interactive Features:", style={"color": t["plot_color"]}),
                html.Ul([
                    html.Li("🖱️ Click on countries in the map to see detailed analysis"),
                    html.Li("📊 Use dropdowns and sliders to filter data"),
                    html.Li("🎯 Hover over charts to see detailed information"),
                    html.Li("📱 All charts are responsive and work on different screen sizes")
                ]),
                
                html.H4("Navigation:", style={"color": t["plot_color"], "marginTop": "20px"}),
                html.Ul([
                    html.Li("Use the navigation menu to jump between sections"),
                    html.Li("Each section focuses on a different aspect of the data"),
                    html.Li("Charts are linked and update based on your selections")
                ]),
                
                html.H4("Tips for Exploration:", style={"color": t["plot_color"], "marginTop": "20px"}),
                html.Ul([
                    html.Li("Start broad with country and genre overviews"),
                    html.Li("Then drill down using filters to find specific insights"),
                    html.Li("Compare different time periods to see trends"),
                    html.Li("Look for correlations between ratings and popularity")
                ])
            ])
        ], style={"marginBottom": "30px", "padding": "20px", "backgroundColor": t["card_bg"]}),
        
        # Data Understanding Section
        html.Div([
            html.H3("📊 Understanding the Data", style={"color": t["header_bg"]}),
            html.Div([
                html.H4("Data Sources:", style={"color": t["plot_color"]}),
                html.Ul([
                    html.Li("Netflix catalog data with 8,000+ titles"),
                    html.Li("IMDb ratings and user votes"),
                    html.Li("Metacritic critic scores"),
                    html.Li("Geographic and temporal information")
                ]),
                
                html.H4("What You Can Discover:", style={"color": t["plot_color"], "marginTop": "20px"}),
                html.Ul([
                    html.Li("🌍 Which countries produce the most content"),
                    html.Li("⭐ How critics and audiences rate differently"),
                    html.Li("📈 Content trends over time"),
                    html.Li("🎭 Popular genres and their characteristics"),
                    html.Li("🎬 Quality vs popularity relationships")
                ])
            ])
        ], style={"padding": "20px", "backgroundColor": t["card_bg"]})
    ])
