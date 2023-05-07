import collections
from typing import List


def main():
    so = Solution()
    print(so.isValid(s="()[]{}"))


class Solution:
    def isValid(self, s: str) -> bool:
        look_up = {"(": ")", "[": "]", "{": "}"}
        stack = []

        for char in s:
            if char in look_up:
                stack.append(char)
            elif not stack or char != look_up[stack.pop()]:
                return False
        return len(stack) == 0


if __name__ == '__main__':
    main()
