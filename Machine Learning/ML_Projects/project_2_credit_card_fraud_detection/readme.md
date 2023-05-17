# PROJECT 2
## Credit Card Fraud Detection
Dataset: https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud
### About Dataset:
The dataset contains transactions made by credit cards by European cardholders.

This dataset presents transactions that occurred in two days, where we have 492 frauds out of 284,807 transactions. The dataset is highly unbalanced, the positive class (frauds) accounts for 0.172% of all transactions.

It contains only numerical input variables which are the result of a PCA transformation. The only features which have not been transformed with PCA are 'Time' and 'Amount'. Feature 'Time' contains the seconds elapsed between each transaction and the first transaction in the dataset. The feature 'Amount' is the transaction Amount.

Feature 'Class' is the response variable and it takes value 1 in case of fraud and 0 otherwise.


### Model Used :- Logistic Regression (Multiple Logistic Regression)

The Project is built in Python using the Following Libraries:
</br></br>

 * numpy
 * pandas
 * sklearn
