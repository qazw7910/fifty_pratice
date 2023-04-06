def main():
    so = Solution()
    print(so.maxArea(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]))


class Solution:
    def maxArea(self, height: list[int]) -> int:
        # initialize the maximum area to be 0
        max_area = 0
        # initialize the left and right pointers
        left, right = 0, len(height) - 1

        # loop until the two pointers meet
        while left < right:
            area = min(height[left], height[right]) * (right - left)  # calculate the area
            max_area = max(max_area, area)  # update the maximum area found so far

            # move the pointer with the smaller height to the right
            if height[left] < height[right]:
                left += 1

            # move the pointer with the smaller height to the left
            else:
                right -= 1

        return max_area


if __name__ == '__main__':
    main()
