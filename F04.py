# Yang di bawah contoh Test Case yang dibuat sendiri

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
         [0,0,0,0,0]]

def validasi(user : list, username : str):
    i = 0
    while i < 100 and user[i] != [0 for i in range(3)]:
        if user[i][0] == username:
            return i
        i += 1
    return -1

def hilangkan_jin():
    username = input()
    idx = validasi(user,username)
    if idx == -1:
        print("Tidak ada jin dengan username tersebut.")

    else:
        print('Apakah anda yakin ingin menghapus jin dengan username Jin1 (Y/N)?')
        jawab_hilang = input()
        if jawab_hilang == "Y":
            for i in range(100):
                if candi[i][1] == username:
                    candi[i][1] = 0
                    candi[i][2] = 0
                    candi[i][3] = 0
                    candi[i][4] = 0
            ganti = False
            i = 0
            Neff = 0
            while i < 1000 and user[i] != [0 for i in range(3)]: 
                if i == idx:
                    ganti = True
                elif ganti:
                    user[i-1] = user[i]
                i += 1
                Neff += 1
            user[Neff-1] = [0 for _ in range(3)]
            print("Jin telah berhasil dihapus dari alam gaib.")

hilangkan_jin()
