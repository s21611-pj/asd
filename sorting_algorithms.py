import timeit

# bubblesort
def bubble_sort(array):
    time = []
    start = timeit.default_timer()
    size = len(array)
    for i in range(size - 1):
        for j in range(0, size - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    stop = timeit.default_timer()
    time.append(stop - start)
    print(str("BUBBLE SORT: ") + str("{0:.10f}".format(sum(time) / len(time))))
    print(array)

# quicksort
def partition(array, p, r):
    pivot = array[r]
    smaller = p
    for i in range(p, r):
        if array[i] <= pivot:
            array[smaller], array[i] = array[i], array[smaller]
            smaller = smaller + 1
    array[smaller], array[r] = array[r], array[smaller]
    return smaller

def quick_sort(array, p, r):
    if p < r:
        q = partition(array, p, r)
        quick_sort(array, p, q - 1)
        quick_sort(array, q + 1, r)

def run_quick_sort(arr):
    time = []
    start = timeit.default_timer()
    quick_sort(arr, 0, len(arr) - 1)
    stop = timeit.default_timer()
    time.append(stop - start)
    print(str("QUICK SORT: ") + str("{0:.10f}".format(sum(time) / len(time))))
    print(arr)

#heapsort
def heapify(array, size, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < size and array[largest] < array[left]:
        largest = left
    if right < size and array[largest] < array[right]:
        largest = right
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, size, largest)

def heap_sort(array):
    size = len(array)
    time = []
    start = timeit.default_timer()
    for i in range(size // 2 - 1, -1, -1):
        heapify(array, size, i)
    for i in range(size - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)
    stop = timeit.default_timer()
    time.append(stop - start)
    print(str("HEAP SORT: ") + str("{0:.10f}".format(sum(time) / len(time))))
    print(array)