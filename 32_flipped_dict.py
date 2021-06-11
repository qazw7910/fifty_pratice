def flipped_dict(input_data):

    return {value : key
            for key, value in input_data.items()}

if __name__ == '__main__':
    print(flipped_dict({'a':1, 'b':2, 'c':3}))