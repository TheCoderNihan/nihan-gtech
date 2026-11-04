# A function is a block of code which only runs when it is called. A function helps avoiding code repetition.

def Hello(): # A function is defined using the def keyword
    print("Hello World")

Hello() # You need to call a function to execute it
# Function names follow the same rules as variable names in Python, Function names are case-sensitive (hel and HEL are different)

# Functions can send data back to the code that called them using the return statement.
def temp():
    return "Hello from return"
    print("This is not executed") # A function exits the function and stop executing after the return statement

a = temp()
print(a)

def pass_used():
    pass # Function definitions cannot be empty. Use pass statement as placeholder if no code exists now

# Information can be passed into functions as arguments.
def greeting(name , age): # Here name , age is parameter
    print("Hello ", name , " Age is ", age)

greeting("User" , 10) # Here "User" , 10 is argument
greeting("John Doe" , 20)
# By default, a function must be called with the correct number of arguments. Else you will get an error

def India(state = "Kerala"): # Default Parameter Values
    print(state , " is in India")
India("Gujarat")
India("Himachal Pradesh")
India() # If function is called without the argument, it uses the default value.

def student(name , age):
    print("Name: ",name)
    print("Age: ",age)
student( age = 23 , name = "Jack") # Keyword Arguments:  You specify parameter name while calling.

def student_new(name , age):
    print("Name: ",name)
    print("Age: ",age)
student_new( 23 , "Jack") # Positional arguments: When you call a function with arguments without using keywords
student_new("Jack" , 23) # Changing the order changes the result

def Fruits (x):
    for i in x:
        print(i)
abc = ["apple", "banana", "cherry"]
Fruits(abc) # List as an argument

# *args and **kwargs allow functions to accept a unknown number of arguments.
# *args allows a function to accept any number of positional arguments. args becomes a tuple containing all the passed arguments
# **kwargs allows a function to accept any number of keyword arguments. kwargs becomes a dictionary containing all the keyword arguments
def sum(*numbers): # *args
    total  = 0
    for i in numbers:
        total += i
    print("Sum: ", total)
    print(type(numbers))

sum (1 , 2, 3, 4 ,5)
sum (15 , 23, 33, 28)
sum (7)

# RECURSION
# Recursion is when a function calls itself.
# It must have a base condition to stop; else the function would call itself forever, causing a stack overflow error.

def factorial(n): # Factorial means multiplying a positive integer by all the positive integers below it until 1
    if n == 0 or n == 1:
        return 1 # base condition
    else:
        return n * factorial(n-1) # recursion

print(factorial(5))
print(factorial(2))
print(factorial(10))