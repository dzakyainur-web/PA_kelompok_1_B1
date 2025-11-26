from Data import admin, clear

def Ubah_DataAdmin():
    clear()
    if len(admin) == 0:
        print("BELUM ADA NASABAH")

    else:
        print("DAFTAR DATA ADMIN (PENGUBAHAN DATA) :")
        for key, value in admin.items():
            print(f"\n{key}\nNAMA : {value[0]}\nPASSWORD : {value[1]}")

        ubah1 = int(input("\nADMIN NOMOR BERAPA ? "))
        daftar_key = list(admin.keys())
        key_dipilih = daftar_key[ubah1 -1]

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

                admin[key_dipilih][0] = ubah3
                print("NAMA BERHASIL DIGANTI")
                input("TEKAN ENTER UNTUK MELANJUTKAN")
                clear()
                break

        elif ubah2 == '2':
            password_lama = admin[key_dipilih][1]
            while True:
                ubah4 = input("masukkan password baru : ".strip())
                if ubah4 == "":
                    print("password tidak boleh kosong".upper())
                    continue

                if password_lama == ubah4:
                    print("PASSWORD TIDAK BOLEH SAMA")
                    continue

                admin[key_dipilih][1] = ubah4
                print("PASSWORD BERHASIL DIGANTI")
                input("tekan enter untuk melanjutkan".upper())
                clear()
                break

        else:
            clear()
            print("tidak ada pilihan".upper())