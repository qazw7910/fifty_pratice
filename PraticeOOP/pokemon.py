from abc import ABCMeta, abstractmethod
import random


class Pokemon(metaclass=ABCMeta):
    __attack_power = int
    __defense = int
    __speed = int
    __mental_power = int

    def __init__(self, attack_power=8, defense=5, speed=3, mental_power=1):
        self.__attack_power = attack_power
        self.__defense = defense
        self.__speed = speed
        self.__mental_power = mental_power

    @abstractmethod
    def attack(self):
        pass

    def get_attack_power(self):
        return self.__attack_power

    def get_defense(self):
        return self.__defense

    def get_speed(self):
        return self.__speed

    def get_mental_power(self):
        return self.__mental_power


class Psyduck(Pokemon):
    def __init__(self):
        super().__init__(mental_power=10)

    def attack(self):
        return self.get_attack_power()


class MewTwo(Pokemon):
    def __init__(self):
        super().__init__(attack_power=12, defense=12, speed=12, mental_power=12)

    def attack(self):
        return self.get_attack_power()


class Rock:
    def __init__(self):
        self.rock_value = 3000


if __name__ == '__main__':
    pokemons = ['mewtwo', 'psyduck']

    choice = input("Choose your pokemon Psyduck or Mewtwo:").lower().replace(' ', '')


    def start(choice):

        rock = Rock()
        rock_hp = rock.rock_value
        start_game = True
        count = 0

        while start_game:
            if choice == 'mewtwo':
                mewtwo = MewTwo()
                while rock_hp > 0:
                    count += 1

                    num = random.randint(1, 100)
                    if num < 20:
                        rock_hp -= rock_hp
                        print(
                            f"what was that!!, the critical punch!! \nRock has broken by mewtwo, use total {count} times")
                        start_game = False
                    else:
                        rock_hp -= mewtwo.get_attack_power()
                        if rock_hp > 0:
                            print(f"Rock value is {rock_hp}")
                        else:
                            print(f"Rock has broken by mewtwo, use total {count} times")
                            start_game = False

            elif choice == 'psyduck':
                psyduck = Psyduck()
                while rock_hp > 0:
                    count += 1

                    num = random.randint(1, 100)
                    if num < 20:
                        rock_hp -= rock_hp
                        print(
                            f"what was that!!, the critical punch!! \nRock has broken by psyduck, use total {count} times")
                        start_game = False
                    else:
                        rock_hp -= psyduck.get_attack_power()
                        if rock_hp > 0:
                            print(f"Rock value is {rock_hp}")
                        else:
                            print(f"Rock has broken by psyduck, use total {count} times")
                            start_game = False


    while True:
        choice = input("Choose your pokemon Psyduck or Mewtwo:").lower().replace(' ', '')
        if choice in pokemons:
            start(choice)
            break
        else:
            print("NotFound Pokemon, please try again")
