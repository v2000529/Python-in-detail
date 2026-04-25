#Data Types in Python and Type Casting
#Integer(int)
age = 25
print(age)
print(type(age))

#Float(float)
pi = 3.14       
print(pi)
print(type(pi))

#String(str)
name = "Vishwas"    
print(name)
print(type(name))

#Boolean(bool)
is_student = True   
print(is_student)
print(type(is_student))

#sets(set)
fruits = {"apple", "banana", "cherry"}
print(fruits)
print(type(fruits))

#Complex(complex)
z = 2 + 3j  
print(z)
print(type(z))

#List(list)
numbers = [1, 2, 3, 4, 5]
print(numbers)
print(type(numbers))

#Tuple(tuple)
coordinates = (10, 20)
print(coordinates)
print(type(coordinates))

#Dictionary(dict)
person = {"name": "Vishwas", "age": 25}
print(person)
print(type(person))

#Type Casting
#Implicit Type Casting
num_int = 10
num_float = 3.14
result = num_int + num_float
print(result)
print(type(result))

#Explicit Type Casting
num_str = "100"
num_int = 100
num_str = int(num_str)
num_sum = num_str + num_int
print(num_sum)
print(type(num_sum))