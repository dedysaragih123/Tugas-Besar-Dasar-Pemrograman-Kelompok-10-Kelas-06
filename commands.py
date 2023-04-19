"""
1 5 9 13 17 - Ciko
2 6 10 14 18 - Bagas
3 7 11 15 19 - Cinta
4 8 12 16 20 - Dedy
"""

from tools import string_strip, cari_index_username, data_remove

# untuk menyimpan data login, saat kosong bernilai ["","",""]
current_login = ["", "", ""]
# current_login : array [0..2] of string = ["", "", ""]

from data import users, candi, bahan_bangunan
# type Data : < isi_data : matriks of string,
#               n_baris : int,
#               n_kolom : int >

# Prosedur run(command, users, candi, bahan_bangunan):
# Membaca masukkan dari user dan melakukan command tersebut
def run(command: str) -> None:
    command = string_strip(command) # Agar command bersih dari spasi kosong
    global current_login
    if(command == "login"):
        current_login = login(current_login)
    elif(command == "logout"):
        current_login = logout(current_login)
    elif(current_login == ["" for _ in range(3)]):
        if(command == "help"):
            pass
        elif(command == "exit"):
            pass
        elif(any(command == string for string in ["logout","summonjin","hapusjin","ubahjin","bangun","kumpul","batchkumpul","batchbangun","laporanjin","laporancandi","hancurkancandi","ayamberkokok","save"])):
            print(f"{command} gagal!")
            print("Anda perlu login terlebih dahulu!")
        else:
            print(f"command \"{command}\" tidak dikenal.")
    else:
        if(command == "summonjin"):
            pass
        elif(command == "hapusjin"):
            pass
        elif(command == "ubahjin"):
            ubahjin(users)
        elif(command == "bangun"):
            pass
        elif(command == "kumpul"):
            pass
        elif(command == "batchkumpul"):
            pass
        elif(command == "batchbangun"):
            pass
        elif(command == "laporanjin"):
            if(current_login[2] == "bandung_bondowoso"):
                laporanjin(users,candi,bahan_bangunan)
            else:
                print("Laporan jin hanya dapat diakses oleh akun Bandung Bondowoso.")
        elif(command == "laporancandi"):
            pass
        elif(command == "hancurkancandi"):
            pass
        elif(command == "save"):
            pass
        elif(command == "help"):
            pass
        elif(command == "exit"):
            pass
        else:
            print(f"command \"{command}\" tidak dikenal.")

# F01 - Login 
# Fungsi login(users)
# Melakukan aksi login dan mengembalikan data hasil login yaitu array string [username,password,role]
def login(current_login) -> list[str]: 
    # KAMUS LOKAL
        # index : int
        # username, password : str
        # current_login : array [0..2] of string
            # data : matrix of string
    # ALGORITMA
    # Cek apakah sudah login atau belum
    if(current_login != ["" for _ in range(3)]):
        print("Login gagal!")
        print(f"Anda telah login dengan username {current_login[0]}, silahkan lakukan “logout” sebelum melakukan login kembali.")
        return current_login
    # unpack data users
    isi_users = users.isi
    # Input data login (sudah dibersihkan dari spasi awal dan akhir)
    username = input("Username: ")
    password = input("Password: ")
    # mencari index username, jika tidak ditemukan maka bernilai -1
    index = cari_index_username(users,username)
    if(index != -1): # username ditemukan 
        # cek apakah password sesuai atau tidak
        if(password == isi_users[index][1]):
            print(f"Selamat datang, {username}!")
            print("Masukkan command \"help\" untuk daftar command yang dapat kamu panggil")
            return isi_users[index]
        else: # password salah
            print("Password salah!")
            return ["" for _ in range(3)]
    else:
        print("Username tidak terdaftar!")
        return ["" for _ in range(3)]

# F02 - Logout 
# Fungsi logout()
# Melakukan logout akun dengan cara mengosongkan data current_login
def logout(current_login) -> list[str]:
    # KAMUS LOKAL
        # current_login : array [0..2] of string
    # ALGORITMA
    if(current_login == ["" for _ in range(3)]):
        print("Logout gagal!")
        print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
        return current_login
    else:
        current_login = ["" for _ in range(3)]
        print("Logout berhasil! ")
        return ["", "", ""]

# F03 - Summon Jin
# Fungsi summonjin()
# Mensummon / membuat jin baru
def summonjin():
    pass

# F04 - Hilangkan Jin
# Fungsi hapusjin()
# Menghapus jin serta candi yang dibuatnya
def hapusjin(users: list[list[list[str]],int,int], candi: list[list[list[str]],int,int]):
    # unpack data
    data_users = users[0]
    data_candi = candi[0]
    n_baris_users = users[1]
    n_baris_candi = candi[1]
    n_kolom_users = users[2]
    n_kolom_candi = candi[2]
    # input username
    username = input("Masukkan username jin : ")
    # cek username, jika tidak ditemukan maka bernilai -1
    index = cari_index_username(users,username)
    if(index == -1):
        print("Tidak ada jin dengan username tersebut.")
    else:
        jawab_hapus = input("Apakah anda yakin ingin menghapus jin dengan username Jin1 (Y/N)? ")
        if(jawab_hapus == "Y"): # jin dihapuskan
            print(users)
            # menghapuskan candi yang dibuat oleh jin tersebut
            for i in range(n_baris_candi):
                if data_candi[i][1] == username:
                    data_candi[i][1] = ""
                    data_candi[i][2] = ""
                    data_candi[i][3] = ""
            # hapus data jin tersebut
            data_users = data_remove(users,index)
            
            print("\nJin telah berhasil dihapus dari alam gaib.")
            print(users)
        elif(jawab_hapus == "N"): 
            quit()
        else: # bukan Y/N 
            print("Tidak ada opsi. Ulangi!")
            hapusjin(users,candi)

# F05 - Ubah Tipe Jin
# Prosedur ubahjin(users)
# Mengubah role dari jin, jika role pembangun maka dapat diubah ke pengumpul dan sebaliknya
def ubahjin(users: list[list[list[str]],int,int]) -> None:
    # KAMUS LOKAL
        # data : matrix of string
        # n_baris, i, index : int
        # username, ubah: str
        # ditemukan : bool
    # ALGORITMA
    # unpack data users
    data = users[0]
    n_baris = users[1]
    # input user
    username = input("Masukkan username jin: ")
    ditemukan = False
    # Cari username
    for i in range(n_baris):
        if(username == data[i][0]):
            ditemukan = True
            index = i
            break
    if(ditemukan): # username ditemukan
        if(data[index][2]=="jin_pengumpul"): # role pengumpul menjadi pembangun
            ubah = input("Jin ini bertipe \"Pengumpul\". Yakin ingin mengubah ke tipe \"Pembangun\" (Y/N)? ")
            if(ubah == "Y"):
                data[index][2] = "jin_pembangun"
                print("Jin telah berhasil diubah.")
            else:
                print("Jin tidak diubah.")
        else: # role pembangun menjadi pengumpul
            ubah = input("Jin ini bertipe \"Pembangun\". Yakin ingin mengubah ke tipe \"Pengumpul\" (Y/N)? ")
            if(ubah == "Y"):
                data[index][2] = "jin_pengumpul"
                print("Jin telah berhasil diubah.")
            else:
                print("Jin tidak diubah.")
    else: # username tidak ditemukan
        print("\nTidak ada jin dengan username tersebut.")
    users[0] = data

# F06 - Jin Pembangun
def bangun():
    pass

# F07 - Jin Pengumpul
def kumpul():
    pass

# F08 - Batch Kumpul/Bangun
def batchkumpul():
    pass
def batchbangun():
    pass

# F09 - Laporan Jin
def laporanjin(users: list[list[list[str]],int,int], candi: list[list[list[str]],int,int], bahan_bangunan: list[list[list[str]],int,int]) -> None:
    total_jin = 0
    total_pengumpul = 0
    total_pembangun = 0
    data_users = users[0]
    data_candi = candi[0]
    data_bahan_bangunan = bahan_bangunan[0]
    n_baris_users = users[1]
    n_baris_candi = candi[1]
    for i in range(n_baris_users):
        if(data_users[i][2] == "jin_pengumpul"):
            total_jin += 1
            total_pengumpul += 1
        elif(data_users[i][2] == "jin_pembangun"):
            total_jin += 1
            total_pembangun += 1
    print(f"> Total Jin: {total_jin}")
    print(f"> Total Jin Pengumpul: {total_pengumpul}")
    print(f"> Total Jin Pembangun: {total_pembangun}")
    
    # BAGIAN RIBET INI BELUM SELESAI
    
    print(f"> Jumlah Pasir : {data_bahan_bangunan[0][2]} unit")
    print(f"> Jumlah Batu : {data_bahan_bangunan[1][2]} unit")
    print(f"> Jumlah Air : {data_bahan_bangunan[2][2]} unit")

# F10 - Ambil Laporan Candi

# F11 - Hancurkan Candi

# F12 - Ayam Berkokok

# F13 - Load (Gunakan argparse)
# Prosedur load()
# Menggunakan argparse agar dapat meload / membuka kembali data yang sudah disave sebelumnya, 
# prosedur ini sendiri dijalankan hanya sekali saja pada command line / terminal
def load() -> None:
    import argparse
    # KAMUS LOKAL 
        # parser, args : objek dari library argparse
        # nama_folder : str
    parser = argparse.ArgumentParser(add_help=False,usage='%(prog)s <nama_folder>')
    parser.add_argument("nama_folder",nargs="?",type=str,default="")
    args = parser.parse_args() 
    if(args.nama_folder == ""):
        print("Tidak ada nama folder yang diberikan!\n")
        parser.print_usage()
        exit()
    elif(args.nama_folder == "src" ): # "src" karena file yang berisi data csv bernama src
        print("Loading...")
        # load data
        print("Selamat datang di program \"Manajerial Candi\"")
    else:
        print(f"Folder \"{args.nama_folder}\" tidak ditemukan.")
        exit()

# F14
def save():
    pass

# F15


#F16
def exit():
    print("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ",end='')
    jawab_exit = input()
    if jawab_exit == 'y'or jawab_exit == 'Y':
        save() 
        quit()
    elif jawab_exit == 'n' or jawab_exit == 'N':
        quit()
    else: 
        exit()


