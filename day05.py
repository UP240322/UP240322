# Day 5 

# 1

el = list()
print(el)

#puto 2

list_nums= ["1", "2", "3", "4", "5", "6"]

# 3

print(len(list_nums))

# 4

print(list_nums[0])
print(list_nums[-1])
middle = len(list_nums)//2
print(list_nums[middle])

# 5

mixed_data_types = ["patricio", 19, 1.72, "single", "Aguascalientes"]

# 6

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# 7

print(it_companies)

# 8

print(len(it_companies))

# 9

print(it_companies[0])
print(it_companies[-1])
middle = len(it_companies)//2
print(it_companies[middle])

# 10

it_companies[1] = "gogle"
print(it_companies)

# 11

it_companies.append("apple")
print(it_companies)

# 12

middle = len(it_companies)//2
it_companies.insert(middle,"intel")
print(it_companies)

# 13

it_companies[4] = it_companies[4].upper()
print(it_companies)

# 14

print("#; ".join(it_companies))

# 15

print("IBM" in it_companies)
print("Google" in it_companies)

# 16

it_companies.sort()
print(it_companies)

# 17

it_companies.reverse()
print(it_companies)

# 18

first_3 = it_companies[:3]
print(first_3)

# 19

last_3 = it_companies[-3:]
print(last_3)

# 20
middle = len(it_companies)//2
print(it_companies[middle:middle+1])

# 21

del it_companies[0]
print(it_companies)

# 22

middle = len(it_companies)//2
del it_companies [middle:middle+1]
print(it_companies)

# 23

del it_companies[-1]
print(it_companies)

# 24

del it_companies[:]
print(it_companies)

# 25

del it_companies

# 26

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
join = front_end + back_end
print(f"{front_end} + {back_end}\n= {join}")

# 27

full_stack = join
redux = full_stack.index("Redux")
position = redux+1
full_stack[position:position] = ["Python", "SQL"]
print(full_stack)