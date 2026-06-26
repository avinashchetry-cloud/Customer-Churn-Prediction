# Customer Churn Prediction (Baseline Model)

## Overview
This project focuses on predicting customer churn using machine learning. The goal is to identify customers who are likely to leave so that retention strategies can be applied in advance.

A Logistic Regression model is used as a baseline approach for classification.

---

## Problem Statement
Customer churn is a major issue for subscription-based businesses. The objective is to build a model that can classify whether a customer will churn or not based on available features.

---

## Dataset
The dataset contains customer demographic, account, and usage-related features used to predict churn behavior.

---

## Workflow

### 1. Data Preprocessing
- Handled missing values (if any)
- Encoded categorical variables
- Feature scaling where required
- Train-test split performed

### 2. Model Building
- Logistic Regression used as baseline classifier

### 3. Evaluation Metrics
- Accuracy: ~0.75  
- ROC-AUC: ~0.74  
- Confusion Matrix used for detailed performance analysis

---

## Key Observations
- Model shows moderate predictive capability
- Baseline performance is acceptable but not optimized
- Results indicate scope for further improvement in feature engineering and model tuning

---

## Future Improvements
- Handle class imbalance using techniques like SMOTE or class weighting
- Hyperparameter tuning
- Try advanced models like Random Forest, XGBoost, and Gradient Boosting
- Threshold optimization for better recall
- Feature engineering to improve signal quality

---

## Tech Stack
- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn

---

## Status
Baseline version completed. Further optimization in progress.
