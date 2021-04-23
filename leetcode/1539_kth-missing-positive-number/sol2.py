"""
https://leetcode.com/problems/excel-sheet-column-title/

Right-to-Left approach (C -> BC -> ABC)
(Python, 100%)
"""
__author__ = "Hwamin Kim"
__email__ = "quicksort00@gmail.com"
__license__ = "Apache-2.0"
__version__ = "1.0.0"


DIV = [pow(26, i) for i in range(9)]


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        """
        Note 1)
            A = 1
            AA = 1 + 26
            AAA = 1 + 26 + 26^2
            BAA = 1 + 26 + 2*26^2
            ABA = 1 + 2*26 + 26^2
            ...

        Note 2)
            A(n) = 1 + 26 + 26^2 + ... + 26^n = (26^(n+1) - 1) / 25

        Note 3)
            BBA = 1 + (2 * 26) + (2 * 26^2)
            BB  = (2 * 26) + (2 * 26^2)
            B   = (2 * 26^2)
        """
        result = ''
        i = 1
        while columnNumber > 0:
            res = columnNumber % DIV[i] // DIV[i-1]
            if res == 0:
                # When the character is 'Z'
                res = 26
            columnNumber -= (res * DIV[i-1])
            result = chr(ord('A') - 1 + res) + result
            i += 1
        return result
