import os

super_admin = ("super", "123")

admin = {
    "admin 1" : ["Jaki", "12345"],
    "admin 2" : ["Attar", "1234567890"]
}

admin_terakhir = 2

users = {
    "user 1" : ["apel", "123", 0, [], []],
    "user 2" : ["mangga", "321", 0, [], []]
}

def clear():
    os.system("cls" if os.name == "nt" else "clear")

