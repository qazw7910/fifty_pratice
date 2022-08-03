class Solution:
    def merge(self, intervals: [[int]]):

        intervals.sort(key=lambda x: x[0])
        ans = []
        for x, y in intervals:
            if not ans:
                ans.append([x, y])
                continue
            pre_x, pre_y = ans[-1]
            if pre_y > x:
                ans.pop()
                ans.append([pre_x, max(pre_y, y)])
            else:
                ans.append([x, y])
        return ans
if __name__ == '__main__':
    intervals = [[4, 9], [2, 6], [8, 10], [15, 18]]
    solution = Solution()
    print(solution.merge(intervals))