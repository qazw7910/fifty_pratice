# https://medium.com/citycoddee/python進階技巧-3-神奇又美好的-decorator-嗷嗚-6559edc87bc0
def print_func_name(func):
    def wrap_1():
        print(f"Now use function '{func.__name__}'")
        func()

    return wrap_1


def print_time(func):
    import time
    def wrap_2():
        print("Now the Unix time is {}".format(int(time.time())))
        func()

    return wrap_2


@print_func_name
@print_time
def dog_bark():
    print("Bark")

@print_time
@print_func_name
def cat_miaow():
    print("Miaow")
if __name__ == '__main__':
    # dog_bark()

    cat_miaow()