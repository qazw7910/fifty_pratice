import operator

def prefix(to_solve):

    def isnumber(num):
        return num.replace('.','').isnumber()

    operation = {
        '+' : operator.add,
        '-' : operator.sub,
        '*' : operator.mul,
        '/' : operator.truediv
    }

    items = to_solve.split()
    while len(items) > 1:
        for i in range(len(items) - 2):
            op, n1, n2 = items[i : i+3]
            if op in operation and isnumber(n1) and isnumber(n2):
                break
    items = items[:i] + [str(operation[op](float(n1),float(n2)))] + items[i+3:]
    return float[items[0]]
if __name__ == '__main__':
    print(prefix('+ 2 3'))