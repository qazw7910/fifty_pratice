from collections import defaultdict
def record_rainfall():
    rainfall = defaultdict(int)

    while True:
        if not (city_name := input('輸入程式:')):
            break
        if not (rain_mm := input('輸入雨量: ')):
            break

        rainfall[city_name] += int(rain_mm)

    for city, rain in rainfall:
        print(f'{city}城市,{rain}雨量')


record_rainfall()