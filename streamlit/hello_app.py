import streamlit as st

st.title("Hello My App")
st.subheader("Web-app with Streamit.")
st.text("Welcome to your first interactive app!!!")
st.write("Choose your favourite sports.")

select = st.selectbox("Your favourite sports: ",["Cricket","Football","Badminton","Tennis","Hockey"])
st.write(f"Your favourite  sport : {select} !!")

st.success("Your Favurite sport has been selected !!")
