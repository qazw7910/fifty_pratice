'''class Scoop():

    def __init__(self, flavor):
        self.flavor = flavor

class Bowl():

    def __init__(self):
        self.scoops = []

    def add_scoop(self, *new_scoops):
        for new_scoop in new_scoops:
            self.scoops.append(new_scoop)

    def flavors(self):
        return '/'.join(scoop.flavor for scoop in self.scoops)

bowl = Bowl()
bowl.add_scoop(Scoop('香草'))
bowl.add_scoop(Scoop('巧克力'), Scoop('草莓'))
print(bowl.flavors())'''
############################################
'''class Scoop:

    def __init__(self,flavor):
        self.flavor = flavor

class Bowl:

    def __init__(self):
        self.scoops = []

    def add_scoop(self, *new_scoops):
        for new_scoop in new_scoops:
            self.scoops.append(new_scoop)

    def __str__(self):
        flavors = '/'.join(scoop.flavor for scoop in self.scoops)
        return f'冰淇淋口味: {flavors}'

bowl = Bowl()
bowl.add_scoop(Scoop('草莓'))
bowl.add_scoop(Scoop('巧克力'),Scoop('香草'))
print(bowl)'''
#######################################################
class Scoop:
    def __init__(self, flavor):
        self.flavor = flavor

    def __repr__(self):
        return f'Scoop({self.flavor})'

class Bowl:
    def __init__(self):
        self.scoops = []

    def add_scoops(self, *new_scoops):
        for new_scoop in new_scoops:
            self.scoops.append(new_scoop)

    def __repr__(self):
        return f'Bowl(scoop = {self.scoops})'

bowl = Bowl()
bowl.add_scoops(Scoop('草莓'))
bowl.add_scoops(Scoop('巧克力'), Scoop('香草'))

print(bowl)


























