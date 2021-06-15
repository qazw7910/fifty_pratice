class Scoop:

    def __init__(self, flavor):
        self.flavor = flavor

    def __repr__(self):
        return f'Scoop({self.flavor})'

class Bowl:

    max_scoops = 3

    def __init__(self):
        self.scoops = []

    def add_scoops(self, *new_scoops):
        for new_scoop in new_scoops:
            if len(self.scoops) < self.max_scoops:
                self.scoops.append(new_scoop)

    def __repr__(self):
        return f'Bowl(Scoop={self.scoops})'

class ExtraBowl(Bowl):

    max_scoops = 5

bowl = ExtraBowl()
bowl.add_scoops(Scoop('香草'), Scoop('草莓'))
bowl.add_scoops(Scoop('辣椒'), Scoop('芭樂'))
bowl.add_scoops(Scoop('香蕉'), Scoop('檸檬'))
print(bowl)

'''class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f'你好，我是{self.name}'

class Employee(Person):
    pass

employee = Employee()
#employee('職員ghost')   cannot use this way because __init__ need name 
#TypeError: __init__() missing 1 required positional argument: 'name'
print(employee)'''

