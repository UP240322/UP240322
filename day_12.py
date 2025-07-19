import random
import string

# Nivel 1


def random_user_id():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

def user_id_gen_by_user():
    num_chars = int(input('Número de caracteres por ID: '))
    num_ids = int(input('Cantidad de IDs a generar: '))
    ids = []
    for i in range(num_ids):
        ids.append(''.join(random.choices(string.ascii_letters + string.digits, k=num_chars)))
    for uid in ids:
        print(uid)
    return '' 

def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f'rgb({r},{g},{b})'

# Nivel 2


def list_of_hexa_colors(n):
    colors = []
    for i in range(n):
        color = '#' + ''.join(random.choices('0123456789abcdef', k=6))
        colors.append(color)
    return colors

def list_of_rgb_colors(n):
    colors = []
    for i in range(n):
        colors.append(rgb_color_gen())
    return colors

def generate_colors(tipo, cantidad):
    if tipo == 'hexa':
        return list_of_hexa_colors(cantidad)
    elif tipo == 'rgb':
        return list_of_rgb_colors(cantidad)
    else:
        return []
    
    
# Nivel 3


def shuffle_list(lst):
    copia = lst[:]
    random.shuffle(copia)
    return copia

def unique_random_numbers():
    return random.sample(range(10), 7)