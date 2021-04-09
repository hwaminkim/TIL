"""
https://leetcode.com/problems/3sum/
3 Sum

O(n^2) Solution with sorting + 2 pointers
    - For sorted array, 2 sum will take O(n) time.
        - 2 pointer approach
    - Therefore, we can apply two-sum problem for every element in array.

Trick for reducing length of input.
    - Since the problem only requires maximum 3 elements, there is no meaning
      4 or more same elements in array.
    - Therefore, we can reduce the `nums` by reducing same elements.
    - In the Leetcode solution, they used while loop on two-sum routine,
      but this is better because it also can reduce sorting (O(n*logn)) by this
      reduction routine (O(n))
"""
__author__ = "Hwamin Kim"
__email__ = "quicksort00@gmail.com"
__license__ = "Apache-2.0"
__version__ = "1.0.0"


from collections import Counter


class Solution:
    def threeSum(self, nums: 'List[int]') -> 'List[List[int]]':
        # Reducing `nums`
        nums = sorted([k for k, v in Counter(nums).items()
                       for _ in range(min(v, 3))])

        result = set()
        def two_sum(start: int, target: int) -> None:
            low = start + 1
            high = len(nums) - 1
            while low < high:
                sums = nums[low] + nums[high]
                if sums < target:
                    low += 1
                elif sums > target:
                    high -= 1
                else:
                    result.add((nums[start], nums[low], nums[high]))
                    low += 1
                    high -= 1

        for idx_start in range(len(nums)-2):
            if nums[idx_start] > 0:
                break
            two_sum(idx_start, -nums[idx_start])
        return result
