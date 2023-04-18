import random

jumlah_candi = 100
def generate_bahan_bangunan() :
    pasir = random.randint(1,5)
    batu = random.randint(1,5)
    air = random.randint(1,5)
    return(f"{pasir} pasir, {batu} batu, {air} air")

#def cek_bahan_bangunan(bahan_bangunan) :
    #if generate_bahan_bangunan

def bangun() :
    global jumlah_candi
    bahan_bangunan = generate_bahan_bangunan()
    #if cek_bahan_bangunan(bahan_bangunan) :
    jumlah_candi -= 1
    print("Candi berhasil dibangun.")
    print(f"Sisa candi yang perlu dibangun: {jumlah_candi}.")

while jumlah_candi > 0 :
    bangun()