# PART 2: IF-ELIF-ELSE STATEMENT

# Fields for examples of if-elif-else statement.

conditionOne = True
conditionTwo = False


# 'if' Statement - Allows conditional execution of a code block based on a specified condition.
# Syntax : if condition:
#             code to be executed if the condition is True

if conditionOne and conditionTwo:
    print("Both conditions are true.")


# 'else Statement - Allows for the execution of one block of code if a specified condition is true, and another block if the condition is false.
# Syntax: if condition:
#            code to be executed if the condition is True
#         else:
#            code to be executed if the condition is False

if conditionOne and conditionTwo:
    print("Both conditions are true.")
else:
    print("At least one condition is false.")


# 'elif' (else if) Statement - Allows the execution of different blocks of code based on the evaluation of multiple conditions.
# Syntax: if condition:
#            code to be executed if the condition is True
#         elif conditionTwo:
#            code to be executed  if conditionTwo is True
#         else:
#            code to be executed if none of the conditions are True

if conditionOne and conditionTwo:
    print("Both conditions are true.")
elif conditionOne or conditionTwo:
    print("At least one condition is true")
else:
    print("All of the conditions are false.")


# Nested Conditional Statemment - Involves placing 'if, elif or else' statements within another, allowing for conditional execution of code blocks based on multiple levels of conditions.
# Syntax: if conditionOne:
#            if conditionTwo:
#               code to be executed if both condition1 and condition2 are True

if conditionOne:
    if conditionTwo:
        print("Both conditions are true.")
    else:
        print("Only first condition is true.")
else:
    print("Terminated.")


# Ternary Operator - It is a powerful tool for writing concise and readale code when dealing with simple conditional expressions.
# Syntax: value_if_true if condition else value_if_false

print("The condition is " + "true" if conditionOne else "false")