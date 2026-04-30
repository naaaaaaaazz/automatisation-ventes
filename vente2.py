import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import random

# ==============================
#  FONCTION SCRIPT PRINCIPAL
# ==============================
def run_script(nb_lignes):

    random.seed(42)

    data = {
        "ID": list(range(1, nb_lignes + 1)),
        "Prix": [round(random.uniform(5, 100), 2) for _ in range(nb_lignes)],
        "Quantite": [random.randint(1, 10) for _ in range(nb_lignes)],
        "Remise": [random.choice([0, 5, 10, 15, 20, 25, 30, 35, 40]) for _ in range(nb_lignes)]
    }

    df = pd.DataFrame(data)

    # sauvegarde CSV
    df.to_csv("ventes.csv", index=False)

    if df.empty:
        return None

    # calculs
    df["CA_Brut"] = df["Prix"] * df["Quantite"]
    df["CA_Net"] = df["CA_Brut"] * (1 - df["Remise"] / 100)
    df["TVA"] = df["CA_Net"] * 0.20

    # analyse
    ca_total = df["CA_Net"].sum()
    meilleur = df.loc[df["CA_Net"].idxmax()]

    # graphiques (SANS show)
    fig1, ax1 = plt.subplots()
    ax1.bar(df["ID"], df["CA_Net"])
    ax1.set_title("CA Net par produit")

    fig2, ax2 = plt.subplots()
    ax2.pie(df["CA_Net"])
    ax2.set_title("Répartition du CA Net")

    return df, ca_total, meilleur, fig1, fig2


# ==============================
#  INTERFACE STREAMLIT
# ==============================
st.title("📊 Analyse des ventes")

nb_lignes = st.slider("Nombre de produits", 0, 1000, 15)

if st.button("🚀 Lancer l'analyse"):

    result = run_script(nb_lignes)

    if result is None:
        st.warning("Aucune donnée générée")
    else:
        df, ca_total, meilleur, fig1, fig2 = result

        st.success("Analyse terminée !")

        # KPI
        st.metric("💰 CA Total", round(ca_total, 2))
        st.write(f"🏆 Meilleur produit : ID {meilleur['ID']}")

        # tableau
        st.dataframe(df)

        # graphiques
        st.pyplot(fig1)
        st.pyplot(fig2)