import sys

mylist = []

for i in range(15):
    l_size = sys.getsizeof(mylist)
    t_size = sys.getsizeof(tuple(mylist))
    print(f'len = {len(mylist)}, list size = {l_size}, tuple size = {t_size}')
    mylist.append(i)