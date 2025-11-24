from Data import admin, clear

def Tambah_DataAdmin():
    clear()
    print("=silahkan registrasi untuk admin baru=".upper())
    username = input("masukkan username anda : ")
    password = input("masukkan password anda : ")
    cek = False

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
        print("==BERHASIL REGISTRASI==")