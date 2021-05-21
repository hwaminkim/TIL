"""
https://leetcode.com/problems/rank-transform-of-an-array/

Simple sorted dict approach (NlogN)
"""
__author__ = "Hwamin Kim"
__email__ = "quicksort00@gmail.com"
__license__ = "Apache-2.0"
__version__ = "1.0.0"


class Solution:
    def arrayRankTransform(self, arr: [int]) -> [int]:
        rank_map = {n: i+1 for i, n in enumerate(sorted(set(arr)))}
        return [rank_map[n] for n in arr]
