# https://docs.python.org/3/library/array.html#module-array
# seacrch, insert, delete an unsorted arr
# ///idea: performent by linear traversal
# An array is a collection of items stored at contiguous memory locations.
def findElement(arr, n, key):
    for i in range(n):
        if (arr[i] == key):
            return i
    return -1
arr = [12, 34, 10, 6, 40]
key = 40
n = len(arr)
index = findElement(arr, n, key)
if index != -1:
    print("Element Fround at position " + str(index + 1))
else:
    print("Element not found")
#insert at the end
def insert(arr, element):
    arr.append(element)
arr = [12, 16, 20, 40, 50, 70]
key = 26
print("Before inserting ", arr)
insert(arr, key)
print("After Inserting ", arr)
# delete operation
arr = [10, 50, 30, 40, 20]
key = 30
print("Array before deletion: ", arr)
arr.remove(key)
print("Array after deletion ", arr)

# search, insert, delete in a sort array
# idea: using binary search
def binarySearch(arr, low, high, key):
    mid = (low + high)/2
    if (key == arr[int(mid)]):
        return mid
    if (key > arr[int(mid)]):
        return binarySearch(arr, (mid + 1), high, key)
    if (key > arr[int(mid)]):
        return binarySearch(arr, low, (mid-1), key)
    return 0

arr = [5, 6, 7, 8, 9, 10]
n = len(arr)
key = 10
print("index:", int(binarySearch(arr, 0, n-1, key)))
def insertSorted(arr, n, key, capacity):
    if (n > capacity):
        return n
    i = n-1
    while i >= 0 and arr[i] > key:
        arr[ i + 1] = arr[i]
        i -= 1
    arr[i + 1] = key
    return (n+1)
arr = [12, 16, 20, 40, 50, 70]
for i in range(20):
    arr.append(0)
capacity = len(arr)
n = 6
key = 26
print("Befor Insertion ", end =" ")
for i in range(n):
    print(arr[i], end = " ")

def deleteElement(arr, n, key):
    pos = binarySearch(arr, 0, n-1, key)
    if (pos == -1):
        print("Element not found")
        return n
    for i in range(int(pos), int(n-1)):
        arr[i] = arr[i+1]
    return n-1

arr = [10, 20, 30, 40, 50]
n = len(arr)
key = 30
print("Array before deletion")
for i in range(n):
    print(arr[i], end= " ")
n = deleteElement( arr, n, key)
print("\n\nArray after deletion")
for i in  range(n):
    print(arr[i], end= " ")
# reverse an array or string

def reverseListNum(A, start, end):
    while start < end:
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1
A = [1, 2, 3, 4, 5, 6]
print(A)
reverseListNum(A, 0, 5)
print("Reversed list is ")
print(A)


def reverseList(A):
    print(A[::-1])
A = ['a', 'b', 'c']
print(A)
print(reverseList(A))

def findSingle(ar, n):
    res = ar[0]
    for i in range(1, n):
        res = res ^ ar[i]
    return res

ar = [9, 3, 5, 5, 3 ,8, 8]
print("elemect occurrring once is", findSingle(ar, len(ar)) )

