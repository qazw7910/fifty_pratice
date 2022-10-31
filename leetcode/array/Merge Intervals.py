def main():
    so = Solution()
    print(so.merge(intervals=[[1, 3], [2, 6], [8, 10], [15, 18]]))


class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])
        tmp = []
        for x, y in intervals:
            if not tmp:
                tmp.append([x, y])
                continue
            pre_x, pre_y = tmp[-1]
            if pre_y >= x:
                tmp.pop()
                tmp.append([pre_x, max(pre_y, y)])
            else:
                tmp.append([x, y])
        return tmp



if __name__ == '__main__':
    main()
