import Login, register, Data
from prettytable import PrettyTable

t = PrettyTable()
t.field_names = ["Nama"]
t.add_row(["1. REGIS"])
t.add_row(["2. LOGIN"])
t.add_row(["3. KELUAR"])
t.align = "l"
t.header = False

t2 = PrettyTable()
t2.field_names = ["TERIMA KASIH"]

main = True
while main:
    try:
        print(t)
        
        main2 = int(input("INPUT ANGKA 1/2/3 : "))

        if main2 == 1:
            Data.clear()
            register.regis()

        elif main2 == 2:
            Data.clear()
            Login.login()

        elif main2 == 3:
            Data.clear()
            main = False
            print(t2)

        else:
            Data.clear()
            print("NOMOR TIDAK VALID\n")
    
    except ValueError:
        Data.clear()
        print("INPUT HANYA BERUPA ANGKA")