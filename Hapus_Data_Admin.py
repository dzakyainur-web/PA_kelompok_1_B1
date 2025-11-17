from Data import admin

def Hapus_DataAdmin():
    if len(admin) == 0:
        print("BELUM ADA ADMIN")

    else:
        hapus = int(input("\nDATA NOMOR BBERAPA YANG INGIN DI HAPUS? "))
        daftar_key = list(admin.keys())

        if 1 <= hapus <= len(daftar_key):
            key_dihapus = daftar_key[hapus - 1]
            del admin[key_dihapus]
            print(f"DATA ADMIN '{key_dihapus}' BERHASIL DIHAPUS")

        else:
            print("NOMOR DATA ADMIN TIDAK VALID")