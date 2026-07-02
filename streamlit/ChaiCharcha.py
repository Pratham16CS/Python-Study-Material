import streamlit as st

# Sets the browser tab title and favicon
st.set_page_config(page_title="ChaiCharcha", page_icon="☕")

# Sets the main app title
st.title("☕ChaiCharcha: The Ultimate Taste Poll")
col1,col2 = st.columns(2)

with col1:
    st.header("Masala Chai")
    st.image('https://images.pexels.com/photos/2697931/pexels-photo-2697931.jpeg',width=200)
    vote1 = st.button("Vote Masala Chai.")

with col2:
    st.header("Adrak Chai")
    st.image('https://images.pexels.com/photos/905485/pexels-photo-905485.jpeg',width=200)
    vote2 = st.button("Vote Adrak Chai.")


if vote1:
    st.success("Thanks for voting masala chai.")

elif vote2:
    st.success("Thanks for voting adrak chai.")

name = st.sidebar.text_input("Enter your name: ")
tea = st.sidebar.selectbox("Choose your chai",["Masala","Kesar","Adrak"])

if name and tea:
    st.sidebar.write(f"Welcome {name} and your {tea} chai is getting ready.")

with st.expander("Show chai making instructions"):
    st.write("""
            1. Boil water with tea leaves.
            2. Add milk and spices.
            3. Serve hot.
            """)
    
st.markdown('### Welcome to Chai App')
st.markdown('> Blockquote')
