def pl_word(word):
    if word[0] in 'aeiou':
        return f'{word}way'
    return f'{word[1:]}{word[0]}ay'

def pl_file(filename):
    with open(filename,'r') as f:
        return ' '.join([pl_word(word).lower().replace('.','')
                         for line in f
                         for word in line.split()
                         ])


if __name__ == '__main__':
    print(pl_file(r'document/text2.txt'))