import numpy as np
from numpy import VisibleDeprecationWarning


class DoThi():
    def __init__(self):
        ...

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


if __name__ == "__main__":
    data1 = DoThi()
    data2 = DoThi()
    a = 'DoThiCoHuong.txt'
    data1.check_graph(a)
