import streamlit as st
from PIL import Image
import time

# konfigurasi halaman
st.set_page_config(page_title="My Portfolio", page_icon="random")

# foto profil
profile_pic = Image.open("assets/semangat dong.png")  # ganti dengan foto profilmu

# data profil
name = "Muhammad Reza Adi Kusuma"
description = "Data Scientist | Data Engineer | Web Scraping"
bio = "Saya adalah seorang data enthusiast dengan pengalaman dalam analisis data, machine learning, dan web scraping"

# tautan kontak
linkedin_url = "https://www.linkedin.com/in/muhammadrezaadikusuma/"
github_url = "https://github.com/rezakusuma40"
email = "muhammadkusumareza@gmail.com"

# menampilkan profil
col1, col2 = st.columns([1, 3])
with col1:
  st.image(profile_pic, width=150)
with col2:
  st.markdown(f"# {name}")
  st.write(description)
  st.write(bio)
  st.write(f"📧 [Email](mailto:{email}) | 🌐 [LinkedIn]({linkedin_url}) | 💻 [GitHub]({github_url})")

st.write("---")

# daftar proyek
st.subheader("📂 Project")
projects = [
  {"title": "Prediksi Harga Airbnb", "description": "Pemodelan machine learning untuk memprediksi harga penginapan.", "image": "assets/airbnb price prediction.jpg", "link": "#"},
  {"title": "Private Lease Cars Scraping", "description": "Web scraping data situs penyewaan mobil.", "image": "assets/private cars lease.jpg", "link": "https://github.com/rezakusuma40/Private_Lease_Cars_Scraping"},
  {"title": "Investment Tweets Processing", "description": "Membuat End-to-end ETL pipeline untuk memproses tweet tentang investasi.", "image": "assets/investment tweets.jpeg", "link": "https://github.com/rezakusuma40/SBD_Cilsy_Final_Project"},
]

cols = st.columns([1, 1, 1])
for index, project in enumerate(projects):
  with cols[index % 3]:
    image = Image.open(project["image"]).resize((300, 200))  # memastikan ukuran gambar seragam
    st.image(image, use_container_width=True)
    st.markdown(f"### [{project['title']}]({project['link']})")
    st.write(project['description'])

# Menampilkan ikon technical skills
st.subheader("🛠 Technical Skills")
skills = [
  ("Python", "assets/icons/python.svg"),
  ("PostgreSQL", "assets/icons/postgresql.svg"),
  ("BeautifulSoup", "assets/icons/beautifulsoup.png"),
  ("Selenium", "assets/icons/selenium.svg"),
  ("Pandas", "assets/icons/pandas.svg"),
  ("NumPy", "assets/icons/numpy.svg"),
  ("Matplotlib", "assets/icons/matplotlib.svg"),
  ("Seaborn", "assets/icons/seaborn.svg"),
  ("Scikit-learn", "assets/icons/scikit-learn.svg"),
  ("Tableau", "assets/icons/tableau.svg"),
  ("Power BI", "assets/icons/power-bi.svg"),
  ("Apache Spark", "assets/icons/spark.svg"),
  ("Apache Airflow", "assets/icons/airflow.svg"),
  ("Apache Kafka", "assets/icons/kafka.svg"),
  ("BigQuery", "assets/icons/bigquery.svg"),
  ("Cloud Storage", "assets/icons/gcs.svg"),
  ("Compute Engine", "assets/icons/compute-engine.svg"),
  ("Dataproc", "assets/icons/dataproc.svg"),
]

skill_cols = st.columns(6)  # Menampilkan dalam 6 kolom agar lebih rapi
for index, (skill, icon) in enumerate(skills):
  with skill_cols[index % 6]:
    st.image(icon, width=50)
    st.write(skill)

st.markdown(
    """
    <style>
    body {
        background-color: #ffffff;  # Replace with your desired color
    }
    </style>
    """,
    unsafe_allow_html=True
)