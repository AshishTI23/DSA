# August-27-2023

# A Ninja has an ‘N’ Day training schedule. He has to perform one of these three
# activities (Running, Fighting Practice, or Learning New Moves) each day. There
# are merit points associated with performing an activity each day. The same activity
# can’t be performed on two consecutive days. We need to find the maximum merit points
# the ninja can attain in N Days.
#
# We are given a 2D Array POINTS of size ‘N*3’ which tells us the merit point of
# specific activity on that particular day. Our task is to calculate the maximum
# number of merit points that the ninja can earn.

from typing import *


class Solution:
    def __init__(self, points: List[List[int]], n: int):
        self.points = points
        self.dp = [[-1 for i in range(4)] for j in range(n)]

    def maximum_points(self, day, last_activity):
        if self.dp[day][last_activity] != -1:
            return self.dp[day][last_activity]

        if day == 0:
            maxi = 0
            for i in range(3):
                if i != last_activity:
                    maxi = max(maxi, self.points[day][i])
            self.dp[day][i] = maxi
            return self.dp[day][i]
        maxi = 0
        for i in range(3):
            if i != last_activity:
                activity = self.points[day][i] + self.maximum_points(day - 1, i)
                maxi = max(maxi, activity)
            self.dp[day][last_activity] = maxi
        return self.dp[day][last_activity]


points = [[10, 40, 70], [20, 50, 80], [30, 60, 90]]

n = len(points)
print(Solution(points, n).maximum_points(n - 1, 3))
