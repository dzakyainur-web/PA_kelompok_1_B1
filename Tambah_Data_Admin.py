from Data import admin, clear

def Tambah_DataAdmin():
    clear()
    print("======= SILAKAN REGISTRASI ADMIN BARU ========")
    print("= KETIK 'BATAL' UNTUK MEMBATALKAN REGISTRASI =")
    print("========= INPUT TIDAK BOLEH KOSONG ===========")

    username = input("\nMasukkan username: ").strip()
    cek = False
    while username == "":
        clear()
        print("======= SILAKAN REGISTRASI ADMIN BARU ========")
        print("= KETIK 'BATAL' UNTUK MEMBATALKAN REGISTRASI =")
        print("========= INPUT TIDAK BOLEH KOSONG ===========")

        username = input("\nMasukkan username: ").strip()

    if username == "BATAL":
        clear()
        print("REGISTRASI DIBATALKAN")
        return

    password = input("Masukkan password: ").strip()
    while password == "":
        password = input("Masukkan password: ").strip()

    for sama1 in admin:
        if admin[sama1][0] == username:
            cek = True
            break

    if cek:
        print("======USERSERNAME TELAH DIGUNAKAN======\n")

    else:
        key_baru = "admin " + str(len(admin)+1)
        admin[key_baru] = [username, password]
        clear()
        print("\n==BERHASIL MENAMBAH ADMIN BARU==\n")