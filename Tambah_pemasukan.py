from Data import users, clear
from prettytable import PrettyTable
from datetime import datetime

def Tambah_pemasukan(userID):
    clear()
    print("=== TAMBAH PEMASUKAN ===")
    while True:
        try:
            jumlah = int(input("Masukkan jumlah pemasukan: "))
        except:
            print("\nINPUT HARUS ANGKA!")
            input("\nTekan ENTER untuk kembali...")
            return
        
        if jumlah <= 0:
            print("\nINPUT TIDAK BOLEH 0 ATAU MINUS")
            input("\nTekan INPUT untuk kembali...")
            continue

        while True:
            sumber = input("Masukkan sumber pemasukan: ").strip()

            if sumber == "":
                print("\nINPUT TIDAK BOLEH KOSONG!!!")
                input("\nTekan ENTER untuk kembali...")
                clear()
                continue

            if sumber.isnumeric():
                print("\nINPUT JANGAN ANGKA SAJA!!!")
                input("\nTekan ENTER untuk kembali...")
                clear()
                continue

            break
    
        tanggal = datetime.now().strftime("%d-%m-%y")
        users[userID][2] += jumlah
        users[userID][3].append([jumlah, sumber, tanggal])
        table = PrettyTable(["Jumlah", "Sumber", "Tanggal"])
        table.add_row([jumlah, sumber, tanggal])
        print("\nPemasukan berhasil ditambahkan!\n")
        print(table)
        input("\nTekan ENTER untuk kembali...")


