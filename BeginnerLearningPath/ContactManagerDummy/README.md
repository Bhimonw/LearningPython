# Aplikasi Manajemen Kontak

## Deskripsi
Aplikasi Manajemen Kontak adalah program Python yang memungkinkan pengguna untuk menambah, menampilkan, dan menyimpan daftar kontak dalam format file CSV. Program ini memiliki antarmuka berbasis teks yang sederhana dan mudah digunakan. Pengguna dapat memasukkan informasi kontak seperti nama dan nomor telepon, serta menampilkan daftar kontak yang sudah disimpan.

## Fitur
- **Menambah Kontak Baru:** Pengguna dapat memasukkan nama dan nomor telepon yang akan disimpan dalam file CSV.
- **Menampilkan Kontak:** Daftar kontak yang sudah tersimpan dalam file CSV akan ditampilkan dalam format tabel yang rapi.
- **Pembuatan Direktori Otomatis:** Jika direktori untuk menyimpan file CSV belum ada, program akan membuatnya otomatis.
- **Penanganan Error yang Informatif:** Aplikasi menangani berbagai kesalahan seperti masalah izin, file yang hilang, atau kesalahan input dengan pesan yang jelas.

## Instalasi
### 1. **Prasyarat:**
   - Python 3.x harus terinstal pada komputer Anda.
   - Tidak ada paket tambahan yang diperlukan karena aplikasi ini menggunakan modul standar Python seperti `csv` dan `os`.

### 2. **Langkah-langkah Instalasi:**
   - Salin file `contactManager.py` ke direktori pilihan Anda.
   - Jalankan program dengan perintah berikut di terminal atau command prompt:
     ```bash
     python contactManager.py
     ```

### 3. **Struktur Direktori:**
   - Aplikasi ini secara otomatis akan membuat folder `./csv/` untuk menyimpan file `kontak.csv`. Pastikan Anda memiliki izin untuk membuat folder dan file di direktori tersebut.

## Cara Penggunaan
### 1. **Menambah Kontak:**
   - Pilih menu `1` untuk menambah kontak baru.
   - Masukkan nama dan nomor telepon ketika diminta. Data akan disimpan dalam file CSV.

### 2. **Menampilkan Kontak:**
   - Pilih menu `2` untuk menampilkan semua kontak yang sudah disimpan.
   - Kontak akan ditampilkan dalam format tabel dengan nama dan nomor telepon.

### 3. **Keluar:**
   - Pilih menu `3` untuk keluar dari aplikasi.

## Contoh Output

### Menambahkan Kontak:
```bash
=== Tambah Kontak Baru ===
Masukkan nama: Rahmalia
Masukkan nomor telepon: 081234567890
Sukses: Kontak 'Rahmalia' berhasil ditambahkan!
Info: Data tersimpan di: /path/to/csv/kontak.csv
````

### Menampilkan Kontak:

```bash
=== Daftar Kontak ===
┌─────────────────────────┬────────────────────┐
│ Nama                    │ Nomor Telepon     │
├─────────────────────────┼────────────────────┤
│ Rahmalia                │ 081234567890       │
└─────────────────────────┴────────────────────┘
Total: 1 kontak.
```
## Fungsi-fungsi Utama

1. **`tambah_kontak(file_path)`**: Menambahkan kontak baru ke dalam file CSV.
2. **`tampilkan_kontak(file_path)`**: Menampilkan semua kontak yang ada dalam file CSV dalam format tabel.
3. **`buat_direktori(directory_path)`**: Memastikan direktori untuk file CSV ada; jika tidak, direktori akan dibuat.
4. **`tulis_kontak_ke_csv(file_path, nama, nomor_telepon, file_exists)`**: Menulis kontak baru ke dalam file CSV, dengan penanganan header untuk file baru.
5. **`tampilkan_menu()`**: Menampilkan menu utama aplikasi untuk memilih aksi (menambah, menampilkan, atau keluar).

## Penanganan Error

Aplikasi ini menangani beberapa jenis kesalahan seperti:

* **PermissionError:** Jika aplikasi tidak memiliki izin untuk membaca/menulis file.
* **IOError:** Jika terjadi masalah dalam membaca atau menulis file.
* **Exception lainnya:** Jika ada kesalahan tak terduga dalam program.

## Pengembangan Selanjutnya

* **Autentikasi Pengguna:** Menambahkan fitur autentikasi untuk memastikan hanya pengguna yang sah yang dapat mengakses aplikasi.
* **Import dan Export:** Menambahkan fitur untuk mengimpor atau mengekspor data kontak dari atau ke file lain (misalnya Excel atau JSON).
* **UI Grafis:** Mengembangkan antarmuka grafis (GUI) untuk aplikasi ini menggunakan **Tkinter** atau framework lainnya.
