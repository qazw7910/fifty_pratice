#https://www.flag.com.tw/Redirect/F1750/17


def dict_diff(first, second):
    output = []
    all_key = sorted(first.keys() | second.keys())

    for key in all_key:
        #print(key, first.get(key), second.get(key))
        if first.get(key) != second.get(key):
            output.append(key)

    return output

d1 = {'a': 1, 'b': 2, 'c': 3, 'd': 5}
d2 = {'a': 1, 'b': 2, 'd': 4, 'e': 6}
if __name__ == '__main__':
    print(dict_diff(d1, d2))