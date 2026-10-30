# Dicts are used to store value in key-value pairs.
# Dict items are ordered and should be unique , it is mutable.
bike = { "brand": "KTM" , "electric": False , "year": 1934 , "colors": ["orange","black"] }
print(bike) ; print(type(bike))

x = bike.get("brand")
y = bike.keys()
z = bike.values()
print(x) ; print(y) ; print(z)

bike["owner"] = "Bajaj"
bike["colors"] = ["orange","black","white"]
print(bike)

bike.pop("owner")
print(bike)
# popitem() removes the last inserted item ; the clear method empties the dict(null dict)

# Copying a dictionary
# Cannot copy a dict by dict2 = dict1, because dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.
# So we use the copy() method
dict_copy = bike.copy()

# A dict that contain other dict inside it is called a nested dict.
fam = { "child1": {"name": "John" , "age": 21} , "child2": {"name": "Doe" , "age": 25} }
print(fam)