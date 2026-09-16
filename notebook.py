import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")


@app.cell
def colab_setup():
    import os
    import subprocess
    import sys

    REPO_URL = "https://github.com/We-Gold/mis587-northwind-analysis.git"

    # On Google Colab: clone the repo (for the data files) and install the pinned requirements.
    # Anywhere else this cell does nothing.
    if "google.colab" in sys.modules:
        if not os.path.isdir("data"):
            subprocess.run(["git", "clone", "--depth", "1", REPO_URL], check=True)
            os.chdir("mis587-northwind-analysis")
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "-q", "-r", "requirements.txt"],
            check=True,
        )
    return


@app.cell
def imports():
    import marimo as mo
    import pandas as pd
    from pathlib import Path

    return Path, mo, pd


@app.cell(hide_code=True)
def intro(mo):
    mo.md("""
    # Northwind Data Overview

    The Northwind database models a small specialty-foods trading company: customers place
    **orders**, handled by **employees**, containing line items (**order details**) for
    **products** supplied by **suppliers** and grouped into **categories**. Employees are
    assigned to sales **territories** within **regions**.
    """)
    return


@app.cell(hide_code=True)
def er_diagram(mo):
    mo.md("""
    ## Entity-relationship diagram

    ![Northwind ER diagram](https://raw.githubusercontent.com/We-Gold/mis587-northwind-analysis/main/northwind-er-diagram.png)
    """)
    return


@app.cell
def load_data(Path, pd):
    DATA_DIR = Path("data")

    # The CSVs are Windows-1252 encoded; keep ID/postal-code columns as strings so leading zeros survive
    tables = {
        _path.stem: pd.read_csv(
            _path,
            encoding="cp1252",
            dtype={"TerritoryID": str, "PostalCode": str, "ShipPostalCode": str},
        )
        for _path in sorted(DATA_DIR.glob("*.csv"))
    }
    return (tables,)


@app.cell
def summary_md(mo):
    mo.md("""
    ## Tables at a glance
    """)
    return


@app.cell(hide_code=True)
def table_summary(pd, tables):
    pd.DataFrame(
        [
            {
                "table": _name,
                "rows": len(_df),
                "columns": _df.shape[1],
                "column names": ", ".join(_df.columns),
            }
            for _name, _df in tables.items()
        ]
    )
    return


@app.cell(hide_code=True)
def join_md(mo):
    mo.md("""
    ## Example: joining two tables

    Attach each order's customer details by merging `orders` and `customers` on `CustomerID`.
    """)
    return


@app.cell
def orders_with_customers(tables):
    customers = tables["Customers"]
    orders = tables["Orders"]

    orders_with_customers = orders.merge(customers, on="CustomerID", how="left")
    orders_with_customers[["OrderID", "OrderDate", "CustomerID", "CompanyName", "Country"]].head()
    return


if __name__ == "__main__":
    app.run()
