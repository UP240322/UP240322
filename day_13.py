# Nivel 1


numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filtered_numbers = [x for x in numbers if x <= 0]  
print(filtered_numbers) 

list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened_output = [item for sublist in list_of_lists for item in sublist[0]]
print(flattened_output)  

tuples_list = [(i, 1, i**1, i**2, i**3, i**4, i**5) for i in range(11)]
print(tuples_list)
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flattened_countries = [
    [country.upper(), country[:3].upper(), city.upper()]
    for country_list in countries
    for (country, city) in country_list
]
print(flattened_countries)
countries_dicts = [
    {'country': country.upper(), 'city': city.upper()}
    for country_list in countries
    for (country, city) in country_list
]
print(countries_dicts)
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
full_names = [
    f'{first} {last}'
    for name_list in names
    for (first, last) in name_list
]
print(full_names)
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)  
y_intercept = lambda x1, y1, m: y1 - m * x1         


m = slope(1, 2, 3, 6)  
b = y_intercept(1, 2, m)  
print(f'Pendiente: {m}, Ordenada al origen: {b}')