class MyEnumerate():

    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration

        value = (self.index, self.data[self.index])
        self.index +=1
        return value

myenu = MyEnumerate('abcde')

for index , letter in myenu:
    print(f'{index}->{letter}')

for index, letter in enumerate('abcde'):
    print(f'{index}->{letter}')

n = [1, 2, 3, 4, 5]
print(type(iter(n)))

d = {'a' : 1, 'b' : 2, 'c' : 3}
print(type(iter(d.items())))

s = 'test'
print(type(iter(s)))