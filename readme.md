# 🚀 LegalAI CBR: Analisis Tindak Pidana Narkotika

**Implementasi Sistem Legal AI Berbasis Case-Based Reasoning untuk Analisis Tindak Pidana Narkotika**

# Pipeline Scraping dan Ekstraksi Data Putusan Narkoba

Notebook ini berfungsi untuk melakukan scraping data putusan terkait kasus narkoba, mengunduh file PDF putusan, dan mengekstrak isi dari file PDF tersebut. Proyek ini dirancang untuk berjalan secara _end-to-end_ di Google Colab, mulai dari pencarian data, pengambilan file, hingga penyimpanan hasil dalam format CSV.

## Bahasa
Dokumentasi ini menggunakan Bahasa Indonesia.

---

## Struktur Proyek

```
.
├── TAHAP1_5.ipynb
├── requirements.txt
└── README.md
```

---

## Kebutuhan Sistem

- Python ≥ 3.8
- Google Colab
- Akses ke Google Drive (untuk penyimpanan file)

---

## Instalasi (Jika ingin dijalankan di lokal)

1. **Clone repository** (jika menggunakan repo Git):
   ```bash
   git clone https://github.com/username/repo-nama.git
   cd repo-nama
   ```

2. **Buat virtual environment (opsional tapi disarankan)**:
   ```bash
   python -m venv env
   source env/bin/activate  # Linux/Mac
   env\Scripts\activate   # Windows
   ```

3. **Install dependensi**:
   ```bash
   pip install -r requirements.txt
   ```

---

## Menjalankan Pipeline di Google Colab

1. Upload file `TAHAP1_5.ipynb` ke Google Colab.
2. Jalankan sel pertama untuk mount Google Drive:
   ```python
   from google.colab import drive
   drive.mount('/content/drive')
   ```
3. Jalankan seluruh sel dari atas ke bawah (Ctrl+F9 atau klik menu Runtime > Run all).
4. Hasil scraping dan ekstraksi akan tersimpan di:
   ```
   /content/drive/MyDrive/CSV/
   /content/drive/MyDrive/PDF/
   ```

---

## Fungsi Utama Pipeline

- Scraping dari situs sumber berdasarkan kata kunci (`keyword`).
- Penyimpanan daftar putusan ke file `.csv`.
- Download file PDF putusan hukum.
- Ekstraksi teks dari PDF menggunakan `pdfminer.six`.
- Penyimpanan hasil ekstraksi ke format CSV.

---

## Contoh Output

- `putusan_narkoba_2025-06-20.csv` – hasil scraping dan ekstraksi.
- PDF dokumen hukum di folder `/PDF/` di Google Drive.

---

## Catatan

- Pastikan Anda memiliki ruang cukup di Google Drive karena PDF bisa cukup besar.
- Gunakan koneksi stabil saat menjalankan proses download dan ekstraksi.
- Beberapa file PDF mungkin gagal diekstrak tergantung strukturnya.

---


