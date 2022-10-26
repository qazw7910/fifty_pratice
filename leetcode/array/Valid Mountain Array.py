def main():
    so = Solution()
    print(so.validMountainArray(arr=[1, 7, 9, 5, 4, 1, 2]))


class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        peak, vally = 0, 0
        for i in range(1, len(arr) - 1):
            if arr[i - 1] < arr[i] > arr[i + 1]:
                peak += 1
            if arr[i - 1] >= arr[i] <= arr[i + 1]:
                vally += 1
        return peak == 1 and vally == 0


if __name__ == '__main__':
    main()
