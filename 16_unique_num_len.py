#https://www.flag.com.tw/Redirect/F1750/16
def unique_num_len(number):
    return len(set(number))

numbers = [1, 2, 3, 1, 2, 3, 4, 1, 2]

if __name__ == '__main__':

    print(unique_num_len(numbers))
