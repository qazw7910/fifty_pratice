from typing import List


def main():
    so = Solution()
    print(so.search(nums=[4, 5, 6, 7, 0, 1, 2], target=0))


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:                              # binary search to divide array
            mid = (low + high) // 2
            if nums[mid] == target:                     # mid judge once
                return mid

            elif nums[low] < nums[mid]:
                if nums[low] == target:                 # low judge once
                    return low
                elif nums[low] < target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[high] == target:                # high judge once
                    return high
                if nums[mid] < target < nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1


if __name__ == '__main__':
    main()
