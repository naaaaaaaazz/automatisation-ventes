import streamlit as st
import pandas as pd

st.title("📊 Analyse des ventes")

# Import fichier
file = st.file_uploader("Importer votre fichier CSV", type=["csv"])

if file is not None:
    df = pd.read_csv(file, sep=";")

    st.write("### Données du fichier")
    st.dataframe(df)

    # Calculs
    df["CA_Brut"] = df["Prix"] * df["Quantite"]
    df["CA_Net"] = df["CA_Brut"] * (1 - df["Remise"]/100)
    df["TVA"] = df["CA_Net"] * 0.20

    st.write("### Résultats")
    st.dataframe(df)

    # CA total
    st.write("### CA total")
    st.success(df["CA_Net"].sum())

    # Graphique
    st.write("### Graphique CA Net")
    st.bar_chart(df.set_index("ID")["CA_Net"])

    # KPIs
    st.metric("CA Total", df["CA_Net"].sum())
    st.metric("Nombre de produits", len(df))
    st.metric("Meilleur CA", df["CA_Net"].max())

    # PRODUIT LE PLUS RENTABLE (AJOUT IMPORTANT)
    best_row = df.loc[df["CA_Net"].idxmax()]
    st.success(f"Produit avec le plus grand bénéfice : {best_row['ID']}")

    # Export CSV (CORRIGÉ - supprimé doublon)
    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        "📥 Télécharger les résultats",
        csv,
        "resultats.csv",
        "text/csv"
    )