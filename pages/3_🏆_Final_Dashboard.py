import streamlit as st
from PIL import Image
import os

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="Final Dashboard", 
    page_icon="🏆", 
    layout="wide"
)

# --- 2. JUDUL & HEADER ---
st.title("🏆 Final Dashboard: Hasil Prediksi Terbaik")
st.markdown("Visualisasi perbandingan performa model pada Data Testing (30% Data Terakhir).")
st.markdown("---")

# --- 3. SCORE CARD (METRIK SKRIPSI) ---
# Angka ini di-hardcode sesuai hasil terbaik di Bab 4 kamu
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="Status Model", value="Final Result", delta="ARIMA Unggul")

with col2:
    st.metric(label="MAPE ARIMA", value="1.84%", delta="Sangat Presisi", delta_color="normal")

with col3:
    st.metric(label="MAPE LSTM", value="3.09%", delta="Akurasi Tinggi (Terbaik)", delta_color="normal")

with col4:
    st.metric(label="RMSE LSTM", value="$3,308.57", delta="Nominal Error")

# --- 4. TAMPILAN GRAFIK (LOGIKA PENCARI GAMBAR PINTAR) ---
st.subheader("📈 Grafik Perbandingan: Aktual vs Prediksi")

# Nama file gambar yang dicari
target_image = "grafik_final.png"

# Logika: Cari di folder saat ini ATAU folder di atasnya (parent)
image_path = None
if os.path.exists(target_image):
    image_path = target_image                 # Ada di folder pages (jarang terjadi)
elif os.path.exists(f"../{target_image}"):
    image_path = f"../{target_image}"         # Ada di folder utama (Skripsi_Meidy) - INI YANG BIASANYA BENAR
elif os.path.exists(f"Skripsi_Meidy/{target_image}"):
    image_path = f"Skripsi_Meidy/{target_image}" # Coba cari spesifik

# Tampilkan Gambar
if image_path:
    try:
        image = Image.open(image_path)
        st.image(image, caption="Gambar 4.19: Visualisasi Hasil Prediksi (Sumber: Olah Data Python)", use_container_width=True)
    except Exception as e:
        st.error(f"Gagal membuka gambar. Error: {e}")
else:
    # Pesan Error yang Membantu
    st.error("⚠️ FILE GAMBAR TIDAK DITEMUKAN!")
    st.warning(f"""
    **Sistem tidak bisa menemukan file `{target_image}`.**
    
    **Solusi:**
    1. Pastikan kamu sudah menaruh file gambar grafik 3.09% di folder utama proyek (sejajar dengan `Home.py`).
    2. Pastikan namanya persis: **`grafik_final.png`** (huruf kecil semua).
    """)

# --- 5. INTERPRETASI HASIL (BAB 4) ---
st.markdown("---")
with st.expander("📝 Penjelasan Analisis", expanded=True):
    st.markdown("""
    **Interpretasi Hasil Visual:**
    1. **Garis Oranye (Harga Asli):** Menunjukkan pergerakan harga pasar yang fluktuatif (Volatile).
    2. **Garis Merah Putus-putus (ARIMA):** Sangat responsif (agresif) menempel harga asli karena update harian.
    3. **Garis Hijau (LSTM):** Menunjukkan pola kurva yang lebih halus (*smooth*) namun sukses mengikuti tren kenaikan besar (*bull run*) tanpa kehilangan arah.
    
    **Kesimpulan:**
    LSTM terbukti mampu memprediksi tren jangka panjang dengan error **3.09%**, membuktikan validitasnya sebagai alat bantu investasi modern.
    """)