#Arithmetic operators
a = 10
b = 5

print("Addition:", a + b)        # Output: 15
print("Subtraction:", a - b)     # Output: 5    
print("Multiplication:", a * b)  # Output: 50
print("Division:", a / b)        # Output: 2.0
print("Floor Division:", a // b) # Output: 2
print("Modulus:", a % b)         # Output: 0
print("Exponentiation:", a ** b) # Output: 100000

#Comparison operators
x = 10  
y = 20
print("Equal to:", x == y)        # Output: False
print("Not equal to:", x != y)    # Output: True
print("Greater than:", x > y)     # Output: False
print("Less than:", x < y)        # Output: True
print("Greater than or equal to:", x >= y)  # Output: False
print("Less than or equal to:", x <= y)     # Output: True

#Logical operators
p = True
q = False
print("Logical AND:", p and q)  # Output: False
print("Logical OR:", p or q)    # Output: True
print("Logical NOT:", not p)    # Output: False

#Assignment operators
c = 10
print("Assignment:", c)          # Output: 10
c += 5
print("Addition Assignment:", c) # Output: 15
c -= 3
print("Subtraction Assignment:", c) # Output: 12
c *= 2
print("Multiplication Assignment:", c) # Output: 24
c /= 4
print("Division Assignment:", c) # Output: 6.0

#Bitwise operators
m = 5  # In binary: 0101
n = 3  # In binary: 0011
print("Bitwise AND:", m & n)  # Output: 1 (In binary: 0001)
print("Bitwise OR:", m | n)   # Output: 7 (In binary: 0111)
print("Bitwise XOR:", m ^ n)  # Output: 6 (In binary: 0110)
print("Bitwise NOT:", ~m)     # Output: -6 (In binary: 1010)
print("Left Shift:", m << 1)  # Output: 10 (In binary: 1010)
print("Right Shift:", m >> 1) # Output: 2 (In binary: 0010)

#Membership operators
fruits = ["apple", "banana", "cherry"]  
print("Membership in list:", "banana" in fruits)  # Output: True
print("Membership in list:", "grape" not in fruits)   # Output: True

#Identity operators
a = [1, 2, 3]   
b = a
c = [1, 2, 3]
print("Identity (is):", a is b)  # Output: True
print("Identity (is):", a is c)  # Output: False    