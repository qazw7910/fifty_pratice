#https://www.flag.com.tw/Redirect/F1750/20
from io import StringIO

def wordcount(filename):
    result = {
        'Character' : 0,
        'Word' : 0,
        'Unique word' : 0,
        'Line' : 0
    }
    unique_words = set()

    with open(filename) as f:
        for line in f:
            word = line.split() #type = list
            result['Character'] += len(line)
            result['Word'] += len(word)
            result['Line'] += 1
            unique_words.update(word)

        result['Unique word'] = len(unique_words)
    for key, value in result.items():
        print( f'{key} : {value}')



if __name__ == '__main__':
    wordcount(r'document/text')
























