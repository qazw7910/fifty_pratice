import collections
from typing import List


def main():
    so = Solution()
    print(so.maxSubArray(nums = [-2,1,-3,4,-1,2,1,-5,4]))


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_num = 0
        max_sum = float("-inf")
        for num in nums:
            cur_num += num
            cur_num = max(cur_num, num)
            max_sum = max(max_sum, cur_num)

        return max_sum


if __name__ == '__main__':
    main()
