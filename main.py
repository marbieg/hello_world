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
