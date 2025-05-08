# 📊 Projet 7 - Modèle de Scoring Crédit

Ce projet a pour objectif de construire un modèle de scoring permettant de prédire la probabilité de défaut de paiement d’un client, et de déterminer si son crédit doit être accordé ou refusé.

## 🎯 Objectifs
- Construire un modèle de prédiction robuste
- Expliquer les prédictions (feature importance globale et locale)
- Mettre en production une API
- Suivre les performances du modèle avec MLflow et Evidently
- Déployer automatiquement l'API avec GitHub Actions

## 🧰 Outils utilisés
- Python, Jupyter Notebook
- Scikit-learn, LightGBM, SHAP, imbalanced-learn
- MLflow
- FastAPI pour l’API
- Streamlit pour l’interface utilisateur
- Evidently pour la détection de data drift
- Git, GitHub, GitHub Actions pour le CI/CD

## 📥 Données utilisées
Les fichiers de données proviennent du dataset Home Credit Default Risk :  
[https://www.kaggle.com/competitions/home-credit-default-risk/data]
Pour lancer le code, placez les fichiers `.csv` dans le dossier `data/`.
Le chargement se fait automatiquement via la fonction `load_all_data(data_dir)`.

## 🗂️ Structure du projet

Projet 7 Modèle de scoring/
├── api/ # Code de l'API FastAPI
├── streamlit/ # Interface utilisateur Streamlit
├── src/ # Fonctions Python génériques
├── data/ # Données et objets enregistrés (y_val, seuils, etc.)
├── bdd/ # Données brutes externes
├── mlartifacts/ # Artifacts produits par MLflow
├── mlruns/ # Dossiers MLflow
├── models/ # Modèles entraînés et enregistrés
├── notebooks/ # Notebooks d’analyse, modélisation et suivi
├── tests/ # Tests unitaires Pytest
├── evidently_report.html # Rapport HTML de data drift
├── requirements.txt
├── environment.yml
└── README.md

## 🛠️ Installation rapide
bash
# Cloner le repo
git clone [https://github.com/ton-utilisateur/ton-repo.git]
cd ton-repo

# Installer les dépendances
pip install -r requirements.txt

## ⚙️ Lancer l'API localement
cd api
uvicorn app:app --reload

## 📲 Tester avec Streamlit
cd streamlit
streamlit run streamlit_app.py
Network URL: [http://192.168.1.11:8501]

## 🧪 Lancer les tests
pytest -s tests/

## 📦 Dépendances
Voir requirements.txt ou environment.yml

## ☁️ Déploiement cloud
L’API est déployée sur [Lien API ici]

## 📊 Suivi MLflow
Interface de tracking disponible en local sur :[http://localhost:5000]