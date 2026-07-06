# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""

import os
import matplotlib.pyplot as plt
import pandas as pd


def pregunta_01():
    """
    El archivo `files/input/shipping-data.csv` contiene información sobre los envios
    de productos de una empresa. Cree un dashboard estático en HTML que
    permita visualizar los siguientes campos:

    * `Warehouse_block`
    * `Mode_of_Shipment`
    * `Customer_rating`
    * `Weight_in_gms`

    Todos los archivos debe ser creados en la carpeta `docs`.
    Su código debe crear la carpeta `docs` si no existe.
    """
    # 1. BUSCAR EL ARCHIVO EN LAS RUTAS POSIBLES (Priorizando files/input/)
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    rutas_posibles = [
        os.path.join("files", "input", "shipping-data.csv"),
        os.path.join(base_dir, "files", "input", "shipping-data.csv"),
        os.path.join("data", "shipping-data.csv"),
        os.path.join(base_dir, "data", "shipping-data.csv"),
        "shipping-data.csv",
    ]

    data_path = None
    for ruta in rutas_posibles:
        if os.path.exists(ruta):
            data_path = ruta
            break

    if data_path is None:
        raise FileNotFoundError(
            f"[ERROR] No se pudo encontrar 'shipping-data.csv'. "
            f"Asegúrate de que exista en la carpeta del proyecto."
        )

    # 2. LEER LOS DATOS Y CREAR LA CARPETA 'docs'
    df = pd.read_csv(data_path)
    os.makedirs("docs", exist_ok=True)

    # ---- GRÁFICO 1: shipping_per_warehouse.png ----
    plt.figure(figsize=(6, 4))
    counts_warehouse = df["Warehouse_block"].value_counts().sort_index()
    counts_warehouse.plot(kind="bar", color="tab:blue", alpha=0.8)
    plt.title("Shipping per Warehouse Block", fontsize=12, fontweight="bold")
    plt.xlabel("Warehouse Block")
    plt.ylabel("Count")
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
    plt.grid(axis="y", linestyle="--", alpha=0.5)
    plt.savefig("docs/shipping_per_warehouse.png", bbox_inches="tight")
    plt.close()

    # ---- GRÁFICO 2: mode_of_shipment.png ----
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
    plt.savefig("docs/mode_of_shipment.png", bbox_inches="tight")
    plt.close()

    # ---- GRÁFICO 3: average_customer_rating.png ----
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
    plt.savefig("docs/average_customer_rating.png", bbox_inches="tight")
    plt.close()

    # ---- GRÁFICO 4: weight_distribution.png ----
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
    plt.savefig("docs/weight_distribution.png", bbox_inches="tight")
    plt.close()

    # ---- 3. GENERAR EL ARCHIVO HTML (index.html) ----
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

    with open("docs/index.html", "w", encoding="utf-8") as f:
        f.write(html_content)


if __name__ == "__main__":
    pregunta_01()