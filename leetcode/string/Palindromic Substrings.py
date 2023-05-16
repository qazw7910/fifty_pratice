class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        # palindromes = []

        def palidrom_count(left, right, s):
            nonlocal count
            while left >= 0 and right < len(s) and s[right] == s[left]:
                # palindromes.append(s[left: right + 1])
                count += 1
                left -= 1
                right += 1

        for i in range(len(s)):
            palidrom_count(i, i, s)
            palidrom_count(i, i + 1, s)

        return count


if __name__ == '__main__':
    so = Solution()
    print(so.countSubstrings(s = "aaa"))
