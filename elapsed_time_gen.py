import time
import random

def elapsed_time_gen():

    last_time = time.perf_counter()
    while True:
        now_time = time.perf_counter()
        yield now_time - last_time
        last_time = now_time

elapsed_time = elapsed_time_gen()

for _ in range(5):
    time.sleep(random.randint(1, 10) / 10)
    print(next(elapsed_time))


















