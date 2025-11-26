from Data import users, clear
from prettytable import PrettyTable

def Ubah_Data_User(adminID):
    if len(users) == 0:
        print("TIDAK ADA USER TERDAFTAR.")
        input("Tekan ENTER untuk kembali...")
        return
    
    clear()
    print("=== UBAH DATA USER ===")
    print(f"LOGIN SEBAGAI ADMIN: {adminID}\n")

    user_list = list(users.items())
    tabel_user = PrettyTable()
    tabel_user.field_names = ["No", "User ID", "Username", "Password"]

    for idx, (uid, data) in enumerate(user_list, start=1):
        tabel_user.add_row([idx, uid, data[0], data[1]])

    print(tabel_user)

    try:
        pilih = int(input("\nMasukkan nomor user yang ingin diubah: "))

        if pilih < 1 or pilih > len(user_list):
            raise ValueError("Nomor user tidak valid!")

        user_id, user_data = user_list[pilih - 1]

        clear()
        print(f"=== UBAH DATA USER: {user_id} ===")
        print(f"Username Sekarang : {user_data[0]}")
        print(f"Password Sekarang : {user_data[1]}\n")

        
        new_username = input("Masukkan Username baru: ")
        new_password = input("Masukkan Password baru: ")

        
        if new_username.strip() != "":
            user_data[0] = new_username

        if new_password.strip() != "":
            user_data[1] = new_password

        users[user_id] = user_data 
        print("\nData berhasil diperbarui!")
    
    except ValueError as e:
        print(f"\nError: {e}")
    input("\nTekan ENTER untuk kembali...")
