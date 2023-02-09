import random


def generate_array_with_random_numbers(length: int) -> [int]:
    arr = []
    for i in range(length):
        arr.append(random.randint(-100, 100))
    return arr


def generate_random_key() -> int:
    return random.randint(-200, 200)


print(generate_array_with_random_numbers(10))
