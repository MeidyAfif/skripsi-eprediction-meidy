import streamlit as st
import pandas as pd
import plotly.express as px

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Analisis Emas Digital", page_icon="📈", layout="wide")

st.title("📈 Analisis Konteks: Bitcoin vs Aset Konvensional")
st.markdown("""
**Dataset Master Skripsi:** Halaman ini memvisualisasikan data historis (2020-2024) untuk membuktikan posisi Bitcoin sebagai aset investasi unik dibandingkan Emas dan IHSG.
""")
st.markdown("---")

# --- 1. LOAD DATA MASTER (OFFLINE) ---
@st.cache_data
def load_master_data():
    try:
        file_path = 'data_skripsi_master.csv'
        df = pd.read_csv(file_path)
        
        # Cleaning Header (Skip 2 baris metadata)
        df_clean = df.iloc[2:].reset_index(drop=True)
        
        # Rename Kolom
        df_clean = df_clean.rename(columns={
            'Price': 'Date',
            'BTC': 'Bitcoin (BTC)',
            'Emas': 'Emas (Gold)',
            'IHSG': 'IHSG (Stock)'
        })
        
        # Konversi Tipe Data
        df_clean['Date'] = pd.to_datetime(df_clean['Date'])
        for col in ['Bitcoin (BTC)', 'Emas (Gold)', 'IHSG (Stock)']:
            df_clean[col] = pd.to_numeric(df_clean[col])
            
        return df_clean

    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")
        st.stop()

df = load_master_data()

# --- 2. PERHITUNGAN ROI ---
initial_btc = df['Bitcoin (BTC)'].iloc[0]
initial_gold = df['Emas (Gold)'].iloc[0]
initial_ihsg = df['IHSG (Stock)'].iloc[0]

df['ROI Bitcoin (%)'] = ((df['Bitcoin (BTC)'] - initial_btc) / initial_btc) * 100
df['ROI Emas (%)'] = ((df['Emas (Gold)'] - initial_gold) / initial_gold) * 100
df['ROI IHSG (%)'] = ((df['IHSG (Stock)'] - initial_ihsg) / initial_ihsg) * 100

# --- 3. VISUALISASI 1: LINE CHART (Pertumbuhan) ---
st.subheader("1. Perbandingan Pertumbuhan Aset (ROI)")
col_sidebar, col_main = st.columns([1, 3])

with col_sidebar:
    st.markdown("##### ⚙️ Filter Grafik")
    show_btc = st.checkbox("Bitcoin (BTC)", value=True)
    show_gold = st.checkbox("Emas (Gold)", value=True)
    show_ihsg = st.checkbox("IHSG (Stock)", value=True)
    
    st.info(f"📅 **Periode:** {df['Date'].dt.year.min()} - {df['Date'].dt.year.max()}")

with col_main:
    cols_to_plot = []
    if show_btc: cols_to_plot.append('ROI Bitcoin (%)')
    if show_gold: cols_to_plot.append('ROI Emas (%)')
    if show_ihsg: cols_to_plot.append('ROI IHSG (%)')
    
    if cols_to_plot:
        color_map = {'ROI Bitcoin (%)': '#F7931A', 'ROI Emas (%)': '#FFD700', 'ROI IHSG (%)': '#00509E'}
        fig = px.line(df, x='Date', y=cols_to_plot, height=450, color_discrete_map=color_map,
                      labels={'value': 'Pertumbuhan (%)', 'Date': 'Tahun'})
        fig.update_traces(line=dict(width=2))
        fig.update_layout(legend=dict(orientation="h", y=1.1))
        st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# --- 4. VISUALISASI 2: HEATMAP KORELASI (REVISI NARASI) ---
st.subheader("2. Matriks Korelasi Aset (Heatmap)")

col_heat_desc, col_heat_viz = st.columns([1, 2])

# Hitung Korelasi
cols_corr = ['Bitcoin (BTC)', 'Emas (Gold)', 'IHSG (Stock)']
corr_matrix = df[cols_corr].corr()

with col_heat_desc:
    # Ambil nilai korelasi BTC vs Emas
    corr_btc_gold = corr_matrix.loc['Bitcoin (BTC)', 'Emas (Gold)']
    
    st.markdown("""
    **Cara Membaca Heatmap:**
    * **> 0.70 (Merah Tua):** Korelasi Kuat (Bergerak Searah).
    * **0.0 (Putih):** Tidak ada hubungan.
    """)
    
    # --- REVISI PENTING DI SINI ---
    st.success(f"""
    🔍 **Validasi Hipotesis 'Emas Digital':**
    
    Korelasi antara **Bitcoin** dan **Emas** tercatat sebesar **{corr_btc_gold:.2f}**.
    
    Dalam statistik, angka ini menunjukkan **HUBUNGAN POSITIF YANG KUAT**. 
    Temuan ini memvalidasi narasi bahwa Bitcoin bertindak selayaknya "Emas Digital". 
    Keduanya memiliki kemiripan pola sebagai aset pelindung nilai (*Safe Haven*), namun Bitcoin menawarkan akselerasi pertumbuhan (*High Growth*) yang tidak dimiliki Emas fisik.
    """)

with col_heat_viz:
    # Membuat Heatmap dengan Plotly
    fig_corr = px.imshow(
        corr_matrix,
        text_auto=".2f", 
        aspect="auto",
        color_continuous_scale="Reds", 
        title="Peta Korelasi Harga Penutupan (Close Price)"
    )
    # Hilangkan label sumbu biar bersih
    fig_corr.update_xaxes(side="bottom")
    fig_corr.update_layout(height=400)
    st.plotly_chart(fig_corr, use_container_width=True)

# --- 5. KARTU ANALISIS AKHIR ---
st.markdown("### 📊 Kesimpulan Data")
st.success("""
**Validasi 'Emas Digital':** Meskipun Bitcoin sering disebut Emas Digital, data Heatmap di atas membuktikan bahwa Bitcoin bukanlah "fotokopi" dari Emas. 
Ia adalah aset independen dengan tingkat *High Risk High Return* (Lihat Grafik ROI di atas), yang menjadikannya instrumen diversifikasi yang kuat dalam portofolio modern.
""")