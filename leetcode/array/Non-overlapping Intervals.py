from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # because in constraint intervals[a,b] that must a < b , so just sort b.
        intervals.sort(key=lambda x: x[1])
        remove = 0
        pre_end = intervals[0][0]

        for interval in intervals:
            start = interval[0]

            if start < pre_end:
                remove += 1
            else:
                pre_end = interval[1]

        return remove


if __name__ == '__main__':
    so = Solution()
    print(so.eraseOverlapIntervals(intervals=[[1, 2], [2, 3], [3, 4], [1, 3]]))
