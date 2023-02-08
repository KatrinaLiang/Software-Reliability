from sorting import mergesort
from binary_search import search


def check_membership(arr, key):
    sorted_array = mergesort(arr)
    result = search(sorted_array, key)
    if result == -1:
        return 0
    else:
        return 1


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7]
    print(check_membership(arr, 0))

