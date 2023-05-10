def main():
    so = Solution()
    print(so.maxArea(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]))


class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        max_water = 0
        while left < right:
            max_water = max(
                max_water,
                min(height[left], height[right]) * (right - left)
            )
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_water


if __name__ == '__main__':
    main()
