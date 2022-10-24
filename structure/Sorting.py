import math


def inter_change_sort(arr: []):
    for i in range(-1, len(arr) - 1):
        i += 1
        for j in range(i, len(arr) - 1):
            j += 1
            if arr[i] >= arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


def bubble_sort_max(arr):
    for i in range(len(arr)-1, 0, -1):
        i -= 1
        for j in range(-1, i):
            j += 1
            if arr[j] >= arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def bubble_sort_min(arr):
    for i in range(len(arr)):
        i += 1
        for j in range(i + 1, len(arr) + 1):
            j -= 1
            if arr[j - 1] >= arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
    return arr


def insert_sort(arr: []):
    i: int
    j: int
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1
        while temp < arr[j] and j >= 0:
            arr[j + 1], arr[j] = arr[j], arr[j + 1]
            j -= 1
    return arr


def select_sort(arr):
    i: int
    j: int
    k: int
    for i in range(len(arr) - 1):
        k = i
        for j in range(i + 1, len(arr)):
            if arr[j] <= arr[k]:
                k = j
                arr[k], arr[i] = arr[i], arr[k]
    return arr


def heap_sort(arr):
    n = len(arr)
    for i in range(math.ceil(n / 2) - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
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


def quick_sort(arr):
    def _quicksort(arr, left, right):
        if left < right:
            p = partition(arr, left, right)
            _quicksort(arr, left, p)
            _quicksort(arr, p + 1, right)

    _quicksort(arr, 0, len(arr) - 1)

    def partition(arr, left, right):
        pivot = arr[left]
        while True:
            while arr[left] < pivot:
                left += 1
            while arr[right] > pivot:
                right -= 1
            if left >= right:
                return right
            arr[left], arr[right] = arr[left], arr[right]
            left += 1
            right -= 1

    return arr


def mSort(arr):
    if len(arr) > 1:
        mid = math.ceil(len(arr) / 2)
        left = arr[:mid]
        right = arr[mid:]
        mSort(left)
        mSort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
        return arr


def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


if __name__ == '__main__':
    # arr = [1, 9, 3, 2, 7, 7, 4, 8, 5]
    # arr = [1, 2, 3]
    # arr = [1, 3, 1]
    arr = [8, 2, 2, 4, 5, 3, 0]
    arr = [1, 0, 2, 3, 4, 7, 9]
    arr = [7, 0, 1, 9, 2, 3, 4]
    # arr = inter_change_sort(arr)
    # arr = bubble_sort_max(arr)
    # arr = bubble_sort_min(arr)
    # arr = inter_change_sort(arr)
    # arr = select_sort(arr)
    # arr = quick_sort(arr)
    # arr = mSort(arr)
    # arr = heap_sort(arr)
    arr = insert_sort(arr)
    print(arr)
