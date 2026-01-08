SheFits
A Women’s Clothing Size Prediction System

SheFits is a machine learning–based application that predicts the most suitable women’s clothing size based on body measurements.  
The goal is to reduce size mismatch issues in online clothing shopping.

Features
- Predicts clothing size using body measurements
- Trained using Machine Learning models
- Interactive Streamlit web application
- Clean preprocessing and feature consistency

Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn
- Streamlit
- Joblib

Dataset
- Custom synthetic dataset with 100+ samples
- Features:
  - Height
  - Weight
  - Bust
  - Waist
  - Hip
- Target:
  - Clothing Size (XS, S, M, L, XL)

Model Details
- Baseline: Logistic Regression
- Final Model: Random Forest Classifier
- Feature scaling using StandardScaler
- Label encoding for target classes

Web Application
Built using Streamlit to allow users to:
- Enter body measurements
- Get instant size recommendations


How to Run the Project
bash
pip install -r requirements.txt
streamlit run app.py
