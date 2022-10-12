def main():
    so = Solution()
    print(so.reverseString(s=["h", "e", "l", "l", "o"]))


class Solution:
    def reverseString(self, s: list[str]) -> None:
        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return s


if __name__ == '__main__':
    main()
