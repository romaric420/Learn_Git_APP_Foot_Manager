import streamlit as st
from fruit_manager import *

# Charger les données
inventaire = ouvrir_inventaire()
prix = ouvrir_prix()
tresorerie = ouvrir_tresorerie()

# Titre de l'application
st.title("📊 Dashboard de la Plantation")

# Afficher la trésorerie
st.header("💰 Trésorerie")
st.metric(label="Montant disponible", value=f"{tresorerie:.2f} $")

# Afficher l'inventaire
st.header("🍏 Inventaire")
st.table(inventaire)
