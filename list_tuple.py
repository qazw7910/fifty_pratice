d1 = {'A': 1,'B': 2}
d2 = {'C': 3}
print({**d1, **d2})
d1.update(d2)
print(d1)