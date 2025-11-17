from Data import admin, users

def regis():
    regis = True 
    while regis:

        print("""
        1. Admin
        2. User
        3. Keluar
        """)
        reg = int(input("REGISTRASI SEBAGAI APA"))
        
        if reg == 1:
            print("=SILAHKAN REGISTRASI BAGI ADMIN BARU=")
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
                regis = False
                print("==BERHASIL REGISTRASI==")

        elif reg == 2:
            print("=SILAHKAN REGISTRASI BAGI USER BARU=")
            username = input("masukkan username anda : ")
            password = input("masukkan password anda : ")
            cek = False

            for sama2 in users:
                if users[sama2][0] == username:
                    cek = True
                    break

            if cek:
                print("======USERSERNAME TELAH DIGUNAKAN======\n")

            else:
                key_baru = "admin " + str(len(users)+1)
                users[key_baru] = [username, password]
                regis = False
                print("==BERHASIL REGISTRASI==")

        elif reg == 3:
            regis = False

        else :
            print("tidak masuk dalam pilihan")
