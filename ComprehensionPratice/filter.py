# example 1
List = [0, 1, 2, 0, 'Python']
result = filter(bool, List)
print(result)
# ->filter object need to convert to list
print(list(result))

# example 2
demo_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
demo_list1_result = filter(lambda x: x > 2, demo_list1)
print(demo_list1_result)
# ->filter object need to convert to list
print(list(demo_list1_result))

# example 3
demo_list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def odd(n: int) -> int:
    if n % 2 == 1:
        return n


demo_list2_result = filter(odd, demo_list2)
print(list(demo_list2_result))

# example 4
demo_list3 = [1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8]
demo_list3_result = filter(lambda x: x != 0, demo_list3)
print(list(demo_list3_result))
