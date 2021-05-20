import operator
'''
d = [1, 2, 3, 4, 5]
select1 = operator.itemgetter(1)
select2 = operator.itemgetter(3, 4)
print(select1(d))#2
print(select2(d))#4, 5
'''
people = [
    ('Joe', 'Biden', 'president@usa.gov'),
    ('Emmanuel', 'Macron', 'president@france.gov'),
    ('Justin', 'Trudeau', 'primeminister@canada.gov'),
    ('Angela', 'Merkel', 'primeminister@germany.gov'),
    ('Jacinda', 'Ardern', 'primeminister@newzealand.gov')
    ]

for person in sorted(people, key=operator.itemgetter(1, 0)):
    print(f'{person[1]},{person[0]} : {person[2]}')