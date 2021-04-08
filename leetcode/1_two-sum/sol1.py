"""
https://leetcode.com/problems/two-sum/
The first question of leetcode, and there are many variance of this problem.
Please check similar questions like this.

Very Naive solution with O(n^2)
    - Compare all possible pair of list.
    - It shows good running time on Leetcode than other O(n) solution,
      but inherently slow.
"""
__author__ = "Hwamin Kim"
__email__ = "quicksort00@gmail.com"
__license__ = "Apache-2.0"
__version__ = "1.0.0"


class Solution:
    def twoSum(self, nums: 'List[int]', target: int) -> 'List[int]':
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
