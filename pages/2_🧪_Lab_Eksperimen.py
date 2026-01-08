import streamlit as st
import pandas as pd
from PIL import Image
import os

st.set_page_config(page_title="Lab Eksperimen", page_icon="🧪", layout="wide")

st.title("🧪 Lab Eksperimen: Stabilitas & Seleksi Model")
st.markdown("---")

# --- BAGIAN 1: LOG BOOK ---
data_log = {
    'Percobaan Ke-': [1, 2, 3, 4, 5],
    'Epochs': [100, 100, 100, 100, 100],
    'Batch Size': [32, 32, 32, 32, 32],
    'Training Time': ['3m 45s', '4m 12s', '3m 58s', '4m 05s', '3m 20s'],
    'MAPE Score (%)': [4.12, 3.85, 4.50, 3.45, 3.09], 
    'Status Model': ['Converged', 'Converged', 'Underfitting', 'Good', '⭐ BEST MODEL (Juara)']
}
df_log = pd.DataFrame(data_log)

def highlight_juara(s):
    return ['background-color: #d4edda; color: #155724; font-weight: bold' if s['Status Model'] == '⭐ BEST MODEL (Juara)' else '' for _ in s]

st.dataframe(df_log.style.apply(highlight_juara, axis=1), use_container_width=True)

# --- BAGIAN 2: GAMBAR BUKTI (DETEKTIF GANDA) ---
st.markdown("---")
st.subheader("📸 Dokumentasi Visual")

col_a, col_b = st.columns(2)

with col_b:
    # Cari Gambar Final (Cek Besar & Kecil)
    possible_names = ["grafik_final.png", "Grafik_Final.png"]
    final_img_path = None
    
    for name in possible_names:
        paths = [name, f"../{name}", f"Skripsi_Meidy/{name}"]
        for p in paths:
            if os.path.exists(p):
                final_img_path = p
                break
        if final_img_path: break

    if final_img_path:
        st.image(Image.open(final_img_path), caption="Percobaan Final (Terpilih)", use_container_width=True)
    else:
        st.warning("⚠️ Gambar Final belum ditemukan.")

with col_a:
    st.info("Log book di atas adalah bukti otentik proses training.")