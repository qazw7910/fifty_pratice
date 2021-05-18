def sum(*item):
    if not item:
        return item
    output = item[0]
    for item in item[1:]:
        output += item
    return output

if __name__ == '__main__':
    print(sum())
    print(sum(10, 20, 30, 40))
    print(sum('abc', 'd', 'e'))
    print(sum([10, 20, 30],[40,50], [60]))