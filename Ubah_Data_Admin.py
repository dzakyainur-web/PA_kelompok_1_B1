from Data import admin, clear

def Ubah_DataAdmin():
    UbahAdmin = True
    while UbahAdmin:
        clear()
        if len(admin) == 0:
            print("BELUM ADA ADMIN")
            input("\nketik ENTER untuk kembali...")
            UbahAdmin = False
            return

        else:
            print("KETIK 0 UNTUK MEMBATALKAN PENGUBAHAN DATA")
            print("DAFTAR DATA ADMIN (PENGUBAHAN DATA) :")
            daftar_key = list(admin.keys())
            for i, key in enumerate(daftar_key, start=1):
                print(f"\n{i}. {key}\nNAMA : {admin[key][0]}\nPASSWORD : {admin[key][1]}")

            ubah1 = input("\nADMIN NOMOR BERAPA ? ").strip()
            if ubah1 == "":
                print("INPUT TIDAK BOLEH KOSONG")
                input("TEKAN ENTER UNTUK KEMBALI...")
                clear()
                continue
            
            if not ubah1.isdigit():
                print("HANYA MENERIMA ANGKA")
                input("TEKAN ENTER UNTUK KEMBALI...")
                clear()
                continue

            ubah1 = int(ubah1)

            if ubah1 == 0:
                print("BATAL UBAH DATA")
                input("TEKAN ENTER UNTUK KEMBALI...")
                clear()
                return
            
            if not (1 <= ubah1 <= len(daftar_key)):
                print("NOMOR ADMIN TIDAK VALID")
                input("TEKAN ENTER UNTUK KEMBALI...")
                continue
            
            key_dipilih = daftar_key[ubah1 - 1]

            print("""
    1. NAMA
    2. PASSWORD
    """)
            ubah2 = input("APA YANG INGIN DI UBAH ? ")
            if ubah2 == '1':
                while True:
                    ubah3 = input("masukkan nama baru : ").strip()
                    if ubah3 == "":
                        print("nama tidak boleh kosong".upper())
                        continue

                    if ubah3 == '0':
                        print("BATAL UBAH DATA")
                        input("TEKAN ENTER UNTUK KEMBALI...")
                        clear()
                        return

                    admin[key_dipilih][0] = ubah3
                    print("NAMA BERHASIL DIGANTI")
                    input("TEKAN ENTER UNTUK MELANJUTKAN")
                    clear()
                    return

            elif ubah2 == '2':
                password_lama = admin[key_dipilih][1]
                while True:
                    ubah4 = input("masukkan password baru : ".strip())
                    if ubah4 == "":
                        print("password tidak boleh kosong".upper())
                        continue
                        
                    if ubah4 == '0':
                        print("BATAL UBAH DATA")
                        input("TEKAN ENTER UNTUK KEMBALI...")
                        clear()
                        return
                    
                    if password_lama == ubah4:
                        print("PASSWORD TIDAK BOLEH SAMA")
                        continue

                    admin[key_dipilih][1] = ubah4
                    print("PASSWORD BERHASIL DIGANTI")
                    input("tekan enter untuk melanjutkan".upper())
                    clear()
                    return

            elif ubah2 == '0':
                print("BATAL UBAH DATA")
                input("TEKAN ENTER UNTUK KEMBALI...")
                clear()
                return
            
            else:
                print("tidak ada pilihan".upper())
                input("tekan enter untuk melanjutkan".upper())
                clear()

