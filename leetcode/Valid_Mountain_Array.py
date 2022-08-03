class Solution:
    def validMountainArray(self, arr: list) -> bool:
        peak, vally = 0, 0
        for i in range(1, len(arr)-1):
            if arr[i-1] < arr[i] > arr[i+1]:
                peak += 1
            if arr[i-1] >= arr[i] <= arr[i+1]:
                vally += 1
        return peak == 1 and vally == 0
if __name__ == '__main__':
    so = Solution()
    print(so.validMountainArray([0,2,2,1]))