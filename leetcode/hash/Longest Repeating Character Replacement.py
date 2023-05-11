def main():
    so = Solution()
    print(so.lengthOfLongestSubstring(s = "dvdf"))


class Solution:
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
