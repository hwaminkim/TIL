"""
https://leetcode.com/problems/generate-parentheses/

Backtracking without recursion.

Same idea as the solution1, but not using recursion.
"""
__author__ = "Hwamin Kim"
__email__ = "quicksort00@gmail.com"
__license__ = "Apache-2.0"
__version__ = "1.0.0"


from collections import deque


class Solution:
    def generateParenthesis(self, n: int) -> [str]:
        res = []

        stk = deque([('', 0, 0)])
        while stk:
            cur_str, n_open, n_close = stk.pop()
            if n == n_open == n_close:
                res.append(cur_str)
                continue

            if n_open < n:
                stk.append((cur_str + '(', n_open + 1, n_close))
            if n_open > n_close:
                stk.append((cur_str + ')', n_open, n_close + 1))

        return res
