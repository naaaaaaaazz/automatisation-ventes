import csv                      # permet de lire et écrire des fichiers CSV
import random                   # permet de générer des nombres aléatoires
import sys                      # permet de récupérer les arguments du terminal
import matplotlib.pyplot as plt # permet de créer des graphiques

# ==============================
# 🎯 1. NOMBRE DE LIGNES DYNAMIQUE
# ==============================

# Si un argument est passé dans le terminal → ex: python script.py 20
# sys.argv contient les paramètres passés dans le terminal
if len(sys.argv) > 1:
    nb_lignes = int(sys.argv[1])   # on prend la valeur donnée par l'utilisateur
else:
    nb_lignes = 15                 # sinon valeur par défaut

print(f"📊 Génération de {nb_lignes} lignes...\n")

# ==============================
# 🎲 2. GÉNÉRATION DU FICHIER CSV
# ==============================

random.seed(42)  # fixe les valeurs aléatoires pour obtenir toujours les mêmes résultats

# ouverture du fichier ventes.csv en mode écriture
with open("ventes.csv", "w", newline="") as f:
    writer = csv.writer(f, delimiter=";")  # séparateur ;

    # écriture de la ligne d'en-tête
    writer.writerow(["ID", "Prix", "Quantite", "Remise"])

    # boucle pour générer les données
    for i in range(nb_lignes):

        id_produit = 100 + i  # ID unique pour chaque produit

        # prix aléatoire entre 5 et 100 euros
        prix = round(random.uniform(5, 100), 2)

        # quantité vendue entre 1 et 50
        quantite = random.randint(1, 50)

        # remise en pourcentage entre 1% et 100%
        remise = random.randint(1, 100)

        # écriture d'une ligne dans le fichier CSV
        writer.writerow([id_produit, prix, quantite, remise])

print("✔ ventes.csv généré avec succès.\n")

# ==============================
# 📖 3. LECTURE + CALCULS
# ==============================

ids = []        # liste des IDs pour le graphique
ca_nets = []    # liste des CA nets pour le graphique
resultats = []  # stockage des résultats enrichis (pour export final)

total = 0       # CA total de l'entreprise
max_ca = 0      # meilleur CA trouvé
id_max = ""     # ID du produit le plus rentable

# ouverture du fichier en lecture
with open("ventes.csv", "r") as f:
    lecteur = csv.reader(f, delimiter=";")

    entete = next(lecteur)  # on saute la première ligne (en-tête)

    # lecture ligne par ligne du fichier
    for ligne in lecteur:

        # conversion des données (CSV = texte par défaut)
        prix = float(ligne[1])
        quantite = int(ligne[2])
        remise = float(ligne[3])

        # ==============================
        # 💰 CALCULS FINANCIERS
        # ==============================

        ca_brut = prix * quantite  # chiffre d'affaires sans remise

        ca_net = ca_brut * (1 - remise / 100)  # CA après remise

        tva = ca_net * 0.20  # TVA de 20%

        total += ca_net  # ajout au total général

        # stockage pour graphique
        ids.append(ligne[0])
        ca_nets.append(ca_net)

        # stockage complet pour export final
        resultats.append(ligne + [ca_brut, ca_net, tva])

        # recherche du produit le plus rentable
        if ca_net > max_ca:
            max_ca = ca_net
            id_max = ligne[0]

# affichage des résultats globaux
print("\n📌 CA Total =", round(total, 2))
print("🏆 Produit le plus rentable =", id_max)

# ==============================
# 📊 4. GRAPHIQUE BARRES
# ==============================

plt.figure(figsize=(12,6))  # taille du graphique

plt.bar(ids, ca_nets, color="#4A90E2", edgecolor="black")

plt.title("CA Net par produit")   # titre
plt.xlabel("ID Produit")          # axe X
plt.ylabel("CA Net")              # axe Y

plt.grid(axis='y', linestyle='--', alpha=0.4)  # grille horizontale

plt.tight_layout()  # ajuste automatiquement les marges

plt.savefig("graph_barres.png", dpi=300)  # sauvegarde image
plt.show()  # affichage

# ==============================
# 🥧 5. GRAPHIQUE CIRCULAIRE
# ==============================

plt.figure(figsize=(8,8))

plt.pie(
    ca_nets,        # valeurs à afficher
    labels=None,    # pas de labels directement sur les parts
    autopct='%1.1f%%',  # affiche les pourcentages
    startangle=90   # rotation du cercle
)

plt.title("Répartition du CA Net")
plt.axis('equal')  # cercle parfait

plt.legend(ids, loc="best", fontsize=8)  # légende avec IDs

plt.savefig("graph_cercle.png", dpi=300)
plt.show()

# ==============================
# 💾 6. EXPORT CSV FINAL
# ==============================

with open("resultats_final.csv", "w", newline="") as f:
    writer = csv.writer(f, delimiter=";")

    # écriture de l'en-tête + nouvelles colonnes
    writer.writerow(entete + ["CA_Brut", "CA_Net", "TVA"])

    # écriture des données enrichies
    for row in resultats:
        writer.writerow(row)

print("✔ fichier resultats_final.csv généré")