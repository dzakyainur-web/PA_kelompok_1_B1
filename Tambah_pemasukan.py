from Data import users, clear
from prettytable import PrettyTable
from datetime import datetime

def Tambah_pemasukan(userID):
    clear()
    print("=== TAMBAH PEMASUKAN ===")
    try:
        jumlah = int(input("Masukkan jumlah pemasukan: "))
    except:
        print("Input jumlah harus angka!")
        return
    sumber = input("Masukkan sumber pemasukan: ")
    tanggal = datetime.now().strftime("%d-%m-%y")
    users[userID][2] += jumlah
    users[userID][3].append([jumlah, sumber, tanggal])
    table = PrettyTable(["Jumlah", "Sumber", "Tanggal"])
    table.add_row([jumlah, sumber, tanggal])
    print("\nPemasukan berhasil ditambahkan!\n")
    print(table)
    input("\nTekan ENTER untuk kembali...")


