import streamlit as st
import requests

st.set_page_config(page_title="Prédiction de Défaut", layout="wide")
st.title("Prédiction de Défaut de Paiement")

# Section 1 : Informations personnelles
st.header("1. Informations personnelles")
col1, col2 = st.columns(2)

with col1:
    CODE_GENDER = st.radio("Sexe", [0, 1], format_func=lambda x: "Femme" if x == 0 else "Homme")
    FLAG_OWN_CAR = st.radio("Possède une voiture ?", [0, 1], format_func=lambda x: "Non" if x == 0 else "Oui")
    FLAG_OWN_REALTY = st.radio("Possède un bien immobilier ?", [0, 1], format_func=lambda x: "Non" if x == 0 else "Oui")
    CNT_CHILDREN = st.number_input("Nombre d'enfants", min_value=0, step=1, max_value=3)
    CNT_FAM_MEMBERS = st.number_input("Nombre de membres dans la famille", min_value=1, step=1)
    AGE = st.number_input("Âge", min_value=18, max_value=100)

with col2:
    FAMILY_STATUS = st.selectbox("Statut familial", ["Married", "Single / not married", "Widow"])
    HOUSING_TYPE = st.selectbox("Type de logement", ["House / apartment", "Office apartment", "Rented apartment", "With parents"])

# Section 2 : Situation financière
st.header("2. Situation financière")
AMT_INCOME_TOTAL = st.number_input("Revenu total", min_value=0.0)
AMT_CREDIT = st.number_input("Montant du crédit", min_value=0.0)
AMT_ANNUITY = st.number_input("Montant de l'annuité", min_value=0.0)
AMT_GOODS_PRICE = st.number_input("Prix des biens", min_value=0.0)
INCOME_PER_PERSON = st.number_input("Revenu par personne", min_value=0.0)
ANNUITY_INCOME_PERC = st.number_input("Annuité / Revenu", min_value=0.0)
PAYMENT_RATE = st.number_input("Taux de paiement", min_value=0.0)
CREDIT_TERM = st.number_input("Durée du crédit", min_value=0.0)

# Section 3 : Caractéristiques régionales
st.header("3. Caractéristiques régionales")
REGION_POPULATION_RELATIVE = st.number_input("Population relative de la région", min_value=0.0)
REGION_RATING_CLIENT_W_CITY = st.selectbox("Note de la région", [1, 2, 3])

# Section 4 : Données externes / historiques
st.header("4. Données externes / historiques")
EXT_SOURCE_1 = st.number_input("Source externe 1", min_value=0.0, max_value=1.0)
EXT_SOURCE_2 = st.number_input("Source externe 2", min_value=0.0, max_value=1.0)
EXT_SOURCE_3 = st.number_input("Source externe 3", min_value=0.0, max_value=1.0)
YEARS_BUILD_AVG = st.number_input("Année moyenne de construction", min_value=0.0)
TOTALAREA_MODE = st.number_input("Surface totale", min_value=0.0)
DEF_60_CNT_SOCIAL_CIRCLE = st.number_input("Défaut cercle social (60 j)", min_value=0.0)

# Section 5 : Situation professionnelle
st.header("5. Situation professionnelle")
IS_UNEMPLOYED = st.radio("Demandeur d'emploi ?", [0, 1], format_func=lambda x: "Non" if x == 0 else "Oui")
contract_type = st.selectbox("Type de contrat", ["Cash loans", "Revolving loans"])
income_type = st.selectbox("Type de revenu", ["Working", "Commercial associate", "Pensioner", "State servant", "Unemployed"])
education_type = st.selectbox("Niveau d'éducation", ["Higher education", "Lower secondary", "Secondary / secondary special"])
sector = st.selectbox("Secteur d'activité", ["Industry", "Trade", "Transport", "Business Entity", "Government", "Security", "Services", "Construction", "Medicine", "Police", "Other"])
occupation = st.selectbox("Métier", ["Labor_Work", "Sales_Services", "Medical_Staff", "Security", "Management_Core", "Other"])

# Section 6 : Historique bancaire et crédit
st.header("6. Historique bancaire et crédit")
BURO_DAYS_CREDIT_MEAN = st.number_input("BURO: Jours de crédit moyen")
BURO_AMT_CREDIT_SUM_MEAN = st.number_input("BURO: Montant crédit moyen")
BURO_AMT_CREDIT_SUM_OVERDUE_MEAN = st.number_input("BURO: Crédit en retard")
BURO_CREDIT_DAY_OVERDUE_MEAN = st.number_input("BURO: Jours de retard moyen")
PREV_AMT_CREDIT_MAX = st.number_input("Crédit précédent max")
PREV_AMT_APPLICATION_MEAN = st.number_input("Demande de crédit moyenne")
PREV_APP_CREDIT_PERC_MEAN = st.number_input("Ratio montant crédit / demande")
PREV_DAYS_DECISION_MIN = st.number_input("Jours depuis décision précédente min")
POS_SK_DPD_MEAN = st.number_input("POS: DPD moyen")
POS_SK_DPD_DEF_MEAN = st.number_input("POS: Défaut moyen")
INSTAL_PAYMENT_DIFF_MEAN = st.number_input("Diff. de paiement moyenne")
INSTAL_PAYMENT_DIFF_MAX = st.number_input("Diff. de paiement max")
INSTAL_DPD_MEAN = st.number_input("INSTAL: DPD moyen")
CC_AMT_BALANCE_MEAN = st.number_input("CC: Solde moyen")
CC_AMT_PAYMENT_TOTAL_CURRENT_MEAN = st.number_input("CC: Paiement total courant")
CC_SK_DPD_MAX = st.number_input("CC: DPD max")
DAYS_EMPLOYED_PERC = st.number_input("Jours employés en %")

# Bouton de prédiction
if st.button('Obtenir la prédiction'):
    one_hot = {
        "NAME_CONTRACT_TYPE_Revolving loans": 1 if contract_type == "Revolving loans" else 0,
        "NAME_INCOME_TYPE_Commercial associate": 1 if income_type == "Commercial associate" else 0,
        "NAME_INCOME_TYPE_Pensioner": 1 if income_type == "Pensioner" else 0,
        "NAME_INCOME_TYPE_State servant": 1 if income_type == "State servant" else 0,
        "NAME_INCOME_TYPE_Unemployed": 1 if income_type == "Unemployed" else 0,
        "NAME_INCOME_TYPE_Working": 1 if income_type == "Working" else 0,
        "NAME_EDUCATION_TYPE_Higher education": 1 if education_type == "Higher education" else 0,
        "NAME_EDUCATION_TYPE_Lower secondary": 1 if education_type == "Lower secondary" else 0,
        "NAME_EDUCATION_TYPE_Secondary / secondary special": 1 if education_type == "Secondary / secondary special" else 0,
        "NAME_FAMILY_STATUS_Married": 1 if FAMILY_STATUS == "Married" else 0,
        "NAME_FAMILY_STATUS_Single / not married": 1 if FAMILY_STATUS == "Single / not married" else 0,
        "NAME_FAMILY_STATUS_Widow": 1 if FAMILY_STATUS == "Widow" else 0,
        "NAME_HOUSING_TYPE_House / apartment": 1 if HOUSING_TYPE == "House / apartment" else 0,
        "NAME_HOUSING_TYPE_Office apartment": 1 if HOUSING_TYPE == "Office apartment" else 0,
        "NAME_HOUSING_TYPE_Rented apartment": 1 if HOUSING_TYPE == "Rented apartment" else 0,
        "NAME_HOUSING_TYPE_With parents": 1 if HOUSING_TYPE == "With parents" else 0,
        "SECTOR_Industry": 1 if sector == "Industry" else 0,
        "SECTOR_Trade": 1 if sector == "Trade" else 0,
        "SECTOR_Transport": 1 if sector == "Transport" else 0,
        "SECTOR_Business Entity": 1 if sector == "Business Entity" else 0,
        "SECTOR_Government": 1 if sector == "Government" else 0,
        "SECTOR_Security": 1 if sector == "Security" else 0,
        "SECTOR_Services": 1 if sector == "Services" else 0,
        "SECTOR_Construction": 1 if sector == "Construction" else 0,
        "SECTOR_Medicine": 1 if sector == "Medicine" else 0,
        "SECTOR_Police": 1 if sector == "Police" else 0,
        "SECTOR_Other": 1 if sector == "Other" else 0,
        "OCCUPATION_Labor_Work": 1 if occupation == "Labor_Work" else 0,
        "OCCUPATION_Sales_Services": 1 if occupation == "Sales_Services" else 0,
        "OCCUPATION_Medical_Staff": 1 if occupation == "Medical_Staff" else 0,
        "OCCUPATION_Security": 1 if occupation == "Security" else 0,
        "OCCUPATION_Management_Core": 1 if occupation == "Management_Core" else 0,
        "OCCUPATION_Other": 1 if occupation == "Other" else 0,
    }

    features = {
        'CODE_GENDER': CODE_GENDER,
        'FLAG_OWN_CAR': FLAG_OWN_CAR,
        'FLAG_OWN_REALTY': FLAG_OWN_REALTY,
        'CNT_CHILDREN': CNT_CHILDREN,
        'AMT_INCOME_TOTAL': AMT_INCOME_TOTAL,
        'AMT_CREDIT': AMT_CREDIT,
        'AMT_ANNUITY': AMT_ANNUITY,
        'AMT_GOODS_PRICE': AMT_GOODS_PRICE,
        'REGION_POPULATION_RELATIVE': REGION_POPULATION_RELATIVE,
        'CNT_FAM_MEMBERS': CNT_FAM_MEMBERS,
        'REGION_RATING_CLIENT_W_CITY': REGION_RATING_CLIENT_W_CITY,
        'EXT_SOURCE_1': EXT_SOURCE_1,
        'EXT_SOURCE_2': EXT_SOURCE_2,
        'EXT_SOURCE_3': EXT_SOURCE_3,
        'YEARS_BUILD_AVG': YEARS_BUILD_AVG,
        'TOTALAREA_MODE': TOTALAREA_MODE,
        'DEF_60_CNT_SOCIAL_CIRCLE': DEF_60_CNT_SOCIAL_CIRCLE,
        'IS_UNEMPLOYED': IS_UNEMPLOYED,
        'BURO_DAYS_CREDIT_MEAN': BURO_DAYS_CREDIT_MEAN,
        'BURO_AMT_CREDIT_SUM_MEAN': BURO_AMT_CREDIT_SUM_MEAN,
        'BURO_AMT_CREDIT_SUM_OVERDUE_MEAN': BURO_AMT_CREDIT_SUM_OVERDUE_MEAN,
        'BURO_CREDIT_DAY_OVERDUE_MEAN': BURO_CREDIT_DAY_OVERDUE_MEAN,
        'PREV_AMT_CREDIT_MAX': PREV_AMT_CREDIT_MAX,
        'PREV_AMT_APPLICATION_MEAN': PREV_AMT_APPLICATION_MEAN,
        'PREV_APP_CREDIT_PERC_MEAN': PREV_APP_CREDIT_PERC_MEAN,
        'PREV_DAYS_DECISION_MIN': PREV_DAYS_DECISION_MIN,
        'POS_SK_DPD_MEAN': POS_SK_DPD_MEAN,
        'POS_SK_DPD_DEF_MEAN': POS_SK_DPD_DEF_MEAN,
        'INSTAL_PAYMENT_DIFF_MEAN': INSTAL_PAYMENT_DIFF_MEAN,
        'INSTAL_PAYMENT_DIFF_MAX': INSTAL_PAYMENT_DIFF_MAX,
        'INSTAL_DPD_MEAN': INSTAL_DPD_MEAN,
        'CC_AMT_BALANCE_MEAN': CC_AMT_BALANCE_MEAN,
        'CC_AMT_PAYMENT_TOTAL_CURRENT_MEAN': CC_AMT_PAYMENT_TOTAL_CURRENT_MEAN,
        'CC_SK_DPD_MAX': CC_SK_DPD_MAX,
        'DAYS_EMPLOYED_PERC': DAYS_EMPLOYED_PERC,
        'INCOME_PER_PERSON': INCOME_PER_PERSON,
        'ANNUITY_INCOME_PERC': ANNUITY_INCOME_PERC,
        'PAYMENT_RATE': PAYMENT_RATE,
        'CREDIT_TERM': CREDIT_TERM,
        'AGE': AGE
    }

    features.update(one_hot)

    response = requests.post("http://127.0.0.1:8000/score", json=features)

    if response.status_code == 200:
        result = response.json()
        proba = result['proba']
        prediction = 1 if proba >= 0.10 else 0

        st.markdown(f"### 🔢 Probabilité de défaut : **{proba:.2%}**")
        if prediction == 1:
            st.error("❌ Crédit REFUSÉ (risque trop élevé)")
        else:
            st.success("✅ Crédit ACCEPTÉ (risque acceptable)")
    else:
        st.error("❌ Erreur lors de l'appel à l'API")
