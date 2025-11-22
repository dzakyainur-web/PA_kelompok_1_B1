# from Data import admin, users, clear
# from prettytable import PrettyTable


# tabel = PrettyTable()
# tabel.field_names = ["cek"]
# tabel.add_row(["1. ADMIN"])
# tabel.add_row(["2. USER"])
# tabel.add_row(["3. KELUAR"])
# tabel.header = False
# tabel.align = "l"

# def regis():
#     regis = True 
#     while regis:
#         try:
#             print(tabel)
#             reg = int(input("REGISTRASI SEBAGAI APA ? "))
            
#             if reg == 1:
#                 print("=SILAHKAN REGISTRASI BAGI ADMIN BARU=")
#                 username = input("masukkan username anda : ")
#                 password = input("masukkan password anda : ")
#                 cek = False

#                 for sama1 in admin:
#                     if admin[sama1][0] == username:
#                         cek = True
#                         break

#                 if cek:
#                     print("======USERSERNAME TELAH DIGUNAKAN======\n")

#                 else:
#                     key_baru = "admin " + str(len(admin)+1)
#                     admin[key_baru] = [username, password]
#                     regis = False
#                     print("==BERHASIL REGISTRASI==")
#                     input("TEKAN ENTER UNTUK MELANJUTKAN")
#                     clear()

#             elif reg == 2:
#                 print("=SILAHKAN REGISTRASI BAGI USER BARU=")
#                 username = input("masukkan username anda : ")
#                 password = input("masukkan password anda : ")
#                 cek = False

#                 for sama2 in users:
#                     if users[sama2][0] == username:
#                         cek = True
#                         break

#                 if cek:
#                     print("======USERSERNAME TELAH DIGUNAKAN======\n")

#                 else:
#                     key_baru = "admin " + str(len(users)+1)
#                     users[key_baru] = [username, password]
#                     regis = False
#                     print("==BERHASIL REGISTRASI==")
#                     input("TEKAN ENTER UNTUK MELANJUTKAN")
#                     clear()

#             elif reg == 3:
#                 clear()
#                 regis = False

#             else :
#                 clear()
#                 print("tidak masuk dalam pilihan")
        
#         except ValueError:
#             clear()
#             print("INPUT HANYA BERUPA ANGKA")

from Data import admin, users, clear
from prettytable import PrettyTable

# Tabel menu registrasi
tabel = PrettyTable()
tabel.field_names = ["Pilihan"]
tabel.add_row(["1. ADMIN"])
tabel.add_row(["2. USER"])
tabel.add_row(["3. KELUAR"])
tabel.header = False
tabel.align = "l"

def regis():
    regis = True
    while regis:
        try:
            print(tabel)
            reg = int(input("REGISTRASI SEBAGAI APA? "))

            # ==================== REGISTRASI ADMIN ====================
            if reg == 1:
                print("= SILAKAN REGISTRASI ADMIN BARU =")
                username = input("Masukkan username: ")
                password = input("Masukkan password: ")

                # Cek apakah username sudah digunakan
                cek = any(admin[key][0] == username for key in admin)

                if cek:
                    print("===== USERNAME SUDAH TERPAKAI =====\n")
                else:
                    key_baru = f"admin_{len(admin) + 1}"
                    admin[key_baru] = [username, password]
                    print("== BERHASIL REGISTRASI ADMIN ==")
                    input("Tekan ENTER untuk melanjutkan...")
                    clear()
                    regis = False

            # ==================== REGISTRASI USER ====================
            elif reg == 2:
                print("= SILAKAN REGISTRASI USER BARU =")
                username = input("Masukkan username: ")
                password = input("Masukkan password: ")

                # Cek apakah username sudah digunakan
                cek = any(users[key][0] == username for key in users)

                if cek:
                    print("===== USERNAME SUDAH TERPAKAI =====\n")
                else:
                    key_baru = f"user_{len(users) + 1}"
                    users[key_baru] = [username, password, 0, [], []]
                    print("== BERHASIL REGISTRASI USER ==")
                    input("Tekan ENTER untuk melanjutkan...")
                    clear()
                    regis = False

            # ==================== KELUAR ====================
            elif reg == 3:
                clear()
                regis = False

            # ==================== SALAH INPUT ====================
            else:
                clear()
                print("Pilihan tidak valid!")

        except ValueError:
            clear()
            print("INPUT HARUS BERUPA ANGKA!")


