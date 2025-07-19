#Level 1


x = 0
print('\nIterating from 0 to 10 using for loop:')
for i in range(11):
    print(i)

print('\nIterating from 0 to 10 using while loop:')
while x <= 10: 
    print(x)
    x += 1

# 2
x = 10
print('\nIterating from 10 to 0 using for loop:')
for i in range(10, -1, -1): 
    print(i)

print('\nIterating from 10 to 0 using while loop:')
while x >= 0:  
    print(x)
    x -= 1

# 3
x = 1
print()
while x <= 7: 
    print(x*'#')
    x += 1

# 4
x = 0
print()
while x < 8:
    print('# ' * 8)
    x+= 1

x = 0
print()
while x < 8:
    y = 0
    while y < 8:
        print('#', end=' ')
        y+= 1
    print() 
    x+= 1

# 5

x = 0
y = 0
print()
while x <=10:                  
    print(f'{x} x {y} = {x*y}')
    x += 1
    y += 1

# 6

lista = ['Python', 'Numpy','Pandas','Django', 'Flask']  
print()
for element in lista:  
    print(element)     

# 7

x = 0
print()
while x <= 100:      
    if x % 2 == 0:    
        print(x)       
    x += 1

# 8

x = 0
print()
while x <= 100:         
    if x % 2 != 0:      
        print(x)
    x += 1

# Nivel 2

# 1. Suma de todos los números del 0 al 100
suma = 0
for i in range(101):
    suma += i
print(f"La suma de todos los números es {suma}.")

# 2. Suma de pares e impares del 0 al 100
suma_pares = 0
suma_impares = 0
for i in range(101):
    if i % 2 == 0:
        suma_pares += i
    else:
        suma_impares += i
print(f"La suma de los pares es {suma_pares}. Y la suma de los impares es {suma_impares}.")


countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
];

# Nivel 3

# 1. Extraer países que contienen 'land'
paises_land = []
for pais in countries:
    if 'land' in pais:
        paises_land.append(pais)
print("Países que contienen 'land':", paises_land)

# 2. Extraer países con exactamente seis letras
paises_seis_letras = []
for pais in countries:
    if len(pais) == 6:
        paises_seis_letras.append(pais)
print("Países con exactamente 6 letras:", paises_seis_letras)

# 3. Extraer países que empiezan con 'E'
paises_E = []
for pais in countries:
    if pais.startswith('E'):
        paises_E.append(pais)
print("Países que empiezan con 'E':", paises_E)

# 4. Extraer países que terminan con 'ia'
paises_ia = []
for pais in countries:
    if pais.endswith('ia'):
        paises_ia.append(pais)
print("Países que terminan con 'ia':", paises_ia)

# 5. Extraer países con la palabra 'island'
paises_island = []
for pais in countries:
    if 'island' in pais.lower():
        paises_island.append(pais)
print("Países que contienen 'island':", paises_island)

# 6. Invertir la lista de países usando un loop
paises_invertidos = []
for i in range(len(countries)-1, -1, -1):
    paises_invertidos.append(countries[i])
print("Lista de países invertida:", paises_invertidos)