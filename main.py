# Program main
# Program utama Managerial Candi
# KAMUS
  # type Data : < isi: matriks of string,
  #               n_baris : int,
  #               n_kolom : int >
  # semua_data : array[0..2] of Data
  # users, candi, bahan_bangunan : Data

# ALGORITMA
# import modul commands yang berisi semua fungsi dan procedure utama
import commands 
semua_data = commands.load() # load data
if(semua_data != []): # load berhasil
  users = semua_data[0]
  candi = semua_data[1]
  bahan_bangunan = semua_data[2] 
  while True:
    masukan = input(">>> ")
    commands.run(masukan,users,candi,bahan_bangunan)
    # commands.run adalah fungsi yang menghubungkan input user dengan fungsi dan procedur utama
    print()

# KETERANGAN :
  # UNTUK MENJALANKAN PROGRAM, KETIK PADA TERMINAL/CONSOLE :
  # python main.py nama_folder 
  # cth: python main.py abcde
