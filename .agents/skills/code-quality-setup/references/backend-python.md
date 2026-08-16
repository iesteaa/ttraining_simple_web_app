# Python Backend Guidance

Load this reference only when a Python backend is in scope.

## Discovery

Inspect relevant active files such as:

- `pyproject.toml`
- `requirements*.txt`
- `uv.lock`, `poetry.lock`, `Pipfile.lock`
- `setup.cfg`, `.flake8`, `.isort.cfg`, `mypy.ini`
- Python version files
- Docker/Compose files
- Makefiles/task runners
- backend VS Code Tasks
- backend GitHub workflow commands

## Tool choices

Offer only choices relevant to the repository and requested responsibility.

| Responsibility | Common choices |
|---|---|
| Formatting | Ruff Formatter, Black, autopep8, keep existing, none |
| General linting | Ruff, Flake8, Pylint, keep existing, none |
| Import sorting | Ruff import rules, isort, keep existing, none |
| Type checking | mypy, Pyright, keep existing, none |

Allow a formatter plus import sorting without general linting when that matches
the user's needs.

## Conflict areas to review

- Ruff Formatter with lint rules that overlap formatter behavior
- Black and isort compatibility/profile
- Black and Flake8 line-length/style ownership
- duplicate formatting responsibility between Ruff Formatter and Black
- duplicate import sorting between Ruff rules and isort
- host/container tool version differences
- cache paths that become unwritable across host/container users

Do not hard-code a conflict resolution without checking the selected versions
and active repository configuration.

## Command authority examples

Choose based on repository evidence and user preference:

- container-first: VS Code Tasks and CI route through the approved container command
- package-manager-first: use the same `uv`, Poetry, or project-script entry point
- host-first: use pinned/locked development dependencies and shared configuration

The plan should avoid multiple independent command definitions when one shared
entry point can be reused.
