# data-viz-netflix

Lightweight Dash-based data visualization app for Netflix datasets — a small project scaffold focused on clear conventions and reusable components.

## Quick start

Prerequisites

- Python 3.13+
- uv (project's package manager / runner)

Install project dependencies (example)

- uv add dash
- uv add pandas
- uv add plotly

Run the app

- uv run python main.py

Testing

- No automated test suite. Manually test by running the app and exercising the UI.

## Project structure (root-level)

- main.py — application entry point (Dash app setup)
- components/ — reusable UI components (each component implements `def render(app: Dash, data: pd.DataFrame)`)
- static/
  - theme.py — shared theme dictionaries (constants in UPPER_CASE)
  - heading.py — shared heading utilities
- data/ — data processing classes and CSV sample files

Use relative imports from project root.

## Conventions & style

- Python 3.13+ required.
- Type hints: modern union syntax (e.g. `str | None`, `Path | str`).
- Imports ordering: dash components first, then pandas/plotly, then local modules.
- Component functions: follow `def render(app: Dash, data: pd.DataFrame)` pattern.
- Use dataclasses for configuration and ABC for interfaces where appropriate.
- Naming:
  - snake_case for variables and functions
  - UPPER_CASE for theme/constants
- No git actions performed by agents/scripts (no commits, branches, or PRs).

## Key dependencies

- Dash — web UI framework
- pandas — data manipulation
- plotly — charting library

## Notes

- Install packages and run commands via `uv` as shown above.
- The repository intentionally has no formal test framework — rely on manual verification via the running app.
- Keep components small and reusable; follow the render function signature to ensure consistency.
