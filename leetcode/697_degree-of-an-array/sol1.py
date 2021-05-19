"""
https://leetcode.com/problems/degree-of-an-array/

"Counter" + "LR index" approach.
- Counter
    Use Counter for recognize the maximum frequency elements.

- LR index
    Use `dict` to store left-most and right-most indices of an index

- Return the shortest subarray with same degree
    1) Get the most frequent elements
    2) Calculate the width of each element
    3) Return the smallest width
"""
__author__ = "Hwamin Kim"
__email__ = "quicksort00@gmail.com"
__license__ = "Apache-2.0"
__version__ = "1.0.0"


from collections import Counter


class Solution:
    def findShortestSubArray(self, nums: [int]) -> int:
        counter = Counter(nums)
        erange = {}
        for i, num in enumerate(nums):
            if num not in erange:
                erange[num] = [i, i]
            else:
                erange[num][1] = i
        max_val = max(counter.values())
        cands = [erange[k][1] - erange[k][0] + 1
                 for k, v in counter.items() if v == max_val]
        return min(cands)
