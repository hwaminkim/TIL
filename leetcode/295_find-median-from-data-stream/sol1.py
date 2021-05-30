"""
https://leetcode.com/problems/find-median-from-data-stream/

Binary search and insertion way.

Main Idea:
    By using the binary search (bisect.insort_left), maintain the sorted array.

Time Complexity:
    addNum: O(n)
    findMedian: O(1)

    It looks like O(nlogn), but actually O(n)
        - Finding a proper location to insert O(nlogn)
        - Inserting a new element in the array O(n)   (in worst case)
            - All the other elements after the insertion point should be pushed
"""
__author__ = "Hwamin Kim"
__email__ = "quicksort00@gmail.com"
__license__ = "Apache-2.0"
__version__ = "1.0.0"


from bisect import insort_left


class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []

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
