from Data import users, clear
from prettytable import PrettyTable

table = PrettyTable()
def Lihat_saldo(userID):
    clear()
    print("=== LIHAT SALDO ===")
    saldo = users[userID][2]
    if saldo == 0:
        print("\n--- SALDO ANDA KOSONG ---")
    else:
        table = PrettyTable(["userID", "saldo"])
        table.add_row([userID, f"Rp {saldo:,}"])
        print(table)
        
    input("\n Tekan ENTER untuk kembali...")


