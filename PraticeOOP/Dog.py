class Dog:
    def __init__(self, name: str, age: int, friendilness: int):
        self.name = name
        self.age = age
        self.friendilness = friendilness

    def likewalk(self):
        return True


class Samoyed(Dog):
    def __init__(self, name, age, friendilness):
        super().__init__(name, age, friendilness)


class Poodle(Dog):
    def __init__(self, name, age, friendilness):
        super().__init__(name, age, friendilness)

    def shedding_amount(self):
        return 0


class GoldRetriever(Dog):
    def __init__(self, name, age, friendilness):
        super().__init__(name, age, friendilness)

    def fetch_abilities(self):
        if self.age < 2:
            return 8
        elif self.age < 10:
            return 10
        else:
            return 8


class GoldDoodle(Poodle, GoldRetriever):
    def __init__(self, name, age, friendilness):
        super().__init__(name, age, friendilness)


if __name__ == '__main__':
    sammy = Samoyed('Sammy', 2, 10)
    print(sammy.name, sammy.age, sammy.friendilness, sammy.likewalk())

    goldie = GoldDoodle('goldie', 1, 10)
    print(goldie.name, goldie.age, goldie.friendilness, goldie.likewalk(), goldie.shedding_amount())
