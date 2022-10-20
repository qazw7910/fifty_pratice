def main():
    so = Solution()
    print(so.merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[1, 3, 6], n=3))


class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]
        return nums1


if __name__ == '__main__':
    main()
