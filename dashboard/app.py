import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Pengaturan dasar halaman dashboard
st.set_page_config(page_title="E-Commerce 2018 Dashboard", layout="wide")

# 1. Judul Dashboard
st.title("📊 E-Commerce Business Performance Dashboard (2018)")
st.markdown("Dashboard interaktif untuk memantau performa bisnis dan kepuasan pelanggan sepanjang tahun 2018.")
st.markdown("---")

# Load data yang sudah kita simpan sebelumnya
base_dir = Path(__file__).resolve().parent

df_reviews = pd.read_csv(base_dir / "dashboard_reviews_2018.csv")
df_categories = pd.read_csv(base_dir / "dashboard_top_10_categories.csv")

# Konversi kolom tanggal agar bisa difilter
if "review_creation_date" in df_reviews.columns:
    df_reviews["review_creation_date"] = pd.to_datetime(df_reviews["review_creation_date"], errors="coerce")

# Sidebar untuk filter interaktif
st.sidebar.header("🔎 Filter Data")
min_date = df_reviews["review_creation_date"].min().date()
max_date = df_reviews["review_creation_date"].max().date()

start_date, end_date = st.sidebar.date_input(
    "Pilih rentang tanggal ulasan",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date,
)

if start_date and end_date and start_date > end_date:
    st.sidebar.error("Tanggal awal tidak boleh lebih besar dari tanggal akhir.")
    st.stop()

filtered_reviews = df_reviews[
    (df_reviews["review_creation_date"].dt.date >= start_date)
    & (df_reviews["review_creation_date"].dt.date <= end_date)
].copy()

st.sidebar.caption(f"Menampilkan {len(filtered_reviews)} ulasan dari rentang {start_date} sampai {end_date}.")

# Membagi halaman menjadi 2 Kolom berdampingan
col1, col2 = st.columns(2)

# ------------------------------------------------------------------
# KOLOM 1: TREN KEPUASAN PELANGGAN
# ------------------------------------------------------------------
with col1:
    st.subheader("📈 Tren Kepuasan Pelanggan (Rating)")

    if filtered_reviews.empty:
        st.warning("Tidak ada data untuk rentang tanggal yang dipilih.")
    else:
        # Membuat visualisasi dengan matplotlib
        fig, ax = plt.subplots(figsize=(8, 5))

        # Mengurutkan bulan agar kronologis
        filtered_reviews["month"] = filtered_reviews["review_creation_date"].dt.to_period("M")
        eda_reviews = filtered_reviews.groupby("month")["review_score"].mean().reset_index()
        eda_reviews["month_str"] = eda_reviews["month"].astype(str)

        sns.lineplot(
            data=eda_reviews,
            x="month_str",
            y="review_score",
            marker="o",
            color="#1f77b4",
            ax=ax,
        )
        ax.set_ylim(3.5, 5.0)
        ax.set_ylabel("Rata-rata Rating")
        ax.set_xlabel("Bulan")
        plt.xticks(rotation=45)

        # Tampilkan di Streamlit
        st.pyplot(fig)
        st.info("💡 **Insight:** Perubahan rating akan otomatis menyesuaikan ketika rentang tanggal diubah.")

# ------------------------------------------------------------------
# KOLOM 2: TOP KATEGORI PRODUK
# ------------------------------------------------------------------
with col2:
    st.subheader("💰 Top 10 Kategori Produk Terlaris")

    # Membuat visualisasi batang horizontal
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(
        data=df_categories,
        x="total_pendapatan",
        y="product_category_name",
        palette="Blues_r",
        ax=ax,
    )
    ax.set_xlabel("Total Pendapatan (USD)")
    ax.set_ylabel("Kategori Produk")

    # Tampilkan di Streamlit
    st.pyplot(fig)
    st.info("💡 **Insight:** Kategori *beleza_saude* (Kecantikan) menyumbang pendapatan tertinggi, disusul oleh *relogios_presentes*.")