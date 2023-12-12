# https://medium.com/citycoddee/python進階技巧-3-神奇又美好的-decorator-嗷嗚-6559edc87bc0
def print_func_name(func):

    def wrap():
        print(f"Now use function {func.__name__} ")
        func()
    return wrap

def dog_bark():
    print("Bark !!!")


def cat_miaow():
    print("Miaow ~~~")


if __name__ == "__main__":
    print_func_name(dog_bark)()
    # > Now use function 'dog_bark'
    # > Bark !!!

    print_func_name(cat_miaow)()
    # > Now use function 'cat_miaow'
    # > Miaow ~~~