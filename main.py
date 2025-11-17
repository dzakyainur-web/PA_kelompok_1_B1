import os
import Login, register

def clear():
    os.system("clear | cls")

main = True
while main:
    print("""
1. regis
2. login
3. keluar
""")
    
    main2 = int(input("masukkkan nomor 1/2/3 : "))

    if main2 == 1:
        print("1")
        register.regis()

    elif main2 == 2:
        Login.login()

    elif main2 == 3:
        print("3")
        main = False

    else:
        print("masukkan 1/2/3")




    