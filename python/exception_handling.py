# An exception is an error that occurs during program execution. Exception handling helps prevent the program from crashing
# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The else block lets you execute code when there is no error.
# finally block always executes whether an exception occurs or not

try:
    print(x)
except:
    print("Error: x not defined")

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = a/b
except ZeroDivisionError: # Specific exceptions canbe given
    print("Error: Division by zero not allowed")
else: # else executes if no error is present
    print("Result is ", result)
finally: # finally will always execute regardless an exception occurs or not
    print("Program finished")

# Common built-in exceptions include: ZeroDivisionError, FileNotFoundError, KeyError, IndexError, TypeError, ValueError etc.

# You can create your own custom exception using raise keyword
# You need to create your own custom exception classes before using them.
class AgeException(Exception):
    pass

age = int(input("Enter your age: "))
if age < 0:
    raise Exception("Age must be positive")
if age < 18:
    raise AgeException("Age must be 18 or above")