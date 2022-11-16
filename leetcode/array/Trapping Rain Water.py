def main():
    so = Solution()
    print(so.trap([0,1,0,2,1,0,1,3,2,1,2,1]))


class Solution:
    def trap(self, height: list[int]) -> int:
        left_max, right_max = height[0], height[-1]
        l, r = 1, len(height) - 2
        res = 0
        while l <= r:
            left_max = max(left_max, height[l])
            right_max = max(right_max, height[r])
            if left_max < right_max:
                res += left_max - height[l]
                l += 1
            else:
                res += right_max - height[r]
                r -= 1
        return res


if __name__ == '__main__':
    main()
