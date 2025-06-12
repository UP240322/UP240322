age = 19
heigth = 1.87
complex_number = complex

#4. Area of triangle
base_triangle = float(input('introduce la base: '))
heigth_triangle = float(input('introduce la altura: '))

a_triangle = base_triangle * heigth_triangle * 0.5

print('El área de un triángulo con base de',base_triangle,'y altura de',heigth_triangle,'es',a_triangle)

#5. Perimeter of triangle
sidea_triangle = float(input('introduce el lado a del triángulo: '))
sideb_triangle = float(input('introduce el lado b del triángulo: '))
sidec_triangle = float(input('introduce eñ lado c del triángulo: '))

perimeter_triangle = sidea_triangle + sideb_triangle +sidec_triangle

print('El perímetro de un triangulo cuyos lados miden',sidea_triangle,sideb_triangle,sidec_triangle,'es',perimeter_triangle)

#6. Area and perimeter of a rectangle 
base_rectangle = 20
heigth_rectangle = 10

a_rectangle = base_rectangle * heigth_rectangle 
p_rectangle = a_rectangle * 2

print('El área de un rectángulo con base de',base_rectangle,'y altura de',heigth_rectangle,'es',a_rectangle,'y su perímetro es de',p_rectangle)

#7. Area and circumference of a circle
pi = 3.14
radius = float(input('introduce el radio: '))

a_circle = pi * radius * radius 
circum = 2 * pi * radius

print('El área del círculo es de',a_circle,'y su circunferencia es de',circum, 'cuando tiene un radio de',radius)

#8. Slope and Euclidian distance

x1 = int(input('introduce el valor de x para el punto 1: '))
y1 = 2 * x1 -2
x2 = int(input('introduce el valor de x para el punto 2: '))
y2 = 2 * x2 -2

#9.Formulas 
slope = (y2 - y1) / (x2 - x1)

p1= (2,2)
p2= (6,10)

sum= ((p2[0] - p1[0]) ** 2) + ((p2[1] - p1[1]) ** 2)

dist = (sum) ** 0.5

#10. Comparison 
print('La pendiente es de',slope, 'y la distancia euclidiana es de',round(dist,2))

#11. Value of func
x_11 = int(input('introduce el valor de x'))
func = (x_11 * x_11) + (6 * x_11) + 9

x_11_ex = 0
func_ex = (x_11 * x_11) + (6 * x_11) + 9

print('El valor de la función "y = x^2 + 6x + 9" cuando x vale',x_11,'es de',func,'y cuando vale',x_11_ex,'es de',func_ex)

#12. Falsely comparison
py = 'python'
dr = 'dragon'

print('python length no es la misma que dragon length:',len(py) is not len(dr))

#13. And operator
print('"on" en python', 'on' in 'python')
print('"on" en jargon', 'on' in 'jargon')
#14. In operator
sentence = '"I hope this course is not full of jargon"'
print('¿Hay "jargon" en el sig. enunciado?',sentence, 'jargon' in sentence)

#15. no "on" 
print('No hay "on" en python.',not 'on' in 'python')
print('No hay "on" en jargon.',not 'on' in 'jargon')

#16. Length of Python to string
length = len(py)         
float_v = float(length) 
r = str(float_v)   

print('En la palabra',py,'hay',r,'letras')

#17. Even numbers 
num = 11

if num % 2 == 0:
    print(num,'es par')
else:
    print(num,'es impar')
    
#18. Floor division

f_div = 7 // 3

str_number = '2.7'    
convert_number = float(str_number)

print(f_div,'es igual a',convert_number, f_div == convert_number) 

#19. Int equal Str 
print(type('10') == type(10))

#20. Int equal Int
print(type(int(float('9.8'))) == type(10))

#21. Pay
hours = float(input("\nIngrese las horas trabajadas: "))
rate = float(input("Ingrese la tarifa por hora: "))
pay = hours * rate
print(f"Su ganancia semanal es {pay}")

#22. Years to sec
years = int(input("\nIngrese cuántos años ha vivido: "))
seconds_per_year = 365 * 24 * 60 *60
total_seconds = years * seconds_per_year
print(f"Usted ha vivido por {total_seconds} segundos.")

#23. Table
print('1 1 1 1 1')
print('2 1 2 4 8')
print('3 1 3 9 27')
print('4 1 4 16 64')
print('5 1 5 25 125')