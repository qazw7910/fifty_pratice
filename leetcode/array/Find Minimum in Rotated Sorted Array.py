from typing import List


def main():
    so = Solution()
    print(so.findMin(nums=[3, 4, 5, 1, 2]))
    # [2,4,5,6,7,0,1]
    # [7,0,1,2,3,4,5]
    # [11,13,15,17]


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        # edge case
        # [0,1,2,4,5,6,7]
        if nums[left] < nums[right]:
            return nums[left]

        # [1]
        if len(nums) == 1:
            return nums[0]
        # binary search
        while left < right:
            mid = (left + right) // 2
            # [4,5,6,7,0,1,2]
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            # [5,6,7,0,1,2,4]
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            # [2,4,5,6,7,0,1]
            if nums[left] < nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

        return -1
if __name__ == '__main__':
    main()
