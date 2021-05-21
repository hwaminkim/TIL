"""
https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/

DP with bottom-up approach

Main Idea (Same as the top-down one):
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

Implement a DP code for bottom-up way.
Since the input range of target is well limited, this method showed a good
result.
"""
__author__ = "Hwamin Kim"
__email__ = "quicksort00@gmail.com"
__license__ = "Apache-2.0"
__version__ = "1.0.0"


class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        if d * f < target or target < d:
            return 0
        if target in (d, d*f):
            return 1
        if d == 1:
            return 1

        dp_table = [[0] * (target+1) for _ in range(d+1)]
        for i in range(1, min(f+1, target+1)):
            dp_table[1][i] = 1

        for bucket in range(2, d+1):
            for k in range(0, target+1):
                total = 0
                for i in range(1, min(f+1, k)):
                    total += dp_table[bucket-1][k-i]
                dp_table[bucket][k] = total
        return dp_table[d][target] % (10 ** 9 + 7)
