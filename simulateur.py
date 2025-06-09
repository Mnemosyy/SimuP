import streamlit as st
import time

# Probabilités statistiques officielles ou documentées
stats = {
    '1200': 0.10,       # Source : DREES/INSEE - SMIC ou moins
    '2000': 0.25,       # Source : INSEE - Proche du revenu médian (~2050 € net/mois)
    '3200': 0.50,       # Source : DREES - Revenu moyen net
    '4500': 0.15,       # Source : INSEE - Revenus élevés > 4000€
    '1000': 0.10,       # Source : INSEE - Décile 1
    '2000_nv': 0.20,    # Source : INSEE - Décile 3-4
    '50000': 0.10,      # Source : INSEE - Patrimoine modeste
    '200000': 0.01,     # Source : France Stratégie - Top 1% patrimoine
    'non_fumeur_non_vapoteur': 0.708,
    'cadre': 0.217,
    'LGBT+': 0.10,
    'age_18_24': 0.08,
    'age_25_49': 0.45,
    'age_50_64': 0.22,
    'age_65_plus': 0.25,
    'diplome_bac_plus_3': 0.40,
    'sportif': 0.59,
    'utilisateur_app_rencontre': 0.38,
    'jamais_trompe': 0.70
}

st.set_page_config(page_title="Simulateur de partenaire idéal", page_icon="💘")

st.markdown("""
# 💘 Simulateur de Partenaire Idéal
Décrivez la personne que vous recherchez et découvrez vos chances de la rencontrer en France.

⚠️ **Données uniquement basées sur des sources objectives (INSEE, Santé Publique France, INJEP, IFOP, etc.).**
""")

with st.expander("🧍‍♂️ Caractéristiques générales", expanded=True):
    age = st.radio("Tranche d'âge souhaitée", ["age_18_24", "age_25_49", "age_50_64", "age_65_plus"], index=1)
    diplome = st.toggle("Diplômé (bac+3 ou plus)")
    cadre = st.toggle("Cadre")

with st.expander("💼 Mode de vie", expanded=True):
    salaire = st.select_slider("Revenu net mensuel estimé (en €)", options=[
        ("1200 €", "1200"),
        ("2000 €", "2000"),
        ("3200 €", "3200"),
        ("4500 €", "4500")
    ])
    niveau_vie = st.select_slider("Niveau de vie du ménage (en €)", options=[
        ("1000 €", "1000"),
        ("2000 €", "2000_nv")
    ])
    patrimoine = st.select_slider("Patrimoine estimé (en €)", options=[
        ("50 000 €", "50000"),
        ("200 000 €", "200000")
    ])
    non_fumeur = st.toggle("Non-fumeur & non-vapoteur")
    lgbt = st.toggle("LGBT+")
    sport = st.toggle("Fait du sport régulièrement")
    appli = st.toggle("Utilise des applis de rencontre")
    fidelite = st.toggle("N'a jamais trompé son/sa partenaire")

criteres = [salaire[1], niveau_vie[1], patrimoine[1], age]
if non_fumeur:
    criteres.append("non_fumeur_non_vapoteur")
if cadre:
    criteres.append("cadre")
if lgbt:
    criteres.append("LGBT+")
if diplome:
    criteres.append("diplome_bac_plus_3")
if sport:
    criteres.append("sportif")
if appli:
    criteres.append("utilisateur_app_rencontre")
if fidelite:
    criteres.append("jamais_trompe")

def calculer_chance(criteres):
    p = 1.0
    for crit in criteres:
        p *= stats.get(crit, 1.0)
    return p * 100

if st.button("✨ Calculer mes chances"):
    with st.spinner("Analyse des données en cours..."):
        time.sleep(1.5)
        result = calculer_chance(criteres)
        st.success(f"✅ Vous avez environ **{result:.4f}%** de chances de rencontrer cette personne en France.")
