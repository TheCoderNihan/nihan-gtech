print("List are mutable and tuples are immutable")

abc = list(("apple", "banana", "cherry", "orange", "Kiwi"))
print(abc)
print(abc[1:4]) # Access List Items
print("mango" in abc) # Check if Item Exists
abc[2] = "mango"
print("mango" in abc)

abc.insert(2,"watermelon") # insert() method inserts an item at the specified index
print(abc)

vehicle = ["car" , "bus"]
abc.extend(vehicle) # extend() works for any iterable object (tuples, sets, dictionaries etc.)
print(abc)

abc.remove("orange") # remove() removes the specified item
abc.pop(0) # pop() removes the specified index. If index is not specified, the pop() method removes the last item.
vehicle.clear()
print(vehicle) # The clear() method empties the list. The list still remains, but it has no content.

abc.sort() # sort() method sort the list alphanumerically, ascending by default
# By default the sort() method is case sensitive, so all capital letters is sorted before lower case letters
print(abc)
abc.sort(reverse = True) # To sort in descending, use reverse = True
print(abc)

lfc = abc.copy() # Use copy() to copy a list
# lfc = abc will not work because lfc will only be a reference to abc, and changes made in abc will automatically also be made in lfc.
print(lfc)

#/// TUPLES \\\

xyz = tuple(("red", "blue", "green", "white", "black", "green"))
this_tuple = ("orange",) # To create tuple with only one item, add a comma after the item, else Python will recognize it as a string.
print(type(this_tuple))

print(xyz[-5:4]) # Accessing a tuple
print("orange" in xyz) # Check if item exists

# Once a tuple is created, you cannot change its values
# So to add or remove from a tuple there is a workaround
# You can convert the tuple into a list, change the list, and then convert the list back into a tuple
vehicle = ("plane" , "car" , "bus")
y = list(vehicle)
y.append("train")
vehicle = tuple(y)
print(vehicle)

print(xyz.count("green")) # count() returns the no.of occurances of a value in a tuple
print(xyz.index("green")) # index() returns the first occurance of the specified value