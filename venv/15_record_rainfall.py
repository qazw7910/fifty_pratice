def record_rainfall():
    rainfall = {}
    while True:
        city_name = input('請輸入程式名字: ')
        if not city_name:
            break
        rain_mm = input('請輸入雨量(mm):')
        if not rain_mm:
            break
        rainfall[city_name] = rainfall.get(city_name, 0) + int(rain_mm)

    for city, rain in rainfall.items():
        print(f'{city}: {rain}mm')

record_rainfall()