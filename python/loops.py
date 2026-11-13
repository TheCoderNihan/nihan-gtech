# Control flow means the order in which the program executes statements.
# Normally, Python runs code from top to bottom. But using control flow statements, we can change that order.
# Python relies on indentation to define scope in the code

mark = int(input("Enter your marks: "))

# Only the first true condition will be executed. Even if multiple conditions are true, Python stops after executing the first matching block.
if mark >= 90: # if condition is true, code runs
    print("Grade A")
elif mark >= 75 and mark < 90: # elif (else if) runs if its condition is true
    print("Grade B")
elif mark >= 40 and mark < 75:
    print("Just pass")
else: # If no other condition is true, else runs
    print("Fail")

# A loop is used to repeat a block of code multiple times
for i in range( 1, 3): # range runs from start to end-1
    print(i)

xyz = "Python"
for i in xyz: # Goes through each character in string
    print(i)

# range syntax is range(start, end, step) . The default step is 1
for j in range(10, 30, 5):
    print("Fives multiple: ", j)
else:
    print("Loop successfully executed")

# continue
for i in ["apple", "orange", "mango", "pineapple"]:
    if i == "mango":
        continue # continue skips one iteration
    print(i, "from for loop")

# while loop
k = 5
while k <= 10: # while runs as long as condition is true
    print("from while loop: ", k)
    if k == 7:
        print("Loop breaks and exits")
        break # break stops loop and executes from the loop
    k += 1 # k = k + `1`

# In Python, blocks like if, for, while, function, class cannot be empty; else error occurs
# So  pass acts as a placeholder to avoid error
for x in range(5):
    pass

# nexted loop means a loop inside a loop
# Printing star pattern
start = int(input("How many start pattern do you want: "))
for i in range( 1, start + 1 ):
    for j in range(i):
        print("*", end = "") # end prints to the same line
    print() # purpose is to move to the next line before the next row starts.