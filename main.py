import commands
semua_data = commands.load()
if(semua_data != []): # load berhasil
  users = semua_data[0]
  candi = semua_data[1]
  bahan_bangunan = semua_data[2] 
  # UNTUK MENJALANKAN PROGRAM, KETIK PADA TERMINAL/CONSOLE :
  # python main.py src

  # type Data : < isi: matriks of string,
  #               n_baris : int,
  #               n_kolom : int >

  # ASUMSI : jumlah candi maksimum adalah 1000 line 
  while True:
    masukan = input(">>> ")
    commands.run(masukan,users,candi,bahan_bangunan)
    print()

