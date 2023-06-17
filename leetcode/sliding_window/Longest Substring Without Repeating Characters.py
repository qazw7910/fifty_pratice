def main():
    so = Solution2()
    print(so.lengthOfLongestSubstring(s="pwwkew"))


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
        l = 0
        output = 0
        seen = {}
        for r in range(len(s)):
            if s[r] not in seen:
                output = max(output, r - l + 1)
            else:
                if seen[s[r]] < l:
                    output = max(output, r - l + 1)
                else:
                    l = seen[s[r]]+ 1
            seen[s[r]] = r
        return output



if __name__ == '__main__':
    main()
