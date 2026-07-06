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

    # ENCONTRAR LA RAÍZ DEL REPOSITORIO AUTOMÁTICAMENTE
    # __file__ es 'homework/pregunta_01.py'. Su padre es 'homework' y el padre de su padre es la raíz del repo.
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_path = os.path.join(base_dir, "data", "shipping-data.csv")
    docs_dir = os.path.join(base_dir, "docs")

    # 1. Crear la carpeta 'docs' en la raíz si no existe
    os.makedirs(docs_dir, exist_ok=True)

    # 2. Leer los datos desde la ruta absoluta calculada
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