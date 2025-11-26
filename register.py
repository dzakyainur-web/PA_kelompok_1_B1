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
                clear()
                print("======= SILAKAN REGISTRASI ADMIN BARU ========")
                print("= KETIK 'BATAL' UNTUK MEMBATALKAN REGISTRASI =")
                print("========= INPUT TIDAK BOLEH KOSONG ===========")

                username = input("\nMasukkan username: ").strip()
                while username == "":
                    clear()
                    print("======= SILAKAN REGISTRASI ADMIN BARU ========")
                    print("= KETIK 'BATAL' UNTUK MEMBATALKAN REGISTRASI =")
                    print("========= INPUT TIDAK BOLEH KOSONG ===========")

                    username = input("\nMasukkan username: ").strip()

                if username == "BATAL":
                    clear()
                    print("REGISTRASI DIBATALKAN")
                    regis = False
                    return

                password = input("Masukkan password: ").strip()
                while password == "":
                    password = input("Masukkan password: ").strip()

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
                clear()
                print("======== SILAKAN REGISTRASI USER BARU ========")
                print("= KETIK 'BATAL' UNTUK MEMBATALKAN REGISTRASI =")
                print("========= INPUT TIDAK BOLEH KOSONG ===========")


                username = input("\nMasukkan username: ").strip()
                while username == "":
                    clear()
                    print("======== SILAKAN REGISTRASI USER BARU ========")
                    print("= KETIK 'BATAL' UNTUK MEMBATALKAN REGISTRASI =")
                    print("========= INPUT TIDAK BOLEH KOSONG ===========")
                    username = input("\nMasukkan username: ").strip()

                if username == "BATAL":
                    clear()
                    print("REGISTRASI DIBATALKAN")
                    regis = False
                    return
                
                password = input("Masukkan password: ").strip()
                while password == "":
                    password = input("Masukkan password: ").strip()

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
            print("COBA-COBA")