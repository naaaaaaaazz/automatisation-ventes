# ==============================
#  IMPORTATIONS
# ==============================
import csv                  # lecture/écriture CSV
import random              # génération de données aléatoires
import sys                 # arguments du terminal
import matplotlib.pyplot as plt  # graphiques


# ==============================
#  1. NOMBRE DE LIGNES DYNAMIQUE
# ==============================

# si l'utilisateur donne une valeur dans le terminal
if len(sys.argv) > 1:
    nb_lignes = int(sys.argv[1])
else:
    nb_lignes = 15  # valeur par défaut

print(f" Génération de {nb_lignes} lignes...\n")


# ==============================
#  2. GÉNÉRATION DU FICHIER CSV
# ==============================

random.seed(42)  # reproductibilité des données

with open("ventes.csv", "w", newline="") as f:
    writer = csv.writer(f, delimiter=";")

    # en-tête
    writer.writerow(["ID", "Prix", "Quantite", "Remise"])

    # génération des données
    for i in range(nb_lignes):
        id_produit = 100 + i
        prix = round(random.uniform(5, 100), 2)
        quantite = random.randint(1, 50)
        remise = random.randint(1, 100)

        writer.writerow([id_produit, prix, quantite, remise])

print("✔ ventes.csv généré avec succès.\n")


# ==============================
#  3. LECTURE + CALCULS
# ==============================

ids = []
ca_nets = []
resultats = []

total = 0
max_ca = 0
id_max = ""

with open("ventes.csv", "r") as f:
    lecteur = csv.reader(f, delimiter=";")

    entete = next(lecteur)

    for ligne in lecteur:

        # conversion
        prix = float(ligne[1])
        quantite = int(ligne[2])
        remise = float(ligne[3])

        # calculs
        ca_brut = prix * quantite
        ca_net = ca_brut * (1 - remise / 100)
        tva = ca_net * 0.20

        total += ca_net

        # stockage
        ids.append(ligne[0])
        ca_nets.append(ca_net)
        resultats.append(ligne + [ca_brut, ca_net, tva])

        # meilleur produit
        if ca_net > max_ca:
            max_ca = ca_net
            id_max = ligne[0]


# ==============================
#  4. RÉSULTATS
# ==============================

print("\n CA Total =", round(total, 2))
print(" Produit le plus rentable =", id_max)


# ==============================
#  5. GRAPHIQUE BARRES
# ==============================

plt.figure(figsize=(12,6))

plt.bar(ids, ca_nets, color="#4A90E2", edgecolor="black")

plt.title("CA Net par produit")
plt.xlabel("ID Produit")
plt.ylabel("CA Net")

plt.grid(axis='y', linestyle='--', alpha=0.4)

plt.tight_layout()

plt.savefig("graph_barres.png", dpi=300)
plt.show()


# ==============================
#  6. GRAPHIQUE CIRCULAIRE
# ==============================

plt.figure(figsize=(8,8))

plt.pie(
    ca_nets,
    labels=None,
    autopct='%1.1f%%',
    startangle=90
)

plt.title("Répartition du CA Net")
plt.axis('equal')

plt.legend(ids, loc="best", fontsize=8)

plt.savefig("graph_cercle.png", dpi=300)
plt.show()


# ==============================
#  7. EXPORT CSV FINAL
# ==============================

with open("resultats_final.csv", "w", newline="") as f:
    writer = csv.writer(f, delimiter=";")

    writer.writerow(entete + ["CA_Brut", "CA_Net", "TVA"])

    for row in resultats:
        writer.writerow(row)

print("✔ fichier resultats_final.csv généré")