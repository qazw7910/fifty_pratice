    #enumerate() use to extract index
    # reverse() use to reverse content or string
'''
def hex_to_dec():
    hexadecimal = input('請輸入十六進位數字: ')
    decimal = 0
    for index, char in enumerate(reversed(hexadecimal)):
        if char.isdigit():
            digit_char = int(char)
        else:
            digit_char = ord(char.upper())  - ord('A') +10
            decimal += digit_char * (16 ** index)
    print(decimal)
'''
def hex_to_dec():
    hex_num = input('輸入十六進位數字')
    decimal = int(hex_num, 16)
    print('十進位結果', decimal)
if __name__ == '__main__':
    hex_to_dec()

