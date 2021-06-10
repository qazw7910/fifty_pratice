def flattern(data):
    output = []
    '''for x in data:
        for y in x:
            output.append(y)
    return output
'''
    return [sub_element
            for element in data
            for sub_element in element]
if __name__ == '__main__':
    print(flattern([[1, 2],[3, 4]]))