def pl_sentence(sentence):
    tmp = []
    for word in sentence.lower().split():
        if word[0] in 'aeiou':
            tmp.append(f'{word}way')
        else:
            tmp.append(f'{word[1:]}{word[0]}ay')
    return ' '.join(tmp)
if __name__ == '__main__':
    print(pl_sentence('i am very cold'))
