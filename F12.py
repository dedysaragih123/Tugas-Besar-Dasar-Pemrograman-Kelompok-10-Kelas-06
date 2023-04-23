# Contoh Test Case
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
         [1,'jinb1',1,1,1],[2,'jinb2',1,2,1],
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
         [1,'jinb1',1,1,1],[2,'jinb2',1,2,1],
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
         [1,'jinb1',1,1,1],[2,'jinb2',1,2,1],
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

def ayamberkokok ():
    banyakcandi = 0
    for i in range(len(candi)): #for i in range (Nmax):
        if candi[i][1] != 0:
            banyakcandi += 1
    print("Kukuruyuk.. Kukuruyuk..")
    print("\nJumlah Candi: " ,banyakcandi )
    if banyakcandi >= 100:
        print("\nYah, Bandung Bondowoso memenangkan permainan!")
    else: #banyakcandi < 100
        print("\nSelamat, Roro Jonggrang memenangkan permainan!")
        print("\n*Bandung Bondowoso angry noise*")
        print("Roro Jonggrang dikutuk menjadi candi.")

ayamberkokok()
quit()