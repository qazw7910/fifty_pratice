def sum_of_two(data, k):
    for a_index, a_value in enumerate(data, 1):
        for b_index, b_value in enumerate(data, 1):

            if a_index != b_index and a_value + b_value == k:
                return [a_index, b_index]

print(sum_of_two([3, 4, 9, 6], 8))
print(sum_of_two([3, 2, 2], 4))
print(sum_of_two([3, 7, 8], 9))