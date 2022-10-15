def main():
    so = Solution()
    print(so.reorderLogFiles(logs=["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]))


class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        digits = []
        letters = []

        for log in logs:

            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)

        letters.sort(key=lambda x: x.split()[1])
        letters.sort(key=lambda x: x.split()[1:])
        result = letters + digits
        return result


if __name__ == '__main__':
    main()
