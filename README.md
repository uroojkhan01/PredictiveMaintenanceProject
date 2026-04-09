# PredictiveMaintenanceProject
A Machine Learning model that predicts equipment failure from sensor data, transforming reactive repairs into predictive maintenance

## Problem
Predict machine failures using sensor data to reduce downtime in industrial systems.

## Dataset
AI4I 2020 Predictive Maintenance Dataset.

## Approach

### 1. Data Analysis
- Performed EDA to understand feature distributions and class imbalance.

### 2. Modeling
- Logistic Regression (baseline)
- Random Forest
- Gradient Boosting

### 3. Model Selection
Gradient Boosting was selected due to higher recall for failure prediction, which is critical in predictive maintenance.

## Results

| Model | Precision | Recall | F1 |
|------|----------|--------|----|
| Logistic | ... | ... | ... |
| RF | ... | ... | ... |
| GB | ... | ... | ... |

## Deployment

Model deployed using FastAPI.
