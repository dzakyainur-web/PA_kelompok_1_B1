from Data import users

def Hapus_DataUser():
    if len(users) == 0:
        print("BELUM ADA ADMIN")

    else:
        hapus = int(input("\nDATA NOMOR BERAPA YANG INGIN DI HAPUS? "))
        daftar_key = list(users.keys())

        if 1 <= hapus <= len(daftar_key):
            key_dihapus = daftar_key[hapus - 1]
            del users[key_dihapus]
            print(f"DATA USER '{key_dihapus}' BERHASIL DIHAPUS")

        else:
            print("NOMOR USER TIDAK VALID")