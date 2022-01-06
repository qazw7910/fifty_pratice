class Solution:
    def two_Sum(nums, target):
        for i in range(len(nums)):
            comp = target - nums[i]

            if (comp in nums) and nums.index(comp) != i:
                return [i, nums.index(comp)]

if __name__ == '__main__':
    use_Solution = Solution
    print((use_Solution.two_Sum(nums = [2,2,11,15], target = 9)))