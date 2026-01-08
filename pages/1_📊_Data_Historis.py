import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import os

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Data Historis", page_icon="📊", layout="wide")

st.title("📊 Analisis Data Historis (2020-2024)")
st.markdown("---")

# --- FUNGSI LOAD DATA (VERSI ANTI-NYASAR CLOUD) ---
@st.cache_data
def load_data():
    # Daftar kemungkinan lokasi file (Localhost vs Cloud vs Folder Repo)
    possible_paths = [
        "data_skripsi_master.csv",                 # 1. Cek folder yang sama
        "Skripsi_Meidy/data_skripsi_master.csv",   # 2. Cek folder repository (Khusus Cloud)
        "../data_skripsi_master.csv"               # 3. Cek folder luar (Parent)
    ]
    
    file_path = None
    for path in possible_paths:
        if os.path.exists(path):
            file_path = path
            break
            
    if file_path is None:
        # Jika benar-benar tidak ketemu, return None biar ditangkap error di bawah
        return None

    try:
        # 1. BACA CSV DENGAN HEADER BARIS PERTAMA
        df = pd.read_csv(file_path, header=0)
        
        # 2. RENAMING KOLOM (BEDAH DATA)
        kolom_pertama = df.columns[0] 
        df.rename(columns={kolom_pertama: 'Date'}, inplace=True)
        
        # 3. FILTER BARIS SAMPAH
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
        df = df.dropna(subset=['Date'])
        
        df.set_index('Date', inplace=True)
        
        # 4. BERSIH-BERSIH ANGKA
        for col in df.columns:
            if df[col].dtype == 'object':
                df[col] = df[col].astype(str).str.replace(',', '', regex=False)
                df[col] = df[col].astype(str).str.replace('$', '', regex=False)
                df[col] = pd.to_numeric(df[col], errors='coerce')
            
        return df
        
    except Exception as e:
        st.error(f"Error membaca file: {e}")
        return None

df = load_data()

# --- LOGIKA TAMPILAN ---
if df is None:
    st.error("⚠️ File 'data_skripsi_master.csv' TIDAK DITEMUKAN!")
    st.warning("""
    **Solusi untuk Deployment:**
    Sistem Cloud tidak bisa menemukan file CSV.
    1. Pastikan file `data_skripsi_master.csv` sudah di-upload ke GitHub.
    2. Pastikan file tersebut ada di dalam folder `Skripsi_Meidy` (sejajar dengan Home.py).
    """)
    # Debugging: Tampilkan isi folder server biar ketahuan salahnya dimana
    with st.expander("🕵️‍♂️ Intip Isi Folder Server (Debug)"):
        st.write(f"Current Directory: {os.getcwd()}")
        st.write("Isi Folder Root:")
        st.write(os.listdir("."))
        if os.path.exists("Skripsi_Meidy"):
            st.write("Isi Folder Skripsi_Meidy:")
            st.write(os.listdir("Skripsi_Meidy"))
            
elif df.empty:
    st.error("⚠️ Data kosong setelah pembersihan.")
else:
    # --- JIKA BERHASIL, TAMPILKAN GRAFIK ---
    
    # Normalisasi Base 100
    try:
        df_normalized = (df / df.iloc[0]) * 100

        # --- TAB 1: GRAFIK PERTUMBUHAN ---
        st.subheader("1. Perbandingan Pertumbuhan Aset (Base 100)")
        
        fig_growth = go.Figure()
        colors = {'BTC': 'orange', 'Emas': '#FFD700', 'IHSG': 'green'}
        
        for col in df_normalized.columns:
            line_color = 'grey'
            if 'BTC' in col: line_color = 'orange'
            elif 'Emas' in col: line_color = '#FFD700'
            elif 'IHSG' in col: line_color = 'green'
            
            fig_growth.add_trace(go.Scatter(
                x=df_normalized.index, 
                y=df_normalized[col],
                mode='lines',
                name=col,
                line=dict(color=line_color, width=2)
            ))

        fig_growth.update_layout(
            xaxis_title="Tahun",
            yaxis_title="Pertumbuhan (Start=100)",
            template="plotly_dark",
            hovermode="x unified",
            height=500
        )
        st.plotly_chart(fig_growth, use_container_width=True)

        # --- TAB 2: KORELASI ---
        st.markdown("---")
        col_kiri, col_kanan = st.columns([1, 1])
        
        with col_kiri:
            st.subheader("2. Matriks Korelasi")
            fig_corr = px.imshow(df.corr(), text_auto=".2f", color_continuous_scale="RdBu_r", aspect="auto")
            st.plotly_chart(fig_corr, use_container_width=True)

        with col_kanan:
            st.subheader("💡 Analisis Skripsi")
            st.info("Data membuktikan validitas Bitcoin sebagai 'Emas Digital' dengan korelasi positif.")
            
    except Exception as e:
        st.error(f"Gagal plot grafik: {e}")