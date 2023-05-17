import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        lookup = collections.Counter(t)
        start = 0
        match = 0
        min_window_size = float("inf")
        min_window_substring = ""

        for end in range(len(s)):
            if s[end] in lookup:
                lookup[s[end]] -= 1
                if lookup[s[end]] == 0:
                    match += 1

            while match == len(lookup) and start < end + 1:
                cur_window_size = end - start + 1
                if cur_window_size < min_window_size:
                    min_window_size = cur_window_size
                    min_window_substring = s[start:end + 1]

                if s[start] in lookup:
                    if lookup[s[start]] == 0:
                        match -= 1
                    lookup[s[start]] += 1

                start += 1

        return min_window_substring if min_window_substring else ""


if __name__ == '__main__':
    so = Solution()
    print(so.minWindow(s="ADOBECODEBANC", t="ABC"))
