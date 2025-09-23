from dash import html
from static import theme


def render():
    t = theme.THEME

    return html.Div(
        [
            html.Div(
                html.H1("Netflix in Numbers", style={"color": t["text"], "margin": "0", "fontSize": "20px"}),
                style={"display": "flex", "alignItems": "center"},
            ),
            html.Img(
                src="https://images.ctfassets.net/y2ske730sjqp/1aONibCke6niZhgPxuiilC/2c401b05a07288746ddf3bd3943fbc76/BrandAssets_Logos_01-Wordmark.jpg?w=940",
                style={"height": "48px", "width": "auto", "marginBottom": "0", "borderRadius": "6px"},
            ),
        ],
        style={
            "display": "flex",
            "alignItems": "center",
            "justifyContent": "space-between",
            "padding": "8px 18px",
            "height": "64px",
            "backgroundColor": t["header_bg"],
            "borderBottom": f"1px solid {t['grid']}",
        },
    )
