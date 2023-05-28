import collections
import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lookup = collections.Counter(nums)
        min_heap = []
        result = []

        for key, value in lookup.items():
            if len(min_heap) == k:
                heapq.heappushpop(min_heap, (value, key))
            else:
                heapq.heappush(min_heap, (value,key))

        for i in range(k-1, -1, -1):
            result.append(min_heap[i][1])
        return result


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    so = Solution()
    print(so.topKFrequent(nums, k))
