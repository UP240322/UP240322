#Level 1


x = 0
print('\nIterating from 0 to 10 using for loop:')
for i in range(11): #se genera un rango desde 0 hasta 10 (se pone 11 pero no se incluye el 11 en el rango)
    print(i)

print('\nIterating from 0 to 10 using while loop:')
while x <= 10:  #mientras que x sea menor o igual a 10 se imprime x y se suma 1
    print(x)
    x += 1

# 2
x = 10
print('\nIterating from 10 to 0 using for loop:')
for i in range(10, -1, -1): #la variable i toma el valor de 10, luego se va restando 1 (con el -1) hasta llegar a 0 (se utiliza -1 pero no se incluye en el rango)
    print(i)

print('\nIterating from 10 to 0 using while loop:')
while x >= 0:   #mientras que x sea mayor o igual a 0 se imprime x y se resta 1
    print(x)
    x -= 1

# 3
x = 1
print()
while x <= 7:  #mientras que x sea menor o igual a 7 se imprime x veces el caracter '#'
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
