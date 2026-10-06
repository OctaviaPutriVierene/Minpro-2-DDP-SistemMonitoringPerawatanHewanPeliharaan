import os
import random
import time

akun = {
    "admin": {
        "password": "121",
        "role": "admin"
    },
    "user": {
        "password": "123",
        "role": "user"
    }
}
data_hewan = {}

def tampilkan_hewan():
    print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-")
    print("DATA SEMUA HEWAN")
    print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-")

    if len(data_hewan) == 0:
        print("Belum ada data hewan.")
    else:
        for kode in data_hewan:
            print("Kode :", kode)
            print("Nama :", data_hewan[kode]["nama"])
            print("Jenis :", data_hewan[kode]["jenis"])
            print("Status makan :", data_hewan[kode]["makan"])
            print("Status minum :", data_hewan[kode]["minum"])
            print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-")
            
    input()

def cari_hewan():
    kode = input("Masukkan kode hewan: ")

    if kode in data_hewan:
        print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-")
        print("Kode :", kode)
        print("Nama :", data_hewan[kode]["nama"])
        print("Jenis :", data_hewan[kode]["jenis"])
        print("Status makan :", data_hewan[kode]["makan"])
        print("Status minum :", data_hewan[kode]["minum"])
        print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-")
    else:
        print("Data hewan tidak ditemukan.")
        
    input()

def update_makan():
    kode = input("Masukkan kode hewan: ")

    if kode in data_hewan:
        print("1. Sudah")
        print("2. Belum")

        pilihan = input("Pilih status makan: ")

        if pilihan == "1":
            data_hewan[kode]["makan"] = "Sudah"
            print("Status makan berhasil diubah.")
        elif pilihan == "2":
            data_hewan[kode]["makan"] = "Belum"
            print("Status makan berhasil diubah.")
        else:
            print("Pilihan tidak tersedia.")
    else:
        print("Data hewan tidak ditemukan.")
        
    input()

def update_minum():
    kode = input("Masukkan kode hewan: ")

    if kode in data_hewan:
        print("1. Sudah")
        print("2. Belum")

        pilihan = input("Pilih status minum: ")

        if pilihan == "1":
            data_hewan[kode]["minum"] = "Sudah"
            print("Status minum berhasil diubah.")
        elif pilihan == "2":
            data_hewan[kode]["minum"] = "Belum"
            print("Status minum berhasil diubah.")
        else:
            print("Pilihan tidak tersedia.")
    else:
        print("Data hewan tidak ditemukan.")
        
    input()

def tambah_hewan():
    kode = str(random.randint(100, 999)) 
    
    while kode in data_hewan:
        kode = str(random.randint(100, 999))

    print("Kode hewan otomatis :", kode)
    nama = input("Masukkan nama hewan: ")
    jenis = input("Masukkan jenis hewan: ")

    data_hewan[kode] = {
        "nama": nama,
        "jenis": jenis,
        "makan": "Belum",
        "minum": "Belum"
    }

    print("Data hewan berhasil ditambahkan.")
    input()

def hapus_hewan():
    kode = input("Masukkan kode hewan yang ingin dihapus: ")

    if kode in data_hewan:
        nama = data_hewan[kode]["nama"]

        del data_hewan[kode]

        print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-")
        print("Data hewan berhasil dihapus.")
        print("Nama :", nama)
        print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-")

        print("Data hewan setelah dihapus:")
        tampilkan_hewan()

    else:
        print("Data hewan tidak ditemukan.")
        input()

def reset_status():
    if len(data_hewan) == 0:
        print("Belum ada data hewan.")
    else:
        for kode in data_hewan:
            data_hewan[kode]["makan"] = "Belum"
            data_hewan[kode]["minum"] = "Belum"

        print("Semua status berhasil direset.")
        
    input()

def menu_admin():
    while True:
        print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-")
        print("MENU ADMIN")
        print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-")
        print("1. Tampilkan semua hewan")
        print("2. Cari hewan")
        print("3. Update status makan")
        print("4. Update status minum")
        print("5. Tambah hewan")
        print("6. Hapus hewan")
        print("7. Reset status")
        print("8. Keluar")
        print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tampilkan_hewan()
        elif pilihan == "2":
            cari_hewan()
        elif pilihan == "3":
            update_makan()
        elif pilihan == "4":
            update_minum()
        elif pilihan == "5":
            tambah_hewan()
        elif pilihan == "6":
            hapus_hewan()
        elif pilihan == "7":
            reset_status()
        elif pilihan == "8":
            os.system("cls" if os.name == "nt" else "clear")
            print("Terima kasih.")
            time.sleep(1)
            break
        else:
            print("Pilihan tidak tersedia.")
            time.sleep(1)

def menu_pengguna():
    while True:
        print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-")
        print("MENU PENGGUNA")
        print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-")
        print("1. Tampilkan semua hewan")
        print("2. Cari hewan")
        print("3. Update status makan")
        print("4. Update status minum")
        print("5. Keluar")
        print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tampilkan_hewan()
        elif pilihan == "2":
            cari_hewan()
        elif pilihan == "3":
            update_makan()
        elif pilihan == "4":
            update_minum()
        elif pilihan == "5":
            os.system("cls" if os.name == "nt" else "clear")
            print("Terima kasih.")
            time.sleep(1)
            break
        else:
            print("Pilihan tidak tersedia.")
            time.sleep(1)

def login():
    while True:
        print("LOGIN SISTEM MONITORING HEWAN")
        print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-")

        username = input("Username: ")
        
        if username == 'stop':
            print("Program dihentikan secara total.")
            break
            
        password = input("Password: ")

        if username in akun:
            if akun[username]["password"] == password:
                if akun[username]["role"] == "admin":
                    print("Login berhasil.")
                    print("Anda masuk sebagai ADMIN.")
                    time.sleep(1)
                    menu_admin()
                elif akun[username]["role"] == "user":
                    print("Login berhasil.")
                    print("Anda masuk sebagai PENGGUNA.")
                    time.sleep(1)
                    menu_pengguna()
            else:
                print("Password salah.")
                time.sleep(1)
        else:
            print("Username tidak ditemukan.")
            time.sleep(1)

login()
