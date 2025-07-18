#1
dog = {}

#2
dog = {'name': 'Coffee', 'color': 'brown', 'breed': 'Cocker', 'legs': 4, 'age': 8}
print(f'Dog = {dog}')

#3
student = {'first_name': 'Guilermo', 'last_name': 'Rdz', 'gender': 'M', 'age': 19, 'marital_status': 'single', 'skills': 'guitarrist', 'country': 'Mexico', 'city': 'Aguascalientes', 'address': 'calle 1234'}
print(f'\nstudent = {student}')

#4
print(f'\nlength of student dictionary = {len(student)}')

#5
print(f'\nskills = {student['skills']}')

#6
student['skills'] = ['guitarrist','NodeJs']
print(f'\nModified skills = {student['skills']}')

#7
print(f'\nKeys of student dictionary = {list(student.keys())}')

#8
print(f'\nValues of student dictionary = {list(student.values())}')

#9
student_items = list(student.items())
print(f'\nStudent items as list of tuples = {student_items}')

#10
del student['marital_status']
print(f'\nStudent dictionary after deletion = {student}')

#11
del dog
print('\nDog deleted.')