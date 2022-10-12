def main():
    so = Solution()
    print(so.checkRecord(s = "PPALLP"))


class Solution:
    def checkRecord(self, s: str) -> bool:
        return s.count('A')<=1 and 'LLL' not in s


if __name__ == '__main__':
    main()