"""
1 5 9 13 17 - Ciko
2 6 10 14 18 - Bagas
3 7 11 15 19 - Cinta
4 8 12 16 20 - Dedy
"""

from tools import string_strip, string_in_array, cari_index_username, data_remove, data_append, int_min, int_maks
from tools import string_leksikografis_min, string_leksikografis_maks

# untuk menyimpan data login, saat kosong bernilai ["","",""]
current_login = ["", "", ""]
# current_login : array [0..2] of string = ["", "", ""]

from data import Data, users, candi, bahan_bangunan
# type Data : < isi_data : matriks of string,
#               n_baris : int,
#               n_kolom : int >

# Prosedur run(command):
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
            if(current_login[2] == "bandung_bondowoso"):
                summonjin(users)
            else:
                print("summonjin hanya dapat diakses oleh akun Bandung Bondowoso.")
        elif(command == "hapusjin"):
            if(current_login[2] == "bandung_bondowoso"):
                hapusjin(users,candi)
            else:
                print("hapusjin hanya dapat diakses oleh akun Bandung Bondowoso.")
        elif(command == "ubahjin"):
            if(current_login[2] == "bandung_bondowoso"):
                ubahjin(users)
            else:
                print("Ubahjin hanya dapat diakses oleh akun Bandung Bondowoso.")
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
    #print(users.isi, users.n_baris, sep=" -> ")

# F01 - Login 
# Fungsi login(current_login)
# Melakukan aksi login dan mengembalikan data hasil login yaitu array string [username,password,role]
def login(current_login: list[str]) -> list[str]: 
    # KAMUS LOKAL
        # index : int
        # username, password : str
        # current_login : array [0..2] of string
        # isi_users : matrix of string
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
# Fungsi logout(current_login)
# Melakukan logout akun dengan cara mengosongkan data current_login
def logout(current_login: list[str]) -> list[str]:
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
# Prosedur summonjin(users)
# Mensummon / membuat jin baru
def summonjin(users: Data) -> None:
    # KAMUS LOKAL
        # n_baris, i : int
        # jenis_jin, username, password, role : str
        # username_valid : bool
        # isi_users : matrix of string 
    # ALGORITMA
    #unpack data
    isi_users = users.isi
    n_baris = users.n_baris
    if(users.n_baris == 102):
        print("Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")
    else:
        print("Jenis jin yang dapat dipanggil:")
        print("  (1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
        print("  (2) Pembangun - Bertugas membangun candi")
        # menentukan jenis jin (pengumpul atau pembangun)
        while True:
            jenis_jin = string_strip(input("\nMasukkan nomor jenis jin yang ingin dipanggil: "))
            print()
            if(jenis_jin == "1"):
                role = "jin_pengumpul"
                print("Memilih jin \"Pengumpul\".")
                break
            elif(jenis_jin == "2"):
                role = "jin_pembangun"
                print("Memilih jin \"Pembangun\".")
                break
            else:
                print(f"Tidak ada jenis jin bernomor \"{jenis_jin}\"!")
        # membuat username yang valid
        while True:
            username = input("\nMasukkan username jin: ")
            username_valid = True
            for i in range(n_baris):
                if(isi_users[i][0] == username):
                    print(f"\nUsername \"{username}\" sudah diambil!")
                    username_valid = False
                    break
            if(username_valid):
                break
        # membuat password yang valid
        while True:
            password = input("Masukkan password jin: ")
            if(5<=len(password)<=25):
                print()
                break
            else:
                print("\nPassword panjangnya harus 5-25 karakter!")
            print()
        # tambahkan data pada users
        users = data_append(users,[username,password,role])
        print("Mengumpulkan sesajen...\nMenyerahkan sesajen...\nMembacakan mantra...")
        print(f"\nJin {username} berhasil dipanggil!")

# F04 - Hilangkan Jin
# Prosedur hapusjin(users,candi)
# Menghapus jin serta candi yang dibuatnya
def hapusjin(users: Data, candi: Data) -> None:
    # KAMUS LOKAL
        # n_baris_candi, i, index : int
        # username, jawab : str
        # isi_candi : matriks of string
    # ALGORITMA
    # unpack data
    isi_candi = candi.isi
    n_baris_candi = candi.n_baris
    # input username
    username = input("Masukkan username jin : ")
    # cek username, jika tidak ditemukan maka index bernilai -1 jika ditemukan maka index bernilai posisi index ditemukannya username
    index = cari_index_username(users,username)
    if(index == -1):
        print("Tidak ada jin dengan username tersebut.")
    else:
        jawab = input("Apakah anda yakin ingin menghapus jin dengan username Jin1 (Y/N)? ")
        if(jawab == "Y"): # jin dihapuskan
            # menghapuskan candi yang dibuat oleh jin tersebut
            for i in range(n_baris_candi):
                if(isi_candi[i][1] == username):
                    isi_candi[i][1] = ""
                    isi_candi[i][2] = ""
                    isi_candi[i][3] = ""
                    isi_candi[i][4] = ""
            # hapus data user jin tersebut
            users = data_remove(users,index)
            print("\nJin telah berhasil dihapus dari alam gaib.")
        elif(jawab != "N"): 
            print(f"Tidak ada opsi \"{jawab}\". Ulangi!")
            hapusjin(users,candi)            

# F05 - Ubah Tipe Jin
# Prosedur ubahjin(users)
# Mengubah role dari jin, jika role pembangun maka dapat diubah ke pengumpul dan sebaliknya
def ubahjin(users: Data) -> None:
    # KAMUS LOKAL
        # n_baris, i, index : int
        # username, ubah: str
        # ditemukan : bool
        # isi_users : matrix of string
    # ALGORITMA
    # unpack data 
    isi_users = users.isi
    # input user
    username = input("Masukkan username jin: ")
    # Cari username jika ditemukan maka mengembalikan indexnya jika tidak ditemukan maka bernilai -1
    index = cari_index_username(users,username)
    if(index != -1): # username ditemukan
        if(isi_users[index][2] == "jin_pengumpul"): # role pengumpul menjadi pembangun
            ubah = input("Jin ini bertipe \"Pengumpul\". Yakin ingin mengubah ke tipe \"Pembangun\" (Y/N)? ")
            if(ubah == "Y"):
                isi_users[index][2] = "jin_pembangun"
                print("Jin telah berhasil diubah.")
            else:
                print("Jin tidak diubah.")
        else: # role pembangun menjadi pengumpul
            ubah = input("Jin ini bertipe \"Pembangun\". Yakin ingin mengubah ke tipe \"Pengumpul\" (Y/N)? ")
            if(ubah == "Y"):
                isi_users[index][2] = "jin_pengumpul"
                print("Jin telah berhasil diubah.")
            else:
                print("Jin tidak diubah.")
    else: # username tidak ditemukan
        print("\nTidak ada jin dengan username tersebut.")
    users.isi = isi_users

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
# Prosedur laporanjin(users,candi,bahan_bangunan)
# Melakukan laporanjin mulai dari total jin masing-masing jenis, jin termalas dan terajin serta bahan bangunan
def laporanjin(users: Data, candi: Data, bahan_bangunan: Data) -> None:
    # KAMUS LOKAL
        # n_baris_users, n_baris_candi, total_jin, total_pengumpul, total_pembangun, i, index : int
        # n_jin, count_maks, count_min, candi_maks, candi_min, index_jin_maks, index_jin_min  : int
        # count_candi_jin : array of integer
        # jin_maks, jin min, jin : array of string
        # isi_users, isi_candi, isi_bahan_bangunan : matriks of string
    # ALGORITMA
    # unpack data
    isi_users = users.isi
    isi_candi = candi.isi
    isi_bahan_bangunan = bahan_bangunan.isi
    n_baris_users = users.n_baris
    n_baris_candi = candi.n_baris
    # menentukan jumlah jin dan tipenya
    total_jin = 0
    total_pengumpul = 0
    total_pembangun = 0
    for i in range(n_baris_users):
        if(isi_users[i][2] == "jin_pengumpul"):
            total_jin += 1
            total_pengumpul += 1
        elif(isi_users[i][2] == "jin_pembangun"):
            total_jin += 1
            total_pembangun += 1
    print(f"> Total Jin: {total_jin}")
    print(f"> Total Jin Pengumpul: {total_pengumpul}")
    print(f"> Total Jin Pembangun: {total_pembangun}")

    # MENCARI JIN TERMALAS DAN TERAJIN
    if(n_baris_candi == 0):
        print("> Jin Terajin: -")
        print("> Jin Termalas: -")
    else:
        n_jin = n_baris_users - 2 # -2 karena akun bondowoso dan Roro bukan jin
        jin = ["" for _ in range(n_jin)]
        for i in range(n_jin):
            jin[i] = isi_users[i+2][0]
        count_candi_jin = [0 for _ in range(n_jin)]
        for i in range(n_baris_candi):
            index = string_in_array(jin,isi_candi[i][1],n_jin)
            if(index != -1):
                count_candi_jin[index] += 1
        # maksimum minimum candi yang dibuat oleh seorang jin
        candi_maks = int_maks(count_candi_jin,n_jin)
        candi_min = int_min(count_candi_jin, n_jin)
        # Menghitung jumlah jin yang membangun candi dengan jumlah maksimum atau minimum
        count_maks = 0
        count_min = 0
        for i in range(n_jin): 
            if(count_candi_jin[i] == candi_maks):
                count_maks += 1
            if(count_candi_jin[i] == candi_min):
                count_min += 1
        # Mencari semua jin yang membangun candi dengan jumlah maksimum atau minimum ke dalam array of string
        jin_maks = ["" for _ in range(count_maks)]
        jin_min = ["" for _ in range(count_min)]
        index_jin_maks = 0
        index_jin_min = 0
        for i in range(n_jin): 
            if(count_candi_jin[i] == candi_maks):
                jin_maks[index_jin_maks] = jin[i]
                index_jin_maks += 1
            if(count_candi_jin[i] == candi_min):
                jin_min[index_jin_min] = jin[i]
                index_jin_min += 1
        # Mengembalikan jin termalas dan terajin berdasarkan leksikografis
        print(f"> Jin Terajin: {string_leksikografis_min(jin_maks,count_maks)}")
        print(f"> Jin Termalas: {string_leksikografis_maks(jin_min,count_min)}")

    # Menentukan jumlah bahan bangunan    
    print(f"> Jumlah Pasir : {isi_bahan_bangunan[0][2]} unit")
    print(f"> Jumlah Batu : {isi_bahan_bangunan[1][2]} unit")
    print(f"> Jumlah Air : {isi_bahan_bangunan[2][2]} unit")

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
        # args.nama_folder : str
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


