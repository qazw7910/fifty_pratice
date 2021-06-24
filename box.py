class Box():
    # 不用__init__的方式
    '''def SetDimension(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth'''
    # 用了__init__的方式
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    def GetVolume(self):
        return self.width * self.height * self.depth


#不用__init__的方式
'''b = Box()
b(10, 20, 30)
print(b.GetVolume())'''
#用__init__的方式
b = Box(10, 20, 30)
print(b.GetVolume())