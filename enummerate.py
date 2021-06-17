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