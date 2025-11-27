from Data import admin, clear

def Lihat_DataAdmin():
    clear()
    print("DAFTAR DATA ADMIN :")
    if len(admin) == 0:
        print("BELUM ADA NASABAH")
        clear()
        return

    for i, (key, value) in enumerate(admin.items(), start=1):
        print(f"\n{i}. {key}")
        print(f"   NAMA     : {value[0]}")
        print(f"   PASSWORD : {value[1]}")

    input("\nTEKAN ENTER UNTUK KEMBALI...")
    clear()