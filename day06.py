#1 
empty_tuple = ()

#2
brothers = ('Leo','Luca','Thiago')
sisters = ('Mia','Lara')

#3
siblings = brothers+sisters

#4 
print('I have',len(siblings),'siblings')

#5 
parents = ('Jesus','Pao')
family_members = siblings + parents
print(family_members)

#level 2 

#1 
brothers = family_members[:5]
parents = family_members[-2:]
print(brothers, parents)

#2
fruits = ('apple','grape','cherry')
vegetables = ('onion','carrot','potato')
animal_products = ('milk','cheese','beef')
food_stuff_tp = fruits+vegetables+animal_products

#3
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

#4
middle = len(food_stuff_lt)//2
print(food_stuff_lt[middle])

#5
print(f'{food_stuff_lt[0]}, {food_stuff_lt[1]}, {food_stuff_lt[3]}')

#6 
del food_stuff_tp

#7
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Is Estonia a nordic country?','Estonia' in nordic_countries)
print('Is Iceland a nordic country?','Iceland' in nordic_countries)