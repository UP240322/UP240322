#Level 1

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(f'It companies: {it_companies}')

#1
print(len(it_companies))

#2 
it_companies.add('Twitter')
print(it_companies)

#3 
it_companies.update(['Tesla','Nvidia','Intel'])
print(it_companies)

#4 
it_companies.remove('Tesla')
print(it_companies)

#5
print('remove() is "strict" and raises an error if the element is missing, while discard() is "lenient" and silently ignores the request if the element is not found. The choice between them depends on whether you need to handle the case of a missing element as an error or simply ignore it.')

#Level 2 

#1 
print(f'A: {A}')
print(f'B: {B}')

#2 
print(A.intersection(B))

#3
print(A.issubset(B))

#4
print(A.isdisjoint(B))

#5 
A.update(B)
B.update(A)

print(f'A: {A}')
print(f'B: {B}')

#6
print(A.symmetric_difference(B))

#7
del A
del B


#3 

#1
st_ages = set(age)
print(len(age))
print(len(st_ages))

#2
print("A **string** is an immutable sequence of characters. Example: 'hello' — you can't change its characters directly.")
print("A **list** is a mutable, ordered collection of items. Example: [1, 2, 3] — you can change, add, or remove items.")
print("A **tuple** is like a list but immutable (cannot be changed after creation). Example: (1, 2, 3) — fixed content.")
print("A **set** is an unordered collection of unique items. Example: {1, 2, 2, 3} becomes {1, 2, 3} — no duplicates allowed.")


#3 
oracion = 'I am a teacher and I love to inspire and teach people'
words = oracion.split()
unique_words = set(words)
print(unique_words)
print(len(unique_words))