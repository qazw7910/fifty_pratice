def num_generator(num):
    return (int(digit)
            for digit in str(num)
            if digit.isnumeric())


numbers = num_generator(3.1546)
print(numbers)
for num in numbers:
    print(type(num))