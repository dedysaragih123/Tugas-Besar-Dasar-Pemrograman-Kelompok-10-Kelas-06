# Contoh Test Case
user = [['berto','ganteng','bandung_bondowoso'],
        ['adril','imba','roro_jonggrang'],
        ['david','gantengTEC','jin_pembangun'],
        ['jinb1',"jinb12", 'jin_pembangun'],
        ['jinb2',"jinb12", 'jin_pembangun'],
        ['jinb3',"jinb12", 'jin_pembangun'],
        ['jinb4',"jinb12", 'jin_pembangun'],
        ['jinb5',"jinb12", 'jin_pembangun'],
        ['jinb6',"jinb12", 'jin_pembangun'],
        ['jinb7',"jinb12", 'jin_pembangun'],
        ['jink1',"jink12", 'jin_pengumpul'],
        ['jink2',"jink12", 'jin_pengumpul'],
        ['jink3',"jink12", 'jin_pengumpul'],
        ['jink4',"jink12", 'jin_pengumpul'],
        ['jink5',"jink12", 'jin_pengumpul'],
        ['jink6',"jink12", 'jin_pengumpul'],
        ['jink7',"jink12", 'jin_pengumpul'],
        [0,0,0]]

candi = [[1,'jinb1',1,1,1],[2,'jinb2',1,2,1],
         [3,'jinb1',1,1,1],[4,'jinb2',1,2,1],
         [5,'jinb1',1,1,1],[6,'jinb2',1,2,1],
         [7,'jinb1',1,1,1],[8,'jinb2',1,2,1],
         [9,'jinb1',1,1,1],[10,'jinb2',1,2,1],
         [11,'jinb1',1,1,1],[12,'jinb2',1,2,1],
         [13,'jinb1',1,1,1],[14,'jinb2',1,2,1],
         [15,'jinb1',1,1,1],[16,'jinb2',1,2,1],
         [17,'jinb1',1,1,1],[18,'jinb2',1,2,1],
         [19,'jinb1',1,1,1],[20,'jinb2',1,2,1],
         [21,'jinb1',1,1,1],[22,'jinb2',1,2,1],
         [23,'jinb1',1,1,1],[24,'jinb2',1,2,1],
         [25,'jinb1',1,1,1],[26,'jinb2',1,2,1],
         [27,0,0,0,0],
         [28,0,0,0,0],
         [29,0,0,0,0],
         [30,0,0,0,0],
         [31,0,0,0,0],
         [32,0,0,0,0],
         [33,0,0,0,0]]

bahan = [0,0,0]

# import ...
from B01 import randomize

def batchkumpul(user:list):
    i = 0
    banyakpengumpul = 0
    while i < 105 and user[i] != [0 for i in range(3)]:
        if user[i][2] == 'jin_pengumpul':
            banyakpengumpul += 1
        i += 1
    
    if banyakpengumpul > 0:
        pasir = batu = air = 0
        for i in range(banyakpengumpul):
            pasir += randomize(0,5)
            batu += randomize(0,5)
            air += randomize(0,5)
        bahan[0] += pasir
        bahan[1] += batu
        bahan[2] += air 
        print("Mengerahkan",banyakpengumpul,"jin untuk mengumpulkan bahan.")
        print("Jin menemukan total", pasir, "pasir", batu, "batu, dan",air, "air.")
    else: #banyakpengumpul != 0
        print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")

def banyakcandi(candi:list)->int:
    hasil = 0
    for i in range(33): #for i in range(Nmax)
        if candi[i][2] != 0:
            hasil += 1
    return hasil
    
def batchbangun(user:list, candi : list, bahan:list):
    i = 0
    bykcandi = banyakcandi(candi)
    banyakpembangun = 0
    while i < 105 and user[i] != [0 for i in range (3)]:
        if user[i][2] == 'jin_pembangun':
            banyakpembangun += 1
        i += 1
    
    if banyakpembangun > 0:
        pasir = batu = air = 0
        list_bahan = [[0 for i in range(3)] for j in range (banyakpembangun)]
        for i in range(banyakpembangun):
            list_bahan[i][0] = randomize(1,5)
            list_bahan[i][1] = randomize(1,5)
            list_bahan[i][2] = randomize(1,5)
            pasir += list_bahan[i][0]
            batu += list_bahan[i][1]
            air += list_bahan[i][2]
        if bahan[0] >= pasir and bahan[1] >= batu and bahan[2] >= air:
            print("Mengerahkan",banyakpembangun, "jin untuk membangun candi dengan total bahan",pasir,'pasir',batu,'batu, dan',air, 'air')
            print("Jin berhasil membangun total",banyakpembangun,'candi')
            bahan[0] -= pasir
            bahan[1] -= batu
            bahan[2] -= air
            i = j = 0
            list_pembangun = [0 for i in range(banyakpembangun)]
            while i < 105 and user[i] != [0 for i in range (3)]:
                if user[i][2] == 'jin_pembangun':
                    list_pembangun[j] = user[i][0]
                    j += 1
                i += 1
            i = j = 0
            while i < 33 and j < banyakpembangun:
                if bykcandi == 100:
                    break
                elif candi[i][2] == 0:
                    candi[i] = [i+1, list_pembangun[j], list_bahan[j][0], list_bahan[j][1], list_bahan[j][2]]
                    bykcandi += 1   
                    j += 1
                i += 1           
        else:
            pasirkurang = max(0, pasir - bahan[0])
            batukurang = max(0, batu - bahan[1])
            airkurang = max(0, air - bahan[2])
            print("Bangun gagal. kurang", pasirkurang,"pasir",batukurang,"batu",airkurang,"air." ) # Candi yang terbangun 0
    else: #banyakpembangun != 0
        print("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu")

# batchkumpul(user)
# batchkumpul(user)
# batchkumpul(user)
batchbangun(user, candi,bahan)
# print(user)
# print(candi)
# print(bahan) yang di komen hanya percobaan membuktikan test case benar