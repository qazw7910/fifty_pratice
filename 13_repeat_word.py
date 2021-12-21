import operator
from collections import Counter
#兩種方法

def most_repeat_word1(word):
    letters = list(set(word))
    letters_count = []
    for letter in letters:
        letters_count.append((letter, word.count(letter)))

    result = sorted(letters_count, key=operator.itemgetter(1))[-1]
    return f'{result[0]} 重複了 {result[1]} 次'

def most_repeat_word2(word):
    result = Counter(word).most_common(1)[0]
    return f'{result[0]}重複了{result[1]}變'

def most_repeat_word3(word):
    letter_count = Counter(word)
    result = letter_count.most_common()[0]
    return f'{result[0]}'

if __name__ == '__main__':

    print(most_repeat_word3('independence'))