from Data import users, clear

def Ganti_Password(userID):
    clear()
    print("=== GANTI PASSWORD ===")

    yakin = input("Yakin ingin mengganti password? (yes/no): ").strip().lower()
    if yakin != "yes":
        print("\nDIBATALKAN")
        input("\nTekan ENTER untuk kembali...")
        return
    
    while True:
        clear()
        print("\n=== GANTI PASSWORD ===")
        print("\nKetik 'batal' jika lupa password")

        # INPUT PASSWORD LAMA
        pw_lama = input("Masukkan password lama: ").strip()

        if pw_lama == "":
            print("\nTIDAK BOLEH KOSONG!")
            input("\nTekan ENTER untuk kembali...")
            continue

        if pw_lama.lower() == "batal":
            print("\nDIBATALKAN")
            input("\nTekan ENTER untuk kembali...")
            return
        
        if pw_lama != users[userID][1]:
            print("\nPassword lama salah!")
            input("\nTekan ENTER untuk kembali...")
            continue

        # INPUT PASSWORD BARU
        pw_baru = input("Masukkan password baru: ").strip()

        if pw_baru == "":
            print("\nPASSWORD BARU TIDAK BOLEH KOSONG!")
            input("\nTekan ENTER untuk kembali...")
            continue

        if pw_baru == pw_lama:
            print("\nPASSWORD BARU TIDAK BOLEH SAMA DENGAN YANG LAMA!")
            input("\nTekan ENTER untuk kembali...")
            continue

        # KONFIRMASI PASSWORD BARU
        konfirmasi = input("Konfirmasi password baru: ").strip()

        if konfirmasi == "":
            print("\nKONFIRMASI TIDAK BOLEH KOSONG!")
            input("\nTekan ENTER untuk kembali...")
            continue

        if pw_baru != konfirmasi:
            print("\nPassword tidak sama!")
            input("\nTekan ENTER untuk kembali...")
            continue

        break

    users[userID][1] = pw_baru
    print("\nPassword berhasil diganti!")
    input("\nTekan ENTER untuk kembali...")
