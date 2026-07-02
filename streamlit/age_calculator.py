import streamlit as st
from datetime import date
from dateutil.relativedelta import relativedelta

st.title("Age Calculator")
st.subheader("Calculate your current age")

today = date.today()

dob = st.date_input("Enter your date of birth",min_value='2000-01-01',max_value=today)

age = relativedelta(today,dob)

st.success(f"Your age: {age.years} years   {age.months} months  {age.days} days")
