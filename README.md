# 📊 Projet 7 - Modèle de Scoring Crédit

Ce projet a pour objectif de construire un modèle de scoring permettant de prédire la probabilité de défaut de paiement d’un client et de déterminer si son crédit doit être accordé ou refusé.

## 🎯 Objectifs
- Construire un modèle de prédiction
- Expliquer les prédictions (feature importance globale et locale)
- Mettre en production une API
- Suivre les performances du modèle avec MLFlow et Evidently

## 🧰 Outils utilisés
- Python, Jupyter Notebook
- Scikit-learn: 
- MLFlow
- Git & GitHub
- Flask ou FastAPI pour l’API
- Streamlit pour l’interface utilisateur
- Evidently pour la détection de data drift

## 🗂️ Structure du projet
Projet7 Modèle de scoring/ │ 
├── data/ → Données brutes (non versionnées) 
├── notebooks/ → Notebooks d’analyse et de modélisation 
├── src/ → Scripts Python (prétraitement, modèle, API...) 
├── models/ → Modèles entraînés 
├── app streamlit/ → Code de l’API 
├── README.md → Ce fichier ! 
├── .gitignore → Fichiers/dossiers à ne pas suivre avec Git 
├── environment.yml → Dépendances conda 
└── requirements.txt → Dépendances pip (optionnel)