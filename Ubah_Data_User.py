from Data import users

def Ubah_DataUser():
    if len(users) == 0:
        print("DATA USER BELUM ADA.")
    
    else:
        print("===DATA USER===")
        for key, value in users.items():
            print(f"\n{key}\nNama: {value[0]}\nPassword: {value[1]}")
        
        ubah1 = int(input("Ubah User Nomor Berapa? "))
        daftar_key = list(users.keys())
        key_dipilih = daftar_key[ubah1 - 1]

        print("1. Ubah Nama")
        print("2. Ubah Password")

        ubah2 = input("Apa yang ingin Anda ubah? ")

        if ubah2 == "1":
            users[key_dipilih][0] = input("Masukkan nama baru")
            print("Nama berhasil diubah!")
        
        elif ubah2 == "2":
            users[key_dipilih][1] = input("Masukkan password baru: ")
            print("Password berhasil diubah")
        
        else:
            print("Pilihan tidak valid.")