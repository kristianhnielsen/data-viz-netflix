from dash import html
from static import theme


def render() -> html.Div:
    t = theme.THEME
    
    return html.Div([
        html.Nav([
            html.A(
                html.Div([
                    html.H4("📊", style={"margin": "0", "fontSize": "20px", "color": t["text_primary"]}),
                ], style={"textAlign": "center"}),
                href="#temporal-analysis",
                style={
                    "textDecoration": "none",
                    "color": t["text_primary"],
                    "padding": "12px 16px",
                    "borderRadius": t["border_radius"],
                    "backgroundColor": t["surface"],
                    "transition": t["transition"],
                    "display": "block",
                    "textAlign": "center",
                    "border": f"1px solid {t['surface_border']}",
                    "width": "60px",
                    "height": "60px",
                    "lineHeight": "60px",
                }
            ),
            
            html.A(
                html.Div([
                    html.H4("🌍", style={"margin": "0", "fontSize": "20px", "color": t["text_primary"]}),
                ], style={"textAlign": "center"}),
                href="#country-analysis",
                style={
                    "textDecoration": "none",
                    "color": t["text_primary"],
                    "padding": "12px 16px",
                    "borderRadius": t["border_radius"],
                    "backgroundColor": t["surface"],
                    "transition": t["transition"],
                    "display": "block",
                    "textAlign": "center",
                    "border": f"1px solid {t['surface_border']}",
                    "width": "60px",
                    "height": "60px",
                    "lineHeight": "60px",
                    "marginLeft": "8px",
                }
            ),
            
            html.A(
                html.Div([
                    html.H4("⭐", style={"margin": "0", "fontSize": "20px", "color": t["text_primary"]}),
                ], style={"textAlign": "center"}),
                href="#ratings-analysis",
                style={
                    "textDecoration": "none",
                    "color": t["text_primary"],
                    "padding": "12px 16px",
                    "borderRadius": t["border_radius"],
                    "backgroundColor": t["surface"],
                    "transition": t["transition"],
                    "display": "block",
                    "textAlign": "center",
                    "border": f"1px solid {t['surface_border']}",
                    "width": "60px",
                    "height": "60px",
                    "lineHeight": "60px",
                    "marginLeft": "8px",
                }
            ),
            
            html.A(
                html.Div([
                    html.H4("🎭", style={"margin": "0", "fontSize": "20px", "color": t["text_primary"]}),
                ], style={"textAlign": "center"}),
                href="#genre-analysis",
                style={
                    "textDecoration": "none",
                    "color": t["text_primary"],
                    "padding": "12px 16px",
                    "borderRadius": t["border_radius"],
                    "backgroundColor": t["surface"],
                    "transition": t["transition"],
                    "display": "block",
                    "textAlign": "center",
                    "border": f"1px solid {t['surface_border']}",
                    "width": "60px",
                    "height": "60px",
                    "lineHeight": "60px",
                    "marginLeft": "8px",
                }
            ),
            
            html.A(
                html.Div([
                    html.H4("📖", style={"margin": "0", "fontSize": "20px", "color": t["text_primary"]}),
                ], style={"textAlign": "center"}),
                href="#user-guide",
                style={
                    "textDecoration": "none",
                    "color": t["text_primary"],
                    "padding": "12px 16px",
                    "borderRadius": t["border_radius"],
                    "backgroundColor": t["surface"],
                    "transition": t["transition"],
                    "display": "block",
                    "textAlign": "center",
                    "border": f"1px solid {t['surface_border']}",
                    "width": "60px",
                    "height": "60px",
                    "lineHeight": "60px",
                    "marginLeft": "8px",
                }
            ),
        ], style={
            "display": "flex",
            "justifyContent": "center",
            "alignItems": "center",
            "backgroundColor": t["background"],
            "padding": "16px 0",
        })
    ], style={
        "position": "sticky",
        "top": "0",
        "zIndex": "1000",
        "backgroundColor": t["background"],
        "backdropFilter": "blur(10px)",
        "borderBottom": f"1px solid {t['surface_border']}",
    })
