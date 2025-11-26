from Data import users, clear
from prettytable import PrettyTable

def Lihat_DataUser(adminID):
    if len(users) == 0:
        print("Data User belum tersedia!")
        return
    
    clear()
    print("=== DAFTAR DATA USER ===")
    print(f"LOGIN SEBAGAI ADMIN: {adminID}\n")
    tabel_user = PrettyTable()
    tabel_user.field_names = ["User ID", "Username", "Password"]
    for key, value in users.items():
        tabel_user.add_row([key, value[0], value[1]])
    print(tabel_user)
    input("\nTekan ENTER untuk kembali...")
    clear()

