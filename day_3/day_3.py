age = 19
heigth = 1.87
complex_number = complex

#4. Area of triangle
base_triangle = 20
heigth_triangle = 10

a_triangle = base_triangle * heigth_triangle * 0.5

print('El área de un triángulo con base de',base_triangle,'y altura de',heigth_triangle,'es',a_triangle)

#5. Perimeter of triangle
sidea_triangle = 5
sideb_triangle = 4
sidec_triangle = 3

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
radius = 3

a_circle = pi * radius * radius 
circum = 2 * pi * radius

print('El área del círculo es de',a_circle,'y su circunferencia es de',circum, 'cuando tiene un radio de',radius)

#8. Slope and Euclidian distance

x= 1
func = 2 * x -2

p1= (2,2)
p2= (6,10)

sum= ((p2[0] - p1[0]) ** 2) + ((p2[1] - p1[1]) ** 2)

dist = (sum) ** 0.5

print('La distancia euclidiana de los puntos',p1, 'y',p2, 'es:',round(dist,2))

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
convert_number = int(str_number)

print(f_div,'es igual a',convert_number, f_div == convert_number) 