# ==============================
#  IMPORTATIONS
# ==============================
import pandas as pd
import matplotlib.pyplot as plt
import random


# ==============================
#  1. GÉNÉRATION DES DONNÉES (DYNAMIQUE)
# ==============================

nb_lignes = 1000  # nombre de produits

data = {
    "ID": list(range(1, nb_lignes + 1)),
    "Prix": [round(random.uniform(5, 100), 2) for _ in range(nb_lignes)],
    "Quantite": [random.randint(1, 10) for _ in range(nb_lignes)],
    "Remise": [random.choice([0, 5, 10, 15, 20, 25, 30, 35, 40]) for _ in range(nb_lignes)]
}

df = pd.DataFrame(data)

# sauvegarde CSV brut
df.to_csv("ventes.csv", index=False)
print("✔ ventes.csv généré !")

# ==============================
#  2. CALCULS
# ==============================

df["CA_Brut"] = df["Prix"] * df["Quantite"]
df["CA_Net"] = df["CA_Brut"] * (1 - df["Remise"] / 100)
df["TVA"] = df["CA_Net"] * 0.20

# ==============================
#  3. ANALYSE
# ==============================

ca_total = df["CA_Net"].sum()
meilleur = df.loc[df["CA_Net"].idxmax()]

print(f"\n CA Total = {ca_total:.2f} €")
print(f" Meilleur produit : ID {meilleur['ID']} → {meilleur['CA_Net']:.2f} €")

# ==============================
#  4. EXPORT FINAL
# ==============================

df.to_csv("resultats_final.csv", index=False)
print("✔ resultats_final.csv exporté !")

# ==============================
#  5. PRÉPARATION DES DONNÉES POUR GRAPHIQUES
# ==============================

ids = df["ID"]
ca_nets = df["CA_Net"]

# ==============================
#  6. GRAPHIQUE BARRES
# ==============================

plt.figure(figsize=(10,5))

plt.bar(ids, ca_nets, width=0.5, color=["#5CD0E7"], edgecolor="pink")
plt.title("CA Net par produit", fontsize=13, fontweight="bold")
plt.xlabel("ID Produit")
plt.ylabel("CA Net (€)")

plt.grid(axis='y', linestyle='--', alpha=0.3)

plt.tight_layout()
plt.savefig("graph_barres_test.png", dpi=300)
plt.show()

# ==============================
#  7. GRAPHIQUE CIRCULAIRE
# ==============================

plt.figure(figsize=(8,8))

plt.pie(
    ca_nets,
    startangle=90
)

plt.title("Répartition du CA Net")
plt.axis('equal')

plt.savefig("graph_cercle_test.png", dpi=300)
plt.show()
print("✔ Graphiques générés avec succès !")