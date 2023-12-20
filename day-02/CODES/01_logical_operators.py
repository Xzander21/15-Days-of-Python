# PART 1: LOGICAL OPERATORS

# Fields for examples of logical operators.
numOne = 10
numTwo = 5
conditionOne = True
conditionTwo = False


# 'and' Operator : The 'and' operator returns 'True' if both the left and right conditions are true; otherwise, it return 'False'.
# 'and' operator in Python is equivalent to the '&&' operator in C language.
# Syntax: conditionOne and conditionTwo

integerResult = numOne > 9 and numTwo < 6 # = TRUE
booleanResult = conditionOne and conditionTwo # = FALSE


# 'or' Operator : The 'or' operator returns 'True' if at least one of the left or right conditions is true; otherwise, it return 'False'.
# 'or' operator in Python is equivalent to the '||' operator in C language.
# Syntax: conditionOne or conditionTwo

integerResult = numOne > 9 or numTwo < 4 # = TRUE
booleanResult = conditionOne or conditionTwo # = TRUE


# 'not' Operator : The 'not' operator is a unary operator that returns the opposite of the boolean value of the condition.
# 'not' operator in Python is equivalent to the '!' operator in C language.
# Syntax: not condition or not (conditionOne and/or conditionTwo)

integerResult = not (numOne > 9 or numTwo < 4) # = FALSE
booleanResult = not (conditionOne or conditionTwo) # = FALSE

