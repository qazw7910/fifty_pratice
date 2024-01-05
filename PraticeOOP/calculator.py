class Currency:
    def __init__(self, code, name):
        self.code = code
        self.name = name

    def get_exchange_rate(self, target_currency):
        exchange_rate = {
            ('TWD', 'USD'): 1 / 30.0,
            ('USD', 'TWD'): 30.0,
            ('TWD', 'JPY'): 3.0,
            ('JPY', 'TWD'): 1 / 3.0,
            ('USD', 'JPY'): 110.0,
            ('JPY', 'USD'): 1 / 110.0,
        }
        return exchange_rate.get((self.code, target_currency.code))


class TWD(Currency):
    def __init__(self):
        super().__init__(code='TWD', name='台幣')


class USD(Currency):
    def __init__(self):
        super().__init__(code='USD', name='美金')


class JPY(Currency):
    def __init__(self):
        super().__init__(code='JPY', name='日幣')


'''
這三種貨幣可以互相轉換
1.製作一個使用者輸入介面(input())
  A.輸入1為 "請輸入基礎貨幣代號 1.台幣 2.美元 3.日圓"
  B.輸入2為 "你有多少x貨幣"
  C.輸入3為 "想換成什麼貨幣 1.台幣 2.美元 3.日圓"
  Bonus: 包含 1 2 3 以外的錯誤提示
'''


def choose_your_currency():
    currency_represent = {1: 'TWD', 2: 'USD', 3: 'JPY'}
    while True:
        try:
            choice = int(input("請輸入您的基礎貨幣代號 1.台幣 2.美元 3.日圓").replace(' ', ''))
            return currency_represent[choice]
        except KeyError:
            print(f"您輸入的代號不在選項內，請重新輸入")
        except ValueError:
            print(f"請重新輸入選項內 1.台幣 2.美元 3.日圓 的數字代號")
        continue


def input_num():
    while True:
        try:
            num = int(input("請輸入您的要兌換的基礎貨幣總額").replace(' ', ''))
            return num
        except TypeError:
            print(f'請輸入數字')
        except ValueError:
            print(f"請輸入數字!!請重新輸入金額!!")
        continue


def choose_target_currency(oringinal_currency):
    currency_represent = {1: 'TWD', 2: 'USD', 3: 'JPY'}
    comfirm_currency = {'TWD': '台幣', 'USD': '美元', 'JPY': '日圓'}
    while True:
        try:
            choice = int(input("請輸入您要兌換的貨幣代號 1.台幣 2.美元 3.日圓").replace(' ', ''))
            if currency_represent[choice] == oringinal_currency:
                print(f'你已經是{comfirm_currency[oringinal_currency]}了')
                continue
            else:
                return currency_represent[choice]
        except KeyError:
            print(f"您輸入的代號不在選項內")
        except ValueError:
            print(f"請輸入選項內 1.台幣 2.美元 3.日圓 的數字代號")
        continue


'''
2.輸出為 "現在x對y匯率為 1:30
x 貨幣 總共可以換 y 貨幣"
ex: 現在台幣兌美元匯率為1:31
31000台幣總共可以換1000美元
'''


def create_money():
    twd = TWD()
    usd = USD()
    jpy = JPY()
    total_type_money = {'TWD': twd, 'USD': usd, 'JPY': jpy}
    return total_type_money


def user_interface():
    comfirm_currency = {'TWD': '台幣', 'USD': '美元', 'JPY': '日圓'}
    total_type_money = create_money()

    while True:
        oringinal_currency = choose_your_currency()
        num = input_num()
        target_currency = choose_target_currency(oringinal_currency)
        exchange_currency_origin = total_type_money[oringinal_currency]
        exchange_currency_target = total_type_money[target_currency]
        exchange_rate = exchange_currency_origin.get_exchange_rate(exchange_currency_target)

        print(f'現在{comfirm_currency[oringinal_currency]}對{comfirm_currency[target_currency]}'
              f'匯率為 {exchange_rate}，{num} {comfirm_currency[oringinal_currency]} '
              f'總共可以換 {num * exchange_rate}{comfirm_currency[target_currency]}')
        break


if __name__ == '__main__':
    user_interface()
