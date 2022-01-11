import collections
class Solution:
    def shiftGrid(self, grid:list, k:int):
        col, nums = len(grid[0]), sum(grid, [])
        k = k % len(nums)
        nums = nums[-k:] + nums[:-k]
        temp = []
        for i in range(0, len(nums), col):
            temp += [nums[i:i+col]]
        return temp

if __name__ == '__main__':
    so = Solution()
    print(so.shiftGrid(grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1))