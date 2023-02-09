from sorting import merge_sort
from binary_search import binary_search


def check_membership(arr, key):
    sorted_array = merge_sort(arr)
    result = binary_search(sorted_array, key)
    if result == -1:
        return 0
    else:
        return 1


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7]
    print(check_membership(arr, 0))

