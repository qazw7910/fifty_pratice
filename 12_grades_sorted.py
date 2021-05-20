import operator

grades = [#global
    ('Alice', 'Wooding', 89),
    ('Bob', 'Johnson', 86),
    ('Cindy', 'Letterman', 93),
    ('David', 'Moor', 86),
    ('Eddie', 'Williams', 91)
    ]

def output_grades():

    grades.sort(key=operator.itemgetter(2), reverse=True)
    output = []
    for name1, name2, grade in grades:
        output.append(f'{name1:12s}{name2:10s}{grade:5.1f}')
    return '\n'.join(output)
    '''for grade in grades:
        output.append(f'{1:12s}{0:8s}{2:.1f}'.format(*grade))
    return '\n'.join(output)
    '''
if __name__ == '__main__':
    print(output_grades())