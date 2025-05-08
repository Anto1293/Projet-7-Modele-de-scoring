from fastapi import FastAPI
from pydantic import BaseModel, Field
import pandas as pd
import mlflow
import numpy as np

# Spécifie correctement l'URI du modèle enregistré
mlflow.set_tracking_uri('http://localhost:5000')

# Charger le modèle depuis le Model Registry de MLflow
model_name = "LightGBM"
model_alias = "final"  # L'alias défini dans MLflow
model = mlflow.pyfunc.load_model(f"models:/{model_name}@{model_alias}")


# Créer l'application FastAPI
app = FastAPI(title="API Scoring Client", description="Prédiction de défaut client")

# Créer un schéma de données pour FastAPI (Input)
class InputData(BaseModel):
    CODE_GENDER: float
    FLAG_OWN_CAR: float
    FLAG_OWN_REALTY: float
    CNT_CHILDREN: float
    AMT_INCOME_TOTAL: float
    AMT_CREDIT: float
    AMT_ANNUITY: float
    AMT_GOODS_PRICE: float
    REGION_POPULATION_RELATIVE: float
    CNT_FAM_MEMBERS: float
    REGION_RATING_CLIENT_W_CITY: float
    EXT_SOURCE_1: float
    EXT_SOURCE_2: float
    EXT_SOURCE_3: float
    YEARS_BUILD_AVG: float
    TOTALAREA_MODE: float
    DEF_60_CNT_SOCIAL_CIRCLE: float
    IS_UNEMPLOYED: float
    BURO_DAYS_CREDIT_MEAN: float
    BURO_AMT_CREDIT_SUM_MEAN: float
    BURO_AMT_CREDIT_SUM_OVERDUE_MEAN: float
    BURO_CREDIT_DAY_OVERDUE_MEAN: float
    PREV_AMT_CREDIT_MAX: float
    PREV_AMT_APPLICATION_MEAN: float
    PREV_APP_CREDIT_PERC_MEAN: float
    PREV_DAYS_DECISION_MIN: float
    POS_SK_DPD_MEAN: float
    POS_SK_DPD_DEF_MEAN: float
    INSTAL_PAYMENT_DIFF_MEAN: float
    INSTAL_PAYMENT_DIFF_MAX: float
    INSTAL_DPD_MEAN: float
    CC_AMT_BALANCE_MEAN: float
    CC_AMT_PAYMENT_TOTAL_CURRENT_MEAN: float
    CC_SK_DPD_MAX: float
    DAYS_EMPLOYED_PERC: float
    INCOME_PER_PERSON: float
    ANNUITY_INCOME_PERC: float
    PAYMENT_RATE: float
    CREDIT_TERM: float
    AGE: float
    NAME_CONTRACT_TYPE_Revolving_loans: float = Field(..., alias="NAME_CONTRACT_TYPE_Revolving loans")
    NAME_INCOME_TYPE_Commercial_associate: float = Field(..., alias="NAME_INCOME_TYPE_Commercial associate")
    NAME_INCOME_TYPE_Pensioner: float
    NAME_INCOME_TYPE_State_servant: float = Field(..., alias="NAME_INCOME_TYPE_State servant")
    NAME_INCOME_TYPE_Unemployed: float
    NAME_INCOME_TYPE_Working: float
    NAME_EDUCATION_TYPE_Higher_education: float = Field(..., alias="NAME_EDUCATION_TYPE_Higher education")
    NAME_EDUCATION_TYPE_Lower_secondary: float = Field(..., alias="NAME_EDUCATION_TYPE_Lower secondary")
    NAME_EDUCATION_TYPE_Secondary_special: float = Field(..., alias="NAME_EDUCATION_TYPE_Secondary / secondary special")
    NAME_FAMILY_STATUS_Married: float
    NAME_FAMILY_STATUS_Single_not_married: float = Field(..., alias="NAME_FAMILY_STATUS_Single / not married")
    NAME_FAMILY_STATUS_Widow: float
    NAME_HOUSING_TYPE_House_apartment: float = Field(..., alias="NAME_HOUSING_TYPE_House / apartment")
    NAME_HOUSING_TYPE_Office_apartment: float = Field(..., alias="NAME_HOUSING_TYPE_Office apartment")
    NAME_HOUSING_TYPE_Rented_apartment: float = Field(..., alias="NAME_HOUSING_TYPE_Rented apartment")
    NAME_HOUSING_TYPE_With_parents: float = Field(..., alias="NAME_HOUSING_TYPE_With parents")
    SECTOR_Industry: float
    SECTOR_Trade: float
    SECTOR_Transport: float
    SECTOR_Business_Entity: float = Field(..., alias="SECTOR_Business Entity")
    SECTOR_Government: float
    SECTOR_Security: float
    SECTOR_Services: float
    SECTOR_Construction: float
    SECTOR_Medicine: float
    SECTOR_Police: float
    SECTOR_Other: float
    OCCUPATION_Labor_Work: float
    OCCUPATION_Sales_Services: float
    OCCUPATION_Medical_Staff: float
    OCCUPATION_Security: float
    OCCUPATION_Management_Core: float
    OCCUPATION_Other: float

# Créer un endpoint POST /predict
@app.post("/score")
def predict(data: InputData):
    # Convertir l'input en DataFrame
    input_df = pd.DataFrame([data.dict(by_alias=True)])
    
    # Utiliser le modèle pour prédire
    prediction = model.predict(input_df)[0]
    
    # Appliquer le seuil optimal pour dire accepté / refusé
    decision = "refusé" if prediction > 0.10 else "accepté"
    
    return {
        "proba": round(float(prediction), 4),
        "décision": decision
    }
