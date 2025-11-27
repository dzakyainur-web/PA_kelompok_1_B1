from Data import users, clear
from prettytable import PrettyTable

def Lihat_RiwayatP(userID):
    clear()
    print("=== RIWAYAT PEMASUKAN DAN PENGELUARAN ===")

    pemasukan = users[userID][3]
    pengeluaran = users[userID][4]

    if not pemasukan and not pengeluaran:
        print("\nBELUM ADA")
        input("\nTekan ENTER untuk kembali...")
        return
    
    else:
        gabung_riwayat = []
        
        tabel_riwayat = PrettyTable(["No", "Jenis", "Jumlah", "Keterangan", "Tanggal"])

        for jumlah_pemasukan, sumber, tanggal in pemasukan:
            gabung_riwayat.append(("Pemasukan", jumlah_pemasukan, sumber, tanggal))
                        
        for jumlah_pengeluaran, tujuan, tanggal in pengeluaran:
            gabung_riwayat.append(("Pengeluaran", jumlah_pengeluaran, tujuan, tanggal))
                        
        for i, (jenis, jumlah, keterangan, tanggal) in enumerate(gabung_riwayat, start = 1):
            tabel_riwayat.add_row([i, jenis, f"Rp {jumlah:,}", keterangan, tanggal])
        print(tabel_riwayat)

        input("\nTekan ENTER untuk kembali...")
        clear()
        return
