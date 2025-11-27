from Data import admin, super_admin, users, admin_terakhir, clear

def Tambah_DataAdmin():
    global admin_terakhir

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
        key_baru = f"admin {admin_terakhir}"
        admin[key_baru] = [username, password]
        print(f"== BERHASIL REGISTRASI ADMIN {key_baru} ==")
        input("Tekan ENTER untuk melanjutkan...")
        clear()
        return