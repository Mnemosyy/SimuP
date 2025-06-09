import streamlit as st

# Probabilités statistiques simplifiées
stats = {
    'extraverti': 0.50,
    'introverti': 0.50,
    'ISTJ': 0.125,
    'ESFJ': 0.11,
    'ESTJ': 0.09,
    'ENFP': 0.07,
    'INFJ': 0.01,
    'sal_loin': 0.10,
    'sal_bas': 0.25,
    'sal_moy': 0.50,
    'sal_elev': 0.15,
    'nf_décile1': 0.10,
    'nf_décile2': 0.20,
    'patrimoine_1pct': 0.01,
    'patrimoine_10pct': 0.10,
    'non_fumeur-et-non-vapoteur': 0.708,
    'cadre': 0.217,
    'LGBT+': 0.10,
    'age_18_24': 0.08,
    'age_25_49': 0.45,
    'age_50_64': 0.22,
    'age_65_plus': 0.25,
    'diplome_bac_plus_3': 0.40,
    'loyal': 0.60,
    'grand': 0.35,
    'beau_belle': 0.30,
    'sens_humour': 0.50,
    'ambitieux': 0.45,
    'aime_animaux': 0.50,
    'veut_enfants': 0.60,
    'spirituel': 0.25,
    'religieux': 0.20,
    'aime_culture': 0.40,
    'ouvert_d_esprit': 0.50,
    'calme': 0.40,
    'communicatif': 0.50,
    'aime_cuisiner': 0.35,
    'aime_lire': 0.40,
    'aime_nature': 0.45
}

st.title("🎯 Simulateur de Probabilité de Partenaire Idéal")
st.markdown("""
Sélectionnez les critères que vous recherchez chez un partenaire, et nous estimerons la probabilité de le/la rencontrer en France.
""")

# Sélection des critères
perso = st.selectbox("Personnalité (MBTI)", ["ISTJ", "ESFJ", "ESTJ", "ENFP", "INFJ"])
temp = st.radio("Tempérament général", ["extraverti", "introverti"])
salaire = st.selectbox("Niveau de revenu personnel", ["sal_loin", "sal_bas", "sal_moy", "sal_elev"])
niveau_vie = st.selectbox("Niveau de vie du ménage", ["nf_décile1", "nf_décile2"])
patrimoine = st.selectbox("Niveau de patrimoine", ["patrimoine_1pct", "patrimoine_10pct"])
non_fumeur = st.checkbox("Non-fumeur & non-vapoteur")
cadre = st.checkbox("Cadre")
lgbt = st.checkbox("LGBT+")
age = st.selectbox("Tranche d'âge", ["age_18_24", "age_25_49", "age_50_64", "age_65_plus"])
diplome = st.checkbox("Diplômé (bac+3 ou plus)")
loyal = st.checkbox("Loyal")
grand = st.checkbox("Grand (taille > 1m80)")
beau = st.checkbox("Beau / Belle")
humour = st.checkbox("Sens de l'humour")
ambition = st.checkbox("Ambitieux / Ambitieuse")
animaux = st.checkbox("Aime les animaux")
enfants = st.checkbox("Souhaite avoir des enfants")
spirituel = st.checkbox("Spirituel(le)")
religieux = st.checkbox("Religieux(se)")
culture = st.checkbox("Intéressé(e) par la culture")
ouverture = st.checkbox("Ouvert(e) d'esprit")
calme = st.checkbox("Calme")
communicatif = st.checkbox("Communicatif(ve)")
cuisine = st.checkbox("Aime cuisiner")
lire = st.checkbox("Aime lire")
nature = st.checkbox("Aime la nature")

# Calcul
criteres = [perso, temp, salaire, niveau_vie, patrimoine, age]
if non_fumeur:
    criteres.append("non_fumeur-et-non-vapoteur")
if cadre:
    criteres.append("cadre")
if lgbt:
    criteres.append("LGBT+")
if diplome:
    criteres.append("diplome_bac_plus_3")
if loyal:
    criteres.append("loyal")
if grand:
    criteres.append("grand")
if beau:
    criteres.append("beau_belle")
if humour:
    criteres.append("sens_humour")
if ambition:
    criteres.append("ambitieux")
if animaux:
    criteres.append("aime_animaux")
if enfants:
    criteres.append("veut_enfants")
if spirituel:
    criteres.append("spirituel")
if religieux:
    criteres.append("religieux")
if culture:
    criteres.append("aime_culture")
if ouverture:
    criteres.append("ouvert_d_esprit")
if calme:
    criteres.append("calme")
if communicatif:
    criteres.append("communicatif")
if cuisine:
    criteres.append("aime_cuisiner")
if lire:
    criteres.append("aime_lire")
if nature:
    criteres.append("aime_nature")

def calculer_chance(criteres):
    p = 1.0
    for crit in criteres:
        p *= stats.get(crit, 1.0)
    return p * 100

if st.button("🧮 Calculer mes chances"):
    result = calculer_chance(criteres)
    st.success(f"Vous avez environ {result:.8f}% de chances de croiser cette personne en France.")
