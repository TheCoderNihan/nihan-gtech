x = "Hi, There" # string
print("Strings are immutable")
print(x[3])
print(len(x)) # To get the length of a string, use the len() function.

# We can return part of a string by Slicing
print(x[:7]) # Leaving the starting index ; range will start from first character
print(x[-6:-2]) # Negative slicing specify positions counted from the end

q = x[-2:-6:-1] # Slicing moves forward by default. To slice backwards, we can use a negative step:
print(q)


print(x.upper()) # The upper() method returns the string in upper case
print(x.lower()) # The lower() method returns the string in lower case
print(x.strip()) # The strip() method removes any whitespace from the beginning or the end
print(x.split(",")) # The split() method splits the string into substrings if it finds instances of the separator

print("Python has a set of built-in methods that you can use on strings."
"\n All string methods return new values. They do not change the original string.")
# Eg. replace() , isalpha() etc.