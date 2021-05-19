"""
https://leetcode.com/problems/group-anagrams/

Sorted string key approach.

If the number of string is S and the length of string is K,
the time complexity will be O(N*logK)
"""
__author__ = "Hwamin Kim"
__email__ = "quicksort00@gmail.com"
__license__ = "Apache-2.0"
__version__ = "1.0.0"


from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: [str]) -> [[str]]:
        group = defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))
            group[key].append(s)
        return list(group.values())
