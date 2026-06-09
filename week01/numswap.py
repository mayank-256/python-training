def swap(a,b):
    a = a+b
    b = a-b
    a = a-b
    return a,b

x = int(input("Enter first number:"))
y = int(input("Enter second number:"))
print(f"Before swapping: x = {x} and y = {y}")
x, y = swap(x, y)
print(f"After swapping: x = {x} and y = {y}")