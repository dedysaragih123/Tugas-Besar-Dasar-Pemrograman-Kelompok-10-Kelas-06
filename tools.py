# FILE INI BERISI FUNGSI BUATAN PELENGKAP
# DAFTAR ISI (biar ngga pusing)
# split         line 8
# splicing      line 41


# Fungsi split(string, key)
# Spesifikasi : Memisahkan suatu string "str" dengan pemisah "key" dan mengembalikan array yang berisi hasil pemisahan
def split(string: str, key: str) -> list[str]:

    # mencari jumlah bagian hasil pemisahan
    count: int = 1
    for i in range(len(string)):
        if(string[i] == key):
            count += 1
    if(count == 1):
        return [string]
    hasil: list[str] = ["" for _ in range(count)]

    # Membagi string menjadi bagian kecil "part" dan digabungkan pada hasil
    index_str: int = 0
    index_hasil: int = 0
    while True:
        if(index_str == len(string)):
            break
        part: str = ""
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
# Spesifikasi : Mengabil bagian string dari index_awal hingga index_akhir 
def string_slice(string: str, index_awal: int, index_akhir: int) -> str:
    hasil: str = ""
    for i in range(index_awal, index_akhir):
        hasil += string[i]
    return hasil


# Fungsi append(data,elemen):
# Spesifikasi : Menambahkan suatu elemen ke dalam array, Asumsi tipe array dan elemen pasti sama
def append(data,elemen):
    isi_data = data[0]
    n_baris = data[1]
    hasil = [0 for _ in range(n_baris+1)]
    for i in range(n_baris):
        hasil[i] = isi_data[i]
    hasil[n_baris] = elemen   
    return hasil