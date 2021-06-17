'''class CycleIterator():
    def __init__(self, data, max_times):
        self.data = data
        self.max_times = max_times
        self.index = 0

    def __next__(self):
        if self.index >= self.max_times:
            raise StopIteration

        value = self.data[self.index % len(self.data)]
        self.index +=1
        return value

class CycleList():
    def __init__(self, data, max_times):
        self.data = data
        self.max_times = max_times

    def __iter__(self):
        return CycleIterator(self.data, self.max_times)'''
from dataclasses import dataclass
@dataclass
class CycleIterator():
    data:list
    max_times:int

    def __post_init__(self):    #不用透過__init__來初始化
        self.index = 0

    def __next__(self):
        if self.index >= self.max_times:
            raise StopIteration

        value = self.data[self.index % len(self.data)]
        self.index += 1
        return value
@dataclass
class CycleList():
    data:list
    max_times:int

    def __iter__(self):
        return CycleIterator(self.data, self.max_times)

clist = CycleList(['a', 'b', 'c'], 5)
for c in clist:
    print(c)





















