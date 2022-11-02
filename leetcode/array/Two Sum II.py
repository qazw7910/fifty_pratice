def main():
    so = Solution()
    print(so.twoSum(numbers=[2, 7, 11, 15], target=9))


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            s = numbers[l] + numbers[r]
            if s < target:
                l += 1
            elif s > target:
                r -= 1
            else:
                return [l + 1, r + 1]


if __name__ == '__main__':
    main()
