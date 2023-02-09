def merge_sort_with_mutation(arr):
    if len(arr) < 1:  # changed > to <
        mid = len(arr) // 2
        l_arr = arr[:mid]
        r_arr = arr[mid:]
        merge_sort_with_mutation(l_arr)
        merge_sort_with_mutation(r_arr)

        i = j = k = 0

        while i < len(l_arr) and j < len(r_arr):
            if l_arr[i] < r_arr[j]:
                arr[k] = l_arr[i]
                i += 1
            else:
                arr[k] = r_arr[j]
                j += 1
            k += 1

        while i < len(l_arr):
            arr[k] = l_arr[i]
            i += 1
            k += 1

        while j < len(r_arr):
            arr[k] = r_arr[j]
            j += 1
            k += 1

    return arr


if __name__ == '__main__':
    arr = [3, 2, 1, 234, 675, 3, 9, 3, 0, 4, 567, 23]
    print("Sorted array is: ")
    print(merge_sort_with_mutation(arr))
