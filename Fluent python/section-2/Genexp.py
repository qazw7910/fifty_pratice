from array import array

symbols = '$¢£¥€¤'

if __name__ == '__main__':
    # must use tuple syntax otherwise only print objects
    print(tuple(ord(symbol) for symbol in symbols))
    # use array can replace tuple syntax
    print(array('I', (ord(symbol) for symbol in symbols)))
