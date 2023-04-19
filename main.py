from data import load
import commands
commands.load() 
# UNTUK MENJALANKAN PROGRAM, KETIK PADA TERMINAL/CONSOLE :
# python main.py src

"""# Anggap semua fungsi yang dipanggil merupakan fungsi yang sudah dibuat sendiri pada modul lain
Nmax = 105
users = [0 for j in  range(3) for i in range(Nmax)] # Matriks data user
candi = [0 for j in range(5) for i in range(Nmax)] # Matriks data candi
bahan_bangunan = [0 for j in range(3) for i in range(Nmax)] # Data bahan bangunan
"""
users: list[list[list[str]],int,int] = load("src/user.csv")                      # [data,n_baris,n_kolom]
candi: list[list[list[str]],int,int] = load("src/candi.csv")                    # n_baris adalah jumlah efektif baris pada matriks data
bahan_bangungan: list[list[list[str]],int,int] = load("src/bahan_bangunan.csv") # n_kolom adalah jumlah efektif kolom pada matriks data
# untuk data hasil login disimpan di commands.py
# ASUMSI : jumlah candi maksimum adalah 1000 line 

while True:
  masukan = input(">>> ")
  commands.run(masukan, users, candi, bahan_bangungan)
  print()

