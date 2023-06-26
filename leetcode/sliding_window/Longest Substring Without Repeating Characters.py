def main():
    so = Solution2()
    print(so.lengthOfLongestSubstring(s="ddvdf"))


class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        maxLength = 0
        usedChars = {}

        for i in range(len(s)):
            if s[i] in usedChars and start <= usedChars[s[i]]:
                start = usedChars[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)

            usedChars[s[i]] = i

        return maxLength


class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        longest_substring_size = 0
        lookup = {}
        for end in range(len(s)):
            if s[end] in lookup and lookup[s[end]] > start:
                start = lookup[s[end]]

            lookup[s[end]] = end + 1

            longest_substring_size = max(longest_substring_size, end - start + 1)

        return longest_substring_size


if __name__ == '__main__':
    main()
