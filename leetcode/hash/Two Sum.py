def main():
    so = Solution()
    print(so.twoSum(nums=[3, 2, 4], target=6))


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i in range(len(nums)):
            a = target - nums[i]
            if a in seen:
                return [seen[a], i]
            else:
                seen[nums[i]] = i


if __name__ == '__main__':
    main()
