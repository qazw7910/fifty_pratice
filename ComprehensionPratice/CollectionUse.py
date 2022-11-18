from collections import ChainMap

baseline = {'music': 'bach', 'art': 'rembrandt'}
adjustments = {'art': 'van gogh', 'opera': 'carmen'}

if __name__ == '__main__':
    print(list(ChainMap(baseline, adjustments)))