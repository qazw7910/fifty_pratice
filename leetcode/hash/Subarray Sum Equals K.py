import collections


def main():
    so = Solution1()
    print(so.subarraySum(nums=[1, 1, 1], k=2))


class Solution1:
    def subarraySum(self, nums: list[int], k: int) -> int:
        counts = collections.Counter()
        counts[0] = 1
        ans = 0
        prefsum = 0
        for num in nums:
            prefsum += num
            ans += counts[prefsum - k]
            counts[prefsum] += 1
        return ans


class Solution2:
    def subarraySum(self, nums: list[int], k: int) -> int:
        ans = 0
        prefsum = 0
        dic = {0: 1}
        for num in nums:
            prefsum += num
            if prefsum - k in dic:
                ans += dic[prefsum - k]
            if prefsum not in dic:
                dic[prefsum] = 1
            else:
                dic[prefsum] += 1
        return ans


if __name__ == '__main__':
    main()
