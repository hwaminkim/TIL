"""
https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/

DP with top-down approach (Time out)

Main Idea:
    This problem can be represented as a recursive formula of the possible
    numbers of bucket filling problem.
        W(n, k) = W(n-1, k-1) + W(n-1, k-2) + ... + W(n-1 k-(n-1))
            n: Remaining buckets (dice)
            k: Remaining numbers for meet the target.
        Since the capacity of all buckets (f) are same and limited, the formula
        can be slightly modified.

        if f+1 < k:
            W(n, k) = W(n-1, k-1) + W(n-1, k-2) + ... + W(n-1 k-f))
        else:
            W(n, k) = W(n-1, k-1) + W(n-1, k-2) + ... + W(n-1 k-(n-1))

Implement a DP code for top-down form.
Unfortunately, due to some optimization problems, it returns time limite exceed.
"""
__author__ = "Hwamin Kim"
__email__ = "quicksort00@gmail.com"
__license__ = "Apache-2.0"
__version__ = "1.0.0"


from functools import lru_cache


class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        if d * f < target or target < d:
            return 0
        if target in (d, d*f):
            return 1
        if d == 1:
            return 1

        @lru_cache
        def way(bucket: int, remaining: int) -> int:
            if bucket == 1:
                if 0 < remaining <= f:
                    return 1
                return 0
            if bucket <= 0:
                return 0
            total = 0
            for i in range(1, min(f+1, remaining)):
                total += way(bucket-1, remaining-i)
            return total

        return way(d, target) % (10 ** 9 + 7)
