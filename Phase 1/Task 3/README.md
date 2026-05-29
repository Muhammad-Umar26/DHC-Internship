# Task 3 - Heart Disease Prediction

## Task Objective
- Build a classification model to predict heart disease risk.
- Clean the dataset, perform EDA, train models, and evaluate performance.
- Report accuracy, ROC AUC, confusion matrix, and feature importance.

## Dataset Used
- Heart Disease UCI dataset stored as heart.csv.
- Patient health attributes include age, cp, trestbps, chol, thalach, oldpeak, ca, thal, and others.
- The target column indicates whether heart disease is present.

## Models Applied
- Logistic Regression
- Decision Tree Classifier

## Key Results and Findings
- Logistic Regression performed better overall with Accuracy 0.8033 and ROC AUC 0.9015.
- Decision Tree achieved Accuracy 0.7869 and ROC AUC 0.7684.
- The strongest predictors were cp, oldpeak, thal, ca, thalach, and exang.
- Low-signal features such as chol and fbs were dropped, which reduced noise and improved interpretability.
- Logistic Regression gave the most reliable separation of the two classes for this split.
