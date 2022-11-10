names = ['Mariya', 'Gendalf', 'Batman']
profs = ['programer', 'wizard', 'superhero']

my_dict = {names[i]: profs[i] for i in range(len(names))}

# my_dict = {key: value for key, value in zip(names, profs)}


# for key, val in zip(names, profs):
#     my_dict[key] = val

my_dict = {key+'man':val for key, val in my_dict.items()}

print(my_dict)
