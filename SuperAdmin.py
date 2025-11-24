import Tambah_Data_Admin, Lihat_Data_Admin, Hapus_Data_Admin, Ubah_Data_Admin
from prettytable import PrettyTable
from Data import clear

def SuperADMIN():
    tabel = PrettyTable()
    tabel.title = "SUPER ADMIN"
    tabel.field_names = ["MENU"]
    tabel.add_row(["1. Tambah Data Admin"])
    tabel.add_row(["2. Lihat Data Admin"])
    tabel.add_row(["3. Ubah Data Admin"])
    tabel.add_row(["4. Hapus Admin"])
    tabel.add_row(["5. Keluar"])
    tabel.align = "l"
    tabel.align["SUPER ADMIN"] = "c"
    tabel.header = False

    SA = True
    while SA:
        print(tabel)

        try:
            superadmin = int(input("silahkan masukkan nomor : "))

            if superadmin == 1:
                Tambah_Data_Admin.Tambah_DataAdmin()

            elif superadmin == 2:
                Lihat_Data_Admin.Lihat_DataAdmin()

            elif superadmin == 3:
                Ubah_Data_Admin.Ubah_DataAdmin()

            elif superadmin == 4:
                Hapus_Data_Admin.Hapus_DataAdmin()

            elif superadmin == 5:
                clear()
                SA = False

            else:
                print("input nomor yang tertera")

        except ValueError:
            print("hanya menerima angka")
