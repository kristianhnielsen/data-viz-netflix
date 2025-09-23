from dash import html


def render():
    return html.Div(
        [
            html.Div(
                html.H1("Netflix in Numbers", style={"color": "#D3DAD9", "margin": "0", "fontSize": "22px"}),
                style={"display": "flex", "alignItems": "center"},
            ),
            html.Img(
                src="https://images.ctfassets.net/y2ske730sjqp/1aONibCke6niZhgPxuiilC/2c401b05a07288746ddf3bd3943fbc76/BrandAssets_Logos_01-Wordmark.jpg?w=940",
                style={"height": "60px", "width": "auto", "marginBottom": "0", "borderRadius": "6px"},
            ),
        ],
        style={
            "display": "flex",
            "alignItems": "center",
            "justifyContent": "space-between",
            "padding": "10px 20px",
            "height": "80px",
            "backgroundColor": "#1F1F1F",
        },
    )
