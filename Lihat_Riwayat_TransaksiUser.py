from Data import users, clear
from prettytable import PrettyTable

def Lihat_Riwayat_Transaksi_User(adminID):
    if len(users) == 0:
        print("TIDAK ADA USER TERDAFTAR.")
        return
    
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

        if pilih < 1 or pilih > len(user_list):
            raise ValueError("Nomor user tidak valid.")

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

            for jumlah, sumber, tanggal in pemasukan:
                gabung_transaksi.append(("Pemasukan", jumlah, sumber, tanggal))
            
            for jumlah, tujuan, tanggal in pengeluaran:
                gabung_transaksi.append(("Pengeluaran", jumlah, tujuan, tanggal))
            
            for i, (jenis, jumlah, detail, tanggal) in enumerate(gabung_transaksi, start = 1):
                tabel_riwayat.add_row([i, jenis, jumlah, detail, tanggal])
            print(tabel_riwayat)

    except ValueError as e:
        print(f"Error: {e}")

    input("\nTekan ENTER untuk kembali...")
    clear()
    print("coba-coba")


