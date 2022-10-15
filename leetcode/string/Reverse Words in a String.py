def main():
    so = Solution()
    print(so.reverseWords("  the sky  is  blue"))


class Solution:
    def reverseWords(self, s: str) -> str:
        arr = list(s)
        arr = self.reverse_string(arr, 0, len(arr) - 1)
        arr = self.reverse_word(arr)
        arr = self.trim_sides(arr)
        arr = self.trim_space(arr)
        return ''.join(arr)

    def reverse_string(self, arr, l, r):
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            r -= 1
            l += 1
        return arr

    def reverse_word(self, arr):
        l, r = 0, 0
        while r < len(arr):
            while r < len(arr) and not arr[r].isspace():
                r += 1
            self.reverse_string(arr, l, r - 1)
            r += 1
            l = r
        return arr

    def trim_sides(self, arr):
        if ''.join(arr).isspace(): return []
        l, r = 0, len(arr) - 1
        while l < r and arr[l].isspace(): l += 1
        while l < r and arr[r].isspace(): r -= 1
        return arr[l:r + 1]

    def trim_space(self, arr):
        res = [arr[0]]
        for i in range(1, len(arr)):
            if res[-1].isspace() and arr[i].isspace():
                continue
            res.append(arr[i])
        return res


if __name__ == '__main__':
    main()
