# Zip in Python

data:any = ("a", 3, "Mohsin")
print(*data)

# Warlus Operator

a: int = 3

if(a < (b:=a+3)):
    print("a is smaller")
else:
    print("b is smaller")