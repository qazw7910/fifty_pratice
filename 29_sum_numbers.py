def sum_number(data):
    return sum([int(x)
                for x in data.split()
                if x.isdigit()])


if __name__ == '__main__':
    print(sum_number('10 abc 20 de44 30 55fg 40'))