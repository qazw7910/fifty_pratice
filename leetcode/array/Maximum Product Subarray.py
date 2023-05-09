from typing import List


def main():
    so = Solution()
    print(so.maxProduct(nums = [2,3,-2,4]))

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max = nums[0]
        cur_min = nums[0]
        final_max = nums[0]

        for i in range(1, len(nums)):
            next_max = cur_max * nums[i]
            next_min = cur_min * nums[i]
            cur_max = max(nums[i], next_max, next_min)
            cur_min = min(nums[i], next_max, next_min)
            final_max = max(final_max, cur_max)

        return final_max

if __name__ == '__main__':
    main()