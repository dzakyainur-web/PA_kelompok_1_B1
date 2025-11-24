from Data import users, clear
from prettytable import PrettyTable
from datetime import datetime

def Tambah_pengeluaran(userID):
    clear()
    print("=== TAMBAH PENGELUARAN ===")
    try:
        jumlah = int(input("Masukkan jumlah pengeluaran: "))
    except:
        print("Input harus angka!")
        return
    untuk = input("Untuk apa pengeluaran ini?: ")
    tanggal = datetime.now().strftime("%d-%m-%y")

    users[userID][2] -= jumlah
    users[userID][4].append([jumlah, untuk, tanggal])
    
    table = PrettyTable(["Jumlah", "untuk", "Tanggal"])
    table.add_row([jumlah, untuk, tanggal])
    print("\Pengeluaran berhasil ditambahkan!\n")
    print(table)
    input("\nTekan ENTER untuk kembali...")




