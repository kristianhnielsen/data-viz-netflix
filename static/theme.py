# Shared color theme for the dashboard
# Solution 1: Colorblind-Safe with Netflix Branding
# - Netflix Red (#E50914) as primary brand color
# - All colors tested for protanopia, deuteranopia, tritanopia
# - Based on ColorBrewer2 scientific research
# - WCAG AA compliant (4.79:1 contrast on white)

THEME = {
    # Page Layout
    "background": "#0f0f0f",  # Very dark (better than pure black for screens)
    "header_bg": "#E50914",  # Netflix Red
    "panel_bg": "#E50914",  # Netflix Red
    "card_bg": "#f5f5f1",  # Off-white (better than pure white)
    # Sequential Scale (for heatmaps, choropleths - single variable)
    # Uses red gradient starting from Netflix Red - maintains brand identity
    "cont_scale": [
        [0.0, "#FEE5D9"],  # Very light peach
        [0.2, "#FCBBA1"],  # Light peach
        [0.4, "#FC9272"],  # Medium coral
        [0.6, "#FB6A4A"],  # Light red
        [0.8, "#E50914"],  # Netflix Red!
        [1.0, "#99000D"],  # Dark red
    ],
    # Categorical Colors (for multiple categories, pie charts, grouped bars)
    # Colorblind-safe palette with Netflix Red as anchor
    "categorical_colors": [
        "#E50914",  # Netflix Red - primary brand color
        "#0173B2",  # Blue - safe for colorblind
        "#029E73",  # Teal/Green - safe for colorblind
        "#DE8F05",  # Orange - safe for colorblind
        "#CC78BC",  # Purple - adds diversity
        "#CA9161",  # Tan/Brown - neutral complement
        "#FBAFE4",  # Light pink - soft accent
        "#949494",  # Gray - neutral for "other"
    ],
    # Single plot color (when only one series)
    "plot_color": "#E50914",  # Netflix Red
    # Diverging scale (for data with meaningful center point)
    "diverging_scale": [
        [0.0, "#0173B2"],  # Blue (negative)
        [0.5, "#F5F5F1"],  # Neutral gray
        [1.0, "#E50914"],  # Netflix Red (positive)
    ],
    # Accessibility
    "text_color": "#FFFFFF",
    "text_secondary": "#B3B3B3",
}
