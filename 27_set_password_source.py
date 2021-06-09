#https://www.flag.com.tw/Redirect/F1750/27
import random
def set_password_source(source):
    def password_gen(length):
        output = []
        for i in range(length):
            output.append(random.choice(source))
        return ''.join(output)  #把list轉成str
    return password_gen

if __name__ == '__main__':
    my_password_gen = set_password_source('123456789abcdefghi')#先放公式進去所創建的my_password_gen,my_password_gen他會被存在記憶體裡,
    print(my_password_gen(10))                                 #再用my_password_gen(n)去呼叫my_password_gen裡的password_gen()
    print(type(my_password_gen(6)))
