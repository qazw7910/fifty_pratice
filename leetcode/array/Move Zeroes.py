def main():
    so = Solution()
    print(so.moveZeroes(nums=[0, 1, 0, 3, 12]))


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        end = len(nums)
        i = 0
        while i < end:
            if nums[i] == 0:
                del nums[i]
                nums.append(0)
                end -= 1
            else:
                i += 1
        return nums


if __name__ == '__main__':
    main()
