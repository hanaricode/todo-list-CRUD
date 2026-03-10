# 📝 Tentang

 Aplikasi manajemen tugas berbasis terminal yang dibuat dengan Python (bersifat tidak tersimpan).

## 🚀 Fitur

- **Lihat Tugas** — Menampilkan semua tugas beserta deskripsi, status, dan estimasi waktu
- **Tambah Tugas** — Menambahkan tugas baru dengan judul, deskripsi, status, dan estimasi waktu
- **Tandai Selesai** — Mengubah status tugas menjadi "Selesai" berdasarkan ID
- **Hapus Tugas** — Menghapus tugas dari daftar berdasarkan ID

---

## 🛠️ Teknologi

- Python 3.11.9
- Modul bawaan: `unittest`, `io`, `unittest.mock`

---

## 📂 Struktur File

```
📁 todo-list/
├── script.py                    # File utama program
├── test_tambah_tugas.py         # Unit test fungsi tambah tugas
├── test_tandai_selesai.py       # Unit test fungsi tandai selesai
├── test_lihat_tugas.py          # Unit test fungsi lihat tugas
├── test_hapus_tugas.py          # Unit test fungsi hapus tugas
└── README.md
```

## 📖 Cara Menggunakan

Setelah program dijalankan, akan muncul menu seperti berikut:

```
Selamat Datang di Aplikasi To-Do List
1. Lihat Semua Tugas
2. Tambah Tugas
3. Tandai Tugas Selesai
4. Hapus Tugas
5. Keluar
Masukkan pilihan Anda:
```

Masukkan angka **1–5** sesuai operasi yang diinginkan.

---

## 🧪 Cakupan Unit Test

| File Test               | Fungsi yang Diuji   | Skenario                          |
|-------------------------|---------------------|-----------------------------------|
| `test_tambah_tugas.py`  | `tambah_tugas()`    | Input valid                       |
| `test_tandai_selesai.py`| `tandai_selesai()`  | ID valid, ID tidak ditemukan      |
| `test_lihat_tugas.py`   | `lihat_tugas()`     | List kosong, 1 item, banyak item  |
| `test_hapus_tugas.py`   | `hapus_tugas()`     | ID valid, ID tidak ditemukan      |
