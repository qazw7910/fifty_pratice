class Solution:
    def rotate(self, nums:list, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        nums[:] = nums[(n-k):] + nums[:(n-k)]
        return nums

if __name__ == '__main__':
    so = Solution()
    print(so.rotate([1,2,3,4,5,6,7], 3))
