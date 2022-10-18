def main():
    so = Solution()
    print(so.rotate(nums=[1, 2, 3, 4, 5, 6, 7], k=3))


class Solution(object):
    def rotate(self, nums, k):
        if nums is not None and k > 0:
            k = k % len(nums)
            nums[:] = nums[-k:] + nums[:-k]

            return nums

if __name__ == '__main__':
    main()
