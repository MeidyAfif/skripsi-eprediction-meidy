import streamlit as st
from PIL import Image
import os

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Final Dashboard", page_icon="🏆", layout="wide")

st.title("🏆 Final Dashboard: Hasil Prediksi Terbaik")
st.markdown("Visualisasi perbandingan performa model pada Data Testing (30% Data Terakhir).")
st.markdown("---")

# --- 2. SCORE CARD ---
col1, col2, col3, col4 = st.columns(4)
with col1: st.metric("Status Model", "Final Result", "ARIMA Unggul")
with col2: st.metric("MAPE ARIMA", "1.84%", "Sangat Presisi")
with col3: st.metric("MAPE LSTM", "3.09%", "Akurasi Tinggi (Terbaik)")
with col4: st.metric("RMSE LSTM", "$3,308.57", "Nominal Error")

# --- 3. LOGIKA PENCARI GAMBAR (VERSI DETEKTIF GANDA) ---
st.subheader("📈 Grafik Perbandingan: Aktual vs Prediksi")

# Daftar kemungkinan nama file (Besar & Kecil)
possible_names = ["grafik_final.png", "Grafik_Final.png"]
image_path = None

# Cari di berbagai folder
for name in possible_names:
    # Cek di folder saat ini, parent, dan folder repo
    paths_to_check = [name, f"../{name}", f"Skripsi_Meidy/{name}"]
    
    for path in paths_to_check:
        if os.path.exists(path):
            image_path = path
            break
    if image_path: break # Kalau sudah ketemu, berhenti mencari

# Tampilkan Gambar
if image_path:
    try:
        image = Image.open(image_path)
        st.image(image, caption="Gambar 4.19: Visualisasi Hasil Prediksi", use_container_width=True)
    except Exception as e:
        st.error(f"Gagal membuka gambar: {e}")
else:
    st.error("⚠️ FILE GAMBAR TIDAK DITEMUKAN!")
    st.warning("Sistem sudah mencari 'grafik_final.png' dan 'Grafik_Final.png' tapi tidak ketemu di folder manapun.")

# --- 4. INTERPRETASI ---
st.markdown("---")
with st.expander("📝 Penjelasan Analisis (Sesuai Bab 4.3)", expanded=True):
    st.markdown("""
    **Interpretasi Hasil Visual:**
    1. **Garis Oranye (Harga Asli):** Menunjukkan pergerakan harga pasar yang fluktuatif (Volatile).
    2. **Garis Merah Putus-putus (ARIMA):** Sangat responsif menempel harga asli.
    3. **Garis Hijau (LSTM):** Menunjukkan pola kurva yang lebih halus (*smooth*) namun sukses mengikuti tren kenaikan besar.
    """)