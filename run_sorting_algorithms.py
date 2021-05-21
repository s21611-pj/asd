import random

from sorting_algorithms import bubble_sort, run_quick_sort, heap_sort

def run():

    # sorted-list
    sorted_list = [1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 9, 10, 11]

    # reversed-sorted-list
    reversed_sorted_list = [11, 10, 9, 9, 8, 7, 7, 6, 5, 4, 3, 2, 1]

    # random-numbers-list
    random_list = []
    for i in range(0, 500):
        n = random.randint(1, 50)
        random_list.append(n)

    print("\nSORTED LIST")
    bubble_sort(sorted_list)
    run_quick_sort(sorted_list)
    heap_sort(sorted_list)

    print("\nREVERSED SORTED LIST")
    bubble_sort(reversed_sorted_list)
    run_quick_sort(reversed_sorted_list)
    heap_sort(reversed_sorted_list)

    print("\nRANDOM NUMBERS LIST")
    bubble_sort(random_list)
    run_quick_sort(random_list)
    heap_sort(random_list)


if __name__ == '__main__':
    run()
