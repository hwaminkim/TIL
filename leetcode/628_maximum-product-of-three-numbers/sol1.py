"""
https://leetcode.com/problems/maximum-product-of-three-numbers/
Maximum Product of Three Numbers

The tricky part
    - `nums` can store both negative and positive number.
    - Example 1)
        - nums: [-5, -4, 1, 2, 3]
        - Answer: 60    (-5 * -4 * 3)
    - Example 2)
        - nums: [-2, -1, 1, 4, 5]
        - Answer: 20    (1 * 4 * 5)
    - Both examples store positivie and negative numbers, but selected numbers
      (positions) are different.
    - So, there are two possibility for making maximum product.
        1) MAX[0] * MAX[1] * MAX[2]    (MAX[0] is the largest value of `nums`)
        2) MAX[0] * MIN[0] * MIN[1]    (MIN[0] is the smallest value of `nums`)
    - Using single smallest value is meaninglesss cause it may return negative
      value.
    - Therefore, we only need five numbers: MAX[0:3], MIN[0:2]

Summary of Time Complexity about Heap
    - Building Binary Heap: O(n)
        - https://www.geeksforgeeks.org/time-complexity-of-building-a-heap/
        - https://stackoverflow.com/questions/9755721/how-can-building-a-heap-be-on-time-complexity
        - It looks O(n*logn), but every call fo `heapify` size reduced by 2
        - Therefore, the tight bound is O(n)
    - Heap Sort: O(n*logn)
        - Building -> O(n) / Pop n elements from heap -> O(logn)
        - Therefore, O(n * log n)
    - Get maximum value from min heap: O(n)
    - Get maximum k values from min heap: O(n * logk)

Time complexity of this Solution:
    - O(n * log3 + n * log2) = O(n)

Other Solutions:
    - There exists Single Scan solution (O(n)) on Leetcode by manually
      comparing and swapping 3 maximum values and 2 minimum values, but I
      prefre this way since it mathematically compact and easy to understand
      code.
"""
__author__ = "Hwamin Kim"
__email__ = "quicksort00@gmail.com"
__license__ = "Apache-2.0"
__version__ = "1.0.0"


from heapq import nlargest, nsmallest
from math import prod


class Solution:
    def maximumProduct(self, nums: 'List[int]') -> int:
        llarge = nlargest(3, nums)
        lsmall = nsmallest(2, nums)
        return max(prod(llarge), prod(lsmall)*llarge[0])
