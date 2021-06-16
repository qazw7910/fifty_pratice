#https://www.flag.com.tw/Redirect/F1750/42
#執行dict[鍵]=值,會呼叫__setitem__()
#存取dict[鍵]=值,會呼叫__getitem__()

class Str_Dict(dict): # Str_Dict 繼承 dict

    def __setitem__(self, key, value):
        dict.__setitem__(self, str(key), value)

    def __getitem__(self, key):
        if not str(key) in self:
            self[key] = None
        return dict.__getitem__(self, str(key))

sd = Str_Dict()
sd[1] = 1
sd[3.14] = 3.14
sd['10'] = 'test'

print(sd['a'])
print(sd)
