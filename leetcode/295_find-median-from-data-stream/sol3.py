"""
https://leetcode.com/problems/find-median-from-data-stream/

Using min & max heap for keeping smaller & larger values.

Main Idea:
        While keeping the median value, we can dump other values in two lists -
      the smaller and the larger. However, the order of input can be arbitrary,
      so we should maintain both lists are sorted. We only need the maximum
      value of the smaller and the minimum value of the larger, we can
      implement it by using two heaps.
        Unfortunately, python default heap only supports min-heap, the
      "smaller" list should use the negated value.

Time Complexity:
    addNum: O(nlogn)    (from O(3*nlogn) time)
    findMedian: O(1)

    The insertion will need nlogn for push, if two heaps are "imbalanced", it
    will use additional push & pop routine, which makes total 3*nlogn time
    complexity.

    The Leetcode solution suggested algorithm takes O(5*nlogn) time, but we can
    reduce it by comparing the length of two lists.
"""
__author__ = "Hwamin Kim"
__email__ = "quicksort00@gmail.com"
__license__ = "Apache-2.0"
__version__ = "1.0.0"


from heapq import heappush, heappop


class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lo = []
        self.hi = []

    def addNum(self, num: int) -> None:
        if (len(self.lo) + len(self.hi)) % 2 == 0:
            if len(self.lo) == 0 or num < self.hi[0]:
                heappush(self.lo, -num)
            else:
                heappush(self.hi, num)
                heappush(self.lo, -heappop(self.hi))
        else:
            if -self.lo[0] < num:
                heappush(self.hi, num)
            else:
                heappush(self.lo, -num)
                heappush(self.hi, -heappop(self.lo))
        #print(self.lo, '/', self.hi)

    def findMedian(self) -> float:
        if len(self.lo) == len(self.hi):
            return (self.hi[0] - self.lo[0]) / 2
        return -self.lo[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
