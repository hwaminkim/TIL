"""
https://leetcode.com/problems/group-anagrams/

***
Main Idea comes from
`jacobdq(https://leetcode.com/jacobdp/)`'s comment of Leetcode
***

Prime number mapped alphabet key approach.

- Main Idea:
    Map alphabet letters of a string as unique prime number.
    Multiply all numbers

- Caution:
    This code works fine since the `int` type in Python does not overflow.
    However, it may cause an overflow on other languages such as C++ or Java.

If the number of string is S and the length of string is K,
the time complexity will be O(N*K)
"""
__author__ = "Hwamin Kim"
__email__ = "quicksort00@gmail.com"
__license__ = "Apache-2.0"
__version__ = "1.0.0"


from collections import defaultdict


PMAP = {
    'a':2,
    'b':3,
    'c':5,
    'd':7,
    'e':11,
    'f':13,
    'g':17,
    'h':19,
    'i':23,
    'j':29,
    'k':31,
    'l':37,
    'm':41,
    'n':43,
    'o':47,
    'p':53,
    'q':59,
    'r':61,
    's':67,
    't':71,
    'u':73,
    'v':79,
    'w':83,
    'x':89,
    'y':97,
    'z':101
}


class Solution:
    def groupAnagrams(self, strs: [str]) -> [[str]]:
        group = defaultdict(list)
        for s in strs:
            key = 1
            for letter in s:
                key *= PMAP[letter]
            group[key].append(s)
        return list(group.values())
