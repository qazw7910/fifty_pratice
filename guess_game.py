import random

def guess_number():
    answer = random.randint(0, 12)

    while True:

        num = input('輸入數字')
        num = int(num)

        if answer == num :
            print('bingo',answer)
            break
        elif  num > answer:
            print('太大')
        else:
            print('太小')


if __name__ == '__main__':
    guess_number()