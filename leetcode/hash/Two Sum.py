def main():
    so = Solution()
    print(so.twoSum(nums=[2, 7, 11, 15], target=26))


class Solution:
    # solution1 hashmap
    # def twoSum(self, nums: list[int], target: int) -> list[int]:
    #     look_up = {}
    #
    #     for index, number in enumerate(nums):
    #         if target - number in look_up:
    #             return [look_up[target - number], index]
    #         else:
    #             look_up[number] = index

    # solution2 two pointers
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        sorted_nums = sorted(zip(nums, range(len(nums))))
        left, right = 0, len(nums) - 1
        while left < right:
            value = sorted_nums[left][0] + sorted_nums[right][0]
            if value == target:
                return [sorted_nums[left][1], sorted_nums[right][1]]
            elif value < target:
                left += 1
            else:
                right -= 1


if __name__ == '__main__':
    main()
