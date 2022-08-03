class Solution:
    def moveZeros(self, nums):
        end = len(nums)
        for i in range(end):
            if nums[i]==0:
                del nums[i]
                nums.append(0)
                end -= 1


        return nums
if __name__ == '__main__':
    so = Solution()
    print(so.moveZeros([0,1]))
