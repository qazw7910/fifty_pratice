def word_generator(filename, max_word):
    index = 0
    with open(filename, 'r') as f:
        for line in f:
            for word in line.split():
                if index >= max_word:
                    return
                yield word.replace('.','')
                index += 1

ten_words = word_generator(r'document/text2.txt', 10)

for word in ten_words:
    print(word)

###########################################

def generator_func(data):
    index = 0
    while True:
        if index >= len(data):
            return
        yield data[index]
        index += 1

letters = generator_func('abc')
print(letters)
for letter in letters:
    print(letter)