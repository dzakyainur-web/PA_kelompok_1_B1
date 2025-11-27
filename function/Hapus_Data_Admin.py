from Data import admin, clear

def Hapus_DataAdmin():
    hapus1 = True
    while hapus1:
        if len(admin) == 0:
            print("BELUM ADA ADMIN")
            hapus1 = False

        else:
            clear()
            print("DAFTAR DATA ADMIN :")
            print("KETIK 0 UNTUK BATAL MENGHAPUS DATA")

            daftar_key = list(admin.keys())
            for i, key in enumerate (daftar_key, start=1):
                print(f"\n{i}. {key}\nNAMA : {admin[key][0]}\nPASSWORD : {admin[key][1]}")
                
            hapus = input("\nDATA NOMOR BBERAPA YANG INGIN DI HAPUS? ").strip()

            if hapus == "":
                print("INPUT TIDAK BOLEH KOSONG")
                input("TEKAN ENTER UNTUK KEMBALI...")
                continue

            if not hapus.isdigit():
                print("HANYA MENERIMA ANGKA")
                input("TEKAN ENTER UNTUK KEMBALI...")
                continue

            hapus = int(hapus)

            if hapus == 0:
                print("MEMBATALKAN PENGHAPUSAN DATA")
                input("TEKAN ENTER UNTUK KEMBALI...")
                clear()
                return

            if 1 <= hapus <= len(daftar_key):
                key_dihapus = daftar_key[hapus - 1]
                del admin[key_dihapus]
                print(f"DATA ADMIN '{key_dihapus}' BERHASIL DIHAPUS")
                input("TEKAN ENTER UNTUK KEMBALI...")
                clear()
                return

            else:
                clear()
                print("NOMOR DATA ADMIN TIDAK VALID")
                input("TEKAN ENTER UNTUK KEMBALI...")
                hapus1 = True
