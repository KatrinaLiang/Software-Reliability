def binary_search(arr, key):
    # return the position of the key, or -1 if not found

    l = 0
    r = len(arr) - 1

    while True:
        mid = (r + l) // 2
        if arr[mid] < key:
            l = mid + 1
        elif arr[mid] > key:
            r = mid - 1
        if l > r or (arr[mid] == key):
            break

    if key == arr[mid]:
        return mid
    else:
        return -1


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7]
    print(binary_search(arr, 5))
