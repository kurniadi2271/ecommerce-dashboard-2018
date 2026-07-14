import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Pengaturan dasar halaman dashboard
st.set_page_config(page_title="E-Commerce 2018 Dashboard", layout="wide")

# 1. Judul Dashboard
st.title("📊 E-Commerce Business Performance Dashboard (2018)")
st.markdown("Dashboard interaktif untuk memantau performa bisnis dan kepuasan pelanggan sepanjang tahun 2018.")
st.markdown("---")

# Load data yang sudah kita simpan sebelumnya
df_reviews = pd.read_csv('dashboard/dashboard_reviews_2018.csv')
df_categories = pd.read_csv('dashboard/dashboard_top_10_categories.csv')

# Membagi halaman menjadi 2 Kolom berdampingan
col1, col2 = st.columns(2)

# ------------------------------------------------------------------
# KOLOM 1: TREN KEPUASAN PELANGGAN
# ------------------------------------------------------------------
with col1:
    st.subheader("📈 Tren Kepuasan Pelanggan (Rating)")
    
    # Membuat visualisasi dengan matplotlib
    fig, ax = plt.subplots(figsize=(8, 5))
    
    # Mengurutkan bulan agar kronologis
    df_reviews['month'] = pd.to_datetime(df_reviews['month']).dt.to_period('M')
    eda_reviews = df_reviews.groupby('month')['review_score'].mean().reset_index()
    eda_reviews['month_str'] = eda_reviews['month'].astype(str)
    
    sns.lineplot(
        data=eda_reviews, 
        x='month_str', 
        y='review_score', 
        marker='o', 
        color='#1f77b4', 
        ax=ax
    )
    ax.set_ylim(3.5, 4.5)
    ax.set_ylabel("Rata-rata Rating")
    ax.set_xlabel("Bulan")
    plt.xticks(rotation=45)
    
    # Tampilkan di Streamlit
    st.pyplot(fig)
    st.info("💡 **Insight:** Terjadi penurunan kepuasan konsumen yang cukup signifikan pada bulan Maret 2018 (3.73).")

# ------------------------------------------------------------------
# KOLOM 2: TOP KATEGORI PRODUK
# ------------------------------------------------------------------
with col2:
    st.subheader("💰 Top 10 Kategori Produk Terlaris")
    
    # Membuat visualisasi batang horizontal
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(
        data=df_categories, 
        x='total_pendapatan', 
        y='product_category_name', 
        palette='Blues_r', 
        ax=ax
    )
    ax.set_xlabel("Total Pendapatan (USD)")
    ax.set_ylabel("Kategori Produk")
    
    # Tampilkan di Streamlit
    st.pyplot(fig)
    st.info("💡 **Insight:** Kategori *beleza_saude* (Kecantikan) menyumbang pendapatan tertinggi, disusul oleh *relogios_presentes*.")