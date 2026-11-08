# File handling is used to create, read, write, and modify files.
# Syntax: open(filename , mode)
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists

# File canbe handled in 2 modes: text or binary mode
import os

file = open("sample.txt","wt") # Here r is read , t is text and the default
file.write("Hello Python") # You cant read in w mode
file.close()

abc = open("sample.txt","rt") # Here r is read , t is text and the default
content = abc.read() # You cant write in r mode
print(content)
abc.close()

# r+ allows to Read and write existing file
# w+ allows to Read and write, overwrites existing content
# a+ Opens a file for reading and appending. New writes go to the end.

# tell() Returns the current position of the file cursor
# seek() Moves the file cursor to a specified position

xyz = open("sample.txt","r+")
print(xyz.tell())
xyz.write("This is for testing purposes , overwrites existing content")
# When Python writes this text, the file cursor moves to the end of the written content.
print(xyz.tell())
result_end = xyz.readlines()
print(result_end)
# readlines() starts reading from the current cursor position.
# But the cursor is already at the end of the file! So there is nothing left to read, and Python returns an empty list

xyz.seek(0) # Moves the cursor to the beginning
print(xyz.tell())
result = xyz.readlines()
print(result)
xyz.close()

if not os.path.exists("demofile.txt"):
    # Create the file if it doesn't exist
    f = open("demofile.txt","x") # x creates a new file , error if file already exists

# You can also use the with statement when opening a file, then no need to close the file
with open("demofile.txt","w") as f:
    f.write("Hello! Welcome to demofile.txt")
    f.write("\nThis file is for testing purposes.") # \n for next line
    f.write("\nThank You\n")

if os.path.exists("demofile.txt"):
    # Reads files if it exists
    with open("demofile.txt","r") as demo_read: # no need to close
        print(demo_read.read())
