# Task 2: End-to-End ML Pipeline with Scikit-learn Pipeline API

## Task Objective
Build a reusable, production-ready machine learning pipeline for predicting customer churn. The workflow should handle preprocessing, model training, hyperparameter tuning, evaluation, and export the final pipeline for reuse.

## Dataset Used
- **Dataset:** Telco Customer Churn
- **File:** `Telco-Customer-Churn.csv`
- **Target column:** `Churn`

## Models Applied
- Logistic Regression
- Random Forest Classifier

Both models were wrapped in a scikit-learn `Pipeline` with preprocessing steps such as scaling and encoding. `GridSearchCV` was used to tune hyperparameters for both models.

## Key Results and Findings
- The best cross-validation ROC AUC was slightly higher for **Random Forest** (`0.8476`) than for **Logistic Regression** (`0.8460`).
- On the test set, both models performed very similarly:
  - Logistic Regression ROC AUC: `0.8350`
  - Random Forest ROC AUC: `0.8351`
- The final selected model was **Random Forest**.
- The complete trained pipeline was exported as `best_pipeline.joblib`.