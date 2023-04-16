import time


def main():
    pass


def count_time(func):
    def wrapper():
        t1 = time.time()
        func()
        t2 = time.time()
        print(f"Total cost time {(t2 - t1):.20f}")

    return wrapper

@count_time
def counter(num):
    a = 0
    for i in range(num):
        a += i
    return a

if __name__ == '__main__':
    print(counter(10))
