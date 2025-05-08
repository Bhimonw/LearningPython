import csv
import os

def ensure_directory_exists(directory_path):
    """
    Memastikan direktori target ada. Jika tidak ada, direktori akan dibuat.
    
    Args:
        directory_path (str): Path direktori yang ingin dicek/dibuat
        
    Returns:
        bool: True jika berhasil, False jika gagal
    """
    if not directory_path:
        return True  # Jika path kosong, berarti direktori saat ini
        
    if not os.path.exists(directory_path):
        try:
            os.makedirs(directory_path)
            print(f"Direktori {directory_path} berhasil dibuat.")
            return True
        except Exception as e:
            print(f"Error: Gagal membuat direktori: {e}")
            return False
    
    return True

def is_file_exists(file_path):
    """
    Memeriksa apakah file sudah ada
    
    Args:
        file_path (str): Path file yang ingin dicek
        
    Returns:
        bool: True jika file ada, False jika tidak ada
    """
    return os.path.isfile(file_path)

def get_absolute_path(file_path):
    """
    Mendapatkan path absolut dari file
    
    Args:
        file_path (str): Path file
        
    Returns:
        str: Path absolut dari file
    """
    return os.path.abspath(file_path)

def tambah_kontak(file_path):
    """
    Fungsi untuk menambahkan kontak baru ke dalam file CSV
    
    Args:
        file_path (str): Path file CSV tempat menyimpan kontak
    """
    print("\n=== Tambah Kontak Baru ===")
    
    # Meminta input dari pengguna
    nama = input("Masukkan nama: ").strip()
    nomor_telepon = input("Masukkan nomor telepon: ").strip()
    
    # Validasi input sederhana
    if not nama or not nomor_telepon:
        print("Error: Nama dan nomor telepon tidak boleh kosong.")
        return
    
    # Pastikan direktori ada
    directory = os.path.dirname(file_path)
    if not ensure_directory_exists(directory):
        return
    
    # Cek apakah file sudah ada
    file_exists = is_file_exists(file_path)
    
    try:
        # Buka file untuk penulisan
        with open(file_path, 'a', newline='') as file_csv:
            writer = csv.writer(file_csv)
            
            # Jika file baru, tambahkan header
            if not file_exists:
                writer.writerow(['Nama', 'Nomor Telepon'])
            
            # Tambahkan data kontak baru
            writer.writerow([nama, nomor_telepon])
        
        # Konfirmasi keberhasilan
        print(f"Sukses: Kontak '{nama}' berhasil ditambahkan!")
        print(f"Info: Data tersimpan di: {get_absolute_path(file_path)}")
    except PermissionError:
        print("Error: Tidak memiliki izin untuk menulis ke file. Pastikan Anda memiliki akses yang tepat.")
    except IOError as e:
        print(f"Error: Tidak dapat menulis ke file: {e}")
    except Exception as e:
        print(f"Error: Terjadi kesalahan tak terduga saat menyimpan: {e}")

def display_table_header(header):
    """
    Menampilkan header tabel dengan format yang rapi
    
    Args:
        header (list): List berisi nama-nama kolom header
    """
    # Menentukan lebar kolom
    nama_width = 25
    telepon_width = 20
    
    # Menampilkan header
    print(f"┌{'─' * nama_width}┬{'─' * telepon_width}┐")
    print(f"│ {header[0]:<{nama_width-2}} │ {header[1]:<{telepon_width-2}} │")
    print(f"├{'─' * nama_width}┼{'─' * telepon_width}┤")

def display_table_row(row, nama_width=25, telepon_width=20):
    """
    Menampilkan baris data dengan format yang rapi
    
    Args:
        row (list): List berisi data yang akan ditampilkan
        nama_width (int): Lebar kolom nama
        telepon_width (int): Lebar kolom telepon
    """
    print(f"│ {row[0]:<{nama_width-2}} │ {row[1]:<{telepon_width-2}} │")

def display_table_footer(nama_width=25, telepon_width=20):
    """
    Menampilkan footer tabel
    
    Args:
        nama_width (int): Lebar kolom nama
        telepon_width (int): Lebar kolom telepon
    """
    print(f"└{'─' * nama_width}┴{'─' * telepon_width}┘")

def tampilkan_kontak(file_path):
    """
    Fungsi untuk menampilkan semua kontak dari file CSV dengan format tabel yang rapi
    
    Args:
        file_path (str): Path file CSV yang berisi data kontak
    """
    print("\n=== Daftar Kontak ===")
    
    # Memeriksa apakah file sudah ada
    if not is_file_exists(file_path):
        print("Info: File kontak belum ada. Silakan tambahkan kontak terlebih dahulu.")
        return
    
    try:
        with open(file_path, 'r', newline='') as file_csv:
            reader = csv.reader(file_csv)
            
            # Membaca header
            header = next(reader, None)
            if not header:
                print("Error: Format file tidak valid atau file kosong.")
                return
                
            # Baca semua baris untuk menghitung jumlah kontak
            rows = list(reader)
            jumlah_kontak = len(rows)
            
            if jumlah_kontak == 0:
                print("Info: Tidak ada kontak yang tersimpan.")
                return
                
            # Tampilkan header tabel
            display_table_header(header)
            
            # Tampilkan setiap baris data
            for row in rows:
                if len(row) >= 2:
                    display_table_row(row)
            
            # Tampilkan footer tabel
            display_table_footer()
            
            # Tampilkan jumlah kontak
            print(f"\nTotal: {jumlah_kontak} kontak.")
            
    except PermissionError:
        print("Error: Tidak memiliki izin untuk membaca file.")
    except IOError as e:
        print(f"Error: Tidak dapat membaca file: {e}")
    except Exception as e:
        print(f"Error: Terjadi kesalahan saat membaca file: {e}")

def tampilkan_menu():
    """
    Menampilkan menu aplikasi
    
    Returns:
        str: Pilihan menu dari pengguna
    """
    print("\nPilih Menu:")
    print("1. Tambah Kontak")
    print("2. Tampilkan Kontak")
    print("3. Keluar")
    
    return input("\nMasukkan pilihan (1/2/3): ").strip()

def main():
    """
    Fungsi utama untuk menjalankan program
    """
    # Konstanta untuk path file
    FOLDER_PATH = "./csv/"
    FILE_NAME = "kontak.csv"
    file_path = os.path.join(FOLDER_PATH, FILE_NAME)
    
    # Header aplikasi
    print("╔════════════════════════════════╗")
    print("║    APLIKASI MANAJEMEN KONTAK   ║")
    print("╚════════════════════════════════╝")
    
    while True:
        pilihan = tampilkan_menu()
        
        if pilihan == '1':
            tambah_kontak(file_path)
        elif pilihan == '2':
            tampilkan_kontak(file_path)
        elif pilihan == '3':
            print("\nTerima kasih telah menggunakan aplikasi ini!")
            break
        else:
            print("Error: Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")

if __name__ == "__main__":
    main()