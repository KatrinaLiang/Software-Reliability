def assert_result(arr: [int], key: int):
    for element in arr:
        if element == key:
            return 1
    return 0
