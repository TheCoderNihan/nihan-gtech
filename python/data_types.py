print("A data type specifies the kind of value a variable stores.")

x = "Hi There" # string
print("Strings are immutable")
print(x[3])
print(len(x)) # To get the length of a string, use the len() function.


y = 20 # int
z = 1.5 # float
print(z)

# Lists are mutable and tuples are immutable ordered collection
a = ['apple' , 'banana'] # list
print(a)
a.append("strawberry")
print(a)

b = ('apple' , 'orange') # tuple
print("Tuples cannot be modified after creation")

# Dictionaries store info in key-value pair ; Keys must be unique
c = {"name" : "Joe" , "age" : 36} # dictionaty
print(c)

# Range represents a sequence of integers mainly used in loops
numbers = range(1,5) # The ending value is excluded
print(numbers)
print(list(numbers))

d = True # bool represents one of two values: True or False.
e = None # None type  represents the absence of a value
print(type(d))
print(type(e))
