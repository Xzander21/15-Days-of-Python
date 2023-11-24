# PART 3: WRITING OUTPUT IN DIFFERENT TYPES OF STRING CONCATENATION

# Fields for Alf's Introduction
name = "Alf"
organization = "AWS Cloud Club"
university = "PUP Manila"

# Method 1: Concatenating strings inside 'print()' function : THE VALUES ARE AUTOMATICALLY SEPARATED BY A SPACE
print("Hi, I am", name, "૮₍ ˶ᵔ ᵕ ᵔ˶ ₎ა and I am the official mascot of", organization, "of", university, "and ready to guide you from the clouds and beyond!")


# Method 2: Using the '+' Operator
alf_introduction = "Hi, I am " + name + " ૮₍ ˶ᵔ ᵕ ᵔ˶ ₎ა and I am the official mascot of " + organization + " of " + university + " and ready to guide you from the clouds and beyond!"
print(alf_introduction)

print("Hi, I am " + name + " ૮₍ ˶ᵔ ᵕ ᵔ˶ ₎ა and I am the official mascot of " + organization + " of " + university + " and ready to guide you from the clouds and beyond!")


# Method 3: Using the 'format()' method
alf_introduction = "Hi, I am {} ૮₍ ˶ᵔ ᵕ ᵔ˶ ₎ა and I am the official mascot of {} of {} and ready to guide you from the clouds and beyond!".format(name, organization, university)
print(alf_introduction)

print("Hi, I am {} ૮₍ ˶ᵔ ᵕ ᵔ˶ ₎ა and I am the official mascot of {} of {} and ready to guide you from the clouds and beyond!".format(name, organization, university))


# Method 4: Using F-strings (Python 3.6 and above) : MOST COMMON
alf_introduction = f"Hi, I am {name} ૮₍ ˶ᵔ ᵕ ᵔ˶ ₎ა and I am the official mascot of {organization} of {university} and ready to guide you from the clouds and beyond!"
print(alf_introduction)

print(f"Hi, I am {name} ૮₍ ˶ᵔ ᵕ ᵔ˶ ₎ა and I am the official mascot of {organization} of {university} and ready to guide you from the clouds and beyond!")


# Method 5: Using the 'join()' method
alf_introductionList = ["Hi, I am ", name, " ૮₍ ˶ᵔ ᵕ ᵔ˶ ₎ა and I am the official mascot of ", organization, " of ", university, " and ready to guide you from the clouds and beyond!"]

alf_introduction = "".join(alf_introductionList)
print(alf_introduction)

print("".join(["Hi, I am ", name, " ૮₍ ˶ᵔ ᵕ ᵔ˶ ₎ა and I am the official mascot of ", organization, " of ", university, " and ready to guide you from the clouds and beyond!"]))


# Method 6: Using the '%' Formatting : SIMILAR IN C LANGUAGE FORMATTING
alf_introduction = "Hi, I am %s ૮₍ ˶ᵔ ᵕ ᵔ˶ ₎ა and I am the official mascot of %s of %s and ready to guide you from the clouds and beyond!" % (name, organization, university)
print(alf_introduction)

print("Hi, I am %s ૮₍ ˶ᵔ ᵕ ᵔ˶ ₎ა and I am the official mascot of %s of %s and ready to guide you from the clouds and beyond!" % (name, organization, university))
