# Final Project: Sistem Pengukuran Sinyal Respirasi dan rPPG

## Deskripsi Proyek

Proyek ini bertujuan untuk menggabungkan sistem pengukuran sinyal respirasi dan
remote-photopletysmography (rPPG) menggunakan Python. Program ini memanfaatkan
video real-time dari webcam untuk mengekstrak dan memvisualisasikan kedua sinyal tersebut.
Teknologi ini dapat digunakan dalam aplikasi kesehatan seperti pemantauan pernapasan
dan detak jantung tanpa kontak.

### Fitur Utama

- Ekstraksi sinyal respirasi dengan filter band-pass.
- Ekstraksi sinyal rPPG berbasis channel hijau (green channel).
- Visualisasi real-time menggunakan matplotlib.

---

## Instalasi

### Persyaratan Sistem

- Python 3.7 atau lebih baru
- Webcam yang berfungsi

<!-- ### Langkah Instalasi
1. Clone repository ini:
   ```bash
   git clone https://github.com/hafiz-dev1/TUBES-DSP.git
   ```
2. Pindah ke direktori proyek:
   ```bash
   cd src
   ```
3. Buat virtual environment (opsional):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Untuk Linux/MacOS
   venv\Scripts\activate    # Untuk Windows
   ```
4. Instal dependencies:
   ```bash
   pip install -r requirements.txt
   ```

--- -->

## Cara Penggunaan

1. Jalankan program utama:
   ```bash
   python src/main.py
   ```
2. Program akan membuka feed webcam dan memproses frame secara real-time.
3. Tekan tombol `q` pada keyboard untuk menghentikan program.

---

## Struktur Direktori

```
final_project_signal/
├── src/
│   ├── main.py          # Program utama
│   ├── respiration.py   # Modul untuk sinyal respirasi
│   ├── rppg.py          # Modul untuk sinyal rPPG
│   └── utils.py         # Fungsi utilitas
├── requirements.txt      # Daftar dependencies
├── readme.md             # Dokumentasi proyek
└── report.pdf            # Laporan teknis
```

---

## Logbook Mingguan

## Kontributor

- **Nama**: Hafiz Amrullah
- **NIM**: 119140177
- **GitHub**: [hafiz-dev1](https://github.com/hafiz-dev1)
