# Netflix-Inspired Dark Theme
# Sophisticated color palette based on actual Netflix interface
# Enhanced visual hierarchy with proper elevation levels
# Optimized for data visualization clarity and user experience

THEME = {
    # Core Layout Colors
    "background": "#141414",        # Netflix's actual dark gray (softer than pure black)
    "surface": "#1f1f1f",           # Card/surface background
    "surface_elevated": "#2a2a2a",   # Hover/active states
    "surface_border": "#333333",         # Subtle borders
    
    # Brand Colors
    "primary": "#e50914",             # Netflix red for accents
    "primary_variant": "#f40612",       # Lighter red for hover states
    "header_bg": "#e50914",            # Header background
    
    # Text Colors
    "text_primary": "#ffffff",           # Main text
    "text_secondary": "#b3b3b3",         # Secondary text
    "text_muted": "#808080",            # Muted/disabled text
    "text_inverse": "#141414",           # Text on primary color
    
    # Data Visualization Colors
    "card_bg": "#1f1f1f",             # Chart backgrounds
    "plot_color": "#e50914",            # Single series plots
    "grid_color": "#404040",             # Chart grid lines
    
    # Sequential Scale (for heatmaps, choropleths)
    "cont_scale": [
        [0.0, "#2a2a2a"],              # Dark surface
        [0.2, "#404040"],              # Medium dark
        [0.4, "#666666"],              # Medium gray
        [0.6, "#b3b3b3"],              # Light gray
        [0.8, "#e50914"],              # Netflix red
        [1.0, "#ff6b6b"],              # Bright red
    ],
    
    # Categorical Colors (optimized for dark theme)
    "categorical_colors": [
        "#e50914",  # Netflix Red
        "#0071e5",  # Bright Blue
        "#00d474",  # Bright Green
        "#ffb347",  # Bright Orange
        "#b469ff",  # Purple
        "#ff6b9d",  # Pink
        "#4ecdc4",  # Teal
        "#95a5a6",  # Gray
    ],
    
    # Diverging Scale (for correlation data)
    "diverging_scale": [
        [0.0, "#0071e5"],              # Blue (negative)
        [0.5, "#666666"],              # Neutral gray
        [1.0, "#e50914"],              # Netflix red (positive)
    ],
    
    # UI Elements
    "shadow": "rgba(0, 0, 0, 0.3)",       # Subtle shadows
    "border_radius": "8px",                # Consistent border radius
    "transition": "all 0.2s ease-in-out",   # Smooth transitions
}
