class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        start = 0
        longest_substring_size = 0
        lookup = {}

        for end in range(len(s)):
            lookup[s[end]] = lookup.get(s[end], 0) + 1
            length = end - start + 1

            while length - max(lookup.values()) > k:
                lookup[s[start]] -= 1
                start += 1
                length = end - start + 1
            longest_substring_size = max(longest_substring_size, length)

        return longest_substring_size


if __name__ == '__main__':
    so = Solution()
    print(so.characterReplacement(s="dvdf", k=1))
