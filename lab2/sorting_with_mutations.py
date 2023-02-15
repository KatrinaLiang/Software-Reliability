def merge_sort_with_mutation(arr):
    if len(arr) > 1:  # changed > to <
        mid = len(arr) // 2
        l_arr = arr[:mid]
        r_arr = arr[mid:]
        merge_sort_with_mutation(l_arr)
        merge_sort_with_mutation(r_arr)

        i = j = k = 0

        while i < len(l_arr) and j < len(r_arr):  # Change ”and” to ”or”
            if l_arr[i] < r_arr[j]:  # Change < to >
                arr[k] = l_arr[i]
                i += 1  # Change += 1 to += 2
            else:
                arr[k] = r_arr[j]
                j += 1  # Change += 1 to = 1
            k += 1

        while i < len(l_arr):
            arr[k] = l_arr[i]
            i -= 1  # Change += 1 to -= 1
            k += 1

        while j < len(r_arr):
            arr[k] = r_arr[j]
            j += 1
            k += 1

    return arr


if __name__ == '__main__':
    arr = [7, 6, 34, 4, 3, 19, 1] # [1, 3, 6, 19, 1, 34, 1]
    print("Sorted array is: ")
    print(merge_sort_with_mutation(arr))
