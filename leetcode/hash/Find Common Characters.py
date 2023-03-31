def main():
    so = Solution()
    print(so.commonChars(words=["bella", "label", "roller"]))


class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        check = list(words[0])
        for word in words[1:]:
            new_check = []
            for ch in word:
                if ch in check:
                    new_check.append(ch)
                    check.remove(ch)
            check = sorted(new_check)
        return check


if __name__ == '__main__':
    main()
