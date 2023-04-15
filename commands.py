"""
1 5 9 13 17 - Ciko
2 6 10 14 18 - Bagas
3 7 11 15 19 - Cinta
4 8 12 16 20 - Dedy
"""

from tools import append

# untuk menyimpan data login
current_login = ["" for _ in range(3)]

def run(command:str, users: list[list[list[str]],int,int], candi: list[list[list[str]],int,int], bahan_bangunan: list[list[list[str]],int,int]) -> None:
    command = command.strip() # PERLU BIKIN SENDIRI strip()
    global current_login
    if(current_login == ["" for _ in range(3)]):
        if(command == "login"):
            current_login = (login(users))
        elif(command == "logout"):
            print("Logout gagal!")
            print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
        elif(command == "help"):
            pass
        elif(command == "exit"):
            pass
        elif(any(command == string for string in ["logout","summonjin","hapusjin","ubahjin","bangun","kumpul","batchkumpul","batchbangun","laporanjin","laporancandi","hancurkancandi","ayamberkokok","save"])):
            print(f"{command} gagal!")
            print("Anda perlu login terlebih dahulu!")
        else:
            print(f"command \"{command}\" tidak dikenal.")
    else:
        if(command == "login"):
            print("Login gagal!")
            print(f"Anda telah login dengan username {current_login[0]}, silahkan lakukan “logout” sebelum melakukan login kembali.")
        elif(command == "logout"):
            current_login = logout()
        elif(command == "summonjin"):
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
def login(users: list[list[list[str]],int,int]) -> list[str]: 
    data = users[0]
    n_baris = users[1]
    username = input("Username: ")
    password = input("Password: ")
    cekUsername = False
    for i in range(n_baris):
        if(username == data[i][0]):
            cekUsername = True
            index = i
            break
    if(cekUsername):
        if(password == data[index][1]):
            print(f"Selamat datang, {username}!")
            print("Masukkan command \"help\" untuk daftar command yang dapat kamu panggil")
            return data[i]
        else:
            print("Password salah!")
            return ["" for _ in range(3)]
    else:
        print("Username tidak terdaftar!")
        return ["" for _ in range(3)]

# F02 - Logout 
def logout() -> list[str]:
    return ["" for _ in range(3)]

# F05 - Ubah Tipe Jin
def ubahjin(users: list[list[list[str]],int,int]) -> None:
    data = users[0]
    n_baris = users[1]
    username = input("Masukkan username jin: ")
    ditemukan = False
    for i in range(n_baris):
        if(username == data[i][0]):
            ditemukan = True
            index = i
            break
    if(ditemukan):
        if(data[index][2]=="jin_pengumpul"):
            ubah = input("Jin ini bertipe \"Pengumpul\". Yakin ingin mengubah ke tipe \"Pembangun\" (Y/N)? ")
            if(ubah == "Y"):
                data[index][2] = "jin_pembangun"
        else:
            ubah = input("Jin ini bertipe \"Pembangun\". Yakin ingin mengubah ke tipe \"Pengumpul\" (Y/N)? ")
            if(ubah == "Y"):
                data[index][2] = "jin_pengumpul"
        print("Jin telah berhasil diubah.")
    else:
        print("\nTidak ada jin dengan username tersebut.")
    users[0] = data

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

# F13 - Load (Gunakan argparse)
def load():
    import argparse
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


