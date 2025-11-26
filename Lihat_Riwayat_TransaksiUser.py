from Data import users, clear
from prettytable import PrettyTable

def Lihat_Riwayat_Transaksi_User(adminID):
    if len(users) == 0:
        print("TIDAK ADA USER TERDAFTAR.")
        input("\nTekan ENTER untuk kembali...")
        clear()
        return
    
    while True:
        clear()
        print("=== LIHAT RIWAYAT TRANSAKSI USER ===")
        print(f"LOGIN SEBAGAI ADMIN: {adminID}\n")

        user_list = list(users.items())
        tabel_user = PrettyTable()
        tabel_user.field_names = ["No", "User ID", "Username"]

        for idx, (uid, data) in enumerate(user_list, start = 1):
            tabel_user.add_row([idx, uid, data[0]])

        print(tabel_user)

        try:
            pilih = int(input("\nPilih nomor user yang ingin dilihat riwayatnya: "))

        except ValueError:
            print("Input harus berupa angka!")
            input("\nTekan ENTER untuk mengulang...")
            continue

        if pilih < 1 or pilih > len(user_list):
            print("Nomor tidak tersedia dalam daftar!")
            input("\nTekan ENTER untuk mengulang...")
            continue        

        user_id, user_data = user_list[pilih - 1]

        clear()
        print(f"=== RIWAYAT TRANSAKSI USER {user_id} ===")
        print(f"Nama: {user_data[0]}\n")

        pemasukan = user_data[3]
        pengeluaran = user_data[4]

        if not pemasukan and not pengeluaran:
            print("Riwayat transaksi belum tersedia")
                
        else:
            tabel_riwayat = PrettyTable(["No", "Jenis", "Jumlah", "Keterangan", "Tanggal"])

            gabung_transaksi = []

            for jumlah_pemasukan, sumber, tanggal in pemasukan:
                gabung_transaksi.append(("Pemasukan", jumlah_pemasukan, sumber, tanggal))
                    
            for jumlah_pengeluaran, tujuan, tanggal in pengeluaran:
                gabung_transaksi.append(("Pengeluaran", jumlah_pengeluaran, tujuan, tanggal))
                    
            for i, (jenis, jumlah, keterangan, tanggal) in enumerate(gabung_transaksi, start = 1):
                tabel_riwayat.add_row([i, jenis, jumlah, keterangan, tanggal])
            print(tabel_riwayat)

        input("\nTekan ENTER untuk kembali...")
        clear()
        return