'''class Foo:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return f'{self.__class__.__name__}(a={self.a!r}, b={self.b!r})'
'''
'''from dataclasses import dataclass
# can ignore __init__ and __repr__ also reduce the hole program code
@dataclass
class Foo:

    a:str
    b:int

    
foo = Foo('Test', 42)

print(foo)'''
# can replace __init__ and __repr__ also reduce the hole program code
from  dataclasses import dataclass

@dataclass
class Animal:
    color:str
    leg_num:int

    def __post_init__(self):
        self.species = self.__class__.__name__

@dataclass
class Elephant(Animal):
    leg_num: int = 4
@dataclass
class Zebra(Animal):
    leg_num: int = 4
@dataclass
class Snake(Animal):
    leg_num: int = 0
@dataclass
class Parrot(Animal):
    leg_num: int = 2

elephant = Elephant('灰')
zebra = Zebra('黑白')
snake = Snake('綠')
parrot = Parrot('灰')

print(elephant)
print(zebra)
print(snake)
print(parrot)




















