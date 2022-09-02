def main():
    so = Solution()
    print(so.nextPermutation([1, 5, 1]))

class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        i = j = len(nums) - 1
        while nums[i] <= nums[i - 1] and i >= 0:
            i -= 1
        if i == 0:
            nums.reverse()
            return nums

        k = i - 1
        while nums[k] >= nums[j]:
            j -= 1
        nums[k], nums[j] = nums[j], nums[k]

        l = k + 1
        r = len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        return nums


if __name__ == '__main__':
    main()
