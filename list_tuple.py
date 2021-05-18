<<<<<<< HEAD
d1 = {'A': 1,'B': 2}
d2 = {'C': 3}
print({**d1, **d2})
d1.update(d2)
print(d1)
=======
def mysum(*item):
    if not item:
        return item
    output = item[0]
    for item in item[1:]:
        if isinstance(item, dict):
            output.update(item)
        else:
            output += item
    return output
if __name__ == '__main__':
    print(mysum({'a': 1, 'b': 2},{'c': 3}))
