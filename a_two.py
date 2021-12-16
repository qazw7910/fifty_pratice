
def find_majority_num1(data):
    from collections import Counter
    return Counter(data).most_common(1)[0][0]

def find_majority_num2(data):
    counter = [(data.count(i),i) for i in set(data)]
    return sorted(counter, reverse=True)

if __name__ == '__main__':
    print(find_majority_num2([1,2,2,3,2,3,1]))