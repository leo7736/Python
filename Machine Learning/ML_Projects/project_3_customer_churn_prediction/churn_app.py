import numpy as np
import pandas as pd
import pickle
import streamlit as st
import json

result = None
df=None

df=pd.read_csv (r"test.csv")
    

# loading the saved model
__model = pickle.load(open(r"Churn_Prediction.pkl", 'rb'))

# loading the column json file
__data_columns = json.load(open(r"churn_columns.json", "r"))['data_columns']
__locations = __data_columns[8:11]  # first 8 columns are creditScore,age,tenure,balance,products,creditCard,activemember,salary
__gender = __data_columns[11:]

def predict_churn(creditScore,age,tenure,balance,products,creditCard,activemember,salary,location,gender):
    try:
        gender_index = __data_columns.index(gender.lower())
        loc_index = __data_columns.index(location.lower())
    except:
        gender_index = -1
        loc_index = -1

    x=np.zeros(len(__data_columns))
    x[0]=creditScore
    x[1]=age
    x[2]=tenure
    x[3]=balance
    x[4]=products
    x[5]=creditCard
    x[6]=activemember
    x[7]=salary
  
    if loc_index >=0 and gender_index >=0:
        x[loc_index]=1
        x[gender_index]=1
    
    status=__model.predict([x])[0]

    if status==1:
        return "The Customer will leave the bank"
    else:
        return "The Customer will not leave the bank"
    
def main():

    global df
    global result
    # giving a title
    st.title('Customer Churn Predictor')

    html_temp = '''
            <style>
            body {
            background-image: url("https://www.shutterstock.com/image-photo/bank-building-574713295");
            background-size: cover;}
            </style>
            <div>
           <h2>Customer Churn Prediction ML app</h2>
           </div>
            '''
    
    st.markdown(html_temp, unsafe_allow_html=True)

    # getting the input data from the user
    creditScore = st.text_input("Credit Score")
    age = st.text_input("Age")
    tenure = st.number_input("Tenure",0,10)
    balance = st.text_input("Enter Account Balance")
    products = st.number_input("Number Of Products",1,4)
    check1=st.selectbox ("Does the customer have a Credit Card?",["yes","no"])
    if check1=="yes":
        creditCard=1
    else:
        creditCard=0
    check2=st.selectbox ("Is the Customer An Active Member?",["yes","no"])
    if check2=="yes":
        activemember=1
    else:
        activemember=0
    salary=st.text_input("Estimated Salary of Customer")
    location = st.selectbox("Location", __locations)
    gender=st.selectbox("Gender", __gender)

    if st.button("Predict"):
        result =predict_churn(creditScore,age,tenure,balance,products,creditCard,activemember,salary,location,gender)

    st.success(f"prediction = {result}")

    st.bar_chart(data=df, x='country', y=None, width=0, height=0, use_container_width=True)


if __name__ == "__main__":
    main()