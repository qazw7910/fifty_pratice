def pig_latin():
    word = input('輸入單字')
    if word[0] in 'aeiou':
        return word+'way'
    else:
        return word[1:] + word[0] + 'ay'

if __name__ == '__main__':
    pig_latin()