# STRING FUNCTIONS

# Fields for examples of string functions.
string_one = "Hello"
string_two = "AWS Cloud Club"


# String Length - The 'len()' function calculates the length of a string, providing the number of characters in the given string.

length_one = len(string_one) # 5
length_two = len(string_two) # 14


# String Slicing - Slicing is a technique to extract a portion of a string. Python uses square brackets to specify the start and end indices.

sliced_string = string_one[1:4]  # Extracts characters from index 1 to 3 - "ell"

# String Cases - The 'upper()' method converts all characters in a string to uppercase, while 'lower()' converts them to lowercase.

uppercase_string = string_one.upper() # "HELLO"
lowercase_string = string_two.lower() # "aws cloud club"


# String Replacement - The 'replace()' method substitutes occurrences of a specified substring with another substring in a given string.

replaced_string = string_one.replace('o', 'u') # Hellu


# String Splitting - The 'split()' method divides a string into a list of substrings based on a specified delimiter.

split_string = "DCC,DSEC,DSWD".split(',') # ['DCC', 'DSEC', 'DSWD']


# String Stripping - The 'strip()' method removes leading and trailing whitespace (including newline characters) from a string. The 'lstrip()' and 'rstrip()' methods removes specified set of characters, from a string. 

whitespace_string = "   Hello   ".strip() # "Hello"
left_stripped = "   Hello   ".lstrip() # "Hello   "
right_stripped = "   Hello   ".rstrip() # "   Hello"


# String Count - The 'count()' method tallies the occurrences of a specific substring within a string.

occurences_count =  string_two.count("Cl") # 2


# String Searching - The 'find()' and 'index()' methods locate the index of the first occurrence of a substring within a string.

find_result = string_one.find('e') # 1
index_result = string_one.index('e') # 1


# String Checking - The 'startswith()' method checks if a string starts with a specified prefix, while 'endswith()' checks if it ends with a specified suffix.

starts_with_he = string_one.startswith("He") # True
ends_with_club = string_two.endswith("Club") # True


# Character Membership - The 'in' and 'not in' operators check if a substring is present or absent in a given string.

contains_n = 'n' in string_one # False
not_contains_x = 'x' not in string_two # True


# Character Case Conversion - The 'capitalize()' method capitalizes the first character of a string, and 'title()' capitalizes the first character of each word.

capitalized_string = lowercase_string.capitalize() # Aws cloud club
titlecased_string = lowercase_string.title() # Aws Cloud Club


# String Repetition - The '*' operator repeats a string by a specified number of times.

repeated_string = string_one * 3 # HelloHelloHello


# String Case Swapping - The 'swapcase()' method swaps the case of each character in a string.

swapped_case = string_two.swapcase() # aws cLOUD cLUB


# String Reversal - To reverse a string, you can use slicing with a step of -1. [::-1].

reversed_string = string_two[::-1] # bulC duolC SWA


# String Case Testing - These methods check if a string is in lowercase, uppercase, or titlecase.

is_lower = string_one.islower() # False
is_upper = string_two.isupper() # False
is_title = string_one.istitle() # True


# Numeric String Checking - The 'isdigit()' method checks if all characters in a string are digits.

numeric_string = "12345"
is_numeric = numeric_string.isdigit() # True