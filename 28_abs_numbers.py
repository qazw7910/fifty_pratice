'''def abs_numbers(nunber):
    return [abs(x) for x in nunber]
'''

def abs_numbers(number):
    return list(map(abs, number))

if __name__ == '__main__':
    print(abs_numbers([1, -2, 3, -4, 5]))
