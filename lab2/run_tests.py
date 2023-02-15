from membership_queries_with_mutation import check_membership
from random_testing import *
from pairwise_testing import Pairwise


def assert_result(arr: [int], key: int):
    for element in arr:
        if element == key:
            return 1
    return 0


def run_random_tests(length: int = 7):
    # generate tests with pairwise testing and random testing -> call membership queries
    # assert result or catch error/exception
    # count number of tests to get an error or false result
    # add timeout

    # random testing
    tot_tests = 0
    for i in range(100):
        count = 0
        while True:
            count += 1
            try:
                random_arr = generate_array_with_random_numbers(length=length)
                random_key = generate_random_key()
                check_res = check_membership(random_arr, random_key)
                right_result = assert_result(random_arr, random_key)
                if not right_result == check_res:
                    raise ValueError("Wrong answer!")
            except Exception as e:
                print("Number of tests to get an error or false result: {}".format(count))
                print(e)
                tot_tests = tot_tests + count
                break

    print("Average tests to get error: {}".format(tot_tests / 100))


def run_pairwise_tests(length: int = 7):
    print("Running pairwise testing")
    count = 0
    test_pairwise = Pairwise(length)
    test_pairwise.generate_all_tests()
    tests = test_pairwise.tests

    for test in tests:
        # print(test)
        count += 1
        try:
            res = check_membership(test[0], test[1])
            right_res = assert_result(test[0], test[1])
            # print("result: {}".format(res))
            # print("right result: {}".format(right_res))
            if not res == right_res:
                raise ValueError("Wrong answer!")
        except Exception as e:
            print("Number of tests to get an error or false result: {}".format(count))
            print(e)
            break
    print(count)


if __name__ == '__main__':
    run_pairwise_tests(100)
