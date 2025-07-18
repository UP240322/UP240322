#Level 1 

#1 
age = int(input('Enter your age: '))

if age >= 18:
    print('You are old enough to learn to drive.')
else:
    age_needed = 18 - age
    print(f'You need {age_needed} more years to learn to drive.')

#2
my_age = 25                                 
your_age = int(input('Enter your age: '))

if your_age > my_age:
    age_difference = your_age - my_age
    year_text = 'year' if age_difference == 1 else 'years'
    print(f'You are {age_difference} {year_text} older than me.')
elif your_age == my_age:
    print('We are the same age.')
else:
    age_difference = my_age - your_age
    year_text = 'year' if age_difference == 1 else 'years'
    print(f'I am {age_difference} {year_text} older than you.')

#3
a = int(input('Enter number one: '))
b = int(input('Enter number two: '))

if a > b:
    print(f'{a} is greater than {b}')
elif a < b:
    print(f'{a} is smaller than {b}')
else:
    print(f'{a} is equal to {b}')
    
    
#Level 2

#1
score = int(input('Enter your score: '))

if 80 <= score <= 100:      
    print('Grade: A')  
elif 70 <= score < 80:
    print('Grade: B')
elif 60 <= score < 70:
    print('Grade: C')
elif 50 <= score < 60:
    print('Grade: D')
elif 0 <= score < 50:
    print('Grade: F')

#2 
month = input('Enter the name of a month: ')

if month in ['September', 'October', 'November']:   
    print('The season is Autumn.')
elif month in ['December', 'January', 'February']:  
    print('The season is Winter.')
elif month in ['March', 'April', 'May']:
    print('The season is Spring.')
elif month in ['June', 'July', 'August']:
    print('The season is Summer.')
else:
    print('That is not a valid month.')  

#3 
fruits = ['banana', 'orange', 'mango', 'lemon']

fruit = input('Enter a fruit: ')

if fruit not in fruits:
    print(fruit, 'is not in the list')      
    print('Adding fruit to the list')       
    fruits.append(fruit)                   
    print('Modified list:', fruits)         
else:
    print('That fruit already exist in the list')
    
    
#Level 3
person={
        'first_name': 'Guillermo',
        'last_name': 'Rdz',
        'age': 19,
        'country': 'Mexico',
        'is_marred': False,
        'skills': ['Js', 'Angular', 'NodeJS', 'MongoDB', 'Python'],
        'address': {
            'street': 'Calle',
            'zipcode': '00000'
        }
    }
print('Skills of person:')
if 'skills' in person:
    skills = person['skills']
    if len(skills) > 0:
        middle_skills = skills[len(skills) // 2]
        print('Middle skills are:', middle_skills)

    if 'Python' in skills:
        print('The person has Python skill')

    if ('JavaScript' in skills and 'React' in skills) and len(skills) == 2:
        print('He is a front end developer')
    elif ('Node' in skills and 'Python' in skills and 'MongoDB') and len(skills) == 3:
        print('He is a backend developer')
    elif ('Node' in skills and 'React' in skills and 'MongoDB') and len(skills) == 3:
        print('He is a fullstack developer')
    else:
        print('unknown title')
    
    if person['is_marred'] and person['country'] == 'Finland':
        print(f'{person[str,'first_name']} {person[str,'last_name']} lives in {person[str,'country']}. He is married.')