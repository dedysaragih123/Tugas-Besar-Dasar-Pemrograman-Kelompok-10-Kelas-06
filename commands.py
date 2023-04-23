"""
1 5 9 13 17 - Ciko
2 6 10 14 18 - Bagas
3 7 11 15 19 - Cinta
4 8 12 16 20 - Dedy
"""

from tools import cari_index_username, data_remove, data_append, int_min, int_maks, int_join, generate_bahan_bangunan
from tools import string_split, string_strip, string_append, string_in_array, string_leksikografis_min, string_leksikografis_maks


# untuk menyimpan data login, saat kosong bernilai ["","",""]
current_login = ["", "", ""]
# current_login : array [0..2] of string = ["", "", ""]

from data import data_save, data_load, Data
# type Data : < isi_data : matriks of string,
#               n_baris : int,
#               n_kolom : int >

# Prosedur run(command):
# Membaca masukkan dari user dan melakukan command tersebut
def run(command: str, users: Data, candi: Data ,bahan_bangunan: Data) -> None:  
    command = string_strip(command) # Agar command bersih dari spasi kosong
    global current_login
    if(command == "login"):
        current_login = login(current_login, users)
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
            if(current_login[2] == "jin_pembangun"):
                bangun(users,candi,bahan_bangunan,current_login[0])
            else:
                print("bangun hanya dapat diakses oleh akun Jin Pembangun")
        elif(command == "kumpul"):
            if(current_login[2] == "jin_pengumpul"):
                kumpul(bahan_bangunan,1,False)
            else:
                print("kumpul hanya dapat diakses oleh akun Jin Pembangun")
        elif(command == "batchkumpul"):
            if(current_login[2] == "bandung_bondowoso"):
                batchkumpul(users,bahan_bangunan)
            else:
                print("batchkumpul hanya dapat diakses oleh akun Bandung Bondowoso.")
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
        elif(command == "ayamberkokok"):
            if(current_login[2] == "roro_jonggrang"):
                ayamberkokok(candi)
            else:
                print("ayamberkokok hanya dapat diakses oleh akun Roro Jonggrang.")
        elif(command == "save"):
            save(users, candi, bahan_bangunan)
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
def login(current_login: list[str], users: Data) -> list[str]: 
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
        # isi_candi : matrix of string
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

def bangun(users: Data, candi: Data, bahan_bangunan: Data, pembuat: str):
    # unpack data
    isi_users = users.isi
    isi_candi = candi.isi
    isi_bahan_bangunan = bahan_bangunan.isi 
    n_baris_candi = candi.n_baris
    # bahan dalam format [pasir,batu,air]
    bahan_dimiliki = [int(isi_bahan_bangunan[0][2]),int(isi_bahan_bangunan[1][2]),int(isi_bahan_bangunan[2][2])]
    bahan_diperlukan = generate_bahan_bangunan()
    if(bahan_dimiliki[0] < bahan_diperlukan[0] or bahan_dimiliki[1] < bahan_diperlukan[1] or bahan_dimiliki[2] < bahan_diperlukan[2]):
        print(f"# Men-generate bahan bangunan ({bahan_diperlukan[0]} pasir, {bahan_diperlukan[1]} batu, dan {bahan_diperlukan[2]} air)")
        print(f"# Memiliki {bahan_dimiliki[0]} pasir, {bahan_dimiliki[1]} batu, {bahan_dimiliki[2]} air")
        print("Bahan bangunan tidak mencukupi.")
        print("Candi tidak bisa dibangun!")
    else:
        # Mengurangi bahan bangunan yang dimiliki
        isi_bahan_bangunan[0][2] = str(int(isi_bahan_bangunan[0][2]) - bahan_diperlukan[0])
        isi_bahan_bangunan[1][2] = str(int(isi_bahan_bangunan[1][2]) - bahan_diperlukan[1])
        isi_bahan_bangunan[2][2] = str(int(isi_bahan_bangunan[2][2]) - bahan_diperlukan[2])
        bahan_bangunan.isi = isi_bahan_bangunan
        # Menghitung jumlah candi yang sudah dibangun 
        count_candi = 0
        for i in range(n_baris_candi):
            if(isi_candi[i][1] != ""):
                count_candi += 1
        if(count_candi < 100): 
            if(count_candi == n_baris_candi): # jika semua baris data candi sudah terisi make buat baris baru
                candi = data_append(candi,[str(n_baris_candi+2),pembuat,str(bahan_diperlukan[0]),str(bahan_diperlukan[1]),str(bahan_diperlukan[2])])
            else:
                for i in range(n_baris_candi):
                    if(isi_candi[i][1] == ""): # indeks candi yang kosong diisi
                        isi_candi[i][1] = pembuat
                        isi_candi[i][2] = str(bahan_diperlukan[0])
                        isi_candi[i][3] = str(bahan_diperlukan[1])
                        isi_candi[i][4] = str(bahan_diperlukan[2])
                        candi.isi = isi_candi
                        break
            print("Candi berhasil dibangun.")
            print(f"Sisa candi yang perlu dibangun: {100-count_candi}")
        else:
            print("Candi berhasil dibangun.")
            print("Sisa candi yang perlu dibangun: 0")

# F07 - Jin Pengumpul ....  REKURSIF!!
# Prosedur kumpul(bahan_bangunan)    
# Mengumpulkan bahan bangunan yang jumlahnya secara acak
def kumpul(bahan_bangunan: Data, jumlah_loop :int, kumpul_batch:bool) -> list[int]:
    # KAMUS LOKAL
        # bahan_dikumpul : array[0..2] of integer
        # isi_bahan_bangunan : matrix of string
    # ALGORITMA
    # unpack data
    isi_bahan_bangunan = bahan_bangunan.isi
    # menentukan jumlah bahan yang dikumpul (acak)
    # bahan_dikumpul dalam format [pasir, batu, air]
    bahan_dikumpul = generate_bahan_bangunan()
    # menambahkan bahan bangunan yang dikumpul ke bahan bangunan total
    isi_bahan_bangunan[0][2] = str(int(isi_bahan_bangunan[0][2]) + bahan_dikumpul[0])
    isi_bahan_bangunan[1][2] = str(int(isi_bahan_bangunan[1][2]) + bahan_dikumpul[1])
    isi_bahan_bangunan[2][2] = str(int(isi_bahan_bangunan[2][2]) + bahan_dikumpul[2])
    bahan_bangunan.isi = isi_bahan_bangunan
    if(kumpul_batch == False): # jika bukan batch kumpul maka tidak perlu diprint
        print(f"Jin menemukan {bahan_dikumpul[0]} pasir, {bahan_dikumpul[1]} batu, dan {bahan_dikumpul[2]} air.")
    elif(jumlah_loop != 1): # jika kumpul_batch = True, jika jumlah_loop yang perlu dilakukan lebih dari 1 maka perlu rekursif
        return int_join(bahan_dikumpul,kumpul(bahan_bangunan,jumlah_loop-1,True),3)
    else: # jika jumlah_loop = 1 maka tidak perlu rekursif
        return bahan_dikumpul

# F08 - Batch Kumpul/Bangun
# Prosedur batchkumpul(users, bahan_bangunan)
# Melakukan pengumpulan bahan bangunan oleh semua jin pengumpul yang ada 
def batchkumpul(users: Data, bahan_bangunan: Data) -> None:
    # KAMUS LOKAL
        # i, n_baris_users, count_jin_pengumpul : int
        # hasil_kumpul : array[0..2] of integer
        # isi_users : matrix of string
    # ALGORITMA
    # unpack data
    isi_users = users.isi
    n_baris_users = users.n_baris
    # Hitung jumlah jin pengumpul
    count_jin_pengumpul = 0
    for i in range(n_baris_users):
        if(isi_users[i][2] == "jin_pengumpul"):
            count_jin_pengumpul += 1
    if(count_jin_pengumpul == 0): # tidak ada jin pengumpul
        print("Kumpul gagal. Anda tidak punya jin pengumpul. Sialhkan summon terlebih dahulu.")
    else: # ada jin pengumpul
        print(f"Mengerahkan {count_jin_pengumpul} jin untuk mengumpulkan bahan.")
        # mengumpulkan bahan
        hasil_kumpul = kumpul(bahan_bangunan,count_jin_pengumpul,True)
        print(f"Jin menemukan total {hasil_kumpul[0]} pasir, {hasil_kumpul[1]} batu, dan {hasil_kumpul[2]} air.")
    
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
        # isi_users, isi_candi, isi_bahan_bangunan : matrix of string
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

    # mencari jin termalas dan terajin
    if(n_baris_candi == 0):
        print("> Jin Terajin: -")
        print("> Jin Termalas: -")
    else:
        # mencari semua jin pembangun 
        jin = ["" for _ in range(total_pembangun)]
        n_jin = total_pembangun
        index = 0
        for i in range(n_baris_users):
            if(isi_users[i][2] == "jin_pembangun"):
                jin[index] = isi_users[i][0]
        # memastikan semua pembuat candi ada dalam array jin, jika tidak maka ditambahkan
        for i in range(n_baris_candi):
            index = string_in_array(jin, isi_candi[i][1], n_jin)
            if(index == -1):
                jin = string_append(jin, isi_candi[i][1], n_jin)
                n_jin += 1
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
# Fungsi ayamberkokok()
def ayamberkokok (candi: Data) -> None:
    # KAMUS LOKAL
        # i, banyak_candi, n_baris_candi : int
        # isi_candi : matrix of string
    # ALGORITMA
    # unpack data
    isi_candi = candi.isi
    n_baris_candi = candi.n_baris
    # hitung banyak candi
    banyak_candi = 0
    for i in range(n_baris_candi):
        if(isi_candi[i][1] != ""):
            banyak_candi += 1
    print("Jumlah Candi: " ,banyak_candi )
    if(banyak_candi >= 100):
        print("Yah, Bandung Bondowoso memenangkan permainan!")
    else: # banyak_candi < 100
        print("\nSelamat, Roro Jonggrang memenangkan permainan!")
        print("\n*Bandung Bondowoso angry noise*")
        print("Roro Jonggrang dikutuk menjadi candi.")

    # KELUAR PROGRAM BELUM DIBUAT!!!


# F13 - Load (Gunakan argparse)
# Prosedur load()
# Menggunakan argparse agar dapat meload / membuka kembali data yang sudah disave sebelumnya, 
# prosedur ini sendiri dijalankan hanya sekali saja pada command line / terminal
def load() -> list[Data]:
    import os
    import argparse
    # KAMUS LOKAL 
        # parser, args : objek dari library argparse
        # args.nama_folder : str
    parser = argparse.ArgumentParser(add_help=False,usage='%(prog)s <nama_folder>')
    parser.add_argument("nama_folder",nargs="?",type=str,default="")
    args = parser.parse_args() 
    path = "save/"+args.nama_folder
    if(path == "save/"):
        print("Tidak ada nama folder yang diberikan!\n")
        parser.print_usage()
        return []
    elif(os.path.exists(path)):
        print("Loading...")
        users = data_load(path+"/user.csv")
        candi = data_load(path+"/candi.csv")
        bahan_bangunan = data_load(path+"/bahan_bangunan.csv")
        print("Selamat datang di program \"Manajerial Candi\"")
        return [users,candi,bahan_bangunan]
    else:
        print(f"Folder \"{path}\" tidak ditemukan.")
        return []

# F14 - Save
# Prosedur save()
# Menyimpan data pada folder dengan parent folder "save"
def save(users: Data, candi: Data, bahan_bangunan: Data) -> None:
    import os
    # KAMUS LOKAL
        # path, current_path : str
        # file_baru : bool
        # path_spilted : matrix of string
    # ALGORITMA
    path = "save/" + input("Masukkan nama folder: ")
    print("\nSaving...\n")
    path_splited = string_split(path,"/")
    current_path = ""
    file_baru = False
    for dir in path_splited:
        current_path += dir
        if(not os.path.exists(current_path)):
            file_baru = True
            print(f"Membuat folder {current_path}...")
            os.mkdir(current_path)
        current_path += "/"
    if(file_baru):
        print()
    data_save(path, "user", users)
    data_save(path, "candi", candi)
    data_save(path, "bahan_bangunan", bahan_bangunan)
    print(f"Berhasil menyimpan data di folder {path}!")

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

