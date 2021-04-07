"""
https://leetcode.com/problems/excel-sheet-column-title/

Left-to-Right approach (A -> AB -> ABC)
"""
__author__ = "Hwamin Kim"
__email__ = "quicksort00@gmail.com"
__license__ = "Apache-2.0"
__version__ = "1.0.0"


BASE_DIV = [(pow(26, i) - 1) // 25 for i in range(9)]
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
             BA = 1 + (2 * 26)
              A = 1
        """
        result = ''
        for i in range(6, 0, -1):
            if columnNumber - BASE_DIV[i] >= DIV[i]:
                res = (columnNumber - BASE_DIV[i]) // DIV[i]
                columnNumber -= (res * DIV[i])
                result += chr(ord('A') + res - 1)
        result += chr(ord('A') + columnNumber - 1)
        return result
