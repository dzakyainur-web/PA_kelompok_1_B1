from Data import clear
from Lihat_Data_User import Lihat_DataUser
from Ubah_Data_User import Ubah_DataUser
from Hapus_Data_User import Hapus_DataUser
from Lihat_Riwayat_TransaksiUser import Lihat_Riwayat_Transaksi_User
from Data import clear

def menu_admin(adminID):
    while True:
        clear()
        print("=== MENU ADMIN ===")
        print("1. Lihat Data User")
        print("2. Ubah Data User")
        print("3. Hapus Akun User")
        print("4. Lihat Riwayat Transaksi User")
        print("5. Logout")
        pilihan_admin = input("Pilih Menu(1-5): ")

        if pilihan_admin == "1":
            Lihat_DataUser(adminID)
        
        elif pilihan_admin == "2":
            Ubah_DataUser(adminID)
        
        elif pilihan_admin == "3":
            Hapus_DataUser(adminID)
        
        elif pilihan_admin == "4":
            Lihat_Riwayat_Transaksi_User(adminID)
        
        elif pilihan_admin == "5":
            clear()
            print("Keluar dari Menu Admin")
            input("\nTekan ENTER untuk keluar...")
            break
        
        else:
            print("Pilihan Anda tidak valid!")
            input("\nTekan ENTER untuk mengulang...")
            