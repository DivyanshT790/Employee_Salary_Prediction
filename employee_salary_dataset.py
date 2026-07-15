import pandas as pd
import numpy as np
import datetime
from sklearn.ensemble import GradientBoostingRegressor
import xgboost as xgb
import streamlit as st
import joblib

def main():
    html_temp = """<h1>Employee_Salary_Prediction</h1>"""

    model = GradientBoostingRegressor()
    model = joblib.load('xgb_model.pkl')

    st.markdown(html_temp,unsafe_allow_html=True)
    st.markdown("This is a web application that predicts the salary of an employee based on their features.")

    p4=st.number_input("please enter the experience of the employee(in years)",0.0,50.0,step=0.5)

    p1=st.number_input("please enter the Age of the employee",18,100,step=1)
    p7=st.number_input("please enter the performance rating of the employee",0,10,step=1)

    s1=st.selectbox("please select the education level of the employee",("Bachelor","Master","PhD", "Diploma"))
    if s1=="Bachelor":
        p3=1
    elif s1=="Master":
        p3=2
    elif s1=="PhD":
        p3=3   
    elif s1=="Diploma":
        p3=0
    
    s2=st.selectbox("please select the department",("Operations","Sales","Marketing","IT","HR","Finance"))
    if s2=="Sales":
        p5=3
    elif s2=="Marketing":
        p5=5
    elif s2=="IT":
        p5=1
    elif s2=="HR":
        p5=4
    elif s2=="Operations":
        p5=0
    elif s2=="Finance":
        p5=2
    s3=st.selectbox("please select the City",("Hyderabad","Mumbai","Chennai","Delhi"))
    if s3=="Hyderabad":
        p11=0
    elif s3=="Mumbai":
        p11=1
    elif s3=="Pune":
        p11=2
    elif s3=="Chennai":
        p11=3
    elif s3=="Bangalore":
        p11=4
    elif s3=="Delhi":
        p11=5
    s4=st.selectbox("please select the job level",("Junior","Mid","Senior","Lead","Manager"))
    if s4=="Junior":
        p6=1
    elif s4=="Mid":
        p6=2
    elif s4=="Senior":
        p6=3
    elif s4=="Lead":
        p6=4
    elif s4=="Manager":
        p6=5
    p8=st.number_input("please enter the number of certifications",0,10,step=1)
    p9=st.number_input("please enter the number of overtime hours",0,100,step=1)
    p10=st.selectbox("please select if the employee works remotely",("Yes","No"))
    if p10=="Yes":
        p10=1
    else:
        p10=0
    p2=st.selectbox("please select the gender of the employee",("Male","Female"))
    if p2=="Male":
        p2=1
    else:
        p2=0
    p12=st.number_input("please enter the company tenure(in years)",0.0,50.0,step=0.5)
    p13=st.number_input("please enter the number of projects completed",0,100,step=1)
    p14=st.number_input("please enter the skill score",0.0,10.0,step=0.1)

    data_new=pd.DataFrame([[p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14]],columns=["Age","Gender","Education","Experience_Years","Department","Job_Level","Performance_Rating","Certifications","Overtime_Hours","Remote_Work","City","Company_Tenure","Projects_Completed","Skill_Score"],index=[0])
    if st.button("Predict"):
        pred=model.predict(data_new)
        st.success(f"The predicted salary of the employee is: {pred[0]:.2f} lakhs")




if __name__ == "__main__":
    main() 
