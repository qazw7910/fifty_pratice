def main():
    so = Solution()
    print(so.maxArea(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]))


class Solution:
    def maxArea(self, height: list[int]) -> int:
        l = 0
        r = len(height) - 1
        width = len(height) - 1
        res = 0
        for w in range(width, 0, -1):
            if height[l] < height[r]:
                res = max(res, height[l] * w)
                l += 1
            else:
                res = max(res, height[r] * w)
                r -= 1
        return res


if __name__ == '__main__':
    main()
