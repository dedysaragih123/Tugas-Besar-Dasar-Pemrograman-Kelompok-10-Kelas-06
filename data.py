from tools import split, string_slice
# BERISI FUNGSI UNTUK AKSES FILE
# type Data : < isi_data : matriks of string,
#               n_baris : int,
#               n_kolom : int >

# Fungsi load(path)
# Membaca data csv di lokasi "path" dan mengembalikan data dalam format [isi_data, n_baris, n_kolom] 
def load(path: str) -> list[list[str],int,int]:
    # KAMUS LOKAL
        # file : file
        # n_baris, n_kolom, i : int
        # cek_kolom, first_row : bool
        # line : str
        # data : Data
    # ALGORITMA
    # Mencari jumlah efektif data
    file = open(path, "r").readlines()
    n_baris = -1 # -1 karena anggap baris pertama (judul) tidak dimasukkan
    n_kolom = 1 # 1 karena pasti kolom berisi satu
    cek_kolom = True
    for line in file:
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
    i= 0
    first_row = True
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
    file.close()
    return [data,n_baris,n_kolom]

# Fungsi save(path, nama_file, data)
# Membaca data csv di lokasi "path" dan mengembalikan [data, jumlah_baris, jumlah_kolom], data dalam bentuk matriks 
def save(path: str, nama_file: str, data: list[list[str],int,int]) -> None:
    # KAMUS LOKAL
        # file : file
        # isi_data : matriks of string
        # n_baris, n_kolom, i, j : int
        # line : str
    # ALGORITMA
    file = open(path,"w+")
    isi_data = data[0]
    n_baris = data[1]
    n_kolom = data[2]
    # Tulis ulang label/ baris 1
    if(nama_file == "user"):
        file.write("username;password;role\n")
    elif(nama_file == "candi"):
        file.write("id;pembuat;pasir;batu;air\n")
    elif(nama_file == "bahan_bangunan"):
        file.write("nama;deskripsi;jumlah\n")
    for i in range(n_baris):
        line = ""
        for j in range(n_kolom):
            line += isi_data[i][j]
            line += ";"
        if(i != n_baris-1):
            line += "\n"
        file.write(line)
    file.close()
