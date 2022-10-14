def main():
    so = Solution()
    print(so.toGoatLatin(sentence="I speak Goat Latin"))
    # "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"



class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split()
        vowels = set("AEIOUaeiou")
        tmp = []
        for i in range(0, len(words)):
            if words[i][0] not in vowels and len(words[i]) > 1:
                w = words[i][1:] + words[i][0] + 'ma' + ('a' * (i + 1))
            elif len(words[i]) < 1:
                w = words[i] + 'ma' + ('a' * (i + 1))
            else:
                w = words[i] + 'ma' + ('a' * (i + 1))
            tmp.append(w)
        return ' '.join(tmp)

if __name__ == '__main__':
    main()
