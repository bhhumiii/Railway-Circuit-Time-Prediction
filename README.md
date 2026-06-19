# Railway Freight Circuit Time Prediction

## Project Overview

This project predicts Railway Freight Rake Circuit Time using Machine Learning techniques. The objective is to estimate the total circuit time of freight rakes based on operational, commodity, route, and loading/unloading features.

## Dataset

* Total Records: 223,793
* Original Features: 94
* Engineered Features: 208+
* Target Variable: Circuit Time (Hours)

## Machine Learning Models

| Model                    | R² Score | MAE   | RMSE  |
| ------------------------ | -------- | ----- | ----- |
| Random Forest (Basic)    | 0.8580   | 18.62 | 34.83 |
| Random Forest (Enhanced) | 0.8735   | 16.19 | 32.87 |
| LightGBM                 | 0.8773   | 16.37 | 32.37 |
| XGBoost                  | 0.8808   | 15.67 | 31.91 |

## Best Model

XGBoost achieved the best performance:

* R² = 0.8808
* MAE = 15.67 Hours
* RMSE = 31.91 Hours

## Key Features

* GRUPCMDT_RMC
* RAKECMDT_RMC
* GRUPTYPE_BOX
* LDNG_ULDG_HOR
* GRUPTYPE_SHRA

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* XGBoost
* Streamlit
* Plotly
* Matplotlib

## Dashboard Features

* Project Overview
* Model Comparison
* Feature Importance Analysis
* Actual vs Predicted Visualization
* Residual Analysis
* Key Insights and Findings

## Author

Bhumi Tiwari
