import math

# Nivel 1

#1
def add_two_numbers(a, b):
    return a + b

#2
def area_of_circle(r):
    return math.pi * r * r

#3
def add_all_nums(*args):
    if not all(isinstance(x, (int, float)) for x in args):
        return 'Todos los elementos deben ser números'
    return sum(args)

#4
def convert_celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

#5
def check_season(month):
    month = month.lower()
    if month in ['diciembre', 'enero', 'febrero']:
        return 'Invierno'
    elif month in ['marzo', 'abril', 'mayo']:
        return 'Primavera'
    elif month in ['junio', 'julio', 'agosto']:
        return 'Verano'
    elif month in ['septiembre', 'octubre', 'noviembre']:
        return 'Otoño'
    else:
        return 'Mes inválido'

#6
def calculate_slope(x1, y1, x2, y2):
    if x2 == x1:
        return 'Pendiente indefinida'
    return (y2 - y1) / (x2 - x1)

#7
def solve_quadratic_eqn(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return 'No hay soluciones reales'
    x1 = (-b + math.sqrt(discriminant)) / (2*a)
    x2 = (-b - math.sqrt(discriminant)) / (2*a)
    return (x1, x2)

#8
def print_list(lst):
    for item in lst:
        print(item)

#9
def reverse_list(lst):
    reversed_lst = []
    for i in range(len(lst)-1, -1, -1):
        reversed_lst.append(lst[i])
    return reversed_lst

#10
def capitalize_list_items(lst):
    return [str(item).capitalize() for item in lst]

#11
def add_item(lst, item):
    return lst + [item]

#12
def remove_item(lst, item):
    return [x for x in lst if x != item]

#13
def sum_of_numbers(n):
    return sum(range(n+1))

#14
def sum_of_odds(n):
    return sum(i for i in range(n+1) if i % 2 != 0)

#15
def sum_of_even(n):
    return sum(i for i in range(n+1) if i % 2 == 0)


# Nivel 2

def evens_and_odds(n):
    evens = sum(1 for i in range(n+1) if i % 2 == 0)
    odds = n + 1 - evens
    print(f'El número de impares es {odds}.')
    print(f'El número de pares es {evens}.')

def factorial(n):
    if n < 0:
        return 'No existe factorial para negativos'
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def is_empty(param):
    return not bool(param)

def calculate_mean(lst):
    return sum(lst) / len(lst) if lst else None

def calculate_median(lst):
    n = len(lst)
    if n == 0:
        return None
    lst_sorted = sorted(lst)
    mid = n // 2
    if n % 2 == 0:
        return (lst_sorted[mid-1] + lst_sorted[mid]) / 2
    else:
        return lst_sorted[mid]

def calculate_mode(lst):

    if not lst:
        return None
    counts = {}
    for x in lst:
        counts[x] = counts.get(x, 0) + 1
    max_count = max(counts.values())
    return [k for k, v in counts.items() if v == max_count]

def calculate_range(lst):
    return max(lst) - min(lst) if lst else None

def calculate_variance(lst):
    mean = calculate_mean(lst)
    return sum((x - mean) ** 2 for x in lst) / len(lst) if lst else None

def calculate_std(lst):
    return math.sqrt(calculate_variance(lst)) if lst else None



# Nivel 3

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def all_unique(lst):
    return len(lst) == len(set(lst))

def all_same_type(lst):
    return all(type(x) == type(lst[0]) for x in lst)

def is_valid_variable(var):
    import keyword
    return var.isidentifier() and not keyword.iskeyword(var)



def most_spoken_languages(data, top=10):
    language_counts = {}
    for country in data:
        for lang in country['languages']:
            language_counts[lang] = language_counts.get(lang, 0) + 1
    def sort_by_count(item):
        return item[1]
    sorted_langs = sorted(language_counts.items(), key=sort_by_count, reverse=True)
    return sorted_langs[:top]

def most_populated_countries(data, top=10):
    def sort_by_population(country):
        return country['population']
    sorted_countries = sorted(data, key=sort_by_population, reverse=True)
    return sorted_countries[:top]