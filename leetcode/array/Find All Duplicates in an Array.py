def main():
    so = Solution()
    print(so.findDuplicates([4, 5, 2, 7, 8, 2, 3, 1]))

#test
class Solution(object):
    def findDuplicates(self, nums):
        res = []
        for i in range(len(nums)):
            ind = abs(nums[i]) - 1
            if nums[ind] < 0:
                res.append(ind + 1)
            else:
                nums[ind] *= -1
        return res


if __name__ == '__main__':
    main()
