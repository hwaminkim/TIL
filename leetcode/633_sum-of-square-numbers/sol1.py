"""
https://leetcode.com/problems/sum-of-square-numbers/

*** `float` type has its own function `is_integer()` which is very useful.
*** Note `float` also has `as_integer_ratio()` function.

Main Idea: Check squared root is an integer
    - If a^2 + b^2 = c, sqrt(c - b^2) should be an integer. (the a)
    - For all possible integer b, try there exists an possible case

Complexity:
    O(sqrt(c) * logc)

    - Try sqrt(c) numbers of possible integers.
    - logc for sqrt() function at the worst case.
"""
__author__ = "Hwamin Kim"
__email__ = "quicksort00@gmail.com"
__license__ = "Apache-2.0"
__version__ = "1.0.0"


from math import sqrt


class Solution:
    def judgeSquareSum(self, num_c: int) -> bool:
        if num_c == 0:
            return True

        num_b = 1
        while True:
            a_square = num_c - (num_b**2)
            if a_square < 0:
                return False
            if sqrt(a_square).is_integer():
                return True
            num_b += 1
