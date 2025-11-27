from Data import admin, users, super_admin, clear
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
                while True:
                    clear()
                    print("======= SILAKAN REGISTRASI ADMIN BARU ========")
                    print("= KETIK 'BATAL' UNTUK MEMBATALKAN REGISTRASI =")
                    print("========= INPUT TIDAK BOLEH KOSONG ===========")

                    username = input("\nMasukkan username: ").strip()

                    if username == "":
                        clear()
                        print("\nINPUT TIDAK BOLEH KOSONG")
                        input("\nTekan ENTER untuk kembali...")
                        continue

                    if username.upper() == "BATAL":
                        clear()
                        print("REGISTRASI DIBATALKAN")
                        input("\nTekan ENTER untuk kembali...")
                        clear()
                        return

                    password = input("Masukkan password: ").strip()
                    while password == "":
                        password = input("Masukkan password: ").strip()

                    cek1 = any(admin[key][0] == username for key in admin)
                    cek2 = any(users[key][0] == username for key in users)
                    cek3 = super_admin[0] == username

                    if cek1 or cek2 or cek3 == True:
                        print("===== USERNAME SUDAH TERPAKAI =====\n")
                        input("tekan enter untuk lanjutkan...".upper())
                        continue

                    else:
                        key_baru = f"admin_{len(admin) + 1}"
                        admin[key_baru] = [username, password]
                        print("== BERHASIL REGISTRASI ADMIN ==")
                        input("Tekan ENTER untuk melanjutkan...")
                        clear()
                        return

            # ==================== REGISTRASI USER ====================
            elif reg == 2:
                while True:
                    clear()
                    print("======== SILAKAN REGISTRASI USER BARU ========")
                    print("= KETIK 'BATAL' UNTUK MEMBATALKAN REGISTRASI =")
                    print("========= INPUT TIDAK BOLEH KOSONG ===========")


                    username = input("\nMasukkan username: ").strip()
                    if username == "":
                        clear()
                        print("\nINPUT TIDAK BOLEH KOSONG")
                        input("\nTekan ENTER untuk kembali...")
                        continue

                    if username.upper() == "BATAL":
                        clear()
                        print("REGISTRASI DIBATALKAN")
                        input("\nTekan ENTER untuk kembali...")
                        clear()
                        return
                    
                    password = input("Masukkan password: ").strip()
                    while password == "":
                        password = input("Masukkan password: ").strip()

                    cek1 = any(admin[key][0] == username for key in admin)
                    cek2 = any(users[key][0] == username for key in users)
                    cek3 = super_admin[0] == username

                    if cek1 or cek2 or cek3 == True:
                        print("===== USERNAME SUDAH TERPAKAI =====\n")
                        input("tekan enter untuk lanjutkan...".upper())
                        
                    else:
                        key_baru = f"user_{len(users) + 1}"
                        users[key_baru] = [username, password, 0, [], []]
                        print("== BERHASIL REGISTRASI USER ==")
                        input("Tekan ENTER untuk melanjutkan...")
                        clear()
                        return

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