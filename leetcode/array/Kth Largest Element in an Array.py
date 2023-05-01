import heapq
from typing import List


def main():
    so = Solution()
    print(so.findKthLargest(nums = [3,2,1,5,6,4], k = 2))

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        for num in nums:
            if len(min_heap) < k:
                heapq.heappush(min_heap, num)
            else:
                heapq.heappushpop(min_heap, num)
        return min_heap[0]

if __name__ == '__main__':
    main()