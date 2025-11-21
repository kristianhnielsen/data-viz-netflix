from dash import html
from static import theme


def render() -> html.Div:
    t = theme.THEME
    
    return html.Div([
        html.Div([
            html.H2("📊 Netflix Data Explorer", 
                   style={"color": t["text_primary"], "marginBottom": "16px", "fontWeight": "300"}),
            
            html.Div([
                html.Div([
                    html.H4("🎬", style={"margin": "0", "fontSize": "24px", "color": t["primary"]}),
                    html.P("Ratings", style={"margin": "4px 0 0 0", "fontSize": "14px", "color": t["text_secondary"]})
                ], style={"textAlign": "center", "padding": "20px", "backgroundColor": t["surface"], "borderRadius": t["border_radius"], "marginBottom": "12px"}),
                
                html.Div([
                    html.H4("🌍", style={"margin": "0", "fontSize": "24px", "color": t["primary"]}),
                    html.P("Geography", style={"margin": "4px 0 0 0", "fontSize": "14px", "color": t["text_secondary"]})
                ], style={"textAlign": "center", "padding": "20px", "backgroundColor": t["surface"], "borderRadius": t["border_radius"], "marginBottom": "12px"}),
                
                html.Div([
                    html.H4("📈", style={"margin": "0", "fontSize": "24px", "color": t["primary"]}),
                    html.P("Trends", style={"margin": "4px 0 0 0", "fontSize": "14px", "color": t["text_secondary"]})
                ], style={"textAlign": "center", "padding": "20px", "backgroundColor": t["surface"], "borderRadius": t["border_radius"], "marginBottom": "12px"}),
                
                html.Div([
                    html.H4("🎭", style={"margin": "0", "fontSize": "24px", "color": t["primary"]}),
                    html.P("Genres", style={"margin": "4px 0 0 0", "fontSize": "14px", "color": t["text_secondary"]})
                ], style={"textAlign": "center", "padding": "20px", "backgroundColor": t["surface"], "borderRadius": t["border_radius"]})
            ], style={"display": "grid", "gridTemplateColumns": "1fr 1fr", "gap": "12px", "marginBottom": "24px"}),
            
            html.Div([
                html.H3("💡 Quick Tips", style={"color": t["text_primary"], "marginBottom": "12px", "fontWeight": "300"}),
                html.Ul([
                    html.Li("Click any country on the map to explore its content", style={"marginBottom": "8px", "color": t["text_secondary"]}),
                    html.Li("Use filters to focus on specific genres or time periods", style={"marginBottom": "8px", "color": t["text_secondary"]}),
                    html.Li("Hover over charts for detailed information", style={"marginBottom": "8px", "color": t["text_secondary"]}),
                    html.Li("Compare IMDb scores vs critic ratings to find hidden gems", style={"color": t["text_secondary"]})
                ], style={"paddingLeft": "20px", "margin": "0"})
            ], style={"padding": "24px", "backgroundColor": t["surface"], "borderRadius": t["border_radius"]})
        ], style={"padding": "40px 24px", "backgroundColor": t["background"]})
    ])
