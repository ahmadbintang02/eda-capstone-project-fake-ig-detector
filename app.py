import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Konfigurasi Halaman
st.set_page_config(page_title="Instagram Fake Account Detector", layout="wide")

# Judul dan Deskripsi
st.title("🛡️ Instagram Fake Account Analysis Dashboard")
st.markdown("""
Aplikasi ini memvisualisasikan hasil analisis deteksi akun palsu untuk membantu mengidentifikasi profil yang tidak autentik (fake)
""")

# Load Data
@st.cache_data
def load_data():
    df = pd.read_csv("instagram_account.csv")
    return df

df_train = load_data()

# Sidebar Navigasi
st.sidebar.title("Menu Analisis")
menu = st.sidebar.selectbox("Pilih Pertanyaan Bisnis:", 
    ["Ringkasan Data", "Distribusi Fitur Profil", "Korelasi Fitur", "Pola Post vs Followers"])

# Logika Konten
if menu == "Ringkasan Data":
    st.subheader("1. Dataset Overview")
    st.write(df_train)
    st.write(f"Total Data: {df_train.shape[0]} akun")

elif menu == "Distribusi Fitur Profil":
    st.header("2. Perbandingan Distribusi Fitur Profil")
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Rasio Angka pada Username")
        fig, ax = plt.subplots()
        sns.kdeplot(data=df_train, x='nums/length username', hue='fake', fill=True, palette='coolwarm', ax=ax)
        st.pyplot(fig)
        st.write("**Insight:** Akun palsu (1) cenderung memiliki rasio angka yang jauh lebih tinggi di username-nya.")

    with col2:
        st.subheader("Panjang Deskripsi Bio")
        fig, ax = plt.subplots()
        sns.boxplot(x='fake', y='description length', data=df_train, palette='viridis', ax=ax)
        st.pyplot(fig)
        st.write("**Insight:** Akun asli (0) memiliki variasi bio yang panjang, sementara akun palsu hampir selalu 0.")

elif menu == "Korelasi Fitur":
    st.header("3. Fitur Paling Kuat Menentukan Akun Fake")
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(df_train.corr(), annot=True, cmap='RdYlGn', fmt='.2f', ax=ax)
    st.pyplot(fig)
    st.write("**Insight:** Profile pic (-0.64) dan nums/length username (0.59) adalah indikator terkuat.")

elif menu == "Pola Post vs Followers":
    st.header("4. Pola Interaksi (Post vs Followers)")
    fig, ax = plt.subplots()
    sns.barplot(x='fake', y='#posts', data=df_train, palette='Oranges', ax=ax)
    st.pyplot(fig)
    st.write("**Insight:** Akun palsu memiliki rata-rata postingan yang sangat rendah dibandingkan akun asli.")