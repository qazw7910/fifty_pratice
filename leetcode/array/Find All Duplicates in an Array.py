def main():
    so = Solution()
    print(so.findDuplicates([4, 5, 2, 7, 8, 2, 3, 1]))


class Solution(object):
    def findDuplicates(self, nums):
        freq_dict = {}

        for num in nums:
            freq_dict[num] = freq_dict.get(num, 0) + 1

        result = []
        for key, value in freq_dict.items():
            if value >= 2:
                result.append(key)

        return result


if __name__ == '__main__':
    main()
