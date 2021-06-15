class Scoop:
    def __init__(self, flavor):
        self.flavor = flavor

    def __repr__(self):
        return f'Scoop({self.flavor})'

class Bowl:
    max_scoop = 3

    def __init__(self):
        self.scoops = []

    def add_scoops(self, *new_scoops):
        for new_scoop in new_scoops:
            if len(self.scoops) < self.max_scoop:
                self.scoops.append(new_scoop)

    def __repr__(self):
        return f'Bowl(Scoops={self.scoops})'

bowl = Bowl()
bowl.add_scoops(Scoop('香草'))
bowl.add_scoops(Scoop('草莓'),Scoop('巧克力'))
bowl.add_scoops(Scoop('草莓'),Scoop('巧克力'))
print(bowl)