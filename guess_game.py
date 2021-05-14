import random

def guess_number():
    answer = random.randint(0, 12)

    while True:

        str_num = input('輸入數字')

        if str_num.isdigit():

            num = int(str_num)
            if answer == num :
                print('bingo',answer)
                break
            elif  num > answer:
                print('太大')
            else:
                print('太小')
        else:
            print('請輸入數值!')

if __name__ == '__main__':
    guess_number()