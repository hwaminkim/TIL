"""
https://leetcode.com/problems/two-sum-bsts/

Simple Brute-Force approach (N1 * N2)
"""
__author__ = "Hwamin Kim"
__email__ = "quicksort00@gmail.com"
__license__ = "Apache-2.0"
__version__ = "1.0.0"


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def twoSumBSTs(self, root1: 'TreeNode', root2: 'TreeNode',
                   target: int) -> bool:
        def dfs(root: 'TreeNode') -> int:
            stk = deque([root])
            while stk:
                cur_node = stk.pop()
                if cur_node is None:
                    continue
                yield cur_node.val
                stk.append(cur_node.right)
                stk.append(cur_node.left)

        for e1 in dfs(root1):
            for e2 in dfs(root2):
                if e1 + e2 == target:
                    return True
        return False
