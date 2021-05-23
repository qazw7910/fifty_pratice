import operator
from collections import Counter
#兩種方法

def most_repeat_word(word):
    letters = list(set(word))
    letter_count = []
    for letter in letters:
        letter_count.append((letter, word.count(letter)))
    result = sorted(letter_count, key=operator.itemgetter(1))[-1]
    return f'{result[0]}重複了{result[1]}次'

def most_repeat_word2(word):
        result = Counter(word).most_common(1)[0]
        print(f'{result[0]}重複了{result[1]}變')

if __name__ == '__main__':

    print(most_repeat_word2('independence'))