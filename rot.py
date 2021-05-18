import codecs
print(codecs.encode('apple','rot13'))
def rot13(word):
    output =[]
    for i in word.lower():
        new_ord = ord(i) + 13
        if new_ord > ord('z'):
            new_ord -= 26
        output.append(chr(new_ord))
    return ''.join(output)

if __name__ == '__main__':
    print(rot13('apple'))