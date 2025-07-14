# Bengaluru House Price Prediction using Regression

## 🚀 Live Demo

Experience the interactive house price predictor live here:

[Bengaluru House Price Predictor App](https://bengaluru-house-prediction-using-regression-zwpj5v9ovqdihzstrz.streamlit.app/)


---

## 💡 Project Overview

This project implements a machine learning model to predict house prices in Bengaluru, India, based on key property features. The interactive web application, built with Streamlit, allows users to input details about a property and get an instant price prediction.

## ✨ Features

* **User-Friendly Interface:** An intuitive web interface built with Streamlit for easy input and prediction.
* **Location-Based Prediction:** Users can select specific locations in Bengaluru to get more accurate predictions.
* **Key Property Features:** Predicts prices based on total square footage, number of bedrooms, bathrooms, and balconies.
* **Regression Model:** Utilizes a pre-trained regression model (e.g., Linear Regression, Decision Tree, Random Forest) for price estimation.
* **Data Preprocessing:** Handles categorical and numerical data preprocessing consistent with the model's training.

## 🛠 Technologies Used

* **Python:** The core programming language.
* **Streamlit:** For building the interactive web application.
* **Pandas:** For data manipulation and loading the dataset.
* **NumPy:** For numerical operations.
* **Scikit-learn:** For machine learning model training and prediction 
* **Pickle:** For saving and loading the trained machine learning model/pipeline.
* **Git & GitHub:** For version control and project hosting.
* **GitHub Codespaces:** Cloud-based development environment.
* **Streamlit Community Cloud:** For deploying the live web application.


## 🚀 How to Run Locally

If you want to run this application on your local machine:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Yamini26284/Bengaluru-House-Prediction-using-Regression.git](https://github.com/Yamini26284/Bengaluru-House-Prediction-using-Regression.git)
    cd Bengaluru-House-Prediction-using-Regression
    ```
2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run the Streamlit app:**
    ```bash
    streamlit run App.py
    ```
    The app will open in your default web browser (usually at `http://localhost:8501`).

## 📊 Model Details

* **Model Type:** A Linear Regression model was trained on a dataset of Bengaluru house prices.
* **Data:** The `Cleaned_data.csv` contains preprocessed house features.
* **Preprocessing:** Categorical features (like `location`) were **one-hot encoded** to convert them into a numerical format, and numerical features (`total_sqft`, `bath`, `balcony`, `bedrooms`) were **scaled** using `StandardScaler` to normalize their ranges.

## 📧 Contact

Feel free to connect or reach out:

* **GitHub:** 'https://github.com/Yamini26284'

---

