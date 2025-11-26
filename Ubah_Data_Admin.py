# from Data import admin, clear

# def Ubah_DataAdmin():
#     UbahAdmin = True
#     while UbahAdmin:
#         clear()
#         if len(admin) == 0:
#             print("BELUM ADA ADMIN")
#             input("\nketik ENTER untuk kembali...")
#             UbahAdmin = False

#         else:
#             print("DAFTAR DATA ADMIN (PENGUBAHAN DATA) :")
#             for key, value in admin.items():
#                 print(f"\n{key}\nNAMA : {value[0]}\nPASSWORD : {value[1]}")

#             ubah1 = int(input("\nADMIN NOMOR BERAPA ? ").strip())
#             if ubah1 == "":
#                 print("INPUT TIDAK BOLEH KOSONG")
#                 input("TEKAN ENTER UNTUK KEMBALI...")
#                 clear()
            
#             daftar_key = list(admin.keys())
#             key_dipilih = daftar_key[ubah1 -1]

#             print("""
#     1. NAMA
#     2. PASSWORD
#     """)
#             ubah2 = input("APA YANG INGIN DI UBAH ? ")
#             if ubah2 == '1':
#                 while True:
#                     ubah3 = input("masukkan nama baru : ").strip()
#                     if ubah3 == "":
#                         print("nama tidak boleh kosong".upper())
#                         continue

#                     admin[key_dipilih][0] = ubah3
#                     print("NAMA BERHASIL DIGANTI")
#                     input("TEKAN ENTER UNTUK MELANJUTKAN")
#                     clear()
#                     break

#             elif ubah2 == '2':
#                 password_lama = admin[key_dipilih][1]
#                 while True:
#                     ubah4 = input("masukkan password baru : ".strip())
#                     if ubah4 == "":
#                         print("password tidak boleh kosong".upper())
#                         continue

#                     if password_lama == ubah4:
#                         print("PASSWORD TIDAK BOLEH SAMA")
#                         continue

#                     admin[key_dipilih][1] = ubah4
#                     print("PASSWORD BERHASIL DIGANTI")
#                     input("tekan enter untuk melanjutkan".upper())
#                     clear()
#                     break

#             else:
#                 clear()
#                 print("tidak ada pilihan".upper())
from Data import admin, clear

def Ubah_DataAdmin():
    UbahAdmin = True
    while UbahAdmin:
        clear()
        if len(admin) == 0:
            print("BELUM ADA ADMIN")
            input("\nKetik ENTER untuk kembali...")
            UbahAdmin = False
            return

        # tampilkan daftar admin
        while True:
            clear()
            print("DAFTAR DATA ADMIN (PENGUBAHAN DATA) :")
            for key, value in admin.items():
                print(f"\n{key}\nNAMA : {value[0]}\nPASSWORD : {value[1]}")

        # --- input nomor admin dengan validasi ---
            raw = input("\nADMIN NOMOR BERAPA ? ").strip()
            if raw == "":
                print("INPUT TIDAK BOLEH KOSONG")
                input("TEKAN ENTER UNTUK KEMBALI...")
                clear
                continue  

            try:
                ubah1 = int(raw)
            except ValueError:
                print("MASUKKAN ANGKA YANG VALID!")
                input("TEKAN ENTER UNTUK MENGULANG...")
                clear()
                # tampilkan ulang daftar, ulangi loop input nomor
                for key, value in admin.items():
                    print(f"\n{key}\nNAMA : {value[0]}\nPASSWORD : {value[1]}")
                continue

            # cek range
            daftar_key = list(admin.keys())
            if ubah1 < 1 or ubah1 > len(daftar_key):
                print("NOMOR ADMIN TIDAK TERSEDIA!")
                input("TEKAN ENTER UNTUK MENGULANG...")
                clear()
                # tampil ulang daftar
                for key, value in admin.items():
                    print(f"\n{key}\nNAMA : {value[0]}\nPASSWORD : {value[1]}")
                continue

            # jika valid, ambil key yang dipilih dan keluar dari loop input nomor
            key_dipilih = daftar_key[ubah1 - 1]
            break

        # pilihan ubah (nama / password)
        print("""
1. NAMA
2. PASSWORD
""")
        ubah2 = input("APA YANG INGIN DI UBAH ? ").strip()

        if ubah2 == '1':
            while True:
                ubah3 = input("Masukkan nama baru : ").strip()
                if ubah3 == "":
                    print("NAMA TIDAK BOLEH KOSONG")
                    continue
                admin[key_dipilih][0] = ubah3
                print("NAMA BERHASIL DIGANTI")
                input("TEKAN ENTER UNTUK MELANJUTKAN")
                clear()
                break

        elif ubah2 == '2':
            password_lama = admin[key_dipilih][1]
            while True:
                ubah4 = input("Masukkan password baru : ").strip()
                if ubah4 == "":
                    print("PASSWORD TIDAK BOLEH KOSONG")
                    continue
                if ubah4 == password_lama:
                    print("PASSWORD TIDAK BOLEH SAMA DENGAN PASSWORD LAMA")
                    continue
                admin[key_dipilih][1] = ubah4
                print("PASSWORD BERHASIL DIGANTI")
                input("TEKAN ENTER UNTUK MELANJUTKAN")
                clear()
                break
        else:
            clear()
            print("TIDAK ADA PILIHAN".upper())
            input("TEKAN ENTER UNTUK KEMBALI...")
            clear()
