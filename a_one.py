from  itertools import  combinations

def sum_of_two(data, k):
    for a_index, a_value in enumerate(data):
        for b_index, b_value in enumerate(data):

            if a_index != b_index and a_value + b_value == k:

                return [a_index, b_index]

        return []


if __name__ == '__main__':
    print(sum_of_two([2,7,11,15],9))