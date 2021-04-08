"""
https://leetcode.com/problems/two-sum/

O(n) solution using hash
    - If n(i) + n(j) = target, it means target - n(i) = n(j).
    - In other words, we just can store (target - n(i)) and check n(j) for
      every number in nums
"""
__author__ = "Hwamin Kim"
__email__ = "quicksort00@gmail.com"
__license__ = "Apache-2.0"
__version__ = "1.0.0"


class Solution:
    def twoSum(self, nums: 'List[int]', target: int) -> 'List[int]':
        memo = {}
        for i, n in enumerate(nums):
            if n in memo:
                return [memo[n], i]
            memo[target - n] = i
