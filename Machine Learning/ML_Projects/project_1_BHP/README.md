# Bangalore House Price Prediction
</br>
This Project is also deployed on -> http://16.16.94.1:8501/
</br></br>

This Model / Project / Web app predicts the price of a Real Estate property / House on the basis of Features like: 
</br></br>

* location 
* total_sqft
* bathroom 
* BHK
<hr>

## Concept Used</br></br>
<b>1. Data Collection: -</b> From Kaggle: https://www.kaggle.com/datasets/amitabhajoy/bengaluru-house-price-data<br><br>
<b>2. Data PreProcesing:</b><br>

*Removed irrelevant columns from the dataset.

*Checked for null values and either removed or replaced them.

*Detected outliers using Quantile-based Flooring and Capping

*Added new data based on domain knowledge.
<br>

<b>3. Exploratory Data Analysis (EDA): -</b>

*Conducted data analysis based on domain knowledge. Please refer to the Jupyter file for detailed insights.
</br></br>
<b>4. Model Building:</b><br><br>

*Performed encoding for categorical variables.

*As it is a regression problem with linear models, feature scaling is not required.

*Split the data into training and testing sets using train-test split.

*Tested the model's performance on the divided data using train-test split and cross-validation score.

*<b>Model Used</b> - Linear Regression (Multiple Linear Regression)
</br></br>
<b>5. Deployment: - </b>

*Developed a web application using Streamlit.

*Deployed the application on the AWS EC2 cloud platform.
<hr>

The Project / Web App is built in Python using the Following Libraries:
</br></br>

 * numpy
 * pandas
 * matplotlib
 * seaborn
 * sklearn
 * pickle
 * streamlit
 * json
