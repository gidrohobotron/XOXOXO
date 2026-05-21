# XOXOXO — Quick Reference & Common Commands

## Project Structure
```
XOXOXO/
├── tic_tac_toe/        # Main package
│   ├── __init__.py
│   ├── game.py         # Core logic (board, winner check, moves)
│   └── cli.py          # CLI interface
├── tests/
│   └── test_game.py    # Unit tests (2 tests)
├── .github/workflows/
│   └── ci.yml          # GitHub Actions CI
├── requirements.txt    # Dependencies (pytest, colorama, etc.)
└── .venv/              # Virtual environment
```

## Setup & Activation (Windows)
```powershell
# Activate venv
. .\.venv\Scripts\Activate.ps1

# Set PYTHONPATH (needed for local imports in CI)
$env:PYTHONPATH = "$PWD"
# OR for full path:
$env:PYTHONPATH = "d:\Projects\XOXOXO"
```

## Running Tests Locally
```powershell
# One-liner (from repo root)
. .\.venv\Scripts\Activate.ps1; $env:PYTHONPATH = "$PWD"; python -m pytest -q

# Verbose (shows more details)
python -m pytest -v
```

## GitHub Actions CI
**File:** `.github/workflows/ci.yml`

**Key fix applied:** Added `env.PYTHONPATH: ${{ github.workspace }}` to job so pytest finds `tic_tac_toe` module.

**Runs on:** Push to main/feature/*, PR to main
**Python version:** 3.11
**Triggers:** Automatically on push/PR

## Pre-commit hooks

We added `.pre-commit-config.yaml` with the following hooks:

- `black` — code formatter
- `isort` — import sorting (Black profile)
- `flake8` — linting
- `pytest` (local) — optional hook that runs tests on commit

Installation and usage:

```powershell
# install dev deps
pip install -r requirements.txt

# install pre-commit hooks for this repo
pre-commit install

# run hooks against all files once
pre-commit run --all-files
```

Notes:
- The pytest hook runs tests on each commit and may slow down commits; consider enabling it only for major changes or CI.
- If you prefer not to add `pre-commit` to `requirements.txt`, install it globally or in your dev environment.

## Common Issues & Fixes

### ModuleNotFoundError: No module named 'tic_tac_toe'
- **Cause:** Python can't find package (missing PYTHONPATH).
- **Fix:** Set `PYTHONPATH=$PWD` before running pytest.
- **In CI:** Already added to job env vars.

## Useful Links
- Repo: https://github.com/gidrohobotron/XOXOXO
- PR #1 (Init): https://github.com/gidrohobotron/XOXOXO/pull/1

## Notes for Future
- Package is not installed via pip (no setup.py yet) — rely on PYTHONPATH workaround.
- If adding more tests, keep them in `tests/` folder with `test_*.py` naming.
