#linear saarch
def liearSearch(arr: [], target: int):
    is_found : int
    for i in range(0, len(arr)):
        if arr[i] == target:
            is_found = arr[i]
            print("Found in arr key: ", target)
        if arr[i] != target:
            is_found = None
    if is_found == None:
        print("Not found")
arr = [1, 2, 3, 4, 5]
# target = 10
# target = 5
# liearSearch(arr, target)
#Binary search
def binarySearch(arr: [], target: int):
    left = 0
    right = len(arr) - 1
    mid = 0
    is_found : int
    while (left <= right):
        mid = (left + right) // 2
        if arr[mid] == target:
            print("Found in arr: ", arr[mid])
        if arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
        is_found = arr[mid]
    if is_found != arr[mid]:
        print("Not found")
arr = [1, 2, 3, 4, 4, 5]
binarySearch(arr, 4)
#Recuirsive search
def recuirsiveSearch(arr: [], target: int):



    left = 0
    right = len(arr)
    mid = (left + right) // 2
    if arr[mid] == target:
        print("Found in arr: ", arr[mid])
    if arr[mid] > target:
        recuirsiveSearch(arr[:mid], target)
    if arr[mid] < target:
        recuirsiveSearch(arr[mid + 1:], target)
