import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Konfigurasi Halaman
st.set_page_config(page_title="Instagram Fake Account Detector", layout="wide")

# Custom CSS untuk mempercantik tampilan
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stAlert {
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# Judul dan Deskripsi
st.title("🛡️ Instagram Fake Account Analysis Dashboard")
st.markdown("""
Aplikasi ini menyajikan visualisasi interaktif dari hasil analisis deteksi akun palsu. 
""")

# Load Data
@st.cache_data
def load_data():
    # Pastikan file sesuai dengan nama di repositori kamu
    df = pd.read_csv("instagram_account.csv")
    return df

df_train = load_data()

# Sidebar Navigasi
st.sidebar.image("https://img.icons8.com/fluency/96/instagram-new.png", width=80)
st.sidebar.title("Menu Analisis")
menu = st.sidebar.selectbox("Pilih Tahapan Analisis:", 
    ["Ringkasan Data", "Distribusi Fitur Profil", "Korelasi Fitur", "Pola Post vs Followers", "Kesimpulan Akhir"])

# Logika Konten
if menu == "Ringkasan Data":
    st.header("📋 1. Dataset Overview")
    
    # Menampilkan metrik utama
    col_m1, col_m2, col_m3 = st.columns(3)
    col_m1.metric("Total Sampel Akun", len(df_train))
    col_m2.metric("Akun Asli (0)", len(df_train[df_train['fake'] == 0]))
    col_m3.metric("Akun Palsu (1)", len(df_train[df_train['fake'] == 1]))
    
    st.write("Berikut adalah cuplikan data mentah yang digunakan dalam analisis ini:")
    st.dataframe(df_train.head(10), use_container_width=True)
    
    st.info("""
    **Catatan:** Dataset ini mencakup berbagai fitur profil seperti jumlah pengikut, jumlah postingan, keberadaan foto profil, 
    hingga rasio angka pada nama pengguna.
    """)

elif menu == "Distribusi Fitur Profil":
    st.header("👥 2. Perbandingan Karakteristik Profil")
    st.markdown("Bagaimana perbedaan fisik profil antara manusia asli dan akun bot?")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Rasio Angka pada Username")
        fig, ax = plt.subplots()
        sns.kdeplot(data=df_train, x='nums/length username', hue='fake', fill=True, palette='coolwarm', ax=ax)
        st.pyplot(fig)
        with st.expander("Lihat Analisis Detail"):
            st.write("""
            **Analisis:** Grafik menunjukkan puncak distribusi yang sangat berbeda. Akun asli menumpuk di angka 0 (tanpa angka), 
            sedangkan akun palsu menyebar ke arah kanan. 
            
            **Insight:** Sistem otomatis pembuat akun sering menyisipkan angka acak agar username unik secara cepat.
            """)

    with col2:
        st.subheader("Panjang Deskripsi Bio")
        fig, ax = plt.subplots()
        sns.boxplot(x='fake', y='description length', data=df_train, palette='viridis', ax=ax)
        st.pyplot(fig)
        with st.expander("Lihat Analisis Detail"):
            st.write("""
            **Analisis:** Akun palsu memiliki kotak (box) yang sangat tipis di angka 0 jika dilihat disini ada disebelah kanan
                     Sedangkan akun asli memiliki kotak (box) yang cukup tebal untuk pemberian biodata di profil nya.
            
            **Insight:** Akun asli cenderung memberikan informasi diri untuk membangun kepercayaan, 
            sedangkan pembuat bot mengabaikan pengisian bio karena dianggap tidak efisien untuk pembuatan akun massal.
            """)

elif menu == "Korelasi Fitur":
    st.header("🔗 3. Hubungan Antar Fitur (Heatmap)")
    st.write("Fitur apa yang mengisaratkan bahwa sebuah akun itu palsu?")
    
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(df_train.corr(), annot=True, cmap='RdYlGn', fmt='.2f', linewidths=0.5, ax=ax)
    st.pyplot(fig)
    
    st.success("""
    **Interpretasi Peta Korelasi:**
    - **Foto Profil (-0.64):** Ini adalah indikator terkuat. Akun tanpa foto profil memiliki kecenderungan sangat tinggi menjadi akun palsu.
    - **Rasio Angka (0.59):** Hubungan positif kuat; semakin banyak angka, semakin besar kemungkinan palsu.
    - **Bio (-0.46):** Semakin pendek bio, semakin besar risiko akun tersebut adalah bot.
    """)

elif menu == "Pola Post vs Followers":
    st.header("📈 4. Analisis Perilaku: Postingan vs Pengikut")
    
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x='fake', y='#posts', data=df_train, palette='Oranges', ax=ax)
    plt.xticks([0, 1], ['Asli (Manusia)', 'Palsu (Bot)'])
    st.pyplot(fig)
    
    st.warning("""
    **Analisis Anomali:**
    Hasil visualisasi menunjukkan ketimpangan yang ekstrem. Akun asli menunjukkan aktivitas produksi konten yang konsisten. 
    Sebaliknya, akun palsu seringkali memiliki jumlah postingan yang mendekati nol namun memiliki statistik pengikut (followers) yang tetap ada.
    """)

elif menu == "Kesimpulan Akhir":
    st.header("🏁 Kesimpulan Strategis")
    st.markdown("""
    Berdasarkan seluruh rangkaian analisis data eksploratif di atas, berikut adalah ringkasan yang dapat diambil:
    
    1. **Identitas adalah Kunci:** Ketidakberadaan foto profil dan nama pengguna yang berantakan (penuh angka) adalah 'Red Flag' pertama yang paling mudah dikenali.
    2. **Investasi Profil:** Akun asli berinvestasi pada biodata dan foto profil untuk menjalin hubungan organik.
    3. **Konsistensi vs Angka:** Jangan tertipu oleh jumlah pengikut. Akun bot diciptakan sebagai angka statistik, bukan sebagai pengguna aktif.
    
    **Saran:** Gunakan parameter Foto Profil, Rasio Angka Username, dan Panjang Bio sebagai filter utama dalam sistem deteksi otomatis Anda.
    """)
