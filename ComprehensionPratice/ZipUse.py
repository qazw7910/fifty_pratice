answer = ['A', 'B', 'B', 'E', 'D', 'C']
wenwen = ['B', 'B', 'B', 'E', 'A', 'C']
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def main():
    print(check4(a))


def check1(answer, wenwen):
    n = 0
    for i in range(len(answer)):
        if answer[i] != wenwen[i]:
            n += 1
    return n


def check2(answer, wenwen):
    return len([1 for i in range(len(answer)) if answer[i] != wenwen[i]])


def check3(answer, wenwen):
    return len([1 for x, y in zip(answer, wenwen) if x != y])

def check4(a):
    return list(list(zip(*a)))[1][1]



if __name__ == '__main__':
    main()
