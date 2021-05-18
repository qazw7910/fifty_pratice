def str_sort(s):
    return ''.join(sorted(s, key=str.lower))

if __name__ == '__main__':
    print(str_sort('Python'))