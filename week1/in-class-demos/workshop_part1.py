# crazy_list = [1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7]
# print(crazy_list[3][1][2][0])

animals = ['Lion', 'Tiger', 'Elephant', 'Giraffe', 'Cheetah']

# has_Zebra = False
# for animal in animals:
#     if animal == 'Zebra':
#         has_Zebra = True
#         break
#
# if animals.__contains__('Zebra'):
#     has_Zebra = True
#
# try:
#     animals.index('Zebra')
# except ValueError:
#     print('No Zebra found')

print("Has Zebra:", "Zebra" in animals)

animals.append('Zebra')
animals.remove('Cheetah')

animals = tuple(animals)

print(animals)

animals_dict = {'Lion': 'Brave',
           'Tiger': 'Fierce',
           'Elephant': 'Large',
           'Giraffe': 'Tall',
           'Zebra': 'Striped'}
print(animals_dict)

animal_names = list(animals_dict.keys())
animal_characteristics = list(animals_dict.values())

animal_dict2 = dict(zip(animal_names, animal_characteristics))
print(animal_dict2)

animal_dict3 = {n:c for n, c in zip(animal_names, animal_characteristics)}
print(animal_dict3)  # list comprehension