from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0

        while i < len(intervals):
            if newInterval[0] > intervals[i][1]:
                result.append(intervals[i])
            elif newInterval[1] < intervals[i][0]:
                result.append(newInterval)
                return result + intervals[i:]
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]

            i += 1
        result.append(newInterval)
        return result


if __name__ == '__main__':
    intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    newInterval = [17, 19]
    so = Solution()
    print(so.insert(intervals, newInterval))
