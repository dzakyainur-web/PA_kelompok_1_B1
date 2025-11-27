from Data import admin, users, super_admin, admin_terakhir, clear
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
    global admin_terakhir
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

                    if len(admin) > 0:
                        print("\nDAFTAR ADMIN SAAT INI:")
                        for i, key in enumerate(admin.keys(), start=1):
                            print(f"{i}. {key} (username: {admin[key][0]})")

                    else:
                        print("\nBELUM ADA ADMIN")

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
                    
                    admin_terakhir += 1
                    key_baru = f"admin_{admin_terakhir}"
                    admin[key_baru] = [username, password]
                    print(f"== BERHASIL REGISTRASI ADMIN {key_baru} ==")
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