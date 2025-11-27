import os

super_admin = ("super", "123")

admin = {
    "admin 1" : ["juki", "12345"],
    "admin 2" : ["anto", "1234567890"]
}

users = {
    "user 1" : ["apel", "123", 0, [], []],
    "user 2" : ["mangga", "0000", 0, [], []]
}

def clear():
    os.system("cls" if os.name == "nt" else "clear")

