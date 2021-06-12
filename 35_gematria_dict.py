import string

print(string.ascii_lowercase)
print(list(enumerate(string.ascii_lowercase)))
print(list(enumerate(string.ascii_lowercase, 1)))
def gematria_dict():
    return {index : value
            for value, index in enumerate(string.ascii_lowercase, 1)}
if __name__ == '__main__':
    print(gematria_dict())