def main():
    so = Solution()
    print(so.isAlienSorted(words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"))


class Solution:
    def isAlienSorted(self, words: list[str], order: str):
        dict = {}
        new_words = []
        for key, value in enumerate(order):
            dict[value] = key

        for word in words:
            new = []
            for ch in word:
                new.append(dict[ch])
            new_words.append(new)

        for w1, w2 in zip(new_words, new_words[1:]):
            if w1 > w2:
                return False
        return True

if __name__ == '__main__':
    main()