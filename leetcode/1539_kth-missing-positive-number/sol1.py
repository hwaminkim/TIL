"""
https://leetcode.com/problems/kth-missing-positive-number/

Simple and Iterative approach.
"""
__author__ = "Hwamin Kim"
__email__ = "quicksort00@gmail.com"
__license__ = "Apache-2.0"
__version__ = "1.0.0"


class Solution:
    def findKthPositive(self, arr: 'List[int]', k: int) -> int:
        """
        The array is sorted, and we are only required to find k-th missing
        number. We can except the number of array which is smaller than k.

        ex)
            arr = [3, 7, 10] / k = 6
               number sequence: 1, 2, [3], 4, 5, 6, [7], 8, 9, [10]
                                |  |       |  |  |       |
                             k: 1  2       3  4  5       6
               Therefore, answer is 8 (== k + len([3, 7]))
        """
        for elem in arr:
            if k < elem:
                return k
            k += 1
        return k
