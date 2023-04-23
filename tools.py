# FILE INI BERISI FUNGSI BUATAN PELENGKAP

# type Data : < isi: matriks of string,
#               n_baris : int,
#               n_kolom : int >
class Data:
    def __init__(self, isi, n_baris, n_kolom):
        self.isi = isi
        self.n_baris = n_baris
        self.n_kolom = n_kolom

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

# Fungsi string_strip(string)
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

# Fungsi string_append(array,string,length)
# Menambahkan string ke dalam array of string
def string_append(array: list[str], string: str, length: int) -> list[str]:
    # KAMUS LOKAL
        # i: int
        # array_baru : array of string
    # ALGORITMA
    array_baru = ["" for _ in range(length+1)]
    for i in range(length):
        array_baru[i] = array[i]
    array_baru[length] = string
    return array_baru

# Fungsi string_in_array(array, string, array_length)
# mengecek apakah string terdapat pada array jika iya maka mengembalikan indexnya jika tidak mditemukan mengembalikan nilai -1
def string_in_array(array : list[str], string: str, array_length: int) -> int:
    # KAMUS LOKAL
        # i : int
    # ALGORTIMA
    for i in range(array_length):
        if(array[i] == string):
            return i
    return -1

# Fungsi string_leksikografis_min(array,length)
# Menentukan string terkecil berdasarkan leksikografis
def string_leksikografis_min(array: list[str], length: int) -> str:
    # KAMUS LOKAL
        # i : int
        # min : str
    # ALGORITMA
    min = array[0]
    for i in range(length):
        if(array[i] < min):
            min = array[i]
    return min

# Fungsi string_leksikografis_maks(array,length)
# Menentukan string tertinggi berdasarkan leksikografis
def string_leksikografis_maks(array: list[str], length: int) -> str:
    # KAMUS LOKAL
        # i : int
        # maks : str
    # ALGORITMA
    maks = array[0]
    for i in range(length):
        if(array[i] > maks):
            maks = array[i]
    return maks
    
# Fungsi int_min(array,length)
# Mengembalikan nilai terkecil pada array integer
def int_min(array: list[int], length: int)-> int:
    # KAMUS LOKAL
        # min, i : int
    # ALGORITMA
    min = array[0]
    for i in range(length):
        if(array[i] < min):
            min = array[i]
    return min

# Fungsi int_mals(array,length)
# Mengembalikan nilai terbesar pada array integer
def int_maks(array: list[int], length: int) -> int:
    # KAMUS LOKAL
        # maks, i : int
    # ALGORITMA
    maks = array[0]
    for i in range(length):
        if(array[i] > maks):
            maks = array[i]
    return maks

# Fungsi int_join(array1, array2, length)
# Menjumlahkan tiap index pada dua array integer yang sama ukuran
def int_join(array1: list[int],array2: list[int], length: int,) -> list[int]:
    # KAMUS LOKAL
        # i : int
        # array_hasil : array of integer
    # ALGORITMA
    array_hasil = [0 for _ in range(length)]
    for i in range(length):
        array_hasil[i] = array1[i] + array2[i]
    return array_hasil

# Fungsi data_append(data,elemen):
# Menambahkan suatu elemen ke dalam array, Asumsi tipe array dan elemen pasti sama
def data_append(data: Data, elemen: list[str]) -> Data:
    # KAMUS LOKAL
        # n_baris, i : int
        # isi_data, hasil : matrix of string
    # ALGORITMA
    # unpack data
    isi_data = data.isi
    n_baris = data.n_baris
    hasil = ["" for _ in range(n_baris+1)]
    for i in range(n_baris):
        hasil[i] = isi_data[i]
    # meletakan yang dimasukkan pada ujung matriks hasil
    hasil[n_baris] = elemen 
    data.isi = hasil  
    data.n_baris += 1
    return data

# Fungsi data_remove(data,index)
# Menghapuskan data pada index yang diberikan
def data_remove(data: Data, index: int) -> Data:
    # KAMUS LOKAL
        # n_baris, n_kolom, i : int
        # isi_data, data_baru : matrix of string
    # ALGORTIMA
    # unpack data
    isi_data = data.isi
    n_baris = data.n_baris
    n_kolom = data.n_kolom
    data_baru = [["" for _ in range(n_kolom)] for _ in range(n_baris-1)]
    # menambahkan semua data selain data pada index yang diberikan
    for i in range(index):
        data_baru[i] = isi_data[i]
    for i in range(index+1,n_baris):
        data_baru[i-1] = isi_data[i]
    data.isi = data_baru
    data.n_baris -= 1
    return data

# Fungsi cari_index_username(users,username)
# Mencari username pada data users, jika tidak ditemukan maka mengembalikan -1, jika ditemukan maka mengembalikan index
def cari_index_username(users: Data, username: str) -> int:
    # KAMUS LOKAL
        # n_baris, i : int
        # isi_data : matrix of string
    # ALGORITMA
    isi_users = users.isi
    n_baris = users.n_baris
    for i in range(n_baris):
        if(username == isi_users[i][0]): # username ditemukan
            return i
    return -1


# Fungsi generate_bahan_bangunan()
# Mengembalikan bahan bangunan yang sudah random
from numgen import randomize # import fungsi untuk angka random
def generate_bahan_bangunan():
    pasir = randomize(1,5)
    batu = randomize(1,5)
    air = randomize(1,5)
    return [pasir, batu, air]