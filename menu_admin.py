import os
from Lihat_Data_User import Lihat_DataUser
from Ubah_Data_User import Ubah_DataUser
from Hapus_Data_User import Hapus_DataUser
from Lihat_Riwayat_TransaksiUser import Lihat_Riwayat_Transaksi_User

def clear():
    os.system('cls || clear')

def menu_admin():
    while True:
        clear()
        print("1. Lihat Data User")
        print("2. Ubah Data User")
        print("3. Hapus Akun User")
        print("4. Lihat Riwayat Transaksi User")
        print("5. Logout")
        pilihan_admin = input("Pilih Menu(1-5): ")

        if pilihan_admin == "1":
            Lihat_DataUser()
        
        elif pilihan_admin == "2":
            Ubah_DataUser()
        
        elif pilihan_admin == "3":
            Hapus_DataUser()
        
        elif pilihan_admin == "4":
            Lihat_Riwayat_Transaksi_User()
        
        elif pilihan_admin == "5":
            break
        
        else:
            ("Pilihan Anda tidak valid!")