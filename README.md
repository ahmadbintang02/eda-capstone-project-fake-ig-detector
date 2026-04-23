# 🛡️ Instagram Fake Account Detector - EDA Capstone Project

Repository ini berisi analisis data eksploratif (EDA) dan dashboard interaktif untuk mendeteksi akun Instagram palsu. Proyek ini bertujuan untuk memberikan wawasan bagi pemilik bisnis atau UMKM agar dapat mengidentifikasi akun tidak autentik berdasarkan pola data profil dan aktivitas.

## 📂 Isi Repositori
- `EDA_Project_Capstone.ipynb`: Notebook utama berisi alur Data Wrangling, EDA, hingga Explanatory Analysis.
- `app.py`: File utama untuk menjalankan dashboard interaktif menggunakan Streamlit.
- `requirements.txt`: Daftar library Python yang dibutuhkan untuk menjalankan proyek.
- `instagram_account.csv`: Dataset utama yang digunakan untuk proses analisis.
- `README.md`: Dokumentasi proyek (file yang sedang Anda baca).

## 📊 Pertanyaan Bisnis & Insight Utama
Proyek ini menjawab tiga pertanyaan kunci:
1. **Karakteristik Profil**: Bagaimana perbandingan rasio angka di username dan panjang bio?
   - *Insight*: Akun palsu memiliki rasio angka tinggi dan bio yang seringkali kosong.
2. **Korelasi Terkuat**: Fitur apa yang paling menentukan akun itu palsu?
   - *Insight*: Ketiadaan foto profil (`profile pic`) adalah indikator terkuat (korelasi -0.64).
3. **Pola Interaksi**: Bagaimana hubungan jumlah Postingan vs Followers?
   - *Insight*: Akun palsu seringkali memiliki banyak followers namun jumlah postingan sangat rendah (anomali).

## 🛠️ Library yang Digunakan
- **Pandas**: Digunakan untuk manipulasi data tabel dan proses data wrangling.
- **Numpy**: Digunakan untuk komputasi numerik dan operasi array.
- **Matplotlib & Seaborn**: Digunakan untuk pembuatan visualisasi data, baik pada tahap Exploratory maupun Explanatory.
- **io & google.colab (files)**: Library khusus untuk menangani proses pengunggahan (upload) dataset secara langsung dari komputer lokal ke lingkungan Google Colab.
- **Warnings**: Digunakan untuk mengelola dan memfilter pesan peringatan (warnings) agar output pada Notebook tetap rapi dan profesional.
- **Streamlit**: Digunakan sebagai framework utama untuk men-deploy dashboard analisis ke web (Streamlit Cloud).

- ## 🚀 Cara Menjalankan Project (Local)

Jika Anda ingin menjalankan dashboard ini di komputer lokal, ikuti langkah berikut:

1. **Clone Repositori**:
   git clone https://github.com/ahmadbintang02/eda-capstone-project-fake-ig-detector.git
   cd eda-capstone-project-fake-ig-detector
3. **Instal Library**:
   Pastikan anda sudah menginstal Python, lalu jalankan:
   pip install -r requirements.txt
4. **Jalankan Aplikasi**:
   streamlit run app.py

🌐 Deployment
Dashboard ini juga dapat diakses secara online melalui Streamlit Cloud:
👉 [https://eda-project-capstone-codingcamp2026.streamlit.app]
