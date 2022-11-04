def main():
    so = Solution()
    print(so.twoSum(nums=[3, 2, 4], target=6))


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for key, value in enumerate(nums):
            a = target - value
            if a in seen:
                return [seen[a], key]

            seen[value] = key

if __name__ == '__main__':
    main()
