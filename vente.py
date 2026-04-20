# importation des bibliothèques
import csv  # permet de lire et écrire des fichiers CSV
import matplotlib.pyplot as plt  # permet de créer des graphiques

# listes pour stocker les données du graphique
ids = []        # stocke les identifiants des produits
ca_nets = []    # stocke les chiffres d'affaires nets

# ouverture du fichier CSV en mode lecture
with open("ventes.csv", "r") as fichier:

    # création du lecteur CSV avec séparateur ;
    lecteur = csv.reader(fichier, delimiter=";")

    # lecture de la première ligne (entête du fichier)
    entete = next(lecteur)

    # affichage de l'entête + colonnes calculées
    print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(
        *entete, "CA_Brut", "CA_Net", "TVA"
    ))

    # initialisation des variables
    total = 0       # somme totale des CA Net
    max_ca = 0      # plus grand CA Net trouvé
    id_max = ""     # ID du produit le plus rentable

    # liste pour stocker les résultats finaux
    resultats = []

    # parcours de chaque ligne du fichier CSV
    for ligne in lecteur:

        # éxtraction et conversion des données
        prix = float(ligne[1])        # prix unitaire
        quantite = int(ligne[2])     # quantité vendue
        remise = float(ligne[3])     # remise en %

        # calcul du chiffre d'affaires brut
        CA_Brut = prix * quantite

        # application de la remise pour obtenir le CA Net
        CA_Net = CA_Brut * (1 - remise / 100)

        # calcul de la TVA (20%)
        TVA = CA_Net * 0.20

        # ajout du CA Net au total global
        total += CA_Net

        # affichage des données sous forme de tableau
        print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(
            *ligne, CA_Brut, CA_Net, TVA
        ))

        # stockage pour le graphique
        ids.append(ligne[0])
        ca_nets.append(CA_Net)

        # Stockage pour export CSV final
        resultats.append(ligne + [CA_Brut, CA_Net, TVA])

        # recherche du produit avec le meilleur CA Net
        if CA_Net > max_ca:
            max_ca = CA_Net
            id_max = ligne[0]

    # affichage des résultats globaux
    print("\nCA Total de l'entreprise =", total)
    print("Produit avec le plus grand bénéfice :", id_max)


# création du graphique (CA Net par produit)
plt.figure(figsize=(10,6))  # taille du graphique

# création des barres
plt.bar(ids, ca_nets, color="#7EB5EC")

# ajout du titre et des axes
plt.title("Analyse du chiffre d'affaires net par produit", fontsize=14)
plt.xlabel("ID Produit")
plt.ylabel("CA Net")

# ajout d'une grille pour faciliter la lecture
plt.grid(axis='y', linestyle='--', alpha=0.5)

# affichage des valeurs au-dessus de chaque barre
for i in range(len(ids)):
    plt.text(ids[i], ca_nets[i],
             round(ca_nets[i], 1),
             ha='center', va='bottom')

# affichage du graphique
plt.show()

# création du graphique circulaire
plt.figure(figsize=(8,8))

plt.pie(
    ca_nets,                # données (CA Net)
    labels=ids,             # noms des produits
    autopct='%1.1f%%',      # affichage en pourcentage
    startangle=90           # rotation pour meilleure lecture
)

# titre
plt.title("Répartition du chiffre d'affaires net par produit",fontsize=20)

# cercle parfait
plt.axis('equal')

# affichage
plt.show()

# création du fichier CSV final
with open("resultats_final.csv", "w", newline="") as fichier_sortie:

    # création de l'écrivain CSV
    ecrivain = csv.writer(fichier_sortie, delimiter=";")

    # écriture de l'entête (colonnes originales + nouvelles)
    ecrivain.writerow(entete + ["CA_Brut", "CA_Net", "TVA"])

    # écriture de toutes les lignes calculées
    for ligne in resultats:
        ecrivain.writerow(ligne)