from menu import menu
def func_a():
    return '執行函式A'

def func_b():
    return '執行函式B'

def func_x():
    return '執行函式X'

my_menu = menu(a=func_a,b=func_b,x=func_x)

func = my_menu
print(func)

print(menu.__name__)