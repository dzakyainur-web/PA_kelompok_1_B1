from Data import users, clear
from prettytable import PrettyTable

def Hapus_DataUser(adminID):
    while True:
        if len(users) == 0:
            print("TIDAK ADA USER TERDAFTAR.")
            input("Tekan ENTER untuk kembali...")
            return
        
        clear()
        print("=== HAPUS DATA USER ===")
        print(f"LOGIN SEBAGAI ADMIN: {adminID}\n")

        user_list = list(users.items())
        tabel_user = PrettyTable()
        tabel_user.field_names = ["No", "User ID", "Username", "Password"]

        for idx, (uid, data) in enumerate(user_list, start=1):
            tabel_user.add_row([idx, uid, data[0], data[1]])

        print(tabel_user)

        pilih = input("\nMasukkan nomor user yang ingin dihapus: ")

 
        if not pilih.isdigit():
            print("\nError: Hanya boleh memasukkan angka.")
            input("Tekan ENTER untuk mengulang...")
            continue 
        
        pilih = int(pilih)


        if pilih < 1 or pilih > len(user_list):
            print("\nError: Nomor user tidak ditemukan.")
            input("\nTekan ENTER untuk mengulang...")
            continue
        
        
        user_id, user_data = user_list[pilih - 1]

        clear()
        print("Anda akan menghapus user berikut:\n")
        print(f"User ID   : {user_id}")
        print(f"Username  : {user_data[0]}")
        print(f"Password  : {user_data[1]}\n")

        konfirmasi = input("Yakin ingin menghapus? (y/n): ").lower()

        if konfirmasi == "y":
            del users[user_id]
            print(f"\nUser {user_id} berhasil dihapus!")
            input("\nTekan ENTER untuk kembali...")
            return
        
        elif konfirmasi == "n":
            print("\nPenghapusan dibatalkan.")
            input("\nTekan ENTER untuk kembali...")
            return
        
        else:
            print("\nInput tidak valid! hanya (y/n).")
            input("Tekan ENTER untuk mengulang...")

        









