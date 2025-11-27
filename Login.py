import SuperAdmin
from Data import super_admin, admin, users, clear
from Menu_user import Menu_User
from menu_admin import menu_admin


def login():
    percobaan = 0
    login = True
    print("MAKSIMAL 3 KALI INPUT")
    while login:
        if percobaan < 3:

            print(f"INPUT KE-{percobaan+1}")

            username = input("masukkan username anda : ")
            password = input("masukkan password anda : ")


            if username == super_admin[0] and password == super_admin[1]:
                clear()
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
                        

                clear()
                percobaan += 1
                print("username atau password salah")
                login = True
            

        else:
            clear()
            print("SUDAH INPUT SEBANYAK 3 KALI")
            login = False
            