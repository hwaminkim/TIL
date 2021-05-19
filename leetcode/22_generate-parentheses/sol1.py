"""
https://leetcode.com/problems/generate-parentheses/

Backtracking with recursion.

For every computation brach, there can be two possible choice - open or close
With the constraints of number of opening and closing, run backtracking with
the recursion.

If the input number is N,
the time complexity will be O( 4^N / sqrt(N) )

- How to get the complexity?
    Time complexity == number of all nodes
    Possible number of nodes = C_n (Catalan Number) = 1/(n+1) * (2n_C_n)
                             = 1/(n+1) * (2n * (2n-1) * (2n-2) * ... * n) / (n!)
                             = (4^N) / (N * sqrt(N))
"""
__author__ = "Hwamin Kim"
__email__ = "quicksort00@gmail.com"
__license__ = "Apache-2.0"
__version__ = "1.0.0"


class Solution:
    def generateParenthesis(self, n: int) -> [str]:
        res = []

        def gen_par(cur_str: str, n_open: int, n_close: int):
            if n == n_open == n_close:
                res.append(cur_str)
                return

            if n_open < n:
                gen_par(cur_str + '(', n_open + 1, n_close)
            if n_open > n_close:
                gen_par(cur_str + ')', n_open, n_close + 1)

        gen_par('', 0, 0)
        return res

s = Solution()
for i in range(1, 9):
    print(f'{i}: {s.generateParenthesis(i)}')
