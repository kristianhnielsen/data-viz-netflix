# Agent Guidelines for data-viz-netflix

## Build/Test Commands
- **Package Manager**: `uv` (not pip/npm)  
- **Run App**: `uv run python main.py`
- **Install Dependencies**: `uv add <package>`
- **No formal test suite** - manually test via running the app

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
- `components/` - Reusable UI components (data_table.py, graph.py)
- `static/` - Shared utilities (theme.py, heading.py)
- `data/` - Data processing classes and CSV files
- Use relative imports from project root

## Key Dependencies
- Dash for web framework
- pandas for data manipulation  
- plotly for charts
- No testing framework configured