# ITERATIVE STATEMENTS

# Fields for examples of iterative statements.
departments = ["DCC", "DSWD", "DSEC"]
names = ['Alf', 'Alfina',]
ages = [0.5, 0.25]


# For Loops - Iterates over a sequence, executing a block of code for each element, enhancing readability and supporting advanced iteration features.
# Syntax : for variable in sequence:
#              code to be executed for each element in the sequence
 
for department in departments:
    print(department)


# For Loops with Indices - Iterats through a sequence, effortlessly providing both elements and their respectice indices in each iteration.
# Syntax: for index, value in enumerate(sequence):
#             code to be executed for each element in the sequence
    
for index, department in enumerate(departments):
    # Your code here, using 'index' and 'value'
    print(f"INDEX: {index}, DEPARTMENT {index + 1}: {department}")


# While Loops - Continuously executes a block of code as long as a specified condition remains true, offering a flexible way to repeat tasks until a certain criterion is met.
# Syntax : while condition:
#              code to be executed as long as the condition is True

index = 0
while index < len(departments):
    print(departments[index])
    index += 1


# Improvised Do-While Loops - An improvised do-while loop is created by employing a "while" loop with a conditional break, ensuring the loop executes at least once before checking the exit condition.
# Syntax: while True:
#             code to be executed at least once
#             if exit_condition:
#                 break
    
while (True):
    # Code to be executed in the loop
    print("Alf is strong!")

    # Check the condition for breaking out of the loop
    user_input = input("Do you want to continue? (yes/no): ")
    if user_input.lower() != 'yes':
        break


# Using 'range()' Function - It generates numerical sequences for efficient iteration in loops, offering a compact way to define ranges without storing them explicitly in memory.
# Syntax: for variable in range(start, stop, step):
#             code to be executed for each element in the range
   
for i in range(2, 10, 2):
    print(i)


# Break Statement in Loops - It swiftly exits loops, providing a mechanism to prematurely end iterative processes based on specific conditions.
# Syntax: for variable in sequence:
#              code to be executed for each element in the sequence
#              if condition:
#                  break  - exit the loop if the condition is met
    
for num in range(10):
    if num == 5:
        break
    print(num)


# Continue Statement in Loops - It skips the rest of the code in the current loop iteration, facilitating the selective execution of iterations based on specified conditions.
# Syntax: for variable in sequence:
#              code to be executed for each element in the sequence
#              if condition:
#                  continue  - skip the rest of the code in the current iteration

for num in range(10):
    if num == 5:
        continue
    print(num)


# Nested Loops - It involve placing one loop inside another, enabling the iteration through multiple levels of data structures for handling intricate patterns and multidimensional arrays.
# Syntax: for outer_variable in outer_sequence:
#             for inner_variable in inner_sequence:
#                 code to be executed for each element in the inner sequence
#             Additional code for each element in the outer sequence

for i in range(3):
    for j in range(2):
        print(f'({i}, {j})')


# Iterating Over Multiple Lists Using 'zip()' - It efficiently pairs corresponding elements from multiple lists, allowing for simultaneous iteration and streamlined processing in loops.
# Syntax: for variable1, variable2, ... in zip(list1, list2, ...):
#              code to be executed for each corresponding element in the lists

for name, age in zip(names, ages):
    print(f'{name} is {age} year/s old')








