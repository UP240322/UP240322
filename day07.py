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
it_companies.update(['Nvidia','Tesla'])
 
it_companies.remove('Facebook')

print(it_companies)

print("la diferencia de discard y remove es que si no existe el objeto, discard no saldrá con error")

#------------ Level 2 ------------
#Join A and B
print(A.union(B),'\n')

#Find A intersection B
print("A intersection B:",A.intersection(B),'\n')

#Is A subset of B
print('Is A subset of B:', A.issubset(B),'\n')

#Are A and B disjoint sets
print('Is A and B disjoint:', A.isdisjoint(B),'\n')

#Join A with B and B with A
print('Join A with B',A.union(B),'\n')
print('Join B with A',B.union(A),'\n')

#What is the symmetric difference between A and B
print('Symetric difference:',B.symmetric_difference(A),'\n')

#Delete the sets completely
del A,B

#------------ Level 3 ------------ 
#Convert the ages to a set and compare the length of the list and the set, which one is bigger?
print('Is the set bigger than the list?', len(set(age))  > len(age))

#Explain the difference between the following data types: string, list, tuple and set
print('Strings are sequences of caracters')
print('Lists are ordered, mutable and can be duplicated')
print('Tuples are ordered, inmutable and can be duplicated')
print('Sets are unordered, unique elements with no duplications')

#I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
