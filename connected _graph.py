import numpy as np
class Graph():

    def read_file(self, file_name):
        f = open(f'{file_name}', 'r')
        arr = []
        for line in f.readlines():
            arr.append(line.split())
        return arr


    def check_graph(self, file_name):
        a = 0
        data = self.read_file(file_name=file_name)
        A = np.array(data)
        for i in range(6):
            for j in range(5):
                if A[i][i] != 0:
                    a = 3
                elif A[i][i] == A[j][i]:
                    a = 0
                elif A[i][i] == A[j][i]:
                    a = 1
                    break
        if a == 1:
            print("Day la do thi vo huong")
        elif a == 0:
            print("Day la do thi co huong")
        elif a == 3:
            print("Do thi khong hop le")

"""
doc file kiem tra do thi co huong va do thi vo huong
tao list bang nhan 9 dinh
ham sothanhphanlienthong 
for i in range(dinh):
 if nhan[i] == 0:
 bien so thanh phan lien thong += 1
 nhan[i] = sothanhphanlienthong
 -> viet ham de quy tim cac dinh lien thong(do thi, bang nhan, dinh: int):
 for (i, len())..
"""
g=Graph()
data = g.read_file('connected_graph.txt')
print(data)
g.check_graph('connected_graph.txt')