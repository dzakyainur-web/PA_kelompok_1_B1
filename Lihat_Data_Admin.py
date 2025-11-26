from Data import admin, clear

def Lihat_DataAdmin():
    clear()
    print("DAFTAR DATA ADMIN :")
    if len(admin) == 0:
        print("BELUM ADA NASABAH")

    for key, value in admin.items():
        print(f"\n{key}\nNAMA : {value[0]}\nPASSWORD : {value[1]}")
    input("\nTEKAN ENTER UNTUK KEMBALI...")
    clear()