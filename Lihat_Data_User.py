from Data import users, clear
from prettytable import PrettyTable

def Lihat_DataUser(adminID):
    if len(users) == 0:
        print("Data User belum tersedia!")
        return
    
    clear()
    tabel_user = PrettyTable()
    tabel_user.field_names = (["No","Username", "Password"])

    for idx, (key, value) in enumerate(users.items(), start = 1):
        tabel_user.add_row([idx, key, value[0], value[1]])
    
    print("\n=== DATA USER ===")
    print(f"LOGIN SEBAGAI ADMIN: {adminID}\n")
    print(tabel_user)
    input("\nTekan ENTER untuk kembali...")