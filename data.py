from tools import split, string_slice
# BERISI FUNGSI UNTUK AKSES FILE

# Fungsi load(path)
# Membaca data csv di lokasi "path" dan mengembalikan [data, jumlah_baris, jumlah_kolom], data dalam bentuk matriks 
def load(path: str) -> list[list[str],int,int]:
    
    # Mencari jumlah efektif data
    file = open(path, "r").readlines()
    n_baris: int = -1 # -1 karena anggap baris pertama (judul) tidak dimasukkan
    n_kolom: int = 1 # 1 karena pasti kolom berisi satu
    cek_kolom: bool = True
    for line in file:
        line : str
        n_baris += 1
        if(cek_kolom):
            # penghitungan jumlah kolom hanya perlu dilakukan sekali 
            cek_kolom = False
            for i in range(len(line)):
                if(line[i] == ";"):
                    n_kolom += 1

    # Pengambilan data
    data: list[list[str]] = [["" for _ in range(n_kolom)] for _ in range(n_baris)]
    # pembukaan ulang file agar dapat terbaca lagi
    file = open(path, "r")
    i: int = 0
    first_row: bool = True
    for line in file:
        if(first_row == False): # agar judul csv tidak masuk data contoh (username;password;role)
            # line dilakukan slicing agar new line hilang (\n) # kecuali baris terkahir
            if(i != n_baris-1):
                data[i] = split(string_slice(line,0,len(line)-1),";")
            else:
                data[i] = split(line,";")
            i += 1
        else:
            first_row = False
    print(data)
    file.close()
    return [data,n_baris,n_kolom]