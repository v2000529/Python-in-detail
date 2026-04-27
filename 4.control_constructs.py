#conditional statements(if, elif, else)
weather = "sunny"
if weather == "sunny":
    print("It's a nice day!")
elif weather == "rainy":
    print("Don't forget your umbrella!")
else:
    print("Have a great day regardless of the weather!")

#loops(for, while)
#for loop  
# 1 for loop
for i in range(5):
    print(f"Iteration {i}")

#2 iterating over a list
student_grades = {"Alice": 85, "Bob": 90, "Charlie": 78}
for student, grade in student_grades.items():
    print(f"{student} scored {grade}")

#3 using range with start,stop and step
for i in range(5):
    print(i)

for i in range(1,6):
    print(i)

for i in range(0, 10, 2):
    print(i)

#4nested loops
for i in range(1,5):
    for j in range(1,5):
        print(f"i: {i}, j: {j}")
        print("---")

#while loop
count = 0
while count < 5:
    print(f"Count is {count}")
    count += 1

#break
for i in range(1,10):
    if i == 5:
        print("Breaking the loop at i=5")
        break
    print(i)

#continue
for i in range(1,10):
    if i % 2 == 0:
        continue
    print(i)

#else in loop
number = [1,2,3,4,5]
search_number = 6
for i in number:
    if i == search_number:
        print(f"Found {search_number}!")
        break
else:
    print(f"{search_number} not found in the list.")

#pass
for i in range(5):
    if i == 3:
        pass
    print(i)