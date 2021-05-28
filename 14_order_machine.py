#https://www.flag.com.tw/Redirect/F1750/14
menu = {
    '三明治': 50,
    '咖啡' : 40,
    '沙拉' : 30
}

def order_meal(order):
    total = 0
    while True:
        if order =='':
            break
        elif order in menu:
            price = menu[order]
            total += price
            print( f'你點了{order},目前金額為{menu[order]}')
        else:
            print('我們沒有供應',order)
    return f'你的帳單金額為{total}'



if __name__ == '__main__':
    print(order_meal(input('請輸入餐點')))