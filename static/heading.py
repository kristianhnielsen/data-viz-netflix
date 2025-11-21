from dash import html
from static import theme


def render():
    t = theme.THEME

    return html.Div(
        [
            html.Img(
                src="https://images.ctfassets.net/y2ske730sjqp/1aONibCke6niZhgPxuiilC/2c401b05a07288746ddf3bd3943fbc76/BrandAssets_Logos_01-Wordmark.jpg?w=940",
                style={
                    "height": "32px",
                    "width": "auto",
                    "opacity": "0.9",
                },
            ),
        ],
        style={
            "display": "flex",
            "alignItems": "center",
            "justifyContent": "center",
            "padding": "16px 24px",
            "height": "64px",
            "backgroundColor": t["header_bg"],
            "boxShadow": f"0 2px 8px {t['shadow']}",
        },
    )
