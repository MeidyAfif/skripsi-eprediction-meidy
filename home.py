import streamlit as st
from PIL import Image

# --- 1. KONFIGURASI HALAMAN (Wajib di baris pertama) ---
st.set_page_config(
    page_title="Beranda - E-Prediction Bitcoin",
    page_icon="🏠",
    layout="wide"
)

# --- 2. SIDEBAR (NAVIGASI & PROFIL) ---
with st.sidebar:
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
    st.info("💡 **Tips:** Gunakan menu di samping kiri untuk berpindah halaman.")

# --- 3. KONTEN UTAMA ---

# Header / Judul Besar
st.title("💰 E-Prediction Bitcoin")
st.subheader("Sistem Analisis & Prediksi Aset Kripto sebagai 'Emas Digital'")
st.markdown("---")

# Membagi layar jadi 2 kolom (Kiri: Penjelasan, Kanan: Rangkuman Data)
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    ### 📌 Latar Belakang Penelitian
    Selamat datang di Sistem **E-Prediction**. Aplikasi ini dikembangkan sebagai bagian dari Tugas Akhir Skripsi untuk menjawab tantangan investasi di era ekonomi digital yang penuh ketidakpastian.
    
    **Mengapa Bitcoin?**
    Bitcoin sering dijuluki sebagai *"Emas Digital"* karena karakteristiknya yang unik sebagai pelindung nilai. Namun, volatilitas harganya yang ekstrem seringkali membuat investor ragu.
    
    **Solusi Sistem Ini:**
    Sistem ini membandingkan kinerja dua metode algoritma canggih untuk membedah pola harga Bitcoin:
    * **ARIMA (Statistik Klasik):** Mengandalkan pola linear masa lalu untuk prediksi jangka pendek.
    * **LSTM (Deep Learning):** Menggunakan Jaringan Saraf Tiruan (*Artificial Intelligence*) untuk mempelajari pola non-linear yang kompleks.
    """)
    
    st.success("""
    🎯 **Tujuan Utama:** Membuktikan secara ilmiah apakah Bitcoin dapat diprediksi dengan akurat, serta memvalidasi hipotesisnya sebagai aset investasi modern yang setara dengan Emas.
    """)

with col2:
    st.markdown("### 🔍 Ringkasan Hasil Skripsi")
    
    with st.container(border=True):
        st.markdown("**1. Dataset Penelitian**")
        st.caption("Yahoo Finance (Jan 2020 - Des 2024)")
        
        st.markdown("**2. Metode AI (Champion)**")
        st.caption("🧠 **LSTM** (Long Short-Term Memory)")
        st.caption("• Error Terendah: **3.09%**")
        st.caption("• Karakter: *Trend Follower*")
        
        st.markdown("**3. Metode Statistik**")
        st.caption("📈 **ARIMA** (AutoRegressive Integrated Moving Average)")
        st.caption("• Error Terendah: **1.84%**")
        st.caption("• Karakter: *High Precision*")

# --- 4. PANDUAN NAVIGASI (FOOTER) ---
st.markdown("---")
st.markdown("### 🚀 Panduan Menu Aplikasi")

# Info navigasi biar dosen/pengguna paham isi webnya
col_a, col_b, col_c = st.columns(3)

with col_a:
    st.info("📊 **Halaman 1: Data Historis**\n\nLihat bukti nyata korelasi harga antara Bitcoin vs Emas vs IHSG (Validasi Bab 4).")

with col_b:
    st.warning("🧪 **Halaman 2: Lab Eksperimen**\n\nIntip dapur rekaman hasil pelatihan model LSTM yang bervariasi (Bukti Sifat Stokastik).")

with col_c:
    st.success("🏆 **Halaman 3: Final Dashboard**\n\nLihat hasil prediksi terbaik (Best Model) dan kesimpulan akhir penelitian.")