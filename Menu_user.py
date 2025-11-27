from Data import clear
from Lihat_saldo import Lihat_saldo
from Tambah_pemasukan import Tambah_pemasukan
from Tambah_pengeluaran import Tambah_pengeluaran
from Lihat_RiwayatP import Lihat_RiwayatP
from Hapus_User import Hapus_User
from Ganti_Pass import Ganti_Password

def Menu_User(userID):
    while True:
        clear()
        print("==== MENU USER ====")
        print("1. Lihat Saldo")
        print("2. Tambah Pemasukan")
        print("3. Tambah Pengeluaran")
        print("4. Lihat Riwayat Transaksi")
        print("5. Ganti Password")
        print("6. Hapus User")
        print("7. Logout")
        
        pilihan = input("\nPilih menu (1-7): ")
        if pilihan == "1":
            Lihat_saldo(userID)
        elif pilihan == "2":
            Tambah_pemasukan(userID)
        elif pilihan == "3":
            Tambah_pengeluaran(userID)
        elif pilihan == "4":
            Lihat_RiwayatP(userID)
        elif pilihan == "5":
            Ganti_Password(userID)
        elif pilihan == "6":
            if Hapus_User(userID):   
                return 
        elif pilihan == "7":
            clear()
            print("\nKeluar dari menu user...")
            input("\nTekan ENTER untuk kembali...")
            clear()
            break
        else:
            print("\nPilihan tidak valid!")
            input("Tekan ENTER untuk ulang...")
