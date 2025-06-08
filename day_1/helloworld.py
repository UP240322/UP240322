#Exercises Day 1: Level 2

#2.
print('\nOperaciones:\n')
print(3 + 4)  #Addition
print(3 - 4)  #Substraction
print(3 * 4)  #Multiplication
print(3 % 4)  #Modulus
print(3 / 4)  #Divison
print(3 ** 4) #Exponential
print(3 // 4) #Floor Division Operator

#3.
print('\nStrings:\n')
print('Your name: Guillermo')
print('Your family name: Pao, Leo y Coffee')
print('Your country :Mexico')
print('I am enjoying 30 days of python')

#4.
print('\nCheck data types:\n')
print(type(10))                                #Integer
print(type(9.8))                               #Float
print(type(3.14))                              #Float
print(type(4 - 4j))                            #Complex
print(type(['Asabeneh', 'Python', 'Finland'])) #List
print(type('Guillermo'))                       #String
print(type('Pao, Leo y Coffee'))               #String
print(type('I am enjoying 30 days of python')) #String

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