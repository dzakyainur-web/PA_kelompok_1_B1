from Data import users, clear

def Hapus_User(userID):
    clear()
    print("=== HAPUS AKUN ===")

    konfirm = input("Apakah Anda yakin ingin menghapus akun Anda? (yes/no): ").strip().lower()
    if konfirm != "yes":
        print("Penghapusan dibatalkan.")
        input("\nTekan ENTER untuk kembali...")
        return False

    while True:
        clear()
        print("\n=== PASTIKAN INI AKUN MU ===")
        print("Ketik 'batal' untuk membatalkan dan kembali ke menu.")
        
        pw_input = input("\nMasukkan password akun Anda: ").strip().lower()

        clear()
        if pw_input == "":
            print("\nINPUT TIDAK BOLEH KOSONG")
            print("\nTekan ENTER untuk kembali...")
            continue

        clear()
        if pw_input == "batal":
            print("Penghapusan dibatalkan.")
            input("\nTekan ENTER untuk kembali...")
            return False

        clear()
        if users[userID][1] == pw_input:
            del users[userID]
            print(f"Akun '{userID}' berhasil dihapus.")
            input("\nTekan ENTER untuk melanjutkan...")
            return True
        else:
            print("Password salah! Jika lupa, ketik 'batal' untuk kembali.")
            input("\nTekan ENTER untuk ulang...")
