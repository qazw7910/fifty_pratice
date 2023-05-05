import collections
from typing import List


def main():
    so = Solution()
    print(so.isAnagram(s = "anagram", t = "nagaram"))


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_count = collections.Counter(s)
        t_count = collections.Counter(t)

        for key, value in s_count.items():
            if key in t_count:
                if value != t_count[key]:
                    return False
            else:
                return False

        return True

if __name__ == '__main__':
    main()
