# https://leetcode.com/problems/student-attendance-record-ii/description/
# 552 - Student Attendance Record II
# DP Question, solved using cache then recurse
# Time: O(n), Space: O(n)
# Doable in O(logn) but requires some np arrays
from functools import cache
@cache
def check(day, a, l):
    if day == 0:
        return 1
    # absent on day, late on day, present on day
    count = check(day - 1, a, 0)
    if a + 1 < 2:
        count += check(day - 1, a + 1, 0)
    if l + 1 < 3:
        count += check(day - 1, a, l + 1)
    return count % (10**9 + 7)
class Solution:
    def checkRecord(self, n: int) -> int:
        return check(n, 0, 0)