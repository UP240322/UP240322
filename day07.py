# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))

it_companies.add('Twitter')

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