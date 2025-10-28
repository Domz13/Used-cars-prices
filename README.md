# Used Car Price Prediction with Machine Learning

This project predicts **used car prices** based on features such as mileage, brand, model, and vehicle specifications using **machine learning regression models**.  
It demonstrates an end-to-end workflow — from data preprocessing and feature engineering to model training, evaluation, and deployment through a **Streamlit web app**.

---

##  Project Overview

This project aims to build a **predictive model** that estimates a car’s resale value using historical data and key features that influence pricing.

**Objectives:**
- Analyze the relationship between vehicle features and prices.  
- Train and evaluate multiple machine learning models.  
- Deploy an interactive web app for real-time price prediction.

---

## 🧠 Machine Learning Workflow

### **1. Data Preprocessing**
- Combined brand and model into a single feature: `brand_model`
- Encoded categorical variables using **TargetEncoder**
- Handled missing values and cleaned inconsistent entries
- Applied log transformation to prices (for visualization only)

### **2. Feature Set**
Main predictive features:
- `Mileage`
- `Automatic Transmission`
- `Air Conditioner`
- `Power Steering`
- `Remote Control`
- `brand_model` (target encoded)

### **3. Models Used**
- Linear Regression  
- Decision Tree Regressor  
- Random Forest Regressor  *(best performing)*

### **4. Evaluation Metrics**
- **R² Score**
- **Mean Absolute Error (MAE)**
- **Root Mean Squared Error (RMSE)**

---

## 📈 Visualizations
- Distribution of car prices  
- Actual vs Predicted price comparison  
- Feature importance from Random Forest model  
- Log-transformed plots for improved interpretability  
