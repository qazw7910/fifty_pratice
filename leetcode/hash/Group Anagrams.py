import collections
from typing import List


def main():
    so = Solution()
    print(so.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup = collections.defaultdict(list)

        for word in strs:
            sorted_word = "".join(sorted(word))
            lookup[sorted_word].append(word)
        return lookup.values()
if __name__ == '__main__':
    main()
