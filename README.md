# Northwind Analysis

Exploratory analysis of the Northwind sample database (CSV exports in `data/`, schema in
`northwind-er-diagram.png`).

## Getting Started

### Google Colab

Colab opens Jupyter notebooks straight from GitHub, so use `notebook.ipynb` (a Jupyter export of
`notebook.py`).

1. Open https://colab.research.google.com/github/We-Gold/mis587-northwind-analysis/blob/af6e809/notebook.ipynb

2. Run the first cell. On Colab it clones this repository (for the data files and ER diagram),
   changes into it, and installs the packages in `requirements.txt`.
3. Run the rest of the notebook.

To save your changes, use **File → Save a copy in Drive** (or **Save a copy in GitHub**).

**Please save your changes!**

## Updating the Colab files

`notebook.py` (marimo) is the source of truth. After changing it or the dependencies, regenerate
the Colab files and commit them:

```bash
# requirements.txt from uv.lock
uv export --format requirements-txt --no-hashes --no-dev --no-emit-project -o requirements.txt

# notebook.ipynb from notebook.py
uv run --with nbformat python -m marimo export ipynb notebook.py -o notebook.ipynb --sort top-down -f
```

### Locally (marimo)

```bash
uv sync
uv run marimo edit notebook.py
```