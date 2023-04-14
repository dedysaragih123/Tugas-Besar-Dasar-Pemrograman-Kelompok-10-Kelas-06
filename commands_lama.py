from tools import split

def run(command,users,candi,bahan_bangunan,current_login):
    if(command == "login"): # 0 jika belum login
        current_login = (login(users))
    elif(command == "logout"):
        current_login = logout(current_login)
    else:
        print("\nError invalid command\n")

# F01 - Login (fungsi)
def login(users):
    username = input("Username: ")
    password = input("Password: ")
    print()
    cekUsername = False
    for i in range(len(users)):
        if(username == users[i][0]):
            cekUsername = True
            index = i
            break
    if(cekUsername):
        if(password == users[index][1]):
            print(f"Selamat datang, {username}!")
            print("Masukkan command \"help\" untuk daftar command yang dapat kamu panggil")
        else:
            print("Password salah!")
    else:
        print("Username tidak terdaftar!")
    return users[i]

# F02 - Logout (Prosedur)
def logout(current_login):
    current_login = []
    return current_login

# F03 - Summon Jin
def summonjin(users):
    if(len(users) >= 102):
        print("Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")
    else:
        print("\nJenis jin yang dapat dipanggil:\n(1) Pengumpul - Bertugas mengumpulkan bahan bangunan\n(2) Pembangun - Bertugas membangun candi")
        # menentukan jenis jin
        while True:
            jenis_jin = input("\nMasukkan nomor jenis jin yang ingin dipanggil: ")
            print()
            if(not jenis_jin.isdigit()): # validasi isi tipe jenis_jin dalam bentuk bilangan bulat
                print("Masukkan harus dalam bentuk angka")
            elif(int(jenis_jin) == 1):
                role = "jin_pengumpul"
                print("Memilih jin \"Pengumpul\".")
                break
            elif(int(jenis_jin) == 2):
                role = "jin_pembangung"
                print("Memilih jin \"Pengumpul\".")
                break
            else:
                print(f"Tidak ada jenis jin bernomor \"{jenis_jin}\"!")
        # bikin username
        while True:
            username = input("\nMasukkan username jin: ")
            for i in range(len(users)):
                if(users[i][0] == username):
                    print(f"\nUsername \"{username}\" sudah diambil!")
                    break
            else:
                break
        # bikin password
        while True:
            password = input("Masukkan password jin: ")
            if(5<=len(password)<=25):
                print()
                break
            else:
                print("\nPassword panjangnya harus 5-25 karakter!")
            print()
        # simpan data
        users.append([username,password,role])
        print("Mengumpulkan sesajen...\nMenyerahkan sesajen...\nMembacakan mantra...")
        print(f"\nJin {username} berhasil dipanggil!")
                    
# F04 - Hilangkan Jin
def hapusjin(users):
    username = input("Masukkan username jin: ")
    ditemukan = False
    for i in range(len(users)):
        if(username == users[i][0]):
            ditemukan = True
            index = i
            break
    if(ditemukan):
        hapus = input("Apakah anda yakin ingin menghapus jin dengan username Jin1 (Y/N)? ")
        if(hapus == "Y"):
            users.pop(index) # REVISI
            print("\nJin telah berhasil dihapus dari alam gaib.")
    else:
        print("\nTidak ada jin dengan username tersebut.")
    
# F05 - Ubah Tipe Jin
def ubahjin(users):
    username = input("Masukkan username jin: ")
    ditemukan = False
    for i in range(len(users)):
        if(username == users[i][0]):
            ditemukan = True
            index = i
            break
    if(ditemukan):
        if(users[index][2]=="jin_pengumpul"):
            ubah = input("Jin ini bertipe \"Pengumpul\". Yakin ingin mengubah ke tipe \"Pembangun\" (Y/N)? ")
            if(ubah == "Y"):
                users[index][2] = "jin_pembangun"
        else:
            ubah = input("Jin ini bertipe \"Pembangun\". Yakin ingin mengubah ke tipe \"Pengumpul\" (Y/N)? ")
            if(ubah == "Y"):
                users[index][2] = "jin_pengumpul"
        print("Jin telah berhasil diubah.")
    else:
        print("\nTidak ada jin dengan username tersebut.")

# F06 - Jin Pembangun
def bangun(candi,bahan_bangunan,tipe=0):
    import random
    # bahan dalam format [pasir,batu,air]
    bahan = [random.randint(1,5),random.randint(1,5),random.randint(1,5)]
    if(tipe == 0): # tipe bernilai 1 jika dipakai batchbangun
        print(f"# Men-generate bahan bangunan ({bahan[0]} pasir, {bahan[1]} batu, dan {bahan[2]} air)")
    dibangun = True
    for i in range(len(bahan_bangunan)):
        if(bahan_bangunan[i][0]=="pasir"):
            if(bahan[0] > int(bahan_bangunan[i][2])):
                dibangun = False
                break
        elif(bahan_bangunan[i][0]=="batu"):
            if(bahan[1] > int(bahan_bangunan[i][2])):
                dibangun = False
                break
        elif(bahan_bangunan[i][0]=="air"):
            if(bahan[2] > int(bahan_bangunan[i][2])):
                dibangun = False
                break
    if(tipe == 0):
        if(dibangun):
            for i in range(len(bahan_bangunan)):
                if(bahan_bangunan[i][0]=="pasir"):
                    bahan_bangunan[i][2] = str(int(bahan_bangunan[i][2]) - bahan[0])
                elif(bahan_bangunan[i][0]=="batu"):
                    bahan_bangunan[i][2] = str(int(bahan_bangunan[i][2]) - bahan[1])
                elif(bahan_bangunan[i][0]=="air"):
                    bahan_bangunan[i][2] = str(int(bahan_bangunan[i][2]) - bahan[2])
            if(len(candi) <= 100):
                print(f"Sisa candi yang perlu dibangun: {100 - len(candi)}")
            else:  
                print(f"Sisa candi yang perlu dibangun: 0")  
        else:
            print("Bahan bangunan tidak mencukupi.\nCandi tidak bisa dibangun!")
    else:
        return bahan
        
# F07 - Jin Pengumpul
def kumpul(bahan_bangunan,tipe=0):
    # tipe bernilai 1 jika digunakan dalam batchkumpul
    import random
    # bahan dalam format [pasir,batu,air]
    bahan = [random.randint(1,5),random.randint(1,5),random.randint(1,5)]
    if(tipe == 0):
        print(f"Jin menemukan {bahan[0]} pasir, {bahan[1]} batu, dan {bahan[2]} air.")
    for i in range(len(bahan_bangunan)):
        if(bahan_bangunan[i][0]=="pasir"):
            bahan_bangunan[i][2] = str(int(bahan_bangunan[i][2]) + bahan[0])
        elif(bahan_bangunan[i][0]=="batu"):
            bahan_bangunan[i][2] = str(int(bahan_bangunan[i][2]) + bahan[1])
        elif(bahan_bangunan[i][0]=="air"):
            bahan_bangunan[i][2] = str(int(bahan_bangunan[i][2]) + bahan[2])
    return bahan

# F08 - Batch Kumpul/Bangun
def batchkumpul(users,bahan_bangunan):
    n = 0
    # bahan dan bahan_total dalam format [pasir,batu,air]
    bahan_total = [0,0,0]
    for jin in users:
        if(jin[2] == "jin_pengumpul"):
            n += 1
            bahan = kumpul(bahan_bangunan,1)
            bahan_total[0] += bahan[0]
            bahan_total[1] += bahan[1]
            bahan_total[2] += bahan[2]
    if(n == 0):
        print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")
    else:
        print(f"Mengerahkan {n} jin untuk mengumpulkan bahan.")
        print(f"Jin menemukan total {bahan_total[0]} pasir, {bahan_total[1]} batu, dan {bahan_total[2]} air.")     
def batchbangun(users,candi,bahan_bangunan):
    n = 0
    # bahan dan bahan_total dalam format [pasir,batu,air]
    bahan_total = [0,0,0]
    for jin in users:
        if(jin[2] == "jin_pembangun"):
            n += 1
            bahan = bangun(candi,bahan_bangunan,1)
            bahan_total[0] += bahan[0]
            bahan_total[1] += bahan[1]
            bahan_total[2] += bahan[2]
    if(n == 0):
        print("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")
    else:
        print(f"Mengerahkan {n} jin untuk membangun candi dengan total {bahan_total[0]} pasir, {bahan_total[1]} batu, dan {bahan_total[2]} air.")
        kurang = [0,0,0]
        for i in range(len(bahan_bangunan)):
            if(bahan_bangunan[i][0]=="pasir"):
                if(bahan_total[0] > int(bahan_bangunan[i][2])):
                    kurang[0] = bahan_total[0] - int(bahan_bangunan[i][2])
            elif(bahan_bangunan[i][0]=="batu"):
                if(bahan_total[1] > int(bahan_bangunan[i][2])):
                    kurang[1] = bahan_total[1] - int(bahan_bangunan[i][2])
            elif(bahan_bangunan[i][0]=="air"):
                if(bahan_total[2] > int(bahan_bangunan[i][2])):
                    kurang[2] = bahan_total[2] - int(bahan_bangunan[i][2])
        if(kurang == [0,0,0]):
            print(f"Jin berhasil membangun total {n} candi.")
            for i in range(len(bahan_bangunan)):
                if(bahan_bangunan[i][0]=="pasir"):
                    bahan_bangunan[i][2] = str(int(bahan_bangunan[i][2]) - bahan_total[0])
                elif(bahan_bangunan[i][0]=="batu"):
                    bahan_bangunan[i][2] = str(int(bahan_bangunan[i][2]) - bahan_total[1])
                elif(bahan_bangunan[i][0]=="air"):
                    bahan_bangunan[i][2] = str(int(bahan_bangunan[i][2]) - bahan_total[2])
        else:
            print(f"Bangun gagal. Kurang {kurang[0]} pasir, {kurang[1]} batu, dan {kurang[2]} air.")   

# F09 - Ambil Laporan Jin
def laporanjin(users,bahan_bangunan,current_login):
    if(current_login[0][2] != "bandung_bondowoso"):
        print("Laporan jin hanya dapat diakses oleh akun Bandung Bondowoso.")
    else:
        total_jin = 0
        total_pengumpul = 0
        total_pembangun = 0
        for i in range(len(users)):
            if(users[i][2] == "jin_pengumpul"):
                total_jin += 1
                total_pengumpul += 1
            elif(users[i][2] == "jin_pembangun"):
                total_jin += 1
                total_pembangun += 1
        print(f"> Total Jin: {total_jin}")
        print(f"> Total Jin Pengumpul: {total_pengumpul}")
        print(f"> Total Jin Pembangun: {total_pembangun}")
        
        print(f"> Jumlah Pasir : {bahan_bangunan[0][2]} unit")
        print(f"> Jumlah Batu : {bahan_bangunan[1][2]} unit")
        print(f"> Jumlah Air : {bahan_bangunan[2][2]} unit")

# F10 - Ambil Laporan Candi
# F11 - Hancurkan Candi
# F12 - Ayam Berkokok


# F13 - Load (Gunakan argparse)
def load():
    import argparse
    parser = argparse.ArgumentParser(add_help=False,usage='%(prog)s <nama_folder>')
    parser.add_argument("nama_folder",nargs="?",type=str,default="")
    args = parser.parse_args() 
    if(args.nama_folder == ""):
        print("Tidak ada nama folder yang diberikan!\n")
        parser.print_usage()
    elif(any(args.nama_folder == "src")): # "src" karena file yang berisi data csv bernama src
        print("Loading...")
        # load data
        print("Selamat datang di program \"Manajerial Candi\"")
        print("Silahkan masukkan username Anda")
        print(">>>")
        
    else:
        print(f"Folder \"{args.nama_folder}\" tidak ditemukan.")
    

# F14 - Save
def save():
    import os
    path = input("Masukkan nama folder: ")
    print("\nSaving...\n")
    path_splited = split(path,"/")
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
    print(f"Berhasil menyimpan data di folder {path}!")


# F15 - Help
def help():
    pass


# F16 - Exit
def exit():
    terjawab = False
    while terjawab == False:
        jawab = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
        if(jawab == "y"):
            # save dan keluar
            pass
        elif(jawab == "n"):
            # keluar
            pass


# B01 - Radnom Num Generator $ pakai LCG
# hasilnya memmiliki range dari nmin - nmaks
def randomInt(jumlah,nmin ,nmaks): # dengan seed yang sama hasil pasti sama
    import time
    seed = time.time()
    lcg = []
    hasil = []
    a = 3
    c = 1
    for _ in range(50):
        LCG = ((a*seed)+c) % (10) 
        seed += 1
        lcg.append(LCG)
    for i in lcg:
        if(nmin <= i <= nmaks):
            hasil.append(i)
    return hasil[:jumlah]

for i in range(5):
    print(randomInt(5,1,5))

# B02
# B03
# B04
# B05