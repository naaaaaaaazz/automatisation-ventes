# ==============================
#  IMPORTATIONS
# ==============================

import pandas as pd
import matplotlib.pyplot as plt

# ==============================
#  1. GÉNÉRATION DES DONNÉES
# ==============================

data = {
    "ID": [101, 102, 103],
    "Prix": [15.0, 25.0, 10.0],
    "Quantite": [3, 2, 5],
    "Remise": [10, 5, 0]
}

df = pd.DataFrame(data)

df.to_csv("ventes.csv", index=False)
print("✔ Fichier ventes.csv généré automatiquement !\n")

# ==============================
#  2. CALCULS
# ==============================

#  Chiffre d'affaires brut :
# correspond au montant total AVANT toute remise
df["CA_Brut"] = df["Prix"] * df["Quantite"]

#  Chiffre d'affaires net :
# prend en compte la remise appliquée sur chaque produit
df["CA_Net"] = df["CA_Brut"] * (1 - df["Remise"] / 100)

#  TVA :
# taxe de 20% appliquée sur le CA net
df["TVA"] = df["CA_Net"] * 0.20

# ==============================
#  3. ANALYSE
# ==============================

ca_total = df["CA_Net"].sum()
id_best_product = df.loc[df["CA_Net"].idxmax(), "ID"]

print(" CA Total =", ca_total)
print(" Produit le plus rentable =", id_best_product, "\n")

# ==============================
#  4. EXPORT
# ==============================

df.to_csv("resultats_final.csv", index=False)
print("✔ Fichier exporté avec succès !\n")

# ==============================
#  5. PRÉPARATION DES DONNÉES POUR GRAPHIQUES
# ==============================

ids = df["ID"]
ca_nets = df["CA_Net"]

# ==============================
#  6. GRAPHIQUE BARRES
# ==============================

plt.figure(figsize=(10,5))

plt.bar(ids, ca_nets, width=0.5, color=["#5CD0E7", "#72B800", "#44FDD8"], edgecolor="black")
plt.title("CA Net par produit", fontsize=13, fontweight="bold")
plt.xlabel("ID Produit")
plt.ylabel("CA Net (€)")

plt.grid(axis='y', linestyle='--', alpha=0.3)

plt.tight_layout()
plt.savefig("graph_barres.png", dpi=300)
plt.show()

# ==============================
#  7. GRAPHIQUE CIRCULAIRE
# ==============================

plt.figure(figsize=(8,8))

plt.pie(
    ca_nets,
    labels=ids,
    autopct='%1.1f%%',
    startangle=90
)

plt.title("Répartition du CA Net")
plt.axis('equal')

plt.savefig("graph_cercle.png", dpi=300)
plt.show()

print("✔ Graphiques générés avec succès !")