from Data import users, clear
from prettytable import PrettyTable

def Ubah_Data_User(adminID):
    if len(users) == 0:
        print("TIDAK ADA USER TERDAFTAR.")
        input("Tekan ENTER untuk kembali...")
        return
    
    while True:
        clear()
        print("=== UBAH DATA USER ===")
        print(f"LOGIN SEBAGAI ADMIN: {adminID}\n")

        user_list = list(users.items())
        tabel_user = PrettyTable()
        tabel_user.field_names = ["No", "User ID", "Username", "Password"]

        for idx, (uid, data) in enumerate(user_list, start=1):
            tabel_user.add_row([idx, uid, data[0], data[1]])
        print(tabel_user)

        pilih = input("Masukkan nomor user yang ingin diubah (Ketik 'batal' untuk membatalkan): ").lower()

        if pilih == "batal":
            print("\nPerintah dibatalkan")
            input("\nTekan ENTER untuk kembali...")
            return

        try:
            pilih = int(pilih)
        except ValueError:
            print("\nInput harus angka.")
            input("\nTekan ENTER untuk mengulang")
            continue

        if pilih < 1 or pilih > len(user_list):
            print("\nNomor yang dimasukkan tidak valid!")
            input("\nTekan ENTER untuk mengulang....")
            continue

        user_id, data_lama = user_list[pilih - 1]

        while True:
            clear()
            print(f"UBAH DATA USER: {user_id}")
            print(f"Username sekarang: {data_lama[0]}")
            print(f"Password sekarang: {data_lama[1]}\n")

            new_username = input("Masukkan username baru: ").strip()

            if new_username == "":
                print("\nUsername tidak boleh kosong!")
                input("\nTekan ENTER untuk mengulang...")
                continue

            if new_username.lower() == data_lama[0]:
                print("\nUsername baru tidak boleh sama dengan username lama!")
                input("\nTekan ENTER untuk mengulang...")
                continue

            username_sudah_dipakai = False
            for uid, data in users.items():
                if uid != user_id and data[0]== new_username.lower():
                    username_sudah_dipakai = True
                    break

            if username_sudah_dipakai:
                print("\nUsername sudah dipakai oleh user lain!")
                input("\nTekan ENTER untuk mengulang...")
                continue
                
            new_pw = input("\nMasukkan password baru: ").strip()
                
            if new_pw == "":
                print("\nPassword tidak boleh kosong!")
                input("\nTekan ENTER untuk mengulang...")
                continue

            break

        users[user_id][0] = new_username
        users[user_id][1] = new_pw

        print("\nData berhasil diperbarui!")
        input("\nTekan ENTER untuk kembali...")
        return