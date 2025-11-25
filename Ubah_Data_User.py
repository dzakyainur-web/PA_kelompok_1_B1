from Data import users, clear
from prettytable import PrettyTable

def Ubah_DataUser(adminID):
    if len(users) == 0:
        print("DATA USER BELUM ADA.")
        return
    
    clear()
    tabel_user = PrettyTable(adminID)
    tabel_user.field_names = (["No","Username", "Password"])
    user_keys = list(users.keys())

    for idx, key in enumerate(user_keys, start = 1):
        tabel_user.add_row([idx, key, users[key][1]])
    print("\n=== UBAH DATA USER ===")
    print(tabel_user)

    pilih = input("\nMasukkan nomor user yang ingin diubah: ").strip()

    if pilih == "":
        print("Input tidak boleh kosong")
        return
    
    try:
        pilih = int(pilih)

    except ValueError:
        print("Input harus berupa angka!")
        return
    
    if pilih < 1 or pilih > len(user_keys):
        print("Nomor tidak tersedia.")
        return

    ubah_data = user_keys[pilih - 1]

    new_username = input("Username baru: ").strip()
    new_password = input("Password baru: ").strip()

    if new_username == "" or new_password == "":
        print("Data tidak boleh kosong.")
        return
    
    if new_username in users and new_username != ubah_data:
        print("Username sudah digunakan!")
        return
    
    if new_username != ubah_data:
        users[new_username] = users.pop(ubah_data)
        ubah_data = new_username

    users[ubah_data][1] = new_password

    print("\nData User berhasil diubah!")
    input("\nTekan ENTER untuk kembali..")
