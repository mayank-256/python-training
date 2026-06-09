def calc(a,b):
    x = input("Enter the operation you want to perform (+, -, *, /): ")
    if x == "+":
        return a + b
    elif x == "-":
        return a - b
    elif x == "*":
        return a * b
    elif x == "/":
        return a / b
    
a = int(input("Enter the first number: "))
b = int(input("Enter the second number:"))
ans = calc(a,b)
print(ans)