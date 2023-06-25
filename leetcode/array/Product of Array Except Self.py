import math
import time
from typing import List


def main():
    so = Solution()
    start = time.time()
    print(so.productExceptSelf(nums=[1, 2, 3, 4]))
    end = time.time()
    print((end - start))


class Solution:
    # solution1 time limit
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     output = [1] * len(nums)
    #     # [1, 1, 1, 1]
    #     for i in range(len(nums)):
    #         output[i] = math.prod(nums[:i]) * math.prod(nums[i+1:])
    #     return output
    # ----------------------------------------------------------------
    # solution2
    def productExceptSelf(self, nums: List[int]) -> List[int]:  # TC:O(n) SC:O(1)
        output = [1] * len(nums)
        # [1, 1, 1, 1]
        for i in range(1, len(nums)):  # l->r   TC:O(n)
            output[i] = output[i - 1] * nums[i - 1]
        # [1, 1, 2, 6]
        right_prod = nums[-1]

        for i in range(len(nums) - 2, -1, -1):  # r->l  TC:O(n)
            output[i] *= right_prod
            right_prod *= nums[i]  # 4, 12, 24
        # [1, 1, 8, 6]
        # [1, 12, 8, 6]
        # [24, 12, 8, 6]
        return output


if __name__ == '__main__':
    main()
