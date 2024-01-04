colors = ['black', 'white']
sizes = ['S', 'M', 'L']

tshirts = [(color, size) for size in sizes
                         for color in colors]



if __name__ == '__main__':
    # print(tshirts)
    # 生成器表達式
    for tshirt in ('%s %s' %(c, s) for c in colors for s in sizes):
        print(tshirt)