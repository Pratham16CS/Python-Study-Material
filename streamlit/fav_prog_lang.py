import streamlit as st

st.title("Programming Languages")
st.subheader("A programming language you want to continue with !!")

fav_lang = st.selectbox("Select your favourite Programming language:",["C","Python","Javascript","R","HTML/CSS","Java","Go","Rust"])
st.success(f"{fav_lang} has been selected as your favourite language.")
