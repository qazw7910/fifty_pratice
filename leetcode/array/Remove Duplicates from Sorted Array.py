def main():
    so = Solution()
    print(so.removeDuplicates(nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        x = 1
        for i in range(len(nums)-1):
            if nums[i] != nums[i + 1]:
                nums[x] = nums[i + 1]
                x += 1
        return x ,nums


if __name__ == '__main__':
    main()
