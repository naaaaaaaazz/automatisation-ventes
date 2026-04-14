# Automatisation des Ventes
**Projet de Fin d'Année — Matière : Logiciels**

---

<p align="center">
  <img src="image.png" width="500">
</p>


## 🖇️ Description
Ce projet répond au besoin d’une entreprise de e-commerce dont le volume de données de ventes est devenu trop important pour être géré dans un tableur classique.
Un script Python a été développé pour automatiser la lecture du fichier CSV, effectuer les calculs financiers (chiffre d’affaires brut, net et TVA), identifier le produit le plus rentable, générer un fichier de résultats et proposer une visualisation graphique.

## 📍Objectif
Automatiser le traitement et l’analyse des données de ventes afin de gagner du temps, réduire les erreurs et faciliter la prise de décision.

---

## 📁 Structure du projet
```
automatisation-ventes/
│
├── ventes.csv
├── vente.py
├── resultats_final.csv
├── requirements.txt
├── image.png
├── Figure_1.png 
└── README.md
```
## 🌐 Cloner le projet (GitHub)
Le projet est disponible sur GitHub et peut être cloné pour exécution locale.

Pour télécharger le projet :

```
git clone https://github.com/naaaaaaaazz/automatisation-ventes
```

Accéder au dossier :

```
cd automatisation-ventes
```

---

## ▶️ Installation et exécution
Le projet est disponible sur GitHub et peut être cloné pour exécution locale.

1. Créer un environnement virtuel :

```
python -m venv venv
```

2. Activer l’environnement :

```
venv\Scripts\activate
```

3. Installer les dépendances :

```
pip install -r requirements.txt
```

4. Lancer le programme :

```
python vente.py
```

## 📥 Données d'entrée  
Le fichier ventes.csv doit utiliser le point-virgule `;` comme séparateur et contient les informations suivantes :

```
ID;Prix;Quantite;Remise
101;15.0;3;10
102;25.0;2;5
...
120;80.0;1;20
```

- **ID** : Identifiant du produit  
- **Prix** : Prix unitaire  
- **Quantite** : Quantité vendue  
- **Remise** : Réduction (%)


## ⚙️ Fonctionnalités
1. Lecture du fichier csv `ventes.csv`
2. Calcul du **CA Brut** (Chiffre d’Affaires Brut) : `Prix × Quantité`
3. Calcul du **CA Net** (Chiffre d’Affaires Net) : `CA_Brut × (1 - Remise / 100)`
4. Calcul de la **TVA** (20%) : `CA_Net × 0.20`
5. Affichage du **CA Total** de l'entreprise `Somme de tous les CA Net`
6. Identification du **produit le plus rentable**
7. Génération d’un nouveau fichier `resultats_final.csv`
8. Affichage des résultats sous forme de tableau

## 🎯 Résultat attendu

Après exécution, le programme :
- Génère un fichier resultats_final.csv
- Affiche le chiffre d’affaires total
- Identifie le produit le plus rentable
- Affiche un graphique des ventes

## 📊 Visualisation
Le script affiche un graphique en barres des ventes (chiffre d’affaires net par produit).

<p align="center">
  <img src="Figure_1.png" width="500">
</p>

## 📤 Fichier de sortie

Le fichier resultats_final.csv contient :
`ID;Prix;Quantite;Remise;CA_Brut;CA_Net;TVA`

## 🧠 Compétences mobilisées

* Programmation en Python
* Manipulation de fichiers CSV
* Analyse de données
* Visualisation avec Matplotlib
* Gestion d’environnement virtuel (venv)
* Utilisation de VS Code
* Débogage (Debug)
* Versioning avec Git

## ⭐ Bonus réalisés

✔️ Lecture dynamique des fichiers CSV
✔️ Visualisation graphique avec matplotlib

## 🔧 Gestion de version (Git)
Le projet a été versionné à l’aide de Git afin de suivre les modifications du code.

Commandes utilisées en local :
```
git init
git add .
git commit -m "Version finale du projet"
```

## 👩‍💻 Auteurs

- **HOUAMI Molka**    
- **LOUATI Mariem**  
- **JAZZAR Emna**   

Projet réalisé en collaboration.

## 🛑 Remarque

Assurez-vous que le fichier ventes.csv est présent dans le même dossier que le script Python avant l’exécution.
Si vous avez cloné le projet via GitHub, tous les fichiers sont déjà correctement organisés.



