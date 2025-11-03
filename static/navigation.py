from dash import html
from static import theme


def render() -> html.Div:
    t = theme.THEME
    
    return html.Div([
        html.Nav([
            html.Div([
                html.A(
                    html.Div([
                        html.H4("📊", style={"margin": "0", "fontSize": "24px"}),
                        html.P("Time Analysis", style={"margin": "0", "fontSize": "12px"})
                    ], style={"textAlign": "center"}),
                    href="#temporal-analysis",
                    style={
                        "textDecoration": "none",
                        "color": t["text_color"],
                        "padding": "15px",
                        "borderRadius": "8px",
                        "backgroundColor": t["card_bg"],
                        "transition": "all 0.3s ease",
                        "display": "block",
                        "textAlign": "center"
                    }
                )
            ], style={"width": "18%", "display": "inline-block", "margin": "1%"}),
            
            html.Div([
                html.A(
                    html.Div([
                        html.H4("🌍", style={"margin": "0", "fontSize": "24px"}),
                        html.P("Geographic", style={"margin": "0", "fontSize": "12px"})
                    ], style={"textAlign": "center"}),
                    href="#country-analysis",
                    style={
                        "textDecoration": "none",
                        "color": t["text_color"],
                        "padding": "15px",
                        "borderRadius": "8px",
                        "backgroundColor": t["card_bg"],
                        "transition": "all 0.3s ease",
                        "display": "block",
                        "textAlign": "center"
                    }
                )
            ], style={"width": "18%", "display": "inline-block", "margin": "1%"}),
            
            html.Div([
                html.A(
                    html.Div([
                        html.H4("⭐", style={"margin": "0", "fontSize": "24px"}),
                        html.P("Ratings", style={"margin": "0", "fontSize": "12px"})
                    ], style={"textAlign": "center"}),
                    href="#ratings-analysis",
                    style={
                        "textDecoration": "none",
                        "color": t["text_color"],
                        "padding": "15px",
                        "borderRadius": "8px",
                        "backgroundColor": t["card_bg"],
                        "transition": "all 0.3s ease",
                        "display": "block",
                        "textAlign": "center"
                    }
                )
            ], style={"width": "18%", "display": "inline-block", "margin": "1%"}),
            
            html.Div([
                html.A(
                    html.Div([
                        html.H4("🎭", style={"margin": "0", "fontSize": "24px"}),
                        html.P("Genres", style={"margin": "0", "fontSize": "12px"})
                    ], style={"textAlign": "center"}),
                    href="#genre-analysis",
                    style={
                        "textDecoration": "none",
                        "color": t["text_color"],
                        "padding": "15px",
                        "borderRadius": "8px",
                        "backgroundColor": t["card_bg"],
                        "transition": "all 0.3s ease",
                        "display": "block",
                        "textAlign": "center"
                    }
                )
            ], style={"width": "18%", "display": "inline-block", "margin": "1%"}),
            
            html.Div([
                html.A(
                    html.Div([
                        html.H4("📖", style={"margin": "0", "fontSize": "24px"}),
                        html.P("Guide", style={"margin": "0", "fontSize": "12px"})
                    ], style={"textAlign": "center"}),
                    href="#user-guide",
                    style={
                        "textDecoration": "none",
                        "color": t["text_color"],
                        "padding": "15px",
                        "borderRadius": "8px",
                        "backgroundColor": t["card_bg"],
                        "transition": "all 0.3s ease",
                        "display": "block",
                        "textAlign": "center"
                    }
                )
            ], style={"width": "18%", "display": "inline-block", "margin": "1%"})
        ], style={
            "display": "flex",
            "justifyContent": "space-between",
            "alignItems": "center",
            "padding": "20px",
            "backgroundColor": t["background"],
            "borderRadius": "12px",
            "margin": "20px 0"
        })
    ], style={
        "position": "sticky",
        "top": "0",
        "zIndex": "1000",
        "backgroundColor": t["background"],
        "padding": "10px 0"
    })
