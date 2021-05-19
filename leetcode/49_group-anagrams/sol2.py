"""
https://leetcode.com/problems/group-anagrams/


Letter occurrence tuple key approach.

- Main Idea:
    Map a string by occurrence of letters of a string.
- Example:
    "a"         = (1, 0, 0, 0, 0, 0, ... , 0)
    "zz         = (0, 0, 0, 0, 0, 0, ... , 2)
    ""          = (0, 0, 0, 0, 0, 0, ... , 0)
    "abceaa"    = (3, 1, 1, 0, 1, 0, ... , 0)

If the number of string is S and the length of string is K,
the time complexity will be O(N*K)
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
            key = [0] * 26
            for letter in s:
                key[ord(letter) - ord('a')] += 1
                group[tuple(key)].append(s)
        return list(group.values())
