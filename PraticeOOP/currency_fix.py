
def user_interface():
    comfirm_currency = {'TWD': '台幣', 'USD': '美元', 'JPY': '日圓'}
    total_type_money = create_money()
    while True:
        original_currency_code = choose_your_currency()  # 'TWD'
        num = input_num()
        if num is None:
            print("輸入的金額無效，請重新輸入。")
            continue
        target_currency_code = choose_target_currency(original_currency_code)  # 'USD'
        if target_currency_code is None:
            print("選擇的目標貨幣無效，請重新選擇。")
            continue
        original_currency = total_type_money[original_currency_code]
        target_currency = total_type_money[target_currency_code]
        exchange_rate = original_currency.get_exchange_rate(target_currency)
        if exchange_rate is None:
            print(f"無法找到從 {comfirm_currency[original_currency_code]} 到 {comfirm_currency[target_currency_code]} 的匯率。")
            continue
        exchanged_amount = num * exchange_rate
        print(f'現在{comfirm_currency[original_currency_code]}對{comfirm_currency[target_currency_code]}'
              f'匯率為 1:{exchange_rate}，{num} {comfirm_currency[original_currency_code]} '
              f'總共可以換 {exchanged_amount}{comfirm_currency[target_currency_code]}')
        break  # 成功執行後退出循環

if __name__ == '__main__':
    user_interface()