# Bangalore House Price Prediction

Welcome to the Bangalore House Price Prediction project! This project aims to develop a machine learning model to predict the price of real estate properties in Bangalore based on various features.

This Project is also deployed on -> http://16.16.94.1:8501/

![Bangalore House Price Prediction](https://github.com/leo7736/Python/blob/main/Machine%20Learning/ML_Projects/project_1_BHP/png/New%20Tab%20-%20Google%20Chrome%2018-May-23%209_11_05%20PM.png)



## Project Overview

- Algorithm: Multiple Linear Regression
- Technologies: Python, Scikit-learn, Pandas, NumPy, Streamlit, Seaborn, JSON, Pickle
- Deployment: AWS EC2

## Dataset

The dataset used for this project was obtained from Kaggle. It contains information about various houses in Bangalore, including features like location, total square footage, number of bathrooms, and number of bedrooms.

From Kaggle: https://www.kaggle.com/datasets/amitabhajoy/bengaluru-house-price-data

## Project Structure

The project is organized into the following directories and files:

- `data`: Contains the dataset used for training and testing the model.
- `notebooks`: Includes Jupyter Notebook files for data preprocessing, exploratory data analysis (EDA), and model building.
- `scripts`: Contains Python scripts for preprocessing the data and implementing the machine learning model.
- `models`: Stores the trained model for future use.
- `webapp`: Includes the code for the web application built using Streamlit.

## Getting Started

1. Clone the repository:

```bash
git clone https://github.com/your-username/bangalore-house-price-prediction.git
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Explore the `notebooks` directory to understand the data preprocessing, EDA, and model building steps.

4. Run the Jupyter Notebook files in the appropriate order to reproduce the project's results and analysis.

5. To run the web app locally, navigate to the `webapp` directory and execute the following command:

```bash
streamlit run app.py
```

6. Access the web app by opening the provided URL in your browser.

## Model Building

The model building process involves the following steps:

- Data preprocessing: Irrelevant columns were removed, null values were handled, outliers were detected and treated, and new data based on domain knowledge was added.
- Exploratory Data Analysis (EDA): Detailed analysis was conducted to gain insights into the data. Please refer to the Jupyter Notebook for more information.
- Model training: The categorical variables were encoded, and the data was split into training and testing sets using train-test split. The model's performance was evaluated using cross-validation scores and train-test split. Multiple Linear Regression was used as the model for this project.

## Deployment

The project has been deployed on AWS EC2. You can access the deployed web app to predict house prices by visiting the provided URL.

## Conclusion

This project demonstrates the use of Multiple Linear Regression for predicting house prices in Bangalore. By leveraging various features, the model provides estimates of house prices, enabling users to make informed decisions in the real estate market.
