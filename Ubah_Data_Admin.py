from Data import admin

def Ubah_DataAdmin():
    if len(admin) == 0:
        print("BELUM ADA NASABAH")

    else:
        print("DAFTAR ADMIN :")
        for key, value in admin.items():
            print(f"\n{key}\nNAMA : {value[0]}\nPASSWORD : {value[1]}")

        ubah1 = int(input("ADMIN NOMOR BERAPA ? "))
        daftar_key = list(admin.keys())
        key_dipilih = daftar_key[ubah1 -1]

        print("""
1. NAMA
2. PASSWORD
""")
        ubah2 = input("APA YANG INGIN DI UBAH ? ")
        if ubah2 == '1':
            admin[key_dipilih][0] = input("masukkan nama baru : ")
            print("NAMA BERHASIL DIGANTI")

        elif ubah2 == '2':
            admin[key_dipilih][1] = input("masukkan nama baru : ")
            print("NAMA BERHASIL DIGANTI")

        else:
            print("tidak ada pilihan")