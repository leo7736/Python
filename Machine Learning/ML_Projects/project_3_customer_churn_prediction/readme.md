# Bank Customer Churn Prediction Web App

![Bank Customer Churn](https://github.com/leo7736/Python/blob/main/Machine%20Learning/ML_Projects/project_3_customer_churn_prediction/png/scrnsht1.png)
![Bank Customer Churn](https://github.com/leo7736/Python/blob/main/Machine%20Learning/ML_Projects/project_3_customer_churn_prediction/png/scrnsht3.png)

This project aims to develop an end-to-end web application for predicting bank customer churn using the Random Forest algorithm. The application is built with Streamlit and deployed on AWS EC2 cloud.

[Web App Link](http://16.16.216.242:8501/)

## Project Overview

The project focuses on predicting customer churn in a bank, which is a critical task for businesses to identify and retain valuable customers. The Random Forest algorithm is utilized for its ability to handle complex datasets and provide accurate predictions.

The web application allows users to input relevant customer information and obtain churn predictions instantly. The user-friendly interface facilitates a seamless experience for users, making it convenient to analyze and predict churn probabilities.

## Technologies Used

The following technologies were used to develop and deploy the web app:

- Python: Programming language for implementing the project
- Scikit-learn: Machine learning library for training the Random Forest model
- Pickle: Library for serializing and deserializing machine learning models
- Pandas: Data manipulation library for data preprocessing
- NumPy: Library for numerical computing
- Streamlit: Framework for building interactive web applications
- JSON: Data interchange format for configuration
- AWS EC2: Cloud platform for deploying the web app

## Key Features

- User-friendly interface for inputting customer information
- Real-time prediction of customer churn using the Random Forest model
- Interactive visualization of churn prediction results
- Model persistence using Pickle for efficient deployment
- Seamless deployment on AWS EC2 for easy access and scalability

## Installation

To run the web app locally, follow these steps:

1. Clone the repository:

   ```
   git clone https://github.com/your_username/your_repository.git
   ```

2. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Run the application:

   ```
   streamlit run app.py
   ```

## Usage

1. Access the web app through the provided URL at (http://16.16.216.242:8501/).
2. Enter the customer information in the input fields provided.
3. Click on the "Predict" button to generate the churn prediction.
4. Explore the visualization and results provided by the web app.

## Model Training and Persistence

1. The Random Forest model is trained using the Scikit-learn library on the provided bank customer churn dataset.
2. The trained model is serialized using Pickle to create a persistent model file (`model.pkl`).
3. The serialized model is loaded in the web app for churn prediction.

## Deployment

The web app is deployed on AWS EC2. You can access it using the following link: [Web App Link](http://16.16.216.242:8501/).

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please submit a pull request or open an issue.

## About Dataset
[Link](https://www.kaggle.com/datasets/adammaus/predicting-churn-for-bank-customers)

Features of Datset:


* Credit Score
* Age
* Tenure
* Account balance
* No. of Services(products) Availed
* Credit Card
* Active Member or Not
* Salary
* Location
* Gender



