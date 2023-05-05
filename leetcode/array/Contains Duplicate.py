from typing import List


def main():
    so = Solution()
    print(so.containsDuplicate([1, 5, 1]))


class Solution:
    # solution1 sort TC:O(n log n) SC:O(n)
    # def containsDuplicate(self, nums: List[int]) -> bool:
    #     nums.sort()
    #     for i in range(len(nums)-1):
    #         if nums[i] == nums[i+1]:
    #             return True
    #     return False

    # solution2 TC:O(n) SC:O(n)
    def containsDuplicate(self, nums: List[int]) -> bool:
        return False if len(nums) == len(set(nums)) else True

if __name__ == '__main__':
    main()
