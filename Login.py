import SuperAdmin
from Data import super, admin, users
from Menu_user import Menu_User
from menu_admin import menu_admin


def login():
    percobaan = 0
    login = True
    while login:
        if percobaan < 3:
            print("COBA AJA NIH")
            username = input("masukkan username anda : ")
            password = input("masukkan password anda : ")


            if username == super[0] and password == super[1]:
                print("superadmin")
                SuperAdmin.SuperADMIN()
                break

            else:    
                for key, value in admin.items():
                    if username == value[0] and password == value[1]:
                        print(f"""
                ====ANDA BERHASIL LOGIN SEBAGAI ADMIN====
                SELAMAT DATANG {value[0]}\n""")
                        menu_admin(key)
                        return key

                for key, value in users.items():
                    if username == value[0] and password == value[1]:
                        print(f"""
                ====ANDA BERHASIL LOGIN SEBAGAI USER====
                SELAMAT DATANG {value[0]}\n""")
                        Menu_User(key)  
                        return key
                        

                percobaan += 1
                print("username atau password salah")
                login = True
            

        else:
            print("sudah mencoba 3 kali")
            login = False

