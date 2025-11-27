

from Data import users, clear
from prettytable import PrettyTable
from datetime import datetime

def Tambah_pengeluaran(userID):
    clear()
    print("=== TAMBAH PENGELUARAN ===")

    while True:
        try:
            jumlah = int(input("Masukkan jumlah pengeluaran: "))
        except:
            print("\nINPUT HARUS ANGKA!")
            input("\nTekan ENTER untuk kembali...")
            clear()
            continue
        if jumlah <= 0:
            print("\nINPUT TIDAK BOLEH 0 ATAU MINES")
            input("\nTekan ENTER untuk kembali...")
            clear()
            continue
        
        Saldo_Sekarang = users[userID][2]
        
        while True:
            clear()
            if jumlah > Saldo_Sekarang:
                print("\nSaldo tidak mencukupi!")
                input("\nTekan ENTER untuk kembali...")
                clear()
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
        table = PrettyTable(["Jumlah", "untuk", "Tanggal"])
        table.add_row([f"Rp {jumlah:,}", Tujuan, tanggal])
        
        clear()
        print("\Pengeluaran berhasil ditambahkan!\n")
        print(table)
        input("\nTekan ENTER untuk kembali...")
        return