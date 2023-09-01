# September-01-2023

# We are given an array ‘ARR’ with N positive integers. We need to find if
# there is a subset in “ARR” with a sum equal to K. If there is, return true else return false.


def subset_sum_to_K(n, k, arr):
    dp = [[-1 for j in range(k + 1)] for i in range(n)]

    # Write your code here
    # Return a boolean variable 'True' or 'False' denoting the answer
    def subset_sum(n, k, dp):
        if k == 0:
            return True
        if n == 0:
            return k - arr[n] == 0
        if dp[n][k] != -1:
            return dp[n][k]
        not_take = subset_sum(n - 1, k, dp)
        take = subset_sum(n - 1, k - arr[n], dp) if k >= arr[n] else False
        dp[n][k] = take or not_take
        return dp[n][k]

    return subset_sum(n - 1, k, dp)


arr = [1, 2, 3, 4]
k = 4
n = len(arr)

print(subset_sum_to_K(n, k, arr))
