# Agent Guidelines for data-viz-netflix

## Build/Test Commands

- **Package Manager**: `uv` (not pip/npm)
- **Run App**: `uv run python main.py`
- **Install Dependencies**: `uv add <package>`
- **No formal test suite** - manually test via running the app
- **Do not perform any git actions** - no commits, branches, or PRs

## Code Style & Conventions

- **Python 3.13+** required
- **Type hints**: Use modern syntax (`str | None`, `Path | str`)
- **Imports**: Dash components first, then pandas/plotly, then local modules
- **Functions**: Use `def render(app: Dash, data: pd.DataFrame)` pattern for components
- **Classes**: Use dataclasses for config, ABC for interfaces
- **Variables**: snake_case for all variables and functions
- **Constants**: UPPER_CASE for theme dictionaries

## Project Structure

- `main.py` - Entry point with Dash app setup
- `components/` - Reusable UI components
  - `explore_by_country.py` - Geographic visualizations
  - `explore_by_time.py` - Temporal visualizations
- `static/` - Shared utilities
  - `theme.py` - Theme configs
  - `heading.py` - Shared heading component
- `data/` - Data processing classes and CSV files
- Use relative imports from project root

## Theme System (IMPORTANT)

- **Active Theme**: In `static/theme.py`
- **Netflix Red**: `#E50914` - primary brand color
- **Color Scales**:
  - `t["plot_color"]` - Single Netflix Red for simple charts
  - `t["categorical_colors"]` - 8 colorblind-safe colors for categories
  - `t["cont_scale"]` - Red gradient for sequential data (maps, heatmaps)
  - `t["diverging_scale"]` - Blue-Neutral-Red for diverging data
- **Accessibility**: WCAG AA compliant, colorblind-tested (protanopia, deuteranopia, tritanopia)
- **Usage Pattern**: Import `from static import theme`, then use `t = theme.THEME`

## Visualization Guidelines

- **Choropleth maps** → Use `t["cont_scale"]` (sequential red gradient)
- **Pie charts / multi-category** → Use `t["categorical_colors"]` (8 distinct colors)
- **Single-series charts** → Use `t["plot_color"]` (Netflix Red)
- **Heatmaps** → Use `t["cont_scale"]` (sequential red gradient)
- **Correlation/diverging** → Use `t["diverging_scale"]` (blue-neutral-red)
- **Always add backgrounds**: `plot_bgcolor=t["card_bg"]`, `paper_bgcolor=t["card_bg"]`

## Key Dependencies

- Dash for web framework
- pandas for data manipulation
- plotly for charts
- No testing framework configured

## Documentation Files

- `README.md` - Project overview
