<<<<<<< Updated upstream
# from Data import users, clear

# def Hapus_User(userID):
#     clear()
#     print("=== HAPUS USER ===")

#     yakin = input("Apakah Anda yakin ingin menghapus user? (yes/no): ").lower()
#     if yakin != "yes":
#         print("Penghapusan dibatalkan.")
#         input("\nTekan ENTER untuk kembali...")
#         return
    
#     while True:
#         clear()
#         print("=== KONFIRMASI PENGHAPUSAN ===")
#         user = input("Masukkan username: ")
#         pw = input("Masukkan password: ")

#         if user in users and users[user][0] == pw:
#             break
#         else:
#             print("Username atau password salah, coba lagi!")
#             input("\nTekan ENTER untuk ulang...")

#     del users[user]
#     print(f"User '{user}' berhasil dihapus!")

#     input("\nTekan ENTER untuk kembali...")
=======
>>>>>>> Stashed changes
from Data import users, clear

def Hapus_User(userID):
    clear()
    print("=== HAPUS AKUN ===")

    yakin = input("Apakah Anda yakin ingin menghapus akun Anda? (yes/no): ").lower()
    if yakin != "yes":
        print("\nPenghapusan dibatalkan.")
        input("\nTekan ENTER untuk kembali...")
        return
    
    while True:
        clear()
        print("=== KONFIRMASI PENGHAPUSAN AKUN ===")
        print("\nKetik 'batal' jika kamu lupa password")
    
        pw = input("Masukkan password Anda: ")

        if pw.lower() == "batal":
            print("\nDIBATALKAN")
            input("\nTekan ENTER untuk kembali...")
            return
        
        if pw.strip() == "":
            print("\nPASSWORD TIDAK BOLEH KOSONG!!!")
            input("\nTekan ENTER untuk kembali...")
            continue

        if pw != users[userID][1]:
            print("\nPassword salah!")
            input("\nTekan ENTER untuk ulang...")
            continue
        

        break

    username = users[userID][0]
    del users[userID]

    print(f"Akun '{username}' berhasil dihapus!")
    input("\nTekan ENTER untuk kembali...")
