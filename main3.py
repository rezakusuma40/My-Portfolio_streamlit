import streamlit as st

st.set_page_config(page_title="Streamlit App", page_icon=":shark:", layout="wide")
st.title("My Portfolio")
st.header('Data Scientist')

st.sidebar.title("Navigation")

page = st.sidebar.radio("Go to", ["Home", "About", "Projects", "Contact"])

if page == "Home":
  st.write("Welcome to my portfolio! Feel free to explore the different pages.")
elif page == "About":
  import about_me
  about_me.about_me()
elif page == "Projects":
  import project
  project.show_projects()
elif page == "Contact":
  import contact
  contact.show_contact()