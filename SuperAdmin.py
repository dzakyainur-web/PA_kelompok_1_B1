import Tambah_Data_Admin, Lihat_Data_Admin, Hapus_Data_Admin, Ubah_Data_Admin

def SuperADMIN():
    SA = True
    while SA:
        print("""
        Super Admin
        1. Tambah Data Admin
        2. Lihat Data Admin
        3. Ubah Data Admin
        4. Hapus Admin
        5. Keluar
        """)

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
                SA = False

            else:
                print("input nomor yang tertera")

        except ValueError:
            print("hanya menerima angka")
