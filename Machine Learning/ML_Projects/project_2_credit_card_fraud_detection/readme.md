# Credit Card Fraud Detection

Welcome to the Credit Card Fraud Detection project! This project focuses on developing a machine learning model to detect fraudulent credit card transactions.

## Project Overview

- Algorithm: Logistic Regression
- Accuracy Rate: Above 90%
- Technologies: Python, Scikit-learn, Pandas, NumPy, Seaborn, Jupyter Notebook

## Dataset

Dataset: https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

This dataset presents transactions that occurred in two days, where we have 492 frauds out of 284,807 transactions. The dataset is highly unbalanced, the positive class (frauds) accounts for 0.172% of all transactions.

It contains only numerical input variables which are the result of a PCA transformation. The only features which have not been transformed with PCA are 'Time' and 'Amount'. Feature 'Time' contains the seconds elapsed between each transaction and the first transaction in the dataset. The feature 'Amount' is the transaction Amount.

Feature 'Class' is the response variable and it takes value 1 in case of fraud and 0 otherwise.

## Project Structure

The project is organized into the following directories and files:

- `data`: Contains the dataset used for training and testing the model.
- `notebooks`: Includes Jupyter Notebook files for data exploration, model training, and evaluation.
- `scripts`: Contains Python scripts for preprocessing the data and model implementation.
- `models`: Stores the trained models for future use.
- `results`: Includes evaluation results and performance metrics.

## Getting Started

1. Clone the repository:

```bash
git clone https://github.com/your-username/credit-card-fraud-detection.git
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Explore the `notebooks` directory to understand the data exploration, preprocessing, model training, and evaluation steps.

4. Run the Jupyter Notebook files in the appropriate order to reproduce the project's results and analysis.

## Results

The logistic regression model achieved an accuracy rate of above 90% in detecting credit card fraud. The project also includes an evaluation of performance metrics such as precision, recall, and F1-score to assess the model's effectiveness.

## Conclusion

This project demonstrates the application of logistic regression for credit card fraud detection. By achieving an accuracy rate above 90%, the model shows promising potential in identifying fraudulent transactions and minimizing financial risks.
