#https://www.flag.com.tw/Redirect/F1750/21
def find_longest_word(filename):
    longest = ''
    with open(filename,'r') as f:
        for line in f:
            for word in line.replace('.','').split():
                if len(word) > len(longest):
                    longest = word
    return longest

    '''word = set()
    with open(filename, 'r') as f:
        for line in f:
            word.update(line.replace('.', '').split())

    return sorted(word, key=len)[-1]'''


if __name__ == '__main__':
    print(find_longest_word('document/text2'))








'''str = "this is string example....wow!!! this is really string";
print str.replace("is", "was");
print str.replace("is", "was", 3);

thwas was string example....wow!!! thwas was really string
thwas was string example....wow!!! thwas is really string'''