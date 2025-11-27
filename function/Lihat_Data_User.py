from data.Data import users, clear
from prettytable import PrettyTable

def Lihat_DataUser(adminID):
    if len(users) == 0:
        print("\nData User belum tersedia!")
        input("\nTekan ENTER untuk kembali...")
        clear()
        return
    
    else:
        clear()
        print("=== DAFTAR DATA USER ===")
        print(f"LOGIN SEBAGAI ADMIN: {adminID}\n")

        user_list = list(users.items())
        tabel_user = PrettyTable()
        tabel_user.field_names = ["No", "User ID", "Username", "Password"]

        for idx, (uid, data) in enumerate (user_list, start = 1):
            username = data[0]
            password = data[1]
            tabel_user.add_row([idx, uid, username, password])
        print(tabel_user)
        input("\nTekan ENTER untuk kembali...")