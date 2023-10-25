name : str = 4

print(name) # print
print(type(name)) # type
print(id(name)) # physical address
# print(dir(name)) # classes, methods and attributes
print([i for i in dir(name) if "__" not in i]) # methods and attributes