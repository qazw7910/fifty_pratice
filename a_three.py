
def find_missing_nums(data):
    all_data = set(range(1, len(data)+1))
    return  list(all_data - set(data))

if __name__ == '__main__':
    print(find_missing_nums([1,2,8,5,1,6,4,9,5]))