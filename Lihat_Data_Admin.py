from Data import admin

def Lihat_DataAdmin():
    if len(admin) == 0:
        print("BELUM ADA NASABAH")

    for key, value in admin.items():
        print(f"\n{key}\nNAMA : {value[0]}\nPASSWORD : {value[1]}")
    input("TEKAN ENTER UNTUK KEMBALI")