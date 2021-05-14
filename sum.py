def my_sum(*args, start=0):
    print('加總',args)
    sum = 0
    for i in args:
        sum+= i
    return sum + start

if __name__ == '__main__':
    print(my_sum(1,2,3,4,5, start=10))
