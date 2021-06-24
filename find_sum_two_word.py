
'''def sum_of_two(data, k):
    for a_index, a_value in enumerate(data, 1):
        for b_index, b_value in enumerate(data, 1):

            if a_index != b_index and a_value + b_value == k:
                return [a_index, b_index]
print(sum_of_two([3, 4, 9, 6], 8))
print(sum_of_two([3, 2, 2], 4))
print(sum_of_two([3, 7, 8], 9))
'''
from itertools import combinations
'''for c in combinations([2, 7, 11, 15], 2):
    print(c)
(2, 7)
(2, 11)
(2, 15)
(7, 11)
(7, 15)
(11, 15)'''
def TwoSum(data, k):
    for a, b in combinations(data, k):
        return a

print(TwoSum([3, 4, 9, 6], 2))
