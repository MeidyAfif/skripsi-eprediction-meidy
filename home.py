import streamlit as st
from PIL import Image

# --- 1. KONFIGURASI HALAMAN (Wajib di baris pertama) ---
st.set_page_config(
    page_title="Beranda - E-Prediction Bitcoin",
    page_icon="💰",
    layout="wide"
)

# --- 2. SIDEBAR (NAVIGASI & PROFIL) ---
with st.sidebar:
    # Ganti URL ini dengan foto aslimu jika ada, atau biarkan icon ini
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=100)
    
    st.markdown("""
    ### 👨‍🎓 Profil Pengembang
    **Meidy Afif Maulana**<br>
    *NPM: 2209010063*
    <br><br>
    Sistem Informasi<br>
    Fakultas Ilmu Komputer & Teknologi Informasi<br>
    **Universitas Muhammadiyah Sumatera Utara**
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.info("💡 **Navigasi:** Pilih menu di atas/samping untuk melihat Data Historis, Training, dan Hasil Prediksi.")

# --- 3. KONTEN UTAMA ---

# Header / Judul Besar
st.title("💰 E-Prediction Bitcoin")
st.subheader("Analisis Komparatif Model LSTM vs ARIMA dalam Konteks 'Emas Digital'")
st.markdown("---")

# Membagi layar jadi 2 kolom (Kiri: Penjelasan, Kanan: Scoreboard)
col1, col2 = st.columns([2, 1], gap="medium")

with col1:
    st.markdown("""
    ### 📌 Latar Belakang Penelitian
    Selamat datang di Sistem **E-Prediction**. Aplikasi ini dikembangkan sebagai visualisasi Tugas Akhir Skripsi untuk menjawab tantangan investasi aset kripto.
    
    **Mengapa Bitcoin?**
    Bitcoin sering dijuluki sebagai *"Emas Digital"* karena potensinya sebagai pelindung nilai (*store of value*). Namun, volatilitas harganya yang ekstrem menuntut metode prediksi yang presisi.
    
    **Solusi Sistem Ini:**
    Sistem ini mempertandingkan dua algoritma populer untuk melihat mana yang paling *robust* menghadapi fluktuasi pasar:
    * 📈 **ARIMA (Statistical):** Pendekatan linear yang mengandalkan autokorelasi data historis.
    * 🧠 **LSTM (Deep Learning):** Pendekatan saraf tiruan yang mampu menangkap pola non-linear kompleks.
    """)
    
    st.info("""
    🎯 **Tujuan Utama:** Menentukan model terbaik (*Best Fit*) untuk memprediksi harga Bitcoin dan membuktikan kelayakannya sebagai instrumen investasi modern.
    """)

with col2:
    st.markdown("### 🏆 Ringkasan Hasil (Final)")
    
    with st.container(border=True):
        st.markdown("##### **Model Terbaik (Champion)**")
        # Menggunakan st.metric biar terlihat profesional
        st.metric(
            label="📈 ARIMA (Statistical)",
            value="1.77% (MAPE)",
            delta="Robust / Best Fit",
            delta_color="normal" # Hijau artinya bagus
        )
        st.caption("*Menang karena stabil menangkap tren utama.*")
        
        st.divider()
        
        st.markdown("##### **Model Pembanding**")
        st.metric(
            label="🧠 LSTM (Deep Learning)",
            value="3.19% (MAPE)",
            delta="- Overfitting",
            delta_color="inverse" # Merah artinya warning (kalah/jelek)
        )
        st.caption("*Akurat saat latihan, namun bias saat pengujian.*")

# --- 4. PANDUAN NAVIGASI (FOOTER) ---
st.markdown("---")
st.subheader("🚀 Peta Aplikasi")

# Info navigasi disesuaikan dengan struktur file kita
col_a, col_b, col_c = st.columns(3)

with col_a:
    st.success("📊 **Analisis Emas Digital**\n\nLihat bukti korelasi ROI antara Bitcoin, Emas, dan IHSG (Validasi Bab 4).")

with col_b:
    st.warning("⚙️ **Proses Modeling**\n\nTransparansi proses pelatihan data dan parameter yang digunakan.")

with col_c:
    st.error("🏆 **Evaluasi Akhir**\n\nDashboard utama perbandingan grafik prediksi (Actual vs LSTM vs ARIMA) dan tabel error.")