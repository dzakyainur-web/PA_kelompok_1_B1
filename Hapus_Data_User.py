from Data import users, clear
from prettytable import PrettyTable

def Hapus_DataUser(adminID):
    if len(users) == 0:
        print("Data User belum tersedia.")
        return 
    
    while True:
        clear()
        tabel_user = PrettyTable()
        tabel_user.field_names(["No", "ID User", "Username"])

        user_keys = list(users.keys())

        for idx, key in enumerate(user_keys, start = 1):
            tabel_user.add_row([idx, key, users[key][0]]) 

        print("\n=== HAPUS DATA USER ===")
        print(f"LOGIN SEBAGAI ADMIN: {adminID}\n")
        print(tabel_user)

        hapus = input("Masukkan nomor user yang mau dihapus: ")

        if hapus == "":
            print("Input tidak boleh kosong")
            break

        try:
            hapus = int(hapus)

        except ValueError:
            print("Input harus berupa angka.")
            return

        if hapus < 1 or hapus > len(user_keys):
            print("Nomor tidak valid")
            return

        pilih_hapus = user_keys[hapus - 1]
        username = users[pilih_hapus][0]

        konfir = input(f"Anda yakin mau menghapus{username}? (y/n): ").lower()

        if konfir == "y":
            del users[pilih_hapus]
            print("User berhasil dihapus")
            input("\nTekan ENTER untuk kembali...")

            if len(users) == 0:
                print("Semua user terhapus")
                break
        else:
            print("Dibatalkan")
            input("\nTekan ENTER untuk kembali...")








