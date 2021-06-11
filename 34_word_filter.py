def word_filter(filename):
#set() convert dict dtype also filter repeat element
    vowels = {'a', 'e', 'i', 'o', 'u'}
    with open(filename, 'r') as f:
        words = ([word.replace('.','')
                  for line in f
                    for word in line.split()
                        if len(set(word) & vowels) >= 3])
    return words
if __name__ == '__main__':
    print(word_filter(r'document/text2.txt'))