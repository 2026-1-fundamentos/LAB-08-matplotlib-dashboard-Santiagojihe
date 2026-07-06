# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""


def pregunta_01():
    """
    El archivo `data/shipping-data.csv` contiene información sobre los envios
    de productos de una empresa. Cree un dashboard estático en HTML que
    permita visualizar los siguientes campos:

    * `Warehouse_block`
    * `Mode_of_Shipment`
    * `Customer_rating`
    * `Weight_in_gms`

    Todos los archivos debe ser creados en la carpeta `docs`.
    Su código debe crear la carpeta `docs` si no existe.
    """
    import os
    import matplotlib.pyplot as plt
    import pandas as pd

    # DETERMINAR RUTAS (A prueba de fallos para local y GitHub Classroom)
    # Si existe 'data/shipping-data.csv' en el directorio actual, lo usa; si no, busca desde la raíz del script.
    if os.path.exists("data/shipping-data.csv"):
        data_path = "data/shipping-data.csv"
        docs_dir = "docs"
    else:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        data_path = os.path.join(base_dir, "data", "shipping-data.csv")
        docs_dir = os.path.join(base_dir, "docs")

    # 1. Crear la carpeta 'docs' si no existe
    os.makedirs(docs_dir, exist_ok=True)

    # 2. Leer los datos del CSV
    df = pd.read_csv(data_path)

    # ---- GRÁFICO 1: Shipping per Warehouse Block ----
    plt.figure(figsize=(6, 4))
    counts_warehouse = df["Warehouse_block"].value_counts().sort_index()
    counts_warehouse.plot(kind="bar", color="tab:blue", alpha=0.8)
    plt.title("Shipping per Warehouse Block", fontsize=12, fontweight="bold")
    plt.xlabel("Warehouse Block")
    plt.ylabel("Count")
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
    plt.grid(axis="y", linestyle="--", alpha=0.5)
    plt.savefig(os.path.join(docs_dir, "shipping_per_warehouse.png"), bbox_inches="tight")
    plt.close()

    # ---- GRÁFICO 2: Mode of Shipment ----
    plt.figure(figsize=(6, 4))
    counts_mode = df["Mode_of_Shipment"].value_counts()
    counts_mode.plot(
        kind="pie",
        autopct="%1.1f%%",
        colors=["skyblue", "lightcoral", "lightgreen"],
        startangle=90,
    )
    plt.title("Mode of Shipment", fontsize=12, fontweight="bold")
    plt.ylabel("")  
    plt.savefig(os.path.join(docs_dir, "mode_of_shipment.png"), bbox_inches="tight")
    plt.close()

    # ---- GRÁFICO 3: Average Customer Rating ----
    plt.figure(figsize=(6, 4))
    avg_rating = df.groupby("Warehouse_block")["Customer_rating"].mean()
    avg_rating.plot(kind="bar", color="tab:orange", alpha=0.8)
    plt.title("Average Customer Rating", fontsize=12, fontweight="bold")
    plt.xlabel("Warehouse Block")
    plt.ylabel("Average Rating")
    plt.ylim(0, 5)
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
    plt.grid(axis="y", linestyle="--", alpha=0.5)
    plt.savefig(os.path.join(docs_dir, "average_customer_rating.png"), bbox_inches="tight")
    plt.close()

    # ---- GRÁFICO 4: Weight Distribution ----
    plt.figure(figsize=(6, 4))
    df["Weight_in_gms"].plot(
        kind="hist", bins=20, color="tab:purple", edgecolor="white", alpha=0.8
    )
    plt.title("Weight Distribution", fontsize=12, fontweight="bold")
    plt.xlabel("Weight in gms")
    plt.ylabel("Frequency")
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
    plt.grid(axis="y", linestyle="--", alpha=0.5)
    plt.savefig(os.path.join(docs_dir, "weight_distribution.png"), bbox_inches="tight")
    plt.close()

    # ---- 3. CREAR EL ARCHIVO HTML (Dashboard) ----
    html_content = """<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Shipping Dashboard</title>
    <style>
        body {
            font-family: 'Helvetica Neue', Arial, sans-serif;
            background-color: #f8f9fa;
            margin: 0;
            padding: 20px;
            color: #333;
        }
        h1 {
            text-align: center;
            margin-bottom: 30px;
            color: #222;
        }
        .dashboard-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(450px, 1fr));
            gap: 20px;
            max-width: 1200px;
            margin: 0 auto;
        }
        .card {
            background: #ffffff;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
            padding: 15px;
            text-align: center;
            border: 1px solid #e9ecef;
        }
        img {
            max-width: 100%;
            height: auto;
            border-radius: 4px;
        }
    </style>
</head>
<body>

    <h1>Shipping Data Dashboard</h1>
    
    <div class="dashboard-grid">
        <div class="card">
            <img src="shipping_per_warehouse.png" alt="Shipping per Warehouse Block">
        </div>
        <div class="card">
            <img src="mode_of_shipment.png" alt="Mode of Shipment">
        </div>
        <div class="card">
            <img src="average_customer_rating.png" alt="Average Customer Rating">
        </div>
        <div class="card">
            <img src="weight_distribution.png" alt="Weight Distribution">
        </div>
    </div>

</body>
</html>
"""

    with open(os.path.join(docs_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html_content)


if __name__ == "__main__":
    pregunta_01()