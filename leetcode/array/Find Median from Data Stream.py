from heapq import heappush, heappop


class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        if not self.max_heap or -self.max_heap[0] > num:
            heappush(self.max_heap, -num)
        else:
            heappush(self.min_heap, num)

        if len(self.max_heap) > len(self.min_heap) + 1:
            heappush(self.min_heap, -heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heappush(self.max_heap, -heappop(self.min_heap))

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] - self.max_heap[0]) / 2
        return -self.max_heap[0]

if __name__ == '__main__':
    # ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
    # [[], [1], [2], [], [3], []]
    MedianFinder = MedianFinder()
    MedianFinder.addNum(1)
    MedianFinder.addNum(2)
    print(MedianFinder.findMedian())
    MedianFinder.addNum(3)
    print(MedianFinder.findMedian())