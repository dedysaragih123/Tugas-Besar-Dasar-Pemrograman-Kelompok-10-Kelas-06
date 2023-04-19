# FILE INI BERISI FUNGSI BUATAN PELENGKAP

# Fungsi string_split(string, key)
# Memisahkan suatu string "str" dengan pemisah "key" dan mengembalikan array yang berisi hasil pemisahan
def string_split(string: str, key: str) -> list[str]:
    # KAMUS LOKAL
        # count, i, index_str, index_hasil : int
        # part : str
        # hasil : array of string
    # ALGORITMA
    # Mencari jumlah bagian hasil pemisahan
    count = 1
    for i in range(len(string)):
        if(string[i] == key):
            count += 1
    if(count == 1):
        return [string]
    hasil = ["" for _ in range(count)]
    # Membagi string menjadi bagian kecil "part" dan digabungkan pada hasil
    index_str = 0
    index_hasil = 0
    while True:
        if(index_str == len(string)):
            break
        part = ""
        for i in range(index_str,len(string)):
            if(string[i] == key):
                index_str += 1
                break
            else:
                index_str += 1
                part += string[i]
        hasil[index_hasil] = part
        index_hasil += 1
    return hasil

# Fungsi string_slice(string, index_awal, index_akhir):    
# Mengembalikan bagian string dari index_awal hingga index_akhir 
def string_slice(string: str, index_awal: int, index_akhir: int) -> str:
    # KAMUS LOKAL
        # i : int
        # hasil : str
    # ALGORITMA
    hasil = ""
    for i in range(index_awal, index_akhir):
        hasil += string[i]
    return hasil

# Fungsi string_strip(string):
# Membersihkan string dari karakter kosong / spasi (" ") pada awal dan akhir string
def string_strip(string: str) -> list[str]:
    # KAMUS LOKAL
        # index_awal, index_akhir, i : int
        # hasil : str
    # ALGORITMA
    # cari index dimulai string asli (string yang bukan spasi string kosong " " yang tidak berguna)  
    index_awal = 0
    for i in range(len(string)):
        if(string[i] != " "):
            break
        else:
            index_awal += 1
    # cari index berakhirnya string asli (string yang bukan spasi string kosong " " yang tidak berguna)
    index_akhir = len(string)
    for i in range(len(string)-1,index_awal,-1):
        if(string[i] != " "):
            break
        else:
            index_akhir -= 1
    # mengembalikan string yang sudah bersih
    hasil = ""
    for i in range(index_awal,index_akhir):
        hasil += string[i]
    return hasil

# Fungsi data_append(data,elemen):
# Menambahkan suatu elemen ke dalam array, Asumsi tipe array dan elemen pasti sama
def data_append(data: list[list[list[str]],int,int], elemen: list[list[str]]) -> list[list[list[str]],int,int]:
    # KAMUS LOKAL
        # n_baris, i : int
        # isi_data, hasil : matriks of string
    # ALGORITMA
    # unpack data
    isi_data = data[0]
    n_baris = data[1]
    hasil = ["" for _ in range(n_baris+1)]
    for i in range(n_baris):
        hasil[i] = isi_data[i]
    # meletakan yang dimasukkan pada ujung matriks hasil
    hasil[n_baris] = elemen   
    return [hasil,n_baris+1,data[2]]

# Fungsi data_remove(data,index)
# Menghapuskan data pada index yang diberikan
def data_remove(data: list[list[list[str]],int,int], index: int) -> list[list[list[str]],int,int]:
    # KAMUS LOKAL
        # n_baris, n_kolom, i : int
        # isi_data, data_baru : matriks of string
    # ALGORTIMA
    # unpack data
    isi_data = data[0]
    n_baris = data[1]
    n_kolom = data[2]
    data_baru = [["" for _ in range(n_kolom)] for _ in range(n_baris-1)]
    # menambahkan semua data selain data pada index yang diberikan
    for i in range(index):
        data_baru[i] = isi_data[i]
    for i in range(index+1,n_baris):
        data_baru[i-1] = isi_data[i]
    return [data_baru,n_baris-1,n_kolom]

# Fungsi cari_index_username(users,username)
# Mencari username pada data users, jika tidak ditemukan maka mengembalikan -1, jika ditemukan maka mengembalikan index
def cari_index_username(users: list[list[list[str]]], username: str) -> int:
    # KAMUS LOKAL
        # n_baris, i : int
        # isi_data : matriks of string
    # ALGORITMA
    isi_data = users[0]
    n_baris = users[1]
    for i in range(n_baris):
        if(username == isi_data[i][0]): # username ditemukan
            return i
    return -1
            