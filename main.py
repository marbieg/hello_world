print("Hello world!")

# lists (vectors/tuples in C++, can store different types of data)
lista = [1, 2, 3, 4, 5]
l1 = lista.copy()  # performs deep copy
l1[0] = 100
print(lista)

l2 = lista  # performs shallow copy (like with pointers)
l2[0] = 100
print(lista)

# tuples --> tuples are immutable; we cannot change them

# functions
def factorial(n):
    if n < 2:
        return 1
    elif n == 2:
        return 2
    else:
        return n * factorial(n-1)

print(factorial(4))

# dictionaries (maps in C++; all the keys have to be unique!)
monthConversions = {
    "Jan": "January",
    "Feb": "February"
}
print(monthConversions.get("Dec", "Invalid key"))  # default value

# for loops act as for range loops in C++
friends = ["Mark", "Kevin", "Hannah", "Toby"]
for index in range(len(friends)):
    print(friends[index])

# try-except block
try:
    answer = 10/0
except ZeroDivisionError as err:
    print(err)

# files
employee_file = open("employees.txt", "r+")  # r+ stands for read and write; a is for appending
if employee_file.readable():
    # read() - full text; readline() - one line; readlines() - puts everything into a list
    for employee in employee_file.readlines():
        print(employee)
    # for writing we can append or overwrite
employee_file.close()

# classes
from Student import Student
student1 = Student("Jim", "Business", 3.1, False)
print(student1.on_honor_roll())
