from data import load
#import commands

# Anggap semua fungsi yang dipanggil merupakan fungsi yang sudah dibuat sendiri pada modul lain
Nmax = 105
users = [0 for j in  range(3) for i in range(Nmax)] # Matriks data user
candi = [0 for j in range(5) for i in range(Nmax)] # Matriks data candi
bahan_bangunan = [0 for j in range(3) for i in range(Nmax)] # Data bahan bangunan

load("file/user.csv", users)
load("file/candi.csv", candi)
load("file/bahan_bangunan.csv", bahan_bangunan)

while True:
  masukan = input(">>> ")
#  commands.run(masukan)