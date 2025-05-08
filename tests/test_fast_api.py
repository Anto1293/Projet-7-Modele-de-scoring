from fastapi.testclient import TestClient
from api.app import app


client = TestClient(app)

def test_predict():
    payload = {
    "CODE_GENDER": 0.0,
    "FLAG_OWN_CAR": 1.0,
    "FLAG_OWN_REALTY": 0.0,
    "CNT_CHILDREN": 0.0,
    "AMT_INCOME_TOTAL": 247500.0,
    "AMT_CREDIT": 497520.0,
    "AMT_ANNUITY": 59175.0,
    "AMT_GOODS_PRICE": 450000.0,
    "REGION_POPULATION_RELATIVE": 0.014464,
    "CNT_FAM_MEMBERS": 2.0,
    "REGION_RATING_CLIENT_W_CITY": 2.0,
    "EXT_SOURCE_1": 0.273594,
    "EXT_SOURCE_2": 0.752981,
    "EXT_SOURCE_3": 0.535276,
    "YEARS_BUILD_AVG": 0.7552,
    "TOTALAREA_MODE": 0.0323,
    "DEF_60_CNT_SOCIAL_CIRCLE": 0.0,
    "IS_UNEMPLOYED": 0.0,
    "BURO_DAYS_CREDIT_MEAN": -1050.571429,
    "BURO_AMT_CREDIT_SUM_MEAN": 195504.852273,
    "BURO_AMT_CREDIT_SUM_OVERDUE_MEAN": 0.0,
    "BURO_CREDIT_DAY_OVERDUE_MEAN": 0.0,
    "PREV_AMT_CREDIT_MAX": 138186.0,
    "PREV_AMT_APPLICATION_MEAN": 141840.0,
    "PREV_APP_CREDIT_PERC_MEAN": 1.026443,
    "PREV_DAYS_DECISION_MIN": -1550.0,
    "POS_SK_DPD_MEAN": 0.0,
    "POS_SK_DPD_DEF_MEAN": 0.0,
    "INSTAL_PAYMENT_DIFF_MEAN": 0.0,
    "INSTAL_PAYMENT_DIFF_MAX": 0.0,
    "INSTAL_DPD_MEAN": 0.0,
    "CC_AMT_BALANCE_MEAN": 26793.606316,
    "CC_AMT_PAYMENT_TOTAL_CURRENT_MEAN": 4093.971864,
    "CC_SK_DPD_MAX": 0.0,
    "DAYS_EMPLOYED_PERC": 0.011957,
    "INCOME_PER_PERSON": 123750.0,
    "ANNUITY_INCOME_PERC": 0.239091,
    "PAYMENT_RATE": 0.11894,
    "CREDIT_TERM": 0.11894,
    "AGE": 53.0,
    "NAME_CONTRACT_TYPE_Revolving loans": 0.0,
    "NAME_INCOME_TYPE_Commercial associate": 0.0,
    "NAME_EDUCATION_TYPE_Secondary / secondary special": 0.0,
    "NAME_HOUSING_TYPE_House / apartment": 1.0,
    "NAME_INCOME_TYPE_Pensioner": 0.0,
    "NAME_INCOME_TYPE_State servant": 1.0,
    "NAME_INCOME_TYPE_Unemployed": 0.0,
    "NAME_INCOME_TYPE_Working": 0.0,
    "NAME_EDUCATION_TYPE_Higher education": 1.0,
    "NAME_EDUCATION_TYPE_Lower secondary": 1.0,
    "NAME_FAMILY_STATUS_Married": 0.0,
    "NAME_FAMILY_STATUS_Single / not married": 0.0,
    "NAME_FAMILY_STATUS_Widow": 1.0,
    "NAME_HOUSING_TYPE_Office apartment": 0.0,
    "NAME_HOUSING_TYPE_Rented apartment": 0.0,
    "NAME_HOUSING_TYPE_With parents": 0.0,
    "SECTOR_Industry": 0.0,
    "SECTOR_Trade": 0.0,
    "SECTOR_Transport": 0.0,
    "SECTOR_Business Entity": 1.0,
    "SECTOR_Government": 0.0,
    "SECTOR_Security": 0.0,
    "SECTOR_Services": 0.0,
    "SECTOR_Construction": 0.0,
    "SECTOR_Medicine": 0.0,
    "SECTOR_Police": 0.0,
    "SECTOR_Other": 0.0,
    "OCCUPATION_Labor_Work": 0.0,
    "OCCUPATION_Sales_Services": 0.0,
    "OCCUPATION_Medical_Staff": 0.0,
    "OCCUPATION_Security": 0.0,
    "OCCUPATION_Management_Core": 0.0,
    "OCCUPATION_Other": 1.0
}
    # Effectuer la requête POST
    response = client.post("/score", json=payload)
    
    # Vérifier le statut de la réponse
    assert response.status_code == 200
    
    # Vérifier la présence des clés attendues dans la réponse
    result = response.json()
    assert "proba" in result
    assert "décision" in result
    assert isinstance(result["proba"], float)
    assert result["décision"] in ["accepté", "refusé"]

    print("RESPONSE JSON:", response.json())

