from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest_consec = 0

        for num in nums:
            if num - 1 not in nums:
                cur_consec = 1
                while num + cur_consec in nums:
                    cur_consec += 1
                longest_consec = max(longest_consec,cur_consec)

        return longest_consec

if __name__ == '__main__':
    nums = [100, 4, 200, 1, 3, 2]
    so = Solution()
    print(so.longestConsecutive(nums))
