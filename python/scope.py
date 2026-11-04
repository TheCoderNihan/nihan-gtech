# Scope means from where a variable can be accessed.
# A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.
# A variable created in the main body is a global variable and belongs to the global scope.
# The same variable name inside and outside a function refers to two separate variables: one global and one local.

def test():
    x = 10 # Local variable
    print(x)
test() # x only works in the function

y = 20 # Global variable
def abc():
    print(y)
abc()
print(y)

def my_func(): # The global keyword makes the variable global.
    global z
    z = 300
my_func()
print(z)