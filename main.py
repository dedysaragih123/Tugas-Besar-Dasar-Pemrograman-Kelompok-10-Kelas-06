import commands
commands.load() 
# UNTUK MENJALANKAN PROGRAM, KETIK PADA TERMINAL/CONSOLE :
# python main.py src

# type Data : < isi: matriks of string,
#               n_baris : int,
#               n_kolom : int >

# ASUMSI : jumlah candi maksimum adalah 1000 line 
while True:
  masukan = input(">>> ")
  commands.run(masukan)
  print()

