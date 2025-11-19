from Data import users

def Lihat_DataUser():
    if len(users) == 0:
        print("Data User belum tersedia!")
    else:
        for key, value in users.items():
            print(f"\n{key}\nNama : {value[0]}\nPassword : {value[1]}")
    input("\nTekan ENTER untuk kembali")