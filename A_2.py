from collections import Counter

def find_majority_num(data):
    return Counter(data).most_common(1)[0][0]

print(find_majority_num([1, 2, 2, 3, 2, 3, 1]))