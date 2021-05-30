"""
https://leetcode.com/problems/find-median-from-data-stream/

Binary search and insertion way. (with deque)

Main Idea:
    Okay, the binary search and insertion method (sol1.py) was not efficient
    enough due to the insertion overhead, which is O(n). How about using
    `collections.deque`? It is implemented by the double linked list, so it
    would be beneficial than using just `list` type.

Time Complexity:
    addNum: O(n) --------> (?)
    findMedian: O(n)

    The insertion is still O(n)-ish. Since we need Θ(n/2) for each access.
    Furthermore, we need n/2 time for returning median.
    Therefore, this method is worse than the first solution (using `list` type)
"""
__author__ = "Hwamin Kim"
__email__ = "quicksort00@gmail.com"
__license__ = "Apache-2.0"
__version__ = "1.0.0"


from bisect import insort_left
from collections import deque


class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = deque([])

    def addNum(self, num: int) -> None:
        insort_left(self.arr, num)

    def findMedian(self) -> float:
        length = len(self.arr)
        if length % 2 == 0:
            return (self.arr[length//2-1] + self.arr[(length//2)]) / 2
        return self.arr[length//2]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
