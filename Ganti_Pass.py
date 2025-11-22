from Data import users, clear

def Ganti_Password(userID):
    clear()
    print("=== GANTI PASSWORD ===")

    yakin = input("Yakin ingin mengganti password? (yes/no): ").lower()
    if yakin != "yes":
        print("Dibatalkan...")
        input("\nTekan ENTER untuk kembali...")
        return
    
    while True:
        clear()
        print("=== GANTI PASSWORD ===")
        pw_lama = input("Masukkan password lama: ")

        if pw_lama != users[userID][1]:
            print("Password lama salah!")
            input("\nTekan ENTER untuk kembali...")
            return
        else:
            break  

    pw_baru = input("Masukkan password baru: ")
    konfirmasi = input("Konfirmasi password baru: ")

    if pw_baru != konfirmasi:
        print("Password tidak sama!")
        input("\nTekan ENTER untuk kembali...")
        return

    users[userID][1] = pw_baru
    print("\nPassword berhasil diganti!")
    input("\nTekan ENTER untuk kembali...")
