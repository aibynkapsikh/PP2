# Logical Operators

# Logical operators are used to combine conditional statements:
x = 2
y = 2
# Operator: and
# Description: Returns True if both statements are true
print(x < 5 and  x < 10)

# Operator : or
# Description : Returns True if one of the statements is true
print(x < 5 or x < 4)

# Opearator : not
# Description : Reverse the result, returns False if the result is true
print(not(x < 5 and x < 10))


# Identity Operators

# Operator : is
# Description : Returns True if both variables are the same object 
print(x is y)

# Operator : is not
# Description : Returns True if both variables are not the same object
print(x is not y)

# Membership Operators

# Operator : in 
# Description : Returns True if a sequence with the specified value is present in the object

k = ["banana", "apple"]
print("apple" in k)

# Operator : not in 
# Description : Returns True if a sequence with the specified value is not present in the object
print("pineapple" not in k)


#  Bitwise Operators

# Bitwise operators are used to compare (binary) numbers:

# Operator : &
# Name : AND 
# Description : Sets each bit to 1 if both bits are 1
print(6 & 3)

# Opearator : |
# Name : OR
# Description : Sets each bit to 1 if one of two bits is 1
print(6 | 3)
# Opearator : ^
# Name : XOR
# Description : Sets each bit to 1 if only one of two bits is 1
print(6 ^ 3)

# Opearator : ~
# Name : NOT
# Description : Inverts all the bits 
print(~5)

# Opearator : <<
# Name : Zero fill left shift
# Description : Shift left by pushing zeros in from the right and let the leftmost bits fall off
print(x << 2)
# Opearator : >> 
# Name : Signed right shift	
# Description : Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
print( x >> 2)


