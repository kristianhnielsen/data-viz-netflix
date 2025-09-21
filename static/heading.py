from dash import html


def render():
    return html.Div(
        [
            html.H1("Netflix in Numbers", style={"color": "#D3DAD9"}),
            html.Hr(),
            html.Img(
                src="https://images.ctfassets.net/y2ske730sjqp/1aONibCke6niZhgPxuiilC/2c401b05a07288746ddf3bd3943fbc76/BrandAssets_Logos_01-Wordmark.jpg?w=940",
                style={
                    "height": "300px",
                    "width": "400px",
                    "margin-bottom": "20px",
                    "border-radius": "10px",
                },
            ),
        ]
    )
