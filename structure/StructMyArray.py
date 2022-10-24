# 2 Binary Search
# 1 Linear Search
# define list

# take input list size
# num = int(input("Enter size of list"))
# insert numbers into lst
# for n in range(num):
#     numbers = int(input("enter the array of %d element" %n))
#     lst.append(numbers)
# take input to find number
# x = int(input("enter number search in list:"))
# i = 0
# flag = False
# while i < len(lst):
#     if lst[i] == x:
#         flag = True
#         break
#     i = i + 1
# if flag == 1:
#     print(f'{x} was found at index {i}')
# else:
#     print('not found')

# python program for linear search using for loop

# define list


# take input list size


# append element in list/array


# take input number to be find in list

# 3 BubbleSort
# def BobbleSort(a: [], n: int):
#     temp = 0
#     for i in range(n):
#         i += 1
#         for j in range(i+1, n):
#             j += 1
#             if a[i] > a[j]:
#                 temp = a[j]
#                 a[j] = a[j+1]
#                 a[j+1] = temp
# def InsertSort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1
#         while j >= 0 and key < arr[j]:
#             arr[j+1] = arr[j]
#             j -= 1
#         arr[j+1] = key
# arr = [12, 11, 13, 5, 6]
# InsertSort(arr)
# print("Sorted arr is")
# for i in range(len(arr)):
#     print("%d" %arr[i])

class SelectionSort:
    def __init__(self, arr: [], n: int):
        self.n = n
        self.arr = arr
    def selectSort(self):
        for i in range(self.n):
            min_idx = i
            for j in range(i + 1, self.n):
                if self.arr[j] < self.arr[min_idx]:
                    min_idx = j
            temp = self.arr[min_idx]
            self.arr[min_idx] = arr[i]
            self.arr[i] = temp

    def printArry(self):
        n = len(self.arr)
        for i in range(n):
            print(f'mang sau khi sort {self.arr[i]}')
        print(f'mang sau khi sort {self.arr}')
l = SelectionSort()
l.selectSort([64, 25, 12, 22, 11],5)
l.printArry([64, 25, 12, 22, 11])


