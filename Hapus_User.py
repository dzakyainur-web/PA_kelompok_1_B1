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
from Data import users, clear

def Hapus_User(userID):
    clear()
    print("=== HAPUS USER ===")

    yakin = input("Apakah Anda yakin ingin menghapus user? (yes/no): ").lower()
    if yakin != "yes":
        print("Penghapusan dibatalkan.")
        input("\nTekan ENTER untuk kembali...")
        return
    
    # Mencari userID yang cocok berdasarkan username input
    while True:
        clear()
        print("=== KONFIRMASI PENGHAPUSAN ===")
        username = input("Masukkan username: ")
        pw = input("Masukkan password: ")

        # Cari user berdasarkan username
        targetID = None
        for key, value in users.items():
            if value[0] == username and value[1] == pw:
                targetID = key
                break

        if targetID:
            break
        else:
            print("Username atau password salah, coba lagi!")
            input("\nTekan ENTER untuk ulang...")

    del users[targetID]
    print(f"User '{username}' berhasil dihapus!")

    input("\nTekan ENTER untuk kembali...")
