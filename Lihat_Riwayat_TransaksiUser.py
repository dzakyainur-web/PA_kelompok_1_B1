from Data import users

def Lihat_Riwayat_Transaksi_User():
    if len(users) == 0:
        print("DATA USER BELUM ADA.")
    
    else:
        print("===DATA USER===")
        for key, value in users.items():
            print(f"\n{key}\nNama: {value[0]}\nPassword: {value[1]}")
        
        lihat = int(input("Lihat Riwayat Transaksi User Nomor Berapa? "))
        daftar_key = list(users.keys())
        key_dipilih = daftar_key[lihat - 1]
        riwayat_transaksi = users[key_dipilih][2]
        
        if len(riwayat_transaksi) == 0:
            print(f"Tidak ada riwayat transaksi untuk user '{key_dipilih}'.")
        else:
            print(f"Riwayat Transaksi untuk user '{key_dipilih}':")
            for transaksi in riwayat_transaksi:
                print(f"{transaksi}")
    input("\nTekan ENTER untuk kembali")



    
