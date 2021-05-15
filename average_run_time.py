#.isdigit() cannot use to float
def run_timing():
    total_time = 0.0
    run_number = 0
    while True:
        run_time = input('輸入跑10公里的時間:(按ENTER直接結束)')

        if run_time == '':
            break
        try:
            run_time_value = float(run_time)
            total_time += run_time_value
            run_number += 1
        except Exception as e:
            print('產生錯誤', e)

    if run_number > 0:
        average_time = (total_time/run_number)
    else:
        average_time = 0.0

    print('跑',run_number, '次的平均時間', average_time,'分鐘')

if __name__ == '__main__':
    run_timing()