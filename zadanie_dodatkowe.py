# FIRST METHOD O(n^2)
def sort_max(array):
    size = len(array)
    for i in range(size - 1, -1, -1):
        biggestIdx = 0
        for j in range(0, i + 1, 1):
            if array[j] > array[biggestIdx]:
                biggestIdx = j
        temp = array[i]
        array[i] = array[biggestIdx]
        array[biggestIdx] = temp
    print('SORTED LIST WITH FIRST METHOD: ', array)

# SECOND METHOD O(n)
def sort_zero_and_one(array):
    counter = 0
    size = len(array)
    minimum = min(array)
    maximum = max(array)

    for i in range(size):
        if array[i] == minimum:
            counter += 1

    for i in range(0, counter):
        array[i] = minimum

    for i in range(counter, size):
        array[i] = maximum

    print("SORTED LIST WITH SECOND METHOD: ", array)


if __name__ == '__main__':
    array = [0, 1, 1, 0, 1, 0, 1]
    _array = [50, 30, 50, 50, 30, 30, 50, 50, 30, 50, 50]

    sort_max(array)
    sort_zero_and_one(array)
    sort_zero_and_one(_array)
