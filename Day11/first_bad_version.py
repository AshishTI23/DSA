# August-24-2023
#
# You are a product manager and currently leading a team to develop a new product. Unfortunately,
# the latest version of your product fails the quality check. Since each version is developed based
# on the previous version, all the versions after a bad version are also bad.

# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one,
# which causes all the following ones to be bad.

# You are given an API bool isBadVersion(version) which returns whether version is bad.
# Implement a function to find the first bad version. You should minimize the number of calls to the API.


def is_bad_version(index):
    # Test Bad Version API for n = 5 and bad version starting from 4
    array = [False, False, False, False, True, True]
    return array[index]


class Solution:
    def recursive_first_bad_version(self, n: int) -> int:
        low = 1
        high = n

        def binary_search(low: int, high: int) -> int:
            mid = (low + high) // 2
            is_bad_with_mid = is_bad_version(mid)
            is_bad_with_mid_plus_one = is_bad_version(mid + 1)
            is_bad_with_mid_minus_one = is_bad_version(mid - 1)

            if (
                is_bad_with_mid
                and is_bad_with_mid_plus_one
                and not is_bad_with_mid_minus_one
            ):
                return mid
            if is_bad_with_mid_minus_one:
                return binary_search(low, mid - 1)
            else:
                return binary_search(mid + 1, high)

        return binary_search(low, high)

    def iterative_first_bad_version(self, n: int) -> int:
        pass
