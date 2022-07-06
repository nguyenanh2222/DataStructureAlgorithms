def bubble_sort(arr):
    # giam nghich the trong mang
    n = len(arr)
    swaped = False
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                swaped = True
                arr[j], arr[j+1] = arr[j+1], arr[j]
    if not swaped:
        return
    return arr
def inter_change_sort(arr):
    # giam nghich the trong mang
    # doi cho truc tiep
    n = len(arr)
    for i in range(0, n):
        for j in range(i, n):
            if arr[i] > arr[j]:
                arr[j], arr[i] = arr[i], arr[j]
    return arr
def select_sort(arr):
    # xay dung manh moi tu mang ban dau
    for i in range(1, len(arr)):
        a = arr[i]
        j = i - 1
        while j >= 0 and a < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = a
    return arr
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[largest] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        heapify(arr, n, largest)
def heapSort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

def quick_sort(arr):
    def _quicksort(arr, low, high):
        if low < high:
            p = partition(arr, low, high)
            _quicksort(arr, low, p)
            _quicksort(arr, p+1, high)
    def partition(arr, low, high):
        pivot = arr[low]
        while True:
            while arr[low] < pivot:
                low += 1
            while arr[high] > pivot:
                high -= 1
            if low >= high:
                return high
            arr[low], arr[high] = arr[high], arr[low]
            low += 1
            high -= 1
    _quicksort(arr, 0, len(arr)-1)
    return arr


def mSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        mSort(L)
        mSort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
        return arr

def binary_search(arr, val, start, end):
    if start == end:
        if arr[start] > val:
            return start
        else:
            return start + 1
    if start > end:
        return start

    mid = (start + end) // 2
    if arr[mid] < val:
        return binary_search(arr, val, mid + 1, end)
    elif arr[mid] > val:
        return binary_search(arr, val, start, mid - 1)
    else:
        return mid
def insertion_sort(arr):
    for i in range(1, len(arr)):
        val = arr[i]
        j = binary_search(arr, val, 0, i-1)
        arr = arr[:j] + [val] + arr[j:i] + arr[i+1:]
    return arr
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

if __name__ == '__main__':
    arr = [1, 9, 3, 2, 7, 7, 4, 8, 5]
    # arr = bubble_sort(arr)
    # arr = inter_change_sort(arr)
    # arr = select_sort(arr)
    # arr = quick_sort(arr)
    # arr = mSort(arr)
    # arr = heapSort(arr)
    # arr = insertion_sort(arr)
    printList(arr)



