from Data import users, clear
from prettytable import PrettyTable

def Lihat_Riwayat_Transaksi_User(adminID):
    if len(users) == 0:
        print("TIDAK ADA USER TERDAFTAR.")
        return
    
    print("=== LIHAT RIWAYAT TRANSAKSI USER ===")
    print(f"LOGIN SEBAGAI ADMIN: {adminID}\n")

    user_list = list(users.items())
    tabel_user = PrettyTable()
    tabel_user.field_names(["User ID", "Username"])

    for idx, (uid, data) in enumerate(user_list, start = 1):
        tabel_user.add_row([idx, uid, data[0]])
    print(tabel_user)
    
    try:
        pilih = int(input("\nPilih nomor user yang ingin dilihat riwayatnya: "))
        
        if pilih < 1 or pilih > len(user_list):
            raise ValueError("Nomor user tidak valid.")
            
        user_id, user_data = user_list[pilih - 1]

        clear()
        print(f"=== RIWAYAT TRANSAKSI {user_id} ===")
        print(f"Nama: {user_data[0]}\n")
        
        riwayat = user_data[3]
        
        if not riwayat:
            print("Riwayat transaksi kosong.")
            
        else:
            riwayat = PrettyTable()
            riwayat.field_names = ["No", "Transaksi"]
            for i, item in enumerate(riwayat, start = 1):
                riwayat.add_row([i, item])
            print(riwayat)

    except ValueError as x:
        print(f"Error: {x}")
    input("\nTekan ENTER untuk kembali...")


        
        
    
