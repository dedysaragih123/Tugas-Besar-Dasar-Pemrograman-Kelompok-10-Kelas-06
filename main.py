from data import load
import commands

"""# Anggap semua fungsi yang dipanggil merupakan fungsi yang sudah dibuat sendiri pada modul lain
Nmax = 105
users = [0 for j in  range(3) for i in range(Nmax)] # Matriks data user
candi = [0 for j in range(5) for i in range(Nmax)] # Matriks data candi
bahan_bangunan = [0 for j in range(3) for i in range(Nmax)] # Data bahan bangunan
"""
user: list[list[list[str]],int,int] = load("src/user.csv")
candi: list[list[list[str]],int,int] = load("src/candi.csv")
bahan_bangungan: list[list[list[str]],int,int] = load("src/bahan_bangunan.csv")

while True:
  masukan = input(">>> ")
  commands.run(masukan)