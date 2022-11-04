def main():
    so = Solution()
    print(so.intersection(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4]))


# class Solution:
#     def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
#         if len(nums1) >= len(nums2):
#             long = nums1
#             short = nums2
#         else:
#             long = nums2
#             short = nums1
#
#         seen = []
#         ans = []
#
#         for i in short:
#             if i not in seen:
#                 seen.append(i)
#
#         for i in seen:
#             if i in long:
#                 ans.append(i)
#
#         return ans

class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        ans = list(set1 & set2)

        return ans



if __name__ == '__main__':
    main()
