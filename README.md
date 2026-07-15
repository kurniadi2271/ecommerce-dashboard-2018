# 📊 E-Commerce Dashboard 2018

Dashboard interaktif untuk menganalisis performa bisnis dan kepuasan pelanggan berbasis data E-Commerce 2018.

## ✨ Fitur Utama
- Visualisasi tren kepuasan pelanggan
- Analisis top kategori produk terlaris
- Filter interaktif berdasarkan rentang tanggal
- Tampilan dashboard yang responsif dan modern

## 🛠️ Persiapan Environment

### Menggunakan Anaconda
```bash
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```

### Menggunakan Virtual Environment Python
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## ▶️ Menjalankan Dashboard
```bash
streamlit run dashboard/app.py
```

Setelah aplikasi berjalan, buka URL berikut di browser:
```text
http://localhost:8501
```

## 📁 Struktur Project
```text
dashboard/
  app.py
  dashboard_reviews_2018.csv
  dashboard_top_10_categories.csv
data/
  order_items_dataset.csv
  order_reviews_dataset.csv
  products_dataset.csv
```

## 📌 Catatan
Pastikan semua dependensi terinstall sebelum menjalankan aplikasi agar dashboard berjalan dengan baik.
