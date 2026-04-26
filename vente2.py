import streamlit as st
import pandas as pd
import random

# ==============================
# 🎯 TITRE
# ==============================
st.title("📊 Analyse des ventes (version web)")

# ==============================
# 🎯 NOMBRE DE LIGNES
# ==============================
nb_lignes = st.slider("Nombre de lignes", 2, 1000, 15)

st.write(f"📊 Génération de {nb_lignes} lignes...")

# ==============================
# 🎲 GÉNÉRATION DES DONNÉES
# ==============================
random.seed(42)

data = []

for i in range(nb_lignes):

    id_produit = 100 + i
    prix = round(random.uniform(5, 100), 2)
    quantite = random.randint(1, 50)
    remise = random.randint(1, 100)

    data.append([id_produit, prix, quantite, remise])

# DataFrame
df = pd.DataFrame(data, columns=["ID", "Prix", "Quantite", "Remise"])

# ==============================
# 📋 AFFICHAGE DES DONNÉES
# ==============================
st.subheader("📋 Données générées")
st.dataframe(df)

# ==============================
# 💰 CALCULS
# ==============================
df["CA_Brut"] = df["Prix"] * df["Quantite"]
df["CA_Net"] = df["CA_Brut"] * (1 - df["Remise"] / 100)
df["TVA"] = df["CA_Net"] * 0.20

# ==============================
# 📊 KPI
# ==============================
st.subheader("📈 Résultats")

col1, col2, col3 = st.columns(3)

col1.metric("💰 CA Total", round(df["CA_Net"].sum(), 2))
col2.metric("📦 Quantité totale", int(df["Quantite"].sum()))
col3.metric("🏷️ Remise moyenne", round(df["Remise"].mean(), 2))

# ==============================
# 🏆 MEILLEUR PRODUIT
# ==============================
best = df.loc[df["CA_Net"].idxmax()]
st.success(f"🏆 Produit le plus rentable : {best['ID']}")

# ==============================
# 📊 GRAPHIQUE
# ==============================
st.subheader("📊 CA Net par produit")

st.bar_chart(df.set_index("ID")["CA_Net"])

# ==============================
# 📈 TABLE DES RÉSULTATS
# ==============================
st.subheader("📋 Tableau complet")
st.dataframe(df)