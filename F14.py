import os
import shutil

def save() :
    nama_folder = input("Masukkan nama folder: ") 
    lok_folder = os.path.join(f"save/{nama_folder}")
    print("Saving...")

    if os.path.exists(lok_folder) :
        print("")
    else :
        os.makedirs(lok_folder)
        print(f"Membuat folder {lok_folder}...")

    nama_file = "savedata.txt"
    lok_file = os.path.join(lok_folder, nama_file)
    shutil.copyfile("savedata.txt", lok_file)
    print(f"Berhasil menyimpan data di folder {lok_folder}!")

save()
        