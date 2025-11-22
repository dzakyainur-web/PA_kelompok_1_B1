from Data import users, clear
from prettytable import PrettyTable

def Lihat_RiwayatP(userID):
    clear()
    print("=== RIWAYAT PEMASUKAN DAN PENGELUARAN ===")

    pemasukan = users[userID][3]
    pengeluaran = users[userID][4]

    if not pemasukan and not pengeluaran:
        print("Belum ada riwayat...")
        input("Tekan ENTER untuk kembali...")
        return
    table = PrettyTable(["Jenis", "Jumlah", "Keterangan", "Tanggal"])
    for jumlah, sumber, tanggal in pemasukan:
        table.add_row(["Pemasukan", jumlah, sumber, tanggal])
    for jumlah, untuk, tanggal in pengeluaran:
        table.add_row(["Pengeluaran", jumlah, untuk, tanggal])
    print(table)
    input("\nTekan ENTER untuk kembali...")
