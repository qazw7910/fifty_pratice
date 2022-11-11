def main():
    so = Solution()
    print(so.commonChars(words = ["bella","label","roller"]))

class Solution:
    def commonChars(self, words:list[str])->list[str]:

        check = list(words[0])
        for word in words[1:]:
            newCheck = []
            for ch in word:
                if ch in check:
                    newCheck.append(ch)
                    check.remove(ch)
            check = sorted(newCheck)
        return check
if __name__ == '__main__':
    main()