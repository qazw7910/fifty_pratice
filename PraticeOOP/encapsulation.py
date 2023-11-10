class Son:
    def __init__(self):
        self.color = 'Red'
        self.legs = 'Long'
        self.__IQ = 300

    def play(self):
        print('Play hard.')

    def __eat(self):
        print('good')

    def hungry(self):
        self.__eat()



if __name__ == '__main__':
    nash = Son()
    nash.play()
    nash.hungry()
    # nash.__eat()
    # nash.__IQ