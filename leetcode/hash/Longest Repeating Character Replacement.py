def main():
    so = Solution()
    print(so.characterReplacement(s="ABAB", k=2))


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        lookup = {}
        start = 0

        for end in range(len(s)):
            lookup[s[end]] = lookup.get(s[end], 0) + 1
            length = end - start + 1

            if length - max(lookup.values()) > k:
                lookup[s[start]] -= 1
                start += 1
        return end - start + 1


if __name__ == '__main__':
    main()
