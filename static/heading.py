from dash import html
from static import theme


def render():
    t = theme.THEME

    return html.Div(
        [
            html.Img(
                src="../assets/favicon.png",
                style={
                    "height": "150px",
                    "width": "auto",
                },
            ),
        ],
        style={
            "display": "flex",
            "alignItems": "center",
            "justifyContent": "start",
            "padding": "16px 24px",
            "height": "64px",
            "backgroundColor": t["header_bg"],
            "boxShadow": f"0 2px 8px {t['shadow']}",
        },
    )
