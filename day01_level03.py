
#Exercises Day 1: Level 3
print('\nLevel 3 Exercises:\n')
#1.
print('Ejemplos de tipos de datos:\n')
print(type(10))              #Integer
print(type(9.8))             #Float
print(type(3j))              #Complex
print(type('Hola'))          #String
print(type(True))            #Boolean
print(type(['si', 'no']))    #List
print(type((1, 2 ,3)))       #Tuple
print(type({1, 2 ,3}))       #Set
print(type({'name':'Memo'})) #Dictionary

#2.

#Euclidian distance 
print('\nDistancia Eclidiana:\n')
p1= (2,3)
p2= (10,8)

suma_cuadrados= ((p2[0] - p1[0]) ** 2) + ((p2[1] - p1[1]) ** 2)

distancia = (suma_cuadrados) ** 0.5

print('La distancia euclidiana de los puntos',p1, 'y',p2, 'es:',round(distancia,2))