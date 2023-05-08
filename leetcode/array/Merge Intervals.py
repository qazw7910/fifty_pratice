def main():
    so = Solution()
    print(so.merge(intervals=[[1, 3], [2, 6], [8, 10], [15, 18]]))


class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda interval: interval[0])
        result = []
        
        for interval in intervals:
            if not result or interval[0] > result[-1][1]:
                result.append(interval)
            else:
                result[-1][1] = max(interval[1], result[-1][1])

        return result



if __name__ == '__main__':
    main()
