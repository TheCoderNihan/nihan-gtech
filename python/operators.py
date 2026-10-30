# Operators are used to perform operations on variables and values.
# Arithmetic: + - * / % ** //
print(9 % 2) # Modules returns the remainder
print(5 ** 2) # Exponent
print(10 // 3) # Floor Division always returns integar; rounds to the nearest int

# Assignment: = += -= *= /= %= **= //=
x = 4
x **= 2
print(x)

# Comparision: ==   !=   >   <   >=   <=
y = 10
print(x == y)

# Logical: and , or , not
# and returns True if both statements are true; or returns True if one of the statements is true
# not reverse the result, returns False if the result is true
print(not (x > y) )

# Idendity: is , is not
# is returns True if both variables are the same object
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b) # == - Checks if the values of both variables are equal
print(a is b) # is - Checks if both variables point to the same object in memory

# Membership: in , not in
# in returns True if a sequence with the specified value is present in the object
print("He" not in "Hello")

# PEMDAS is the operational precedence in Python
# Multiplication, division, floor division and modulo have the same precedence.
# If two operators have the same precedence, the expression is evaluated from left to right.

num1 = int( input ("Enter first number: "))
num2 = int( input ("Enter second number: "))
sum = num1 + num2
print("Sum is ", sum)