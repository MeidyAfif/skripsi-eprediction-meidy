import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Proses Modeling", page_icon="⚙️", layout="wide")

st.title("⚙️ Arsitektur & Proses Modeling")
st.markdown("""
Halaman ini menjelaskan transparansi metode **Data Splitting** dan **Hyperparameter Tuning** yang digunakan untuk membangun model LSTM dan ARIMA sesuai Bab 3 dan 4.
""")
st.markdown("---")

# --- 1. LOAD DATA MASTER ---
@st.cache_data
def load_data():
    try:
        # Baca file master (Skip 2 baris metadata)
        df = pd.read_csv('data_skripsi_master.csv', header=2)
        df.columns = ['Date', 'BTC', 'Emas', 'IHSG'] # Rename simpel
        df['Date'] = pd.to_datetime(df['Date'])
        
        # Pastikan numerik
        for col in ['BTC', 'Emas', 'IHSG']:
            df[col] = pd.to_numeric(df[col], errors='coerce')
            
        return df
    except Exception as e:
        st.error(f"Gagal memuat data: {e}")
        st.stop()

df = load_data()

# --- 2. SKENARIO SPLITTING DATA ---
st.subheader("1. Skenario Pembagian Data (Train-Test Split)")

# Logika: Data Testing adalah 548 hari terakhir (Sesuai Bab 4)
test_size = 548
train_size = len(df) - test_size
split_date = df['Date'].iloc[train_size]

# Pisahkan Data
train_data = df.iloc[:train_size]
test_data = df.iloc[train_size:]

# Tampilkan Metrik
c1, c2, c3 = st.columns(3)
with c1:
    st.info(f"📊 **Total Dataset:** {len(df)} Hari")
with c2:
    st.success(f"📘 **Data Latih (Training):** {len(train_data)} Hari\n\n(Jan 2020 - {split_date.strftime('%b %Y')})")
with c3:
    st.warning(f"📙 **Data Uji (Testing):** {len(test_data)} Hari\n\n({split_date.strftime('%b %Y')} - Des 2024)")

# VISUALISASI SPLITTING
fig = go.Figure()

# Plot Training (Biru)
fig.add_trace(go.Scatter(
    x=train_data['Date'], y=train_data['BTC'],
    mode='lines', name='Training Data (Pembelajaran)',
    line=dict(color='#00509E', width=1.5)
))

# Plot Testing (Merah/Orange)
fig.add_trace(go.Scatter(
    x=test_data['Date'], y=test_data['BTC'],
    mode='lines', name='Testing Data (Pengujian)',
    line=dict(color='#F7931A', width=1.5)
))

fig.update_layout(
    title="Visualisasi Pemotongan Data (Cut-Off)",
    xaxis_title="Tahun",
    yaxis_title="Harga Bitcoin (USD)",
    legend=dict(orientation="h", y=1.1),
    height=450
)
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# --- 3. PARAMETER MODEL (HASIL TUNING) ---
st.subheader("2. Konfigurasi Hyperparameter Terbaik")
st.markdown("Parameter ini ditetapkan berdasarkan hasil analisis plot **ACF/PACF** dan uji coba **Grid Search**.")

col_lstm, col_arima = st.columns(2)

# --- PANEL KIRI: LSTM ---
with col_lstm:
    with st.container(border=True):
        st.markdown("### 🧠 LSTM (Deep Learning)")
        st.caption("Arsitektur Jaringan Saraf Tiruan:")
        
        # Buat Dataframe Parameter LSTM
        params_lstm = {
            "Komponen": ["Hidden Layers", "Neurons per Layer", "Epochs", "Batch Size", "Optimizer", "Loss Function"],
            "Konfigurasi": ["2 Layers (Stacked)", "50 Neurons", "50", "32", "Adam", "MSE"]
        }
        st.table(pd.DataFrame(params_lstm).set_index("Komponen"))
        
        st.info("💡 **Alasan:** Epoch 50 dipilih karena grafik Loss sudah konvergen (stabil) dan mencegah overfitting.")

# --- PANEL KANAN: ARIMA ---
with col_arima:
    with st.container(border=True):
        st.markdown("### 📈 ARIMA (Statistical)")
        st.caption("Parameter Order (p, d, q):")
        
        # --- SESUAI SKRIPSI (1,1,1) ---
        st.metric("Best Model", "ARIMA (1, 1, 1)", delta="Berdasarkan Grid Search")
        
        st.markdown("""
        **Penjelasan Parameter:**
        * **p (AutoRegressive) = 1**: Menggunakan 1 lag waktu (harga kemarin) sebagai prediktor utama.
        * **d (Integrated) = 1**: Dipilih karena data asli memiliki tren **tidak stasioner**, sehingga memerlukan 1x proses *differencing*.
        * **q (Moving Average) = 1**: Mengoreksi prediksi menggunakan 1 lag error masa lalu.
        """)
        
        st.success("✅ Konfigurasi ini terpilih karena memiliki nilai AIC/BIC terendah dan lolos uji signifikansi.")

# --- 4. DATA PREVIEW (FULL DATASET 1826) ---
st.markdown("---")
st.subheader("3. Dataset Penelitian Lengkap (Transparansi)")

# --- FUNGSI FORMATTER INDONESIA ---
def format_indo(x):
    # Mengubah format 1234.56 jadi 1.234,56
    return "{:,.2f}".format(x).replace(",", "X").replace(".", ",").replace("X", ".")

# Gunakan 'df' (Full Data) bukan 'train_data'
df_display = df[['Date', 'BTC', 'Emas', 'IHSG']].copy()

# 1. Format Tanggal jadi 'DD-MM-YYYY'
df_display['Date'] = df_display['Date'].dt.strftime('%d-%m-%Y')

# 2. Format Angka jadi Format Indonesia (String)
df_display['BTC'] = df_display['BTC'].apply(format_indo)
df_display['Emas'] = df_display['Emas'].apply(format_indo)
df_display['IHSG'] = df_display['IHSG'].apply(format_indo)

# 3. Rename Kolom biar makin jelas
df_display.columns = ['Tanggal', 'Bitcoin (USD)', 'Emas (USD)', 'IHSG (IDR)']

with st.expander(f"🔍 Klik untuk melihat Full Dataset ({len(df)} Baris Data)", expanded=True):
    # Tampilkan SEMUA data (1826 baris)
    st.dataframe(
        df_display, 
        use_container_width=True, 
        hide_index=True, 
        height=500 # Agak tinggi dikit biar enak scrollnya
    )
    st.caption("Menampilkan seluruh data historis yang digunakan dalam penelitian ini (Training + Testing).")