#!/usr/bin/env python3
'''
vowels = ['a', 'e', 'i', 'o', 'i', 'u', 'a']

for v in vowels:
    # idx = vowels.index(v)
    print(f"{vowels.index(v)} {v}")

for i, v in enumerate(vowels):
    print(i,v)


x = [v for i, v in enumerate(vowels)]
print(x)

counter_list = list(enumerate(vowels))
print(counter_list)

i = 'a'
x = [item for item in counter_list if i in item]
print(x)

i = 4
v = 'i'
x = [item for item in list(enumerate(vowels)) if i in item and v in item]
print(x)

x = [(i, e) for i, e in enumerate(vowels) if e == 'i']
print(x)

dict = {1: "one", 2: "two", 3: "three", 4: "four"}
dict[5] = "five"
dict[6] = "six"
# dict.pop(1, None)
if 1 in dict: del dict[1] 
print(dict)
'''

# ################################################################################
# Write a function that returns the elements on odd positions (0 based) in a list
# ################################################################################
input = [0,1,2,3,4,5]
def solution_01(input):
    new = [val for idx, val in list(enumerate(input)) if idx % 2 != 0]
    return new

print(solution_01(input))

# ################################################################################
# Write a function that returns the cumulative sum of elements in a list
# ################################################################################
input = [1,-1,3]
def solution_02(input):
    accu = 0
    new = []
    for e in input:
        accu = accu + e
        new.append(accu)
    return new

print(solution_02(input))

# ################################################################################
# Write a function that takes a number and returns a list of its digits
# ################################################################################
input = 123
def solution_03(input):
    return [int(i) for i in str(input)]

print(solution_03(input))



# ################################################################################
py_dict = {'e': 1, 'a': 2, 'u': 3, 'o': 4, 'i': 5}
print(sorted(py_dict, reverse = True))

x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
x = {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}
print(x)

full_name = lambda first, last: f"Full name: {first.title()} {last.title()}"
print(full_name("Richard", "Senar"))




# ################################################################################
# Write a function that returns the first non repeating charater in a string
# ################################################################################
input = "AAABBBCCCCDDDEEEFFFFFGGHHL"
def solution_04(input):
    elem = {}
    for i in input:
        elem[i] = elem.get(i, 0) + 1
    for i in input:
        if elem.get(i) == 1:
            return i
    return -1

print(solution_04(input))


# ################################################################################
# Write a function that returns the first non repeating charater in a string
# ################################################################################
# input = [7,-8,9,2,3,-4,5,6,1]
# def solution_05(input):
#     if len(input) <= 0:
#         return None    
#     new = [pow(x, 2) for x in input]
#     new.sort()
#     return new

# print(solution_05(input))


input = [-9,-8,-5,1,2,3,4,5,6]
def solution_06(input):
    idx = 0
    if len(input) == 0:
        return []
    new = [None] * len(input)
    input_len = len(input) -1
    for i in range(input_len,-1,-1):
        if i - idx == 0:
            break
        if pow(input[i], 2) > pow(input[idx], 2):
            new[i] = pow(input[i], 2)
        else:
            new[i] = pow(input[idx], 2)
            idx = idx + 1
    return new

print(solution_06(input))


