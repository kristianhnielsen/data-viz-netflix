from dash import html
from static import theme


def render() -> html.Div:
    t = theme.THEME

    return html.Div(
        [
            html.Nav(
                [
                    html.A(
                        html.Div(
                            [
                                html.H4(
                                    "📊",
                                    style={
                                        "margin": "0",
                                        "fontSize": "20px",
                                        "color": t["text_primary"],
                                    },
                                ),
                                html.Span(
                                    "Time",
                                    style={
                                        "fontSize": "10px",
                                        "color": t["text_secondary"],
                                        "marginTop": "4px",
                                    },
                                ),
                            ],
                            style={
                                "textAlign": "center",
                                "display": "flex",
                                "flexDirection": "column",
                                "justifyContent": "center",
                                "alignItems": "center",
                                "height": "100%",
                            },
                        ),
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
                            "width": "80px",
                            "height": "80px",
                        },
                    ),
                    html.A(
                        html.Div(
                            [
                                html.H4(
                                    "🌍",
                                    style={
                                        "margin": "0",
                                        "fontSize": "20px",
                                        "color": t["text_primary"],
                                    },
                                ),
                                html.Span(
                                    "Country",
                                    style={
                                        "fontSize": "10px",
                                        "color": t["text_secondary"],
                                        "marginTop": "4px",
                                    },
                                ),
                            ],
                            style={
                                "textAlign": "center",
                                "display": "flex",
                                "flexDirection": "column",
                                "justifyContent": "center",
                                "alignItems": "center",
                                "height": "100%",
                            },
                        ),
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
                            "width": "80px",
                            "height": "80px",
                            "marginLeft": "8px",
                        },
                    ),
                    html.A(
                        html.Div(
                            [
                                html.H4(
                                    "⭐",
                                    style={
                                        "margin": "0",
                                        "fontSize": "20px",
                                        "color": t["text_primary"],
                                    },
                                ),
                                html.Span(
                                    "Ratings",
                                    style={
                                        "fontSize": "10px",
                                        "color": t["text_secondary"],
                                        "marginTop": "4px",
                                    },
                                ),
                            ],
                            style={
                                "textAlign": "center",
                                "display": "flex",
                                "flexDirection": "column",
                                "justifyContent": "center",
                                "alignItems": "center",
                                "height": "100%",
                            },
                        ),
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
                            "width": "80px",
                            "height": "80px",
                            "marginLeft": "8px",
                        },
                    ),
                    html.A(
                        html.Div(
                            [
                                html.H4(
                                    "🎭",
                                    style={
                                        "margin": "0",
                                        "fontSize": "20px",
                                        "color": t["text_primary"],
                                    },
                                ),
                                html.Span(
                                    "Genre",
                                    style={
                                        "fontSize": "10px",
                                        "color": t["text_secondary"],
                                        "marginTop": "4px",
                                    },
                                ),
                            ],
                            style={
                                "textAlign": "center",
                                "display": "flex",
                                "flexDirection": "column",
                                "justifyContent": "center",
                                "alignItems": "center",
                                "height": "100%",
                            },
                        ),
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
                            "width": "80px",
                            "height": "80px",
                            "marginLeft": "8px",
                        },
                    ),
                ],
                style={
                    "display": "flex",
                    "justifyContent": "center",
                    "alignItems": "center",
                    "backgroundColor": t["background"],
                    "padding": "16px 0",
                },
            )
        ],
        style={
            "position": "sticky",
            "top": "0",
            "zIndex": "1000",
            "backgroundColor": t["background"],
            "backdropFilter": "blur(10px)",
            "borderBottom": f"1px solid {t['surface_border']}",
        },
    )
