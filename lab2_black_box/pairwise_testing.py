import random


class Pairwise:
    def __init__(self, length: int = 7):
        self.def_arr = []
        for i in range(length, 0, -1):
            self.def_arr.append(i)
        self.def_key = 1

        self.tests = []  # tests[i] is one test case. tests[i][0] is the array, and tests[i][1] is the key

    def generate_random_value(self, excluded_value, low, high):
        random_value = random.randint(low, high)
        while random_value == excluded_value:
            random_value = random.randint(low, high)
        return random_value

    def zero_wise(self):
        self.tests.append([self.def_arr, self.def_key])

    def one_wise(self):
        for i in range(len(self.def_arr)):
            tmp_arr = self.def_arr.copy()
            random_value = self.generate_random_value(tmp_arr[i], -100, 100)
            tmp_arr[i] = random_value
            self.tests.append([tmp_arr, self.def_key])

        tmp_key = self.def_key
        random_key = self.generate_random_value(tmp_key, -200, 200)
        self.tests.append([self.def_arr, random_key])

    def two_wise(self):
        for i in range(len(self.def_arr)):
            for j in range(i + 1, len(self.def_arr)):
                tmp_arr = self.def_arr.copy()
                random_value = self.generate_random_value(tmp_arr[i], -100, 100)
                tmp_arr[i] = random_value
                random_value = self.generate_random_value(tmp_arr[j], -100, 100)
                tmp_arr[j] = random_value
                self.tests.append([tmp_arr, self.def_key])

        for i in range(len(self.def_arr)):
            tmp_key = self.def_key
            random_key = self.generate_random_value(tmp_key, -200, 200)
            tmp_arr = self.def_arr.copy()
            random_value = self.generate_random_value(tmp_arr[i], -100, 100)
            tmp_arr[i] = random_value
            self.tests.append([tmp_arr, random_key])

    def generate_all_tests(self):
        self.zero_wise()
        self.one_wise()
        self.two_wise()


if __name__ == '__main__':
    test_pairwise = Pairwise()
    test_pairwise.generate_all_tests()
    print(test_pairwise.tests)
