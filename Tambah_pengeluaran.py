

from Data import users, clear
from prettytable import PrettyTable
from datetime import datetime

def Tambah_pengeluaran(userID):
    clear()
    print("=== TAMBAH PENGELUARAN ===")
    try:
        jumlah = int(input("Masukkan jumlah pengeluaran: "))
    except:
        print("\nINPUT HARUS ANGKA!")
        input("\nTekan ENTER untuk kembali...")
        return
    
    Saldo_Sekarang = users[userID][2]
    
    while True:
        if jumlah > Saldo_Sekarang:
            print("\nSaldo tidak mencukupi!")
            input("\nTekan ENTER untuk kembali...")
            return
        
        Tujuan = input("Untuk apa pengeluaran ini?: ").strip()

        if Tujuan == "":
            print("\nTujuan pengeluaran tidak boleh kosong!")
            input("\nTekan ENTER untuk kembali...")
            clear()
            continue

        if Tujuan.isnumeric():
            print("\nTujuan pengeluaran tidak boleh berupa angka!")
            input("\nTekan ENTER untuk kembali...")
            clear()
            continue

        break

    tanggal = datetime.now().strftime("%d-%m-%y")
    users[userID][2] -= jumlah
    users[userID][4].append([jumlah, Tujuan, tanggal])
    table = PrettyTable(["Jumlah", "Tujuan", "Tanggal"])
    table.add_row([jumlah, Tujuan, tanggal])
    print("\nPengeluaran berhasil ditambahkan!\n")
    print(table)
    input("\nTekan ENTER untuk kembali...")