1.2

t = ("T", "h", "e", "B", "i", "g", "B", "e", "n")

#t = tuple(input())

str = "".join(str(i) for i in t)

print(str)

1.3

from itertools import groupby

 

cars_list = [('BMW', 'X6'), ('Toyota', 'Yaris'), ('Fiat', '500'), ('Fiat', 'Panda'), ('Toyota', 'Camry 30')]

 

sorted_cars = sorted(cars_list, key=lambda x: x[0])

 

for manufacturer, group in groupby(sorted_cars, key=lambda x: x[0]):

    group_list = list(group)

    count = len(group_list)

    print(f"{manufacturer} {count}", end=" - ")

    for _, model in group_list:

        print(model)

1.4

def count_occurrences(input_tuple):

    element_count = {}

 

    for item in input_tuple:

        if isinstance(item, list):

            key = tuple(item)

        else:

            key = item

 

        if key in element_count:

            element_count[key] += 1

        else:

            element_count[key] = 1

 

    output_tuple = tuple((key, count) for key, count in element_count.items())

 

    return output_tuple

 

sample_input_1 = (55, 6, 777, 54, 6, 76, 7777, 1, 777, 6)

sample_input_2 = ('55', '6', '777', 54, 6, 7777, 9, 777, 6)

sample_input_3 = ((1, 2, 3), (['A', 'B']), (1, 2, 3), (['A']))

 

result_1 = count_occurrences(sample_input_1)

result_2 = count_occurrences(sample_input_2)

result_3 = count_occurrences(sample_input_3)

 

print("Sample Output 1:")

print("Elements and their occurrences:")

print(result_1)

 

print("\nSample Output 2:")

print("Elements and their occurrences:")

print(result_2)

 

print("\nSample Output 3:")

print("Elements and their occurrences:")

print(result_3)

1.5

 

data = (55, 6, 777, 70.0, '7', 'A')

 

result_tuples = []

 

temp_tuple = ()

 

 

for item in data:

 

    if isinstance(item, (int, str)) and len(str(item)) == 1:

 

        temp_tuple += (item,)

    else:

 

        if temp_tuple:

            result_tuples.append(temp_tuple)

            temp_tuple = ()

        if isinstance(item, (float, str)) and len(str(item)) > 1:

            result_tuples.append((item,))

 

if temp_tuple:

    result_tuples.append(temp_tuple)

 

 

for subtuple in result_tuples:

    print(subtuple)

 

1

a = input()

a = tuple(a)

print(a)

2.1

a = input()

a = set(a)

print(a)

2.2

set_A = {1, 2, 3, 4, 5}

set_B = {5, 7, 8, 9, 2, 10}

 

symmetric_difference_set = set_A ^ set_B

print(symmetric_difference_set)

2.3

set_A = {1, 2, 3, 4, 5}

set_B = {5, 7, 8, 9, 2, 10}

 

set_B -= set_A

 

print(set_B)

2.4

set_A = {1, 2, 3, 4, 7}

set_B = {8, 7, 9, 4, 2, 0, 10}

set_C = {4, 0, 1}

 

for element in set_A.copy():

    if element in set_C:

        set_A.remove(element)

        set_B.add(element)

        set_C.remove(element)

        set_C.add(element)

 

print("Updated set_A:", set_A)

print("Updated set_B:", set_B)

print("Updated set_C:", set_C)

 

2.5

from itertools import combinations

import random

 

A = {1, 2, 3, 4, 5, 6}

n = 3

m = 5

 

combinations_list = []

 

A_list = list(A)

 

while len(combinations_list) < m:

    combination = set(random.sample(A_list, n))

    if combination not in combinations_list:

        combinations_list.append(combination)

 

print(combinations_list)

3

from itertools import groupby

 

cars_list = [('BMW', 'X6'), ('Toyota', 'Yaris'), ('Fiat', '500'), ('Fiat', 'Panda'), ('Toyota', 'Camry 30')]

 

sorted_cars = sorted(cars_list, key=lambda x: x[0])

 

for manufacturer, group in groupby(sorted_cars, key=lambda x: x[0]):

    group_list = list(group)

    count = len(group_list)

    print(f"{manufacturer} {count}", end=" - ")

    for _, model in group_list:

        print(model)

 